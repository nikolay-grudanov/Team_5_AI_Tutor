# Copyright 2025 Jina AI. All rights reserved.

from math import sqrt
from typing import Optional, Tuple, Union

import torch
import torch.backends.cuda
import torch.nn as nn
from transformers import AutoModel, AutoModelForCausalLM, PreTrainedModel
from transformers.cache_utils import Cache, DynamicCache
from transformers.generation import GenerationMixin
from transformers.modeling_flash_attention_utils import FlashAttentionKwargs
from transformers.modeling_outputs import (
    BaseModelOutput,
    BaseModelOutputWithPast,
    CausalLMOutputWithPast,
)
from transformers.processing_utils import Unpack

from .blocks_jvlm import (
    MHSDPA,
    Dropout,
    ExtendedEmbedding,
    PatchDropout,
    PatchEmbedding,
    RotaryEmbedding,
    TransformerBlock,
    VisionLanguageConnector,
    build_layer_norm,
    resolve_causal_mask,
)
from .configuration_jvlm import JinaVLMConfig, JinaVLMTextConfig, JinaVLMVisionConfig


class JinaPreTrainedModel(PreTrainedModel):
    config: JinaVLMConfig
    base_model_prefix = 'model'
    supports_gradient_checkpointing = True
    _supports_flash_attn = True
    _supports_sdpa = True
    _no_split_modules = ['TransformerBlock']
    _skip_keys_device_placement = 'past_key_values'
    _can_compile_fullgraph = True
    _supports_attention_backend = True
    _can_record_outputs = {
        'hidden_states': TransformerBlock,
        'attentions': MHSDPA,
    }


class JinaVLMVisionModel(JinaPreTrainedModel):
    config: JinaVLMVisionConfig

    def __init__(self, config: JinaVLMVisionConfig, *args, **kwargs):
        super().__init__(config, *args, **kwargs)
        self.config = config
        self.hidden_size = config.hidden_size
        self.n_layers = config.n_layers
        self.input_size = config.input_size
        self.patch_size = config.patch_size
        self.cls_embed = None
        self.pos_embed = None
        self.rope = None
        self.n_prefix_tokens = 0
        self.interpolation = config.positional_interpolation
        self.use_cls_token = config.use_cls_token
        if self.use_cls_token:
            self.cls_embed = nn.Parameter(torch.zeros(self.hidden_size))
            self.n_prefix_tokens = 1
        if config.use_absolute_positional_embeddings:
            if self.n_positions is None:
                raise ValueError(
                    'A fixed number of positions is required to define positional '
                    'embeddings. Make sure input_size is set.'
                )
            self.pos_embed = nn.Parameter(
                torch.zeros(self.n_positions, self.hidden_size)
            )

        self.patch_embed = PatchEmbedding(
            self.hidden_size,
            config.patch_size,
            config.n_channels,
            config.input_size,
            bias=config.patch_embedding_bias,
            use_linear=(
                config.linear_patch_embedding
                if config.input_size is not None
                else False
            ),
        )
        self.patch_drop = (
            PatchDropout(config.patch_dropout)
            if config.patch_dropout > 0.0
            else nn.Identity()
        )
        self.layers = nn.ModuleList(
            [
                TransformerBlock(
                    config.block_config,
                    self.hidden_size,
                    is_causal=False,
                    layer_idx=i,
                    attn_implementation=self.config._attn_implementation,
                )
                for i in range(self.n_layers)
            ]
        )

        self.pre_lnorm = nn.Identity()
        if self.config.pre_lnorm:
            self.pre_lnorm = build_layer_norm(
                config.block_config.lnorm_config, size=self.hidden_size
            )
        self.post_lnorm = nn.Identity()
        if self.config.post_lnorm:
            self.post_lnorm = build_layer_norm(
                config.block_config.lnorm_config, size=self.hidden_size
            )

        self.vl_connector = VisionLanguageConnector(
            config=config.vl_connector_config,
            input_size=config.hidden_size * len(config.vit_layers),
            intermediate_size=config.hidden_size,
            output_size=config.output_size,
            n_patches=self.n_patches,
        )
        self.vit_layers = self.config.vit_layers
        self.gradient_checkpointing = False

    @property
    def n_patches(self) -> Optional[Tuple[int, int]]:
        if self.input_size is None:
            return None
        h, w = self.input_size
        return h // self.patch_size, w // self.patch_size

    @property
    def n_positions(self) -> Optional[int]:
        if self.input_size is None:
            return None
        n_h, n_w = self.n_patches
        n_pos = n_h * n_w
        if self.use_cls_token:
            n_pos += 1
        return n_pos

    def add_positional_embedding(
        self,
        x: torch.Tensor,
        patch_num: Tuple[int, int],
    ) -> torch.Tensor:
        cls_pos_emb = None
        pos_emb = self.pos_embed
        if self.cls_embed is not None:
            cls_pos_emb = self.pos_embed[0:1]
            pos_emb = self.pos_embed[1:]

        n_pos, dim = pos_emb.shape
        h, w = int(sqrt(n_pos)), int(sqrt(n_pos))
        pos_emb = pos_emb.reshape(h, w, dim)
        patch_num_0, patch_num_1 = patch_num
        if h != patch_num_0 or w != patch_num_1:
            # Derived from
            # https://github.com/facebookresearch/mae/blob/main/util/pos_embed.py
            # antialias: default True in jax.image.resize
            pos_emb = pos_emb.unsqueeze(0).permute(0, 3, 1, 2)
            pos_emb = nn.functional.interpolate(
                pos_emb,
                size=(patch_num_0, patch_num_1),
                mode=self.interpolation,
                align_corners=False,
                antialias=True,
            )
            pos_emb = pos_emb.permute(0, 2, 3, 1).squeeze(0)

        pos_emb = pos_emb.reshape(-1, pos_emb.shape[-1])
        if cls_pos_emb is not None:
            pos = torch.cat([cls_pos_emb[None, :, :], pos_emb[None, :, :]], dim=1).to(
                x.dtype
            )
        else:
            pos = pos_emb[None, :, :].to(x.dtype)
        return x + pos

    def get_visual_features(
        self,
        images: torch.Tensor,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> BaseModelOutput:
        x, shape = self.patch_embed(images)
        if self.cls_embed is not None:
            cls = self.cls_embed.view(1, 1, -1).expand(x.shape[0], -1, -1).to(x.dtype)
            x = torch.cat([cls, x], dim=1)
        if self.pos_embed is not None:
            assert shape == self.n_patches
            x = self.add_positional_embedding(x, shape)

        x = self.patch_drop(x)
        x = self.pre_lnorm(x)

        hidden_states = []
        attentions = []
        for layer in self.layers:
            x, attn = layer(
                x,
                attn_implementation=self.config._attn_implementation,
                **kwargs,
            )
            hidden_states.append(x)
            attentions.append(attn)
        x = self.post_lnorm(x)
        hidden_states.append(x)

        return BaseModelOutput(
            last_hidden_state=x,
            hidden_states=tuple(hidden_states),
            attentions=tuple(attentions),
        )

    def forward(
        self,
        images: torch.Tensor,
        image_masks: torch.Tensor,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> BaseModelOutput:
        b, t, n, d = images.shape
        mask = ~torch.all(images.view(b * t, n, d) == -1, dim=(1, 2), keepdim=True)
        images = images.view(b * t, n, d)
        out = self.get_visual_features(images, **kwargs)
        image_features = out.hidden_states

        features = []
        for layer in self.vit_layers:
            feats = image_features[layer]
            if self.n_prefix_tokens > 0:
                feats = feats[:, 1:]
            features.append(feats)
        image_features = torch.cat(features, dim=-1)
        image_features = image_features * mask
        image_features = image_features.view(b, t, n, -1).contiguous()
        image_features = self.vl_connector(
            image_features,
            image_masks,
            attn_implementation=self.config._attn_implementation,
            **kwargs,
        )
        return BaseModelOutput(
            last_hidden_state=image_features,
            hidden_states=out.hidden_states,
            attentions=out.attentions,
        )


class JinaVLMTextModel(JinaPreTrainedModel):
    config: JinaVLMTextConfig

    def __init__(self, config: JinaVLMTextConfig, *args, **kwargs):
        super().__init__(config, *args, **kwargs)
        if (
            self.config.embedding_size is not None
            and self.config.embedding_size != self.config.vocab_size
        ):
            if self.config.embedding_size < self.config.vocab_size:
                raise ValueError(
                    'Embedding size should be at least as big as vocab size'
                )
            elif self.config.embedding_size % 128 != 0:
                import warnings

                warnings.warn(
                    (
                        'Embedding size is not a multiple of 128! This could hurt '
                        'throughput performance'
                    ),
                    UserWarning,
                )
        # this is super slow so make sure torch won't use it
        torch.backends.cuda.enable_mem_efficient_sdp(False)
        if self.config.additional_vocab_size is not None:
            embedding = ExtendedEmbedding(
                config.embedding_size or config.vocab_size,
                config.additional_vocab_size,
                config.hidden_size,
            )
        else:
            embedding = nn.Embedding(
                config.embedding_size or config.vocab_size,
                config.hidden_size,
            )
        self.embedding = embedding
        self.embedding_dropout = Dropout(config.embedding_dropout)
        self.ln_f = build_layer_norm(
            config.block_config.lnorm_config, size=config.hidden_size
        )
        self.rope = None
        if self.config.rope:
            self.rope = RotaryEmbedding(
                self.config,
                theta=self.config.rope_theta,
                head_dim=self.config.block_config.attn_config.head_dim,
                hidden_size=self.config.hidden_size,
                partial_rotary_factor=self.config.partial_rotary_factor,
                scaling=self.config.rope_scaling,
            )
        layers = [
            TransformerBlock(
                config.block_config,
                hidden_size=config.hidden_size,
                is_causal=True,
                layer_idx=i,
                attn_implementation=self.config._attn_implementation,
            )
            for i in range(config.n_layers)
        ]
        setattr(self.config, 'num_hidden_layers', config.n_layers)
        self.layers = nn.ModuleList(layers)
        self.pos_embedding = None
        if not self.config.rope:
            self.pos_embedding = nn.Embedding(
                config.max_sequence_length,
                config.hidden_size,
            )
        self.gradient_checkpointing = False

    def forward(
        self,
        input_ids: Optional[torch.LongTensor] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None,
        image_features: Optional[torch.Tensor] = None,
        image_input_idx: Optional[torch.LongTensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        causal_mask: Optional[torch.Tensor] = None,
        response_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
        past_key_values: Optional[Cache] = None,
        use_cache: Optional[bool] = None,
        cache_position: Optional[torch.LongTensor] = None,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> BaseModelOutputWithPast:
        if (input_ids is None) ^ (inputs_embeds is not None):
            raise ValueError(
                'You must specify exactly one of input_ids or inputs_embeds'
            )
        has_image = image_features is not None
        assert not (has_image and inputs_embeds is not None), (
            'Cannot provide both image features and input embeddings.'
        )
        bs, sl = input_ids.size() if inputs_embeds is None else inputs_embeds.size()[:2]
        device = input_ids.device if input_ids is not None else inputs_embeds.device
        past_length = (
            past_key_values.get_seq_length() if past_key_values is not None else 0
        )
        # torch.jit.trace() doesn't support cache objects in the output
        if use_cache and past_key_values is None and not torch.jit.is_tracing():
            # TODO: Fix in new transformers version
            # past_key_values = DynamicCache(config=self.config)
            past_key_values = DynamicCache()

        if attention_mask is None:
            if input_ids is None:
                attention_mask = torch.ones((bs, sl), dtype=torch.bool, device=device)
            else:
                attention_mask = input_ids != -1

        if cache_position is None:
            cache_position = torch.arange(past_length, past_length + sl, device=device)

        if position_ids is None:
            position_ids = torch.clamp(
                torch.cumsum(attention_mask.to(torch.int32), dim=-1) - 1,
                min=0,
            ).broadcast_to((bs, attention_mask.shape[-1]))

        if input_ids is not None:
            input_ids = input_ids * (input_ids != -1).to(input_ids.dtype)

        x = inputs_embeds
        if inputs_embeds is None:
            x = self.embedding(input_ids)

        if image_features is not None:
            num_image, num_patch = image_features.shape[1:3]
            assert image_input_idx.shape == (bs, num_image, num_patch)

            # insert the image feature into the embedding.
            image_features = image_features.view(bs, num_image * num_patch, -1)
            image_input_idx = image_input_idx.view(bs, num_image * num_patch)
            valid = image_input_idx >= 0
            batch_idx = torch.arange(bs, device=x.device)
            batch_idx = torch.tile(batch_idx[:, None], [1, image_features.shape[1]])
            image_features = image_features.to(x.device)
            x = x.clone()  # Clone x to avoid in-place operation on leaf tensor
            x[batch_idx[valid], image_input_idx[valid]] += image_features[valid]

        if not self.rope:
            pos = self.transformer.wpe(position_ids)  # type: ignore
            x = pos + x

        x = self.embedding_dropout(x)

        if self.config.normalize_input_embeds:
            x = x * (self.config.hidden_size**0.5)

        causal_mask = resolve_causal_mask(
            attention_mask,
            causal_mask,
            past_key_values=past_key_values,
            batch_size=bs,
            seq_len=sl,
            past_length=past_length,
            device=x.device,
        )
        rope_embeddings = None
        if self.rope is not None:
            rope_embeddings = self.rope(x, position_ids)

        all_hidden_states = []
        all_attention_weights = []
        for layer in self.layers:
            x, att_weights = layer(
                x=x,
                rope_embeddings=rope_embeddings,
                attention_mask=causal_mask,
                past_key_values=past_key_values,
                cache_position=cache_position,
                drop_mask=response_mask,
                attn_implementation=self.config._attn_implementation,
                **kwargs,
            )
            all_hidden_states.append(x)
            if att_weights is not None:
                all_attention_weights.append(att_weights)

        # Apply final layer norm
        # shape: (batch_size, seq_len or 1, d_model)
        x = self.ln_f(x)
        all_hidden_states.append(x)

        return BaseModelOutputWithPast(
            last_hidden_state=x,
            past_key_values=past_key_values,
            hidden_states=tuple(all_hidden_states),
            attentions=tuple(all_attention_weights),
        )


class JinaVLM(JinaPreTrainedModel):
    config: JinaVLMConfig

    def __init__(self, config: JinaVLMConfig):
        super().__init__(config)
        self.vision_model: Optional[JinaVLMVisionModel] = None
        if config.vision_config is not None:
            self.vision_model = JinaVLMVisionModel._from_config(config.vision_config)
        self.language_model = JinaVLMTextModel._from_config(config.text_config)
        self.post_init()

    def get_input_embeddings(self):
        return self.language_model.embedding

    def set_input_embeddings(self, value):
        self.language_model.embedding = value

    def get_decoder(self):
        return self.language_model.layers

    def set_decoder(self, decoder):
        self.language_model.layers = decoder

    def get_image_features(
        self,
        images: torch.Tensor,
        image_masks: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        image_features = self.vision_model(images, image_masks)
        batch_size, num_image, num_patch = image_features.shape[0:3]
        return image_features.view(batch_size, num_image * num_patch, -1)

    def forward(
        self,
        input_ids: Optional[torch.LongTensor] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None,
        images: Optional[torch.Tensor] = None,
        image_masks: Optional[torch.Tensor] = None,
        image_input_idx: Optional[torch.LongTensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        causal_mask: Optional[torch.Tensor] = None,
        response_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
        past_key_values: Optional[Cache] = None,
        use_cache: Optional[bool] = None,
        cache_position: Optional[torch.LongTensor] = None,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> BaseModelOutputWithPast:
        image_features = None
        if images is not None and images.shape[1] > 0:
            image_out = self.vision_model(images, image_masks, **kwargs)
            image_features = image_out.last_hidden_state
        return self.language_model(
            input_ids=input_ids,
            inputs_embeds=inputs_embeds,
            attention_mask=attention_mask,
            causal_mask=causal_mask,
            response_mask=response_mask,
            position_ids=position_ids,
            image_features=image_features,
            image_input_idx=image_input_idx,
            past_key_values=past_key_values,
            use_cache=use_cache,
            cache_position=cache_position,
            **kwargs,
        )


class JinaVLMForConditionalGeneration(JinaPreTrainedModel, GenerationMixin):
    _tied_weights_keys = {
        'lm_head.weight': 'model.language_model.embedding.embedding.weight'
    }
    accepts_loss_kwargs = False
    config: JinaVLMConfig

    def __init__(self, config: JinaVLMConfig):
        super().__init__(config)
        self.model = JinaVLM(config)
        self.lm_head = nn.Linear(
            config.text_config.hidden_size,
            config.text_config.embedding_size or config.text_config.vocab_size,
            bias=False,
        )
        self.post_init()

    def get_input_embeddings(self):
        return self.model.get_input_embeddings()

    def set_input_embeddings(self, value):
        self.model.set_input_embeddings(value)

    def get_decoder(self):
        return self.model.get_decoder()

    def set_decoder(self, decoder):
        self.model.set_decoder(decoder)

    def get_image_features(
        self,
        images: torch.Tensor,
        image_masks: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        return self.model.get_image_features(images, image_masks)

    @property
    def language_model(self):
        return self.model.language_model

    @property
    def vision_model(self):
        return self.model.vision_model

    def forward(
        self,
        input_ids: Optional[torch.LongTensor] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None,
        images: Optional[torch.Tensor] = None,
        image_masks: Optional[torch.Tensor] = None,
        image_input_idx: Optional[torch.LongTensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        causal_mask: Optional[torch.Tensor] = None,
        response_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
        past_key_values: Optional[Cache] = None,
        labels: Optional[torch.LongTensor] = None,
        use_cache: Optional[bool] = None,
        cache_position: Optional[torch.LongTensor] = None,
        logits_to_keep: Union[int, torch.Tensor] = 0,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> CausalLMOutputWithPast:
        outputs = self.model(
            input_ids=input_ids,
            input_embeds=inputs_embeds,
            attention_mask=attention_mask,
            causal_mask=causal_mask,
            response_mask=response_mask,
            position_ids=position_ids,
            images=images,
            image_masks=image_masks,
            image_input_idx=image_input_idx,
            past_key_values=past_key_values,
            use_cache=use_cache,
            cache_position=cache_position,
            **kwargs,
        )
        out = outputs.last_hidden_state
        slice_indices = logits_to_keep
        if isinstance(logits_to_keep, int):
            slice_indices = slice(-logits_to_keep, None)
        logits = self.lm_head(out[:, slice_indices, :])
        loss = None
        if labels is not None:
            loss = self.loss_function(
                logits=logits,
                labels=labels,
                vocab_size=self.config.text_config.vocab_size,
            )
        return CausalLMOutputWithPast(
            loss=loss,
            logits=logits,
            past_key_values=outputs.past_key_values,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )

    def prepare_inputs_for_generation(
        self,
        input_ids: Optional[torch.LongTensor] = None,
        inputs_embeds: Optional[torch.FloatTensor] = None,
        images: Optional[torch.Tensor] = None,
        image_masks: Optional[torch.Tensor] = None,
        image_input_idx: Optional[torch.LongTensor] = None,
        attention_mask: Optional[torch.Tensor] = None,
        response_mask: Optional[torch.Tensor] = None,
        position_ids: Optional[torch.LongTensor] = None,
        past_key_values: Optional[Cache] = None,
        use_cache: Optional[bool] = None,
        cache_position: Optional[torch.LongTensor] = None,
        **kwargs: Unpack[FlashAttentionKwargs],
    ):
        """
        Overwritten -- During decoding we don't want to forward image inputs
        to the model
        """

        inputs = super().prepare_inputs_for_generation(
            input_ids,
            inputs_embeds=inputs_embeds,
            images=images,
            image_masks=image_masks,
            image_input_idx=image_input_idx,
            attention_mask=attention_mask,
            response_mask=response_mask,
            position_ids=position_ids,
            past_key_values=past_key_values,
            cache_position=cache_position,
            use_cache=use_cache,
            **kwargs,
        )
        if cache_position[0] != 0:
            inputs['images'] = None

        return inputs


JinaVLM.register_for_auto_class(auto_class=AutoModel)
JinaVLMForConditionalGeneration.register_for_auto_class(auto_class=AutoModelForCausalLM)
