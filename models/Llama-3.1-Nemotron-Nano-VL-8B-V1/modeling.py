# --------------------------------------------------------
# Adapted from https://huggingface.co/OpenGVLab/InternVL2-Llama3-76B under MIT License
#     LICENSE is in incl_licenses directory.
# --------------------------------------------------------


import warnings
from typing import List, Optional, Tuple, Union

import torch.utils.checkpoint
import transformers
from torch import nn
from torch.nn import CrossEntropyLoss
from transformers import AutoModel, AutoModelForCausalLM, GenerationConfig
from transformers.modeling_outputs import CausalLMOutputWithPast
from transformers.modeling_utils import PreTrainedModel
from transformers.utils import logging

from .configuration import Llama_Nemotron_Nano_VL_Config

logger = logging.get_logger(__name__)


"""
The following code is adapted from the
https://huggingface.co/OpenGVLab/InternVL2-Llama3-76B/blob/main/modeling_internvl_chat.py repository

The chat function is adapted to handle NVLM 1-D tile-tagging design for dynamic high-resolution images.
"""
def version_cmp(v1, v2, op='eq'):
    import operator

    from packaging import version
    op_func = getattr(operator, op)
    return op_func(version.parse(v1), version.parse(v2))


class Llama_Nemotron_Nano_VL(PreTrainedModel):
    config_class = Llama_Nemotron_Nano_VL_Config
    main_input_name = 'pixel_values'
    _supports_flash_attn_2 = True
    _no_split_modules = ['InternVisionModel', 'SiglipVisionModel', 'Qwen2DecoderLayer']

    def __init__(self, config: Llama_Nemotron_Nano_VL_Config):
        super().__init__(config)

        assert version_cmp(transformers.__version__, '4.36.2', 'ge')
        image_size = config.force_image_size
        patch_size = config.patch_size
        self.patch_size = patch_size
        self.template = config.template
        self.num_image_token = int((image_size // patch_size) ** 2 * (config.downsample_ratio ** 2))
        self.downsample_ratio = config.downsample_ratio
        self.ps_version = config.ps_version
        self.image_tag_type = config.image_tag_type

        logger.info(f'num_image_token: {self.num_image_token}')
        logger.info(f'ps_version: {self.ps_version}')

        self.language_model = AutoModelForCausalLM.from_config(config.llm_config, torch_dtype=torch.bfloat16)
        self.vision_model = AutoModel.from_config(config.vision_config, trust_remote_code=True)
        self.vision_model.model._initialize_weights = self.vision_model.model._init_weights  # WAR for transformers issue 38358 

        self.drop_vision_class_token = True

        # Construct the vision projection.
        # Default
        vit_hidden_size = config.vit_hidden_size
        vision_projection_hidden_size = config.projector_hidden_size
        llm_hidden_size = config.llm_config.hidden_size

        self.mlp1 = nn.Sequential(
            nn.LayerNorm(vit_hidden_size * int(1 / self.downsample_ratio) ** 2, bias=True),
            nn.Linear(vit_hidden_size * int(1 / self.downsample_ratio) ** 2, vision_projection_hidden_size, bias=True),
            nn.GELU(),
            nn.Linear(vision_projection_hidden_size, llm_hidden_size, bias=True)
        )
        self.mlp1 = self.mlp1.to(self.language_model.config.torch_dtype)

        self.img_context_token_id = None

    def forward(
            self,
            pixel_values: torch.FloatTensor,
            input_ids: torch.LongTensor = None,
            attention_mask: Optional[torch.Tensor] = None,
            position_ids: Optional[torch.LongTensor] = None,
            image_flags: Optional[torch.LongTensor] = None,
            past_key_values: Optional[List[torch.FloatTensor]] = None,
            labels: Optional[torch.LongTensor] = None,
            use_cache: Optional[bool] = None,
            output_attentions: Optional[bool] = None,
            output_hidden_states: Optional[bool] = None,
            return_dict: Optional[bool] = None,
    ) -> Union[Tuple, CausalLMOutputWithPast]:
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict

        image_flags = image_flags.squeeze(-1)
        input_embeds = self.language_model.get_input_embeddings()(input_ids)

        vit_embeds = self.extract_feature(pixel_values)
        vit_embeds = vit_embeds[image_flags == 1]
        vit_batch_size = pixel_values.shape[0]

        B, N, C = input_embeds.shape
        input_embeds = input_embeds.reshape(B * N, C)

        if torch.distributed.get_rank() == 0:
            print(f'dynamic ViT batch size: {vit_batch_size}, images per sample: {vit_batch_size / B}, dynamic token length: {N}')

        input_ids = input_ids.reshape(B * N)
        selected = (input_ids == self.img_context_token_id)
        try:
            input_embeds[selected] = input_embeds[selected] * 0.0 + vit_embeds.reshape(-1, C)
        except Exception as e:
            vit_embeds = vit_embeds.reshape(-1, C)
            print(f'warning: {e}, input_embeds[selected].shape={input_embeds[selected].shape}, '
                  f'vit_embeds.shape={vit_embeds.shape}')
            n_token = selected.sum()
            input_embeds[selected] = input_embeds[selected] * 0.0 + vit_embeds[:n_token]

        input_embeds = input_embeds.reshape(B, N, C)

        outputs = self.language_model(
            inputs_embeds=input_embeds,
            attention_mask=attention_mask,
            position_ids=position_ids,
            past_key_values=past_key_values,
            use_cache=use_cache,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
            return_dict=return_dict,
        )
        logits = outputs.logits

        loss = None
        if labels is not None:
            # Shift so that tokens < n predict n
            shift_logits = logits[..., :-1, :].contiguous()
            shift_labels = labels[..., 1:].contiguous()
            # Flatten the tokens
            loss_fct = CrossEntropyLoss()
            shift_logits = shift_logits.view(-1, self.language_model.config.vocab_size)
            shift_labels = shift_labels.view(-1)
            # Enable model parallelism
            shift_labels = shift_labels.to(shift_logits.device)
            loss = loss_fct(shift_logits, shift_labels)

        if not return_dict:
            output = (logits,) + outputs[1:]
            return (loss,) + output if loss is not None else output

        return CausalLMOutputWithPast(
            loss=loss,
            logits=logits,
            past_key_values=outputs.past_key_values,
            hidden_states=outputs.hidden_states,
            attentions=outputs.attentions,
        )

    def pixel_shuffle(self, x, scale_factor=0.5):
        n, w, h, c = x.size()
        # N, W, H, C --> N, W, H * scale, C // scale
        x = x.view(n, w, int(h * scale_factor), int(c / scale_factor))
        # N, W, H * scale, C // scale --> N, H * scale, W, C // scale
        x = x.permute(0, 2, 1, 3).contiguous()
        # N, H * scale, W, C // scale --> N, H * scale, W * scale, C // (scale ** 2)
        x = x.view(n, int(h * scale_factor), int(w * scale_factor),
                   int(c / (scale_factor * scale_factor)))
        if self.ps_version == 'v1':
            warnings.warn("In ps_version 'v1', the height and width have not been swapped back, "
                          'which results in a transposed image.')
        else:
            x = x.permute(0, 2, 1, 3).contiguous()
        return x

    def extract_feature(self, pixel_values):
        vit_embeds = self.vision_model(pixel_values).features
        vit_embeds = vit_embeds.to(dtype=torch.bfloat16)
        h = w = int(vit_embeds.shape[1] ** 0.5)
        vit_embeds = vit_embeds.reshape(vit_embeds.shape[0], h, w, -1)
        vit_embeds = self.pixel_shuffle(vit_embeds, scale_factor=self.downsample_ratio)
        vit_embeds = vit_embeds.reshape(vit_embeds.shape[0], -1, vit_embeds.shape[-1])
        vit_embeds = self.mlp1(vit_embeds)
        return vit_embeds

    def _format_image_token(self, query, num_patches_list, IMG_CONTEXT_TOKEN):
        # Split by '<image>' and rejoin with appropriate tokens
        parts = query.split('<image>')
        if len(parts) - 1 != len(num_patches_list):
            raise ValueError(f"Number of <image> tokens ({len(parts) - 1}) doesn't match num_patches_list length ({len(num_patches_list)})")
        
        result = parts[0]
        for num_patches, part in zip(num_patches_list, parts[1:]):
            if self.image_tag_type == "nvlm":
                tile_pos_identifiers = [f"<tile_{j}>" for j in range(1, num_patches)] + ["<tile_global_thumbnail>"]
                image_tokens = ''
                for tile_pos_identifier in tile_pos_identifiers:
                    image_tokens += tile_pos_identifier + IMG_CONTEXT_TOKEN * self.num_image_token
                image_tokens = '<Image>' + image_tokens + '</Image>'
            elif self.image_tag_type == "internvl":
                image_tokens = IMG_CONTEXT_TOKEN * self.num_image_token * num_patches
                image_tokens = '<img>' + image_tokens + '</img>'
            else:
                raise ValueError(f"Unknown image tag type {self.image_tag_type}")
            
            result += image_tokens + part
        
        return result

    """
    Adapts the chat function to handle NVLM 1-D tile-tagging design for dynamic high-resolution images.
    Additionally, it supports the following:
        - Chat without a system prompt.
        - Chat without an image prompt.
    """
    def chat(self, tokenizer, pixel_values, question, generation_config, history=None, return_history=False,
             num_patches=None, IMG_START_TOKEN='<img>', IMG_END_TOKEN='</img>',
             IMG_CONTEXT_TOKEN='<image>', verbose=False, visual_features=None, system_prompt=None):

        if num_patches is None:
            num_patches_list = [pixel_values.shape[0]] if pixel_values is not None else []
        elif isinstance(num_patches, torch.Tensor):
            num_patches_list = num_patches.tolist()
        else:
            num_patches_list = num_patches

        if history is None and pixel_values is not None and '<image>' not in question:
            question = '<image>\n' * len(num_patches_list) + question

        assert pixel_values is None or len(pixel_values) == sum(num_patches_list)

        img_context_token_id = tokenizer.convert_tokens_to_ids(IMG_CONTEXT_TOKEN)
        self.img_context_token_id = img_context_token_id

        eos_token_id = tokenizer.eos_token_id

        messages = []
        if system_prompt is not None:
            messages.append({"role": "system", "content": system_prompt})

        history = [] if history is None else history
        for (old_question, old_answer) in history:
            messages.append({"role": "user", "content": old_question})
            messages.append({"role": "assistant", "content": old_answer})
        
        messages.append({"role": "user", "content": question})
        query = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

        if verbose and pixel_values is not None:
            image_bs = pixel_values.shape[0]
            print(f'dynamic ViT batch size: {image_bs}')

        query = self._format_image_token(query, num_patches_list, IMG_CONTEXT_TOKEN)

        model_inputs = tokenizer(query, return_tensors='pt', add_special_tokens=False)
        input_ids = model_inputs['input_ids'].cuda()
        attention_mask = model_inputs['attention_mask'].cuda()
        generation_config['eos_token_id'] = eos_token_id
        generation_output = self.generate(
            pixel_values=pixel_values,
            visual_features=visual_features,
            input_ids=input_ids,
            attention_mask=attention_mask,
            **generation_config
        )

        response = tokenizer.batch_decode(generation_output)[0]
        response = response.split(tokenizer.eos_token)[0].strip()
        history.append((question, response))
        if return_history:
            return response, history
        else:
            query_to_print = query.replace(IMG_CONTEXT_TOKEN, '')
            query_to_print = query_to_print.replace(f'{IMG_START_TOKEN}{IMG_END_TOKEN}', '<image>')
            if verbose:
                print(query_to_print, response)
            return response

    @torch.no_grad()
    def generate(
            self,
            pixel_values: Optional[torch.FloatTensor] = None,
            input_ids: Optional[torch.FloatTensor] = None,
            attention_mask: Optional[torch.LongTensor] = None,
            visual_features: Optional[torch.FloatTensor] = None,
            generation_config: Optional[GenerationConfig] = None,
            output_hidden_states: Optional[bool] = None,
            return_dict: Optional[bool] = None,
            **generate_kwargs,
    ) -> torch.LongTensor:

        assert self.img_context_token_id is not None
        if pixel_values is not None:
            if visual_features is not None:
                vit_embeds = visual_features.cuda()
                vit_embeds = self.mlp1(vit_embeds)
            else:
                vit_embeds = self.extract_feature(pixel_values)

            input_embeds = self.language_model.get_input_embeddings()(input_ids)
            B, N, C = input_embeds.shape
            input_embeds = input_embeds.reshape(B * N, C)

            input_ids = input_ids.reshape(B * N)
            selected = (input_ids == self.img_context_token_id)
            assert selected.sum() != 0
            input_embeds[selected] = vit_embeds.reshape(-1, C).to(input_embeds.device)

            input_embeds = input_embeds.reshape(B, N, C)
        else:
            input_embeds = self.language_model.get_input_embeddings()(input_ids)

        outputs = self.language_model.generate(
            inputs_embeds=input_embeds,
            attention_mask=attention_mask,
            generation_config=generation_config,
            output_hidden_states=output_hidden_states,
            use_cache=True,
            **generate_kwargs,
        )

        return outputs
