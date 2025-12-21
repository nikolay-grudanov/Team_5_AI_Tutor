# Copyright 2025 Jina AI. All rights reserved.

from dataclasses import asdict, dataclass, is_dataclass
from enum import Enum
from typing import Any, Dict, Optional, Tuple, Type, Union

from transformers import PretrainedConfig


class StrEnum(str, Enum):
    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f"'{str(self)}'"


class ActivationType(StrEnum):
    gelu = 'gelu'
    gelu_10 = 'gelu_10'
    gelu_fast = 'gelu_fast'
    gelu_new = 'gelu_new'
    gelu_python = 'gelu_python'
    gelu_pytorch_tanh = 'gelu_pytorch_tanh'
    gelu_accurate = 'gelu_accurate'
    laplace = 'laplace'
    leaky_relu = 'leaky_relu'
    linear = 'linear'
    mish = 'mish'
    quick_gelu = 'quick_gelu'
    relu = 'relu'
    relu2 = 'relu2'
    relu6 = 'relu6'
    sigmoid = 'sigmoid'
    silu = 'silu'
    swish = 'swish'
    tanh = 'tanh'
    prelu = 'prelu'
    xielu = 'xielu'


class ImagePaddingEmbedType(StrEnum):
    pad_and_partial_pad = 'pad_and_partial_pad'
    pad_embed = 'pad_embed'
    regress = 'regress'


class ImagePooling2DType(StrEnum):
    attention = 'attention'
    attention_meanq = 'attention_meanq'
    attention_2wide = 'attention_2wide'
    none = 'none'
    stack = 'stack'
    token_merger = 'token_merger'


class ImageProjectionType(StrEnum):
    mlp = 'mlp'
    mlpx2 = '2mlp'
    linear = 'linear'


class LayerNormType(StrEnum):
    default = 'default'
    low_precision = 'low_precision'
    rms = 'rms'


def _resolve_subconfig(obj: Union[None, Dict[str, Any], Any], cls: Type[Any]) -> Any:
    if isinstance(obj, dict):
        return cls(**obj)
    elif obj is None:
        return cls()
    return obj


@dataclass
class JinaLNormConfig:
    """Layer Norm configuration.

    Args:
        type (`LayerNormType`, *optional*, defaults to `LayerNormType.default`):
            The layernorm implementation to use.
        with_affine (`bool`, *optional*, defaults to `True`):
            Whether to include bias and weight parameters for the layer norms.
            This only affects layer norms that are immediately followed by a linear
            layer in the forward pass, so everything except QK-norms. To turn off
            affines for QK norms as well, set :attr:`attention_layer_norm_with_affine`
            to ``False``.
        eps (`float`, *optional*, defaults to `None`):
            Epsilon for layer norms.
        bias (`bool`, *optional*, defaults to `None`):
            Whether or not to include bias parameters in layer norm.
    """

    type: LayerNormType = LayerNormType.default
    with_affine: bool = True
    eps: Optional[float] = None
    bias: Optional[bool] = None


@dataclass
class JinaFFNConfig:
    """Feed Forward Network configuration.

    Args:
        activation_type (`ActivationType`, *optional*, defaults to `'silu'`):
            The activation function to use within the MLP layer.
        ratio (`int`, *optional*, defaults to 4):
            The ratio of the MLP dimensionality to ``model_dim``.
        size (`int`, *optional*, defaults to `None`):
            This is only used when ``ratio`` is not set. Set the exact hidden size
            for the MLP. Otherwise the inner MLP hidden size will be set to
            `ratio * model_dim`.
        bias (`bool`, *optional*, defaults to `False`):
            Add bias to the MLP layers.
        inner_lnorm (`bool`, *optional*, defaults to `False`):
            Add inner layer normalization to the FFN module.
        gated_activation (`bool`, *optional*, defaults to `True`):
            Use gated activation in the MLP, i.e. SwiGLU rather than a standard
            activation. Combine with activation type silu for SwiGLU.
        lnorm_config (`JinaLNormConfig`, *optional*, defaults to `JinaLNormConfig()`):
            The inner layernorm configuration.
    """

    activation_type: ActivationType = ActivationType.silu
    ratio: int = 4
    size: Optional[int] = None
    bias: bool = False
    inner_lnorm: bool = False
    gated_activation: bool = True
    lnorm_config: Union[None, Dict[str, Any], JinaLNormConfig] = None

    def __post_init__(self):
        self.lnorm_config = _resolve_subconfig(self.lnorm_config, JinaLNormConfig)


@dataclass
class JinaAttentionConfig:
    """Attention module configuration.

    Args:
        head_dim (`int`, *optional*, defaults to `None`):
            Head dimensionality.
        n_heads (`int`, *optional*, defaults to 12):
            The number of self-attention heads.
        n_kv_heads (`int`, *optional*, defaults to `None`):
            The number of heads to use for keys and values. Defaults to `n_heads`.
            Set this to ``None`` or ``n_heads`` for normal multi-head attention.
            Set this to 1 for multi-query attention.
            Set it to some in-between value for Llama2-style grouped query attention.
        softmax_scale (`float`, *optional*, defaults to `None`):
            Attention softmax scale. If set to `None`, the default inverse of head
            dimension is used.
        sliding_window (`int`, *optional*, defaults to -1):
            Attention sliding window size. If set to -1, no sliding window attention
            is used.
        fp32 (`bool`, *optional*, defaults to `False`):
            Compute attention in float32.
        dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability within the attention modules.
        q_bias (`bool`, *optional*, defaults to `False`):
            Add bias to the query projection.
        k_bias (`bool`, *optional*, defaults to `False`):
            Add bias to the key projection.
        v_bias (`bool`, *optional*, defaults to `False`):
            Add bias to the value projection.
        o_bias (`bool`, *optional*, defaults to `False`):
            Add bias to the output projection.
        q_lnorm (`bool`, *optional*, defaults to `False`):
            Add layer normalization to the query projection.
        k_lnorm (`bool`, *optional*, defaults to `False`):
            Add layer normalization to the key projection.
        v_lnorm (`bool`, *optional*, defaults to `False`):
            Add layer normalization to the value projection.
        qkv_lnorm_on_heads (`bool`, *optional*, defaults to `False`):
            If enabled, Q,K and V layer norms are applied on the heads.
        o_lnorm (`bool`, *optional*, defaults to `False`):
            Add layer normalization to the output projection.
        inner_lnorm (`bool`, *optional*, defaults to `False`):
            Add inner layer normalization to the attention module.
        clip_qkv (`float`, *optional*, defaults to `None`):
            Clip QKV to this value when set.
        lnorm_config (`JinaLNormConfig`, *optional*, defaults to `JinaLNormConfig()`):
            The inner layernorm configuration.
    """

    head_dim: Optional[int] = None
    n_heads: int = 12
    n_kv_heads: Optional[int] = None
    softmax_scale: Optional[float] = None
    sliding_window: int = -1
    fp32: bool = False
    dropout: float = 0.0
    q_bias: bool = False
    k_bias: bool = False
    v_bias: bool = False
    o_bias: bool = False
    q_lnorm: bool = False
    k_lnorm: bool = False
    v_lnorm: bool = False
    qkv_lnorm_on_heads: bool = False
    o_lnorm: bool = False
    inner_lnorm: bool = False
    clip_qkv: Optional[float] = None
    lnorm_config: Union[None, Dict[str, Any], JinaLNormConfig] = None

    def __post_init__(self):
        self.lnorm_config = _resolve_subconfig(self.lnorm_config, JinaLNormConfig)


@dataclass
class JinaTransformerBlockConfig:
    """Transformer model block configuration.

    Args:
        attn_config (`JinaAttentionConfig`, *optional*, defaults to
        `JinaAttentionConfig()`):
            The attention module configuration.
        attn_lscale_init (`float`, *optional*, defaults to `None`):
            Initial value of layer scale gamma in the attention module.
        ffn_config (`JinaFFNConfig`, *optional*, defaults to `JinaFFNConfig()`):
            The attention module configuration.
        ffn_lscale_init (`float`, *optional*, defaults to `None`):
            Initial value of layer scale gamma in the FFN module.
        residual_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for the MLP and attention output within each block.
        residual_response_dropout (`float`, *optional*, defaults to 0.0):
            Dropout applied only to loss/response tokens.
        residual_path_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for the MLP and attention output within each block.
        postnorm (`bool`, *optional*, defaults to `False`):
            Apply norm after the attention/feedforward layers rather than before, as
            introduced in the Swin transformer paper (Liu et al).
        lnorm_config (`JinaLNormConfig`, *optional*, defaults to `JinaLNormConfig()`):
            The inner layernorm configuration.
    """

    attn_config: Union[None, Dict[str, Any], JinaAttentionConfig] = None
    attn_lscale_init: Optional[float] = None
    ffn_config: Union[None, Dict[str, Any], JinaFFNConfig] = None
    ffn_lscale_init: Optional[float] = None
    residual_dropout: float = 0.0
    residual_response_dropout: float = 0.0
    residual_path_dropout: float = 0.0
    postnorm: bool = False
    lnorm_config: Union[None, Dict[str, Any], JinaLNormConfig] = None

    def __post_init__(self):
        self.attn_config = _resolve_subconfig(self.attn_config, JinaAttentionConfig)
        self.ffn_config = _resolve_subconfig(self.ffn_config, JinaFFNConfig)
        self.lnorm_config = _resolve_subconfig(self.lnorm_config, JinaLNormConfig)


@dataclass
class JinaVLConnectorConfig:
    """Vision Language Connector configuration.

    Args:
        pooling_type (`ImagePooling2DType`, *optional*, defaults to
        `ImagePooling2DType.attention`):
            The type of 2D pooling to use for image features.
        padding_embed_type (`ImagePaddingEmbedType`, *optional*, defaults to `None`):
            The type of image padding embedding to use.
        projector_type (`ImageProjectionType`, *optional*, defaults to
        `ImageProjectionType.mlp
            The type of image projector to use.
        attn_pooling_config (`JinaAttentionConfig`, *optional*, defaults to
        `JinaAttentionConfig()`):
            The attention pooling configuration.
        mlp_projector_config (`JinaFFNConfig`, *optional*, defaults to
        `JinaFFNConfig()`):
            The MLP projector configuration.
        pooling_h (`int`, *optional*, defaults to 2):
            The height of the pooling grid.
        pooling_w (`int`, *optional*, defaults to 2):
            The width of the pooling grid.
        spatial_merge_size (`int`, *optional*, defaults to 2):
            The spatial merge size for image features.
        projector_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for the image projector.
        feature_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for the image features.
    """

    padding_embed_type: Optional[ImagePaddingEmbedType] = None
    pooling_type: ImagePooling2DType = ImagePooling2DType.attention
    projector_type: ImageProjectionType = ImageProjectionType.mlp
    attn_pooling_config: Optional[JinaAttentionConfig] = None
    mlp_projector_config: Optional[JinaFFNConfig] = None
    pooling_h: int = 2
    pooling_w: int = 2
    spatial_merge_size: int = 2
    projector_dropout: float = 0.0
    feature_dropout: float = 0.0

    def __post_init__(self):
        self.attn_pooling_config = _resolve_subconfig(
            self.attn_pooling_config, JinaAttentionConfig
        )
        self.mlp_projector_config = _resolve_subconfig(
            self.mlp_projector_config, JinaFFNConfig
        )


class PretrainedConfigWithDataclasses(PretrainedConfig):
    """PretrainedConfig base class with dataclass support."""

    def to_dict(self) -> Dict[str, Any]:
        return {
            key: asdict(value) if is_dataclass(value) else value
            for key, value in super().to_dict().items()
        }


class JinaVLMVisionConfig(PretrainedConfigWithDataclasses):
    """JinaVLM Vision Model configuration.

    Args:
        block_config (`JinaTransformerBlockConfig`, *optional*, defaults to
        `JinaTransformerBlockConfig(`):
            The transformer block configuration to use within the ViT.
        vl_connector_config (`JinaVLConnectorConfig`, *optional*, defaults to
        `JinaVLConnectorConfig()`):
            The VLC (Vision Language Connector) configuration.
        n_layers (`int`, *optional*, defaults to 12):
            The number of layers/blocks.
        hidden_size (`int`, *optional*, defaults to 768):
            The hidden size of the model.
        input_size (`Tuple[int, int]`, *optional*, defaults to `None`):
            The input image size as (height, width). If not set, the model can
            process variable size images.
        patch_size (`int`, *optional*, defaults to 14):
            The patch size to use.
        n_channels (`int`, *optional*, defaults to 3):
            The number of input channels.
        linear_patch_embedding (`bool`, *optional*, defaults to `True`):
            Use a faster linear layer for patch embedding rather than a convolutional
            layer. Requires a fixed input size.
        patch_embedding_bias (`bool`, *optional*, defaults to `True`):
            Add bias to the patch embedding layer.
        patch_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability to use right after the patch embedding layer.
        pre_lnorm (`bool`, *optional*, defaults to `False`):
            Apply layer normalization to the features before feeding them into each
            transformer block.
        post_lnorm (`bool`, *optional*, defaults to `False`):
            Apply layer normalization to the features after feeding them into each
            transformer block.
        use_absolute_positional_embeddings (`bool`, *optional*, defaults to `True`):
            Use absolute positional embeddings rather than RoPE.
        use_cls_token (`bool`, *optional*, defaults to `True`):
            Use a class token.
        positional_interpolation (`str`, *optional*, defaults to `'bicubic'`):
            The interpolation mode to use when interpolating the positional embeddings.
        vit_layers (`Tuple[int, ...]`, *optional*, defaults to `(-1,)`):
            The layers of the ViT to use for image features.
        output_size (`int`, *optional*, defaults to 768):
            The output size of the vision model, after the connector.
    """

    model_type = 'jvlm'
    base_config_key = 'vision_config'

    def __init__(
        self,
        block_config: Optional[JinaTransformerBlockConfig] = None,
        vl_connector_config: Optional[JinaVLConnectorConfig] = None,
        n_layers: int = 12,
        hidden_size: int = 768,
        input_size: Optional[Tuple[int, int]] = None,
        patch_size: int = 14,
        n_channels: int = 3,
        linear_patch_embedding: bool = True,
        patch_embedding_bias: bool = True,
        patch_dropout: float = 0.0,
        pre_lnorm: bool = False,
        post_lnorm: bool = False,
        use_absolute_positional_embeddings: bool = True,
        use_cls_token: bool = True,
        positional_interpolation: str = 'bicubic',
        vit_layers: Tuple[int, ...] = (-1,),
        output_size: int = 768,
        **kwargs: Any,
    ):
        self.block_config = _resolve_subconfig(block_config, JinaTransformerBlockConfig)
        self.vl_connector_config = _resolve_subconfig(
            vl_connector_config, JinaVLConnectorConfig
        )
        super().__init__(**kwargs)

        self.n_layers = n_layers
        self.hidden_size = hidden_size
        self.input_size = input_size
        self.patch_size = patch_size
        self.n_channels = n_channels
        self.linear_patch_embedding = linear_patch_embedding
        self.patch_embedding_bias = patch_embedding_bias
        self.patch_dropout = patch_dropout
        self.pre_lnorm = pre_lnorm
        self.post_lnorm = post_lnorm
        self.use_absolute_positional_embeddings = use_absolute_positional_embeddings
        self.use_cls_token = use_cls_token
        self.positional_interpolation = positional_interpolation
        self.vit_layers = vit_layers
        self.output_size = output_size


class JinaVLMTextConfig(PretrainedConfigWithDataclasses):
    """JinaVLM Text Model configuration.

    Args:
        block_config (`JinaTransformerBlockConfig`, *optional*, defaults to
        `JinaTransformerBlockConfig()`):
            Decoder LM transformer block configuration.
        n_layers (`int`, *optional*, defaults to 12):
            The number of layers/blocks.
        hidden_size (`int`, *optional*, defaults to 768):
            The hidden size of the model.
        embedding_dropout (`float`, *optional*, defaults to 0.0):
            The dropout probability for embeddings.
        max_sequence_length (`int`, *optional*, defaults to 1024):
            The maximum input sequence length supported by the model.
        max_position_embeddings (`int`, *optional*, defaults to `None`):
            Max positional embeddings to use in RoPE cache.
        vocab_size (`int`, *optional*, defaults to 50257):
            Vocabulary size of the model.
        embedding_size (`int`, *optional*, defaults to 50304):
            The number of embeddings, i.e. the number of tokens. If set to ``None`` it
            will default to ``vocab_size``. If ``vocab_size`` is not a multiple of 128,
            setting this to the next multiple of 128 that's greater than ``vocab_size``
            can improve throughput substantially.
        additional_vocab_size (`int`, *optional*, defaults to `None`):
            New tokens to add to the embeddings as part of the vision/language
            connector.
        normalize_input_embeds (`bool`, *optional*, defaults to `False`):
            Normalize input embeddings (both for text and images) before.
        rope (`bool`, *optional*, defaults to `False`):
            Use rotary positional embeddings (RoPE).
        rope_theta (`float`, *optional*, defaults to 1000000.0):
            The base period of the RoPE embeddings.
        partial_rotary_factor (`float`, *optional*, defaults to 1.0):
            The fraction of hidden dimensions to apply RoPE to. For example, a value of
            0.5 will apply RoPE to half of the hidden dimensions, leaving the other half
            unmodified.
        rope_scaling (`Dict`, *optional*):
            Dictionary containing the scaling configuration for the RoPE embeddings.
            NOTE: if you apply a new rope type and you expect the model to work on
            longer `max_position_embeddings`, we recommend you to update this value
            accordingly.
            Expected contents:
                `rope_type` (`str`):
                    The sub-variant of RoPE to use. Can be one of ['default', 'linear',
                    'dynamic', 'yarn', 'longrope', 'llama3'], with 'default' being the
                    original RoPE implementation.
                `factor` (`float`, *optional*):
                    Used with all rope types except 'default'. The scaling factor to
                    apply to the RoPE embeddings. In most scaling types, a `factor` of
                    x will enable the model to handle sequences of length x *
                    original maximum pre-trained length.
                `original_max_position_embeddings` (`int`, *optional*):
                    Used with 'dynamic', 'longrope' and 'llama3'. The original
                    max position embeddings used during pretraining.
                `attention_factor` (`float`, *optional*):
                    Used with 'yarn' and 'longrope'. The scaling factor to be applied
                    on the attention computation. If unspecified, it defaults to value
                    recommended by the implementation, using the `factor` field to infer
                    the suggested value.
                `beta_fast` (`float`, *optional*):
                    Only used with 'yarn'. Parameter to set the boundary for
                    extrapolation (only) in the linear ramp function. If unspecified,
                    it defaults to 32.
                `beta_slow` (`float`, *optional*):
                    Only used with 'yarn'. Parameter to set the boundary for
                    interpolation (only) in the linear ramp function. If unspecified,
                    it defaults to 1.
                `short_factor` (`list[float]`, *optional*):
                    Only used with 'longrope'. The scaling factor to be applied to
                    short contexts (<`original_max_position_embeddings`). Must be a
                    list of numbers with the same length as the hidden size divided by
                    the number of attention heads divided by 2.
                `long_factor` (`list[float]`, *optional*):
                    Only used with 'longrope'. The scaling factor to be applied to
                    long contexts (<`original_max_position_embeddings`). Must be a list
                    of numbers with the same length as the hidden size divided by the
                    number of attention heads divided by 2.
                `low_freq_factor` (`float`, *optional*):
                    Only used with 'llama3'. Scaling factor applied to low frequency
                    components of the RoPE.
                `high_freq_factor` (`float`, *optional*):
                    Only used with 'llama3'. Scaling factor applied to high frequency
                    components of the RoPE.
    """

    model_type = 'jvlm'
    base_config_key = 'text_config'

    def __init__(
        self,
        block_config: Optional[JinaTransformerBlockConfig] = None,
        n_layers: int = 12,
        hidden_size: int = 768,
        embedding_dropout: float = 0.0,
        max_sequence_length: int = 1024,
        max_position_embeddings: Optional[int] = None,
        vocab_size: int = 50257,
        embedding_size: Optional[int] = 50304,
        additional_vocab_size: Optional[int] = None,
        normalize_input_embeds: bool = False,
        rope: bool = False,
        partial_rotary_factor: float = 1.0,
        rope_theta: float = 1000000.0,
        rope_scaling: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ):
        self.block_config = _resolve_subconfig(block_config, JinaTransformerBlockConfig)

        super().__init__(**kwargs)
        self.n_layers = n_layers
        self.hidden_size = hidden_size
        self.embedding_dropout = embedding_dropout
        self.max_sequence_length = max_sequence_length
        self.max_position_embeddings = max_position_embeddings
        self.vocab_size = vocab_size
        self.embedding_size = embedding_size
        self.additional_vocab_size = additional_vocab_size
        self.normalize_input_embeds = normalize_input_embeds
        self.rope = rope
        self.partial_rotary_factor = partial_rotary_factor
        self.rope_theta = rope_theta
        self.rope_scaling = rope_scaling

    # Needed for vLLM
    @property
    def num_attention_heads(self) -> int:
        return self.block_config.attn_config.n_heads


class JinaVLMConfig(PretrainedConfig):
    """JinaVLM configuration.

    Args:
        text_config (`JinaVLMTextConfig`, *optional*, defaults to
        `JinaVLMTextConfig()`):
            The text model configuration.
        vision_config (`JinaVLMVisionConfig`, *optional*, defaults to
        `JinaVLMVisionConfig()`):
            The vision model configuration.
    """

    model_type = 'jvlm'
    sub_configs = {
        'vision_config': JinaVLMVisionConfig,
        'text_config': JinaVLMTextConfig,
    }

    def __init__(
        self,
        text_config: Optional[JinaVLMTextConfig] = None,
        vision_config: Optional[JinaVLMVisionConfig] = None,
        tie_word_embeddings: bool = False,
        **kwargs,
    ):
        self.text_config = _resolve_subconfig(
            text_config, self.sub_configs['text_config']
        )
        self.vision_config = _resolve_subconfig(
            vision_config, self.sub_configs['vision_config']
        )
        if self.text_config.hidden_size != self.vision_config.output_size:
            raise ValueError(
                f'Text hidden size ({self.text_config.hidden_size}) and '
                f'vision output size ({self.vision_config.output_size}) must be '
                'the same for JinaVL'
            )
        super().__init__(**kwargs, tie_word_embeddings=tie_word_embeddings)


JinaVLMConfig.register_for_auto_class()
