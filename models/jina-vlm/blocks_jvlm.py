# Copyright 2025 Jina AI. All rights reserved.

from abc import ABCMeta, abstractmethod
from copy import deepcopy
from functools import wraps
from math import prod, sqrt
from typing import Any, Callable, Dict, Optional, Sequence, Tuple, Union

import einops
import torch
import torch.backends.cuda
import torch.nn as nn
import torch.nn.functional as f
from torch.nn.attention import SDPBackend, sdpa_kernel
from transformers import PretrainedConfig
from transformers.activations import ACT2FN
from transformers.cache_utils import Cache
from transformers.integrations import use_kernel_forward_from_hub
from transformers.modeling_flash_attention_utils import FlashAttentionKwargs
from transformers.modeling_layers import GradientCheckpointingLayer
from transformers.modeling_rope_utils import ROPE_INIT_FUNCTIONS, dynamic_rope_update
from transformers.modeling_utils import ALL_ATTENTION_FUNCTIONS
from transformers.processing_utils import Unpack

from .configuration_jvlm import (
    ImagePaddingEmbedType,
    ImagePooling2DType,
    ImageProjectionType,
    JinaAttentionConfig,
    JinaFFNConfig,
    JinaLNormConfig,
    JinaTransformerBlockConfig,
    JinaVLConnectorConfig,
    LayerNormType,
)


class Dropout(nn.Dropout):
    def __init__(
        self,
        p: float = 0.5,
        inplace: bool = False,
        mask_p: float = 0.0,
        broadcast_dims: Sequence[int] = (),
    ) -> None:
        super().__init__(p, inplace)
        self.mask_p = mask_p
        self.broadcast_dims = broadcast_dims

    def forward(
        self, _input: torch.Tensor, drop_mask: Optional[torch.Tensor] = None
    ) -> torch.Tensor:
        """
        :param _input: A tensor of shape `(batch_size, seq_len, embed_dim)`
        :param drop_mask: A tensor of shape `(batch_size, seq_len)` with values of zero
            or one
        """
        if self.p == 0.0 and (self.mask_p is None or self.mask_p == 0.0):
            return _input
        else:
            if self.mask_p > 0.0 and self.training:
                assert drop_mask is not None
                drop_mask = drop_mask.to(_input.dtype)
                keep_prob = 1.0 - self.p
                keep_prob2 = 1.0 - self.mask_p
                keep_prob = drop_mask * keep_prob2 + (1 - drop_mask) * keep_prob
                keep_prob = keep_prob.unsqueeze(-1)
                dropout_shape = list(_input.shape)
                keep_prob = keep_prob.broadcast_to(dropout_shape)
                multiplier = _input.new_empty(dropout_shape).bernoulli_(keep_prob)
                multiplier.div_(keep_prob)
                return _input * multiplier
            elif self.p > 0.0 and len(self.broadcast_dims) > 0 and self.training:
                keep_prob = 1.0 - self.p
                dropout_shape = list(_input.shape)
                for dim in self.broadcast_dims:
                    dropout_shape[dim] = 1
                keep = _input.new_empty(dropout_shape).bernoulli_(keep_prob)
                multiplier = keep.broadcast_to(_input.shape)
                multiplier.div_(keep_prob)
                return _input * multiplier
            else:
                return f.dropout(_input, self.p, self.training, self.inplace)


class ResidualPathDropout(nn.Module):
    """Drops paths (Stochastic Depth) per sample (when applied in main path of residual
    blocks).

    Taken from
    https://github.com/huggingface/pytorch-image-models/blob/main/timm/layers/drop.py
    """

    def __init__(self, p: float = 0.5, scale_by_keep: bool = True) -> None:
        super(ResidualPathDropout, self).__init__()
        assert 0 <= p < 1.0
        self.p = p
        self.scale_by_keep = scale_by_keep

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Drop paths (Stochastic Depth) per sample (when applied in main path of
        residual blocks).

        This is the same as the DropConnect impl I created for EfficientNet, etc
        networks, however, the original name is misleading as 'Drop Connect' is a
        different form of dropout in a separate paper...
        See discussion:
        https://github.com/tensorflow/tpu/issues/494#issuecomment-532968956

        I've opted for changing the layer and argument names to 'drop path' rather
        than mix DropConnect as a layer name and use 'survival rate' as the argument.
        """
        if self.p == 0.0 or not self.training:
            return x
        keep_prob = 1 - self.p
        # work with diff dim tensors, not just 2D ConvNets
        shape = (x.shape[0],) + (1,) * (x.ndim - 1)
        random_tensor = x.new_empty(shape).bernoulli_(keep_prob)
        if keep_prob > 0.0 and self.scale_by_keep:
            random_tensor.div_(keep_prob)
        return x * random_tensor


class PatchDropout(nn.Module):
    """
    https://arxiv.org/abs/2212.00794
    """

    def __init__(self, p: float = 0.5, exclude_first_token: bool = True):
        super().__init__()
        assert 0 <= p < 1.0
        self.p = p
        self.exclude_first_token = exclude_first_token  # exclude CLS token

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
        if not self.training or self.p == 0.0:
            return x, None

        if self.exclude_first_token:
            _cls_tokens, x = x[:, :1], x[:, 1:]
        else:
            _cls_tokens = torch.jit.annotate(torch.Tensor, x[:, :1])

        batch, ntokens = x.size()
        batch_indices = torch.arange(batch)
        batch_indices = batch_indices[..., None]

        keep_prob = 1 - self.p
        num_patches_keep = max(1, int(ntokens * keep_prob))
        rand = torch.randn(batch, ntokens)
        patch_indices_keep = rand.topk(num_patches_keep, dim=-1).indices

        x = x[batch_indices, patch_indices_keep]
        if self.exclude_first_token:
            x = torch.cat((_cls_tokens, x), dim=1)

        return x, patch_indices_keep


"""
Embedding layers. Adapted from AllenAI Molmo 
https://github.com/allenai/molmo
"""


class ExtendedEmbedding(nn.Module):
    def __init__(
        self,
        num_embeddings: int,
        num_new_embeddings: int,
        num_features: int,
    ):
        super().__init__()
        self.embedding = nn.Parameter(
            torch.zeros(num_embeddings, num_features),
        )
        self.new_embedding = nn.Parameter(
            torch.zeros(num_new_embeddings, num_features),
        )

    @property
    def weight(self):
        return self.embedding

    @weight.setter
    def weight(self, w):
        self.embedding = w

    @property
    def embedding_table(self) -> torch.Tensor:
        return torch.cat([self.embedding, self.new_embedding], dim=0)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return f.embedding(x, self.embedding_table)


class PatchEmbedding(nn.Module):
    def __init__(
        self,
        dim: int = 768,
        patch_size: int = 16,
        num_channels: int = 3,
        input_size: Optional[Tuple[int, int]] = None,
        bias: bool = True,
        use_linear: bool = False,
    ):
        super().__init__()
        self._input_size = input_size
        self._patch_size = (patch_size, patch_size)
        if input_size is not None:
            self._patch_shape = (
                self._input_size[0] // self._patch_size[0],
                self._input_size[1] // self._patch_size[1],
            )
            self._num_patches = prod(self._patch_shape)
        else:
            assert not use_linear, 'Linear patch embedding requires a fixed input size!'
            self._patch_shape = None
            self._num_patches = None
        self._num_channels = num_channels
        self._dim = dim
        self._bias = bias
        if use_linear:
            self.proj = nn.Linear(
                self._num_channels * self._patch_size[0] * self._patch_size[1],
                self._dim,
                bias=self._bias,
            )
            self._proj_impl = 'linear'
        else:
            self.proj = nn.Conv2d(
                self._num_channels,
                self._dim,
                kernel_size=self._patch_size,
                stride=self._patch_size,
                bias=self._bias,
                # padding='valid',
            )
            self._proj_impl = 'conv2d'

    def _linear_pre_projection(self, x: torch.Tensor) -> torch.Tensor:
        b, c, *_ = x.shape
        p1, p2 = self._patch_size
        patches = x.unfold(2, p1, p1).unfold(3, p2, p2)
        patches = patches.permute(0, 2, 3, 4, 5, 1)
        return patches.reshape(b, -1, c * p1 * p2)

    @staticmethod
    def _conv2d_pre_projection(x: torch.Tensor) -> torch.Tensor:
        return x

    def forward(self, x: torch.Tensor) -> Tuple[torch.Tensor, Tuple[int, int]]:
        # shape: (batch_size, n_channels, height, width)
        if len(x.shape) == 4:
            bs, ch, h, w = x.shape
            p1, p2 = self._patch_size
            assert ch == self._num_channels, (
                f'Input tensor has {ch} channels, but model expects '
                f'{self._num_channels} channels'
            )
            if self._input_size is not None:
                assert (h, w) == self._input_size, (
                    f"Input image shape {(h, w)} doesn't match model's "
                    f'{self._input_size}'
                )
                if self._proj_impl == 'linear':
                    patches = x.unfold(2, p1, p1).unfold(3, p2, p2)
                    patches = patches.permute(0, 2, 3, 4, 5, 1)
                    x = patches.reshape(bs, -1, ch * p1 * p2)
            else:
                assert h % p1 == 0 and w % p2 == 0, (
                    f'Input image shape {(h, w)} is not divisible by patch size '
                    f'{self._patch_size}'
                )
            shape = (h // p1, w // p2)

        # shape: (batch_size, seq_len, n_pixels)
        elif len(x.shape) == 3:
            bs, sl, np = x.shape
            h = int(sqrt(sl))
            shape = (h, h)
            if self._input_size is not None:
                assert self._num_patches == sl, (
                    f"Input sequence length ({sl}) doesn't match model's patch shape "
                    f'({self._patch_shape})'
                )
            else:
                assert h * h == sl, (
                    f'Input sequence length {sl} is not a perfect square. Please '
                    f'provide a square sequence length, from which the shape can be '
                    f'inferred. For non-square inputs, use a 4D tensor with shape '
                    f'(batch_size, n_channels, height, width)'
                )
            p1, p2 = self._patch_size
            assert np == self._num_channels * p1 * p2, (
                f'The input number of pixels ({np}) does not match the expected number '
                f'n_channels * patch_size_horizontal * patch_size_vertical '
                f'({self._num_channels * p1 * p2})'
            )
            if self._proj_impl == 'conv2d':
                # Reshape to 4D tensor for Conv2d projection
                x = (
                    x.unfold(1, h, h)
                    .reshape(bs, h, h, p1, p2, self._num_channels)
                    .permute(0, 5, 1, 3, 2, 4)
                    .reshape(bs, self._num_channels, h * p1, h * p2)
                )
        else:
            raise ValueError(
                f'Input tensor must be 3D or 4D, got {len(x.shape)}D tensor with shape '
                f'{x.shape}. Accepted shapes are (batch_size, n_channels, height, '
                f'width) or (batch_size, seq_len, n_pixels)'
            )
        out = self.proj(x.to(dtype=self.proj.weight.dtype))
        if self._proj_impl == 'conv2d':
            out = out.flatten(2).permute(0, 2, 1)
        return out, shape


"""
Rotary Positional Embeddings. Compatible with HuggingFace transformers 
https://github.com/huggingface/transformers/blob/main/src/transformers/
modeling_rope_utils.py
"""


def inv_freq_to_device(rope_forward):
    """Sometimes the inv_freq is calculated on the wrong device, or ends up in lower
    precision than float32.

    This wrapper ensures that inv_freq is always on the right device and in float32
    precision.
    """

    @wraps(rope_forward)
    def wrapper(self, x, position_ids):
        if self.inv_freq.dtype != torch.float32 or self.rope_init_device != x.device:
            invfreq, self.attention_scaling = self.rope_init_fn(
                self.config, x.device, self.max_seq_len_cached
            )
            self.register_buffer('inv_freq', invfreq, persistent=False)
            self.original_inv_freq = self.inv_freq
            self.rope_init_device = x.device
        return rope_forward(self, x, position_ids)

    return wrapper


class RotaryEmbedding(nn.Module):
    inv_freq: torch.Tensor

    def __init__(
        self,
        config: PretrainedConfig,
        theta: float,
        head_dim: int,
        hidden_size: int,
        partial_rotary_factor: float,
        device: Optional[torch.device] = None,
        scaling: Optional[Dict[str, Any]] = None,
    ):
        super().__init__()
        assert hasattr(config, 'rope_theta')
        self.config = deepcopy(config)

        # NOTE: for HF RoPE interface compatibility
        setattr(self.config, 'rope_theta', theta)
        setattr(self.config, 'partial_rotary_factor', partial_rotary_factor)
        setattr(self.config, 'head_dim', head_dim)
        setattr(self.config, 'hidden_size', hidden_size)
        setattr(self.config, 'rope_scaling', scaling or {})

        self.rope_type = 'default'
        if hasattr(config, 'rope_scaling') and config.rope_scaling is not None:
            self.rope_type = config.rope_scaling.get('rope_type', 'default')

        self.rope_init_fn = ROPE_INIT_FUNCTIONS[self.rope_type]
        device = device or torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        seqlen = config.max_position_embeddings or config.max_sequence_length
        invfreq, self.attention_scaling = self.rope_init_fn(self.config, device, seqlen)
        self.rope_init_device = device
        self.register_buffer('inv_freq', invfreq, persistent=False)
        self.original_inv_freq = self.inv_freq
        self.max_seq_len_cached = seqlen
        self.original_max_seq_len = self.max_seq_len_cached

    @torch.no_grad()
    @inv_freq_to_device
    @dynamic_rope_update
    def forward(self, x: torch.Tensor, position_ids: torch.Tensor):
        device_type = (
            x.device.type
            if isinstance(x.device.type, str) and x.device.type != 'mps'
            else 'cpu'
        )
        with torch.autocast(device_type=device_type, enabled=False):
            inv_freq_expanded = self.inv_freq[None, :, None].expand(
                position_ids.shape[0], -1, 1
            )
            position_ids_expanded = position_ids[:, None, :].float()
            freqs = inv_freq_expanded * position_ids_expanded
            freqs = freqs.transpose(1, 2)
            emb = torch.cat((freqs, freqs), dim=-1)
            cos = emb.cos() * self.attention_scaling
            sin = emb.sin() * self.attention_scaling

        return cos, sin


"""
Residual wrapper. Adapted from AllenAI Molmo 
https://github.com/allenai/molmo
"""


class Residual(nn.Module):
    def __init__(self, submodule: nn.Module):
        super().__init__()
        self.submodule = submodule

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x + self.submodule(x)


"""
Layer scaling. Adapted from 
https://github.com/facebookresearch/dinov2/blob/main/dinov2/layers/layer_scale.py
"""


class LayerScale(nn.Module):
    """
    LayerScale appearing in DINO v2
    From
    https://github.com/facebookresearch/dinov2/blob/main/dinov2/layers/layer_scale.py
    """

    def __init__(
        self,
        dim: int,
        init_value: float = 1e-5,
        inplace: bool = False,
    ) -> None:
        super().__init__()
        self.init_value = init_value
        self.inplace = inplace
        self.gamma = nn.Parameter(init_value * torch.ones((dim,)), requires_grad=True)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return x.mul_(self.gamma) if self.inplace else x * self.gamma


"""
Layer normalization. Adapted from AllenAI Molmo 
https://github.com/allenai/molmo
"""


class _LayerNorm(nn.Module, metaclass=ABCMeta):
    def __init__(
        self,
        config: JinaLNormConfig,
        size: int,
        elementwise_affine: Optional[bool] = True,
        eps: float = 1e-05,
        weight_initializer: Optional[Callable] = torch.ones,
        bias_initializer: Optional[Callable] = torch.zeros,
    ):
        super().__init__()
        self.config = config
        self.eps = self.config.eps or eps
        self.normalized_shape = (size,)
        if elementwise_affine or (
            elementwise_affine is None and self.config.with_affine
        ):
            self.weight = nn.Parameter(weight_initializer(self.normalized_shape))
            use_bias = self.config.bias
            if use_bias:
                self.bias = nn.Parameter(bias_initializer(self.normalized_shape))
            else:
                self.register_parameter('bias', None)
        else:
            self.register_parameter('bias', None)
            self.register_parameter('weight', None)

    @abstractmethod
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        raise NotImplementedError

    @staticmethod
    def _cast_if_autocast_enabled(
        tensor: torch.Tensor, dtype: Optional[torch.dtype] = None
    ) -> torch.Tensor:
        # NOTE: `is_autocast_enabled()` only checks for CUDA autocast, so we use the
        # separate function `is_autocast_cpu_enabled()` for CPU autocast.
        # See https://github.com/pytorch/pytorch/issues/110966.
        if tensor.device.type == 'cuda' and torch.is_autocast_enabled():
            return tensor.to(
                dtype=dtype if dtype is not None else torch.get_autocast_gpu_dtype()
            )
        elif tensor.device.type == 'cpu' and torch.is_autocast_cpu_enabled():
            return tensor.to(
                dtype=dtype if dtype is not None else torch.get_autocast_cpu_dtype()
            )
        else:
            return tensor


class LayerNorm(_LayerNorm):
    """The default :class:`LayerNorm` implementation which can optionally run in low
    precision."""

    def __init__(
        self,
        config: JinaLNormConfig,
        size: int,
        low_precision: bool = False,
        elementwise_affine: Optional[bool] = None,
        eps: float = 1e-05,
    ):
        super().__init__(
            config, size=size, elementwise_affine=elementwise_affine, eps=eps
        )
        self.low_precision = low_precision

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if self.low_precision:
            module_device = x.device
            downcast_x = self._cast_if_autocast_enabled(x)
            downcast_weight = (
                self._cast_if_autocast_enabled(self.weight)
                if self.weight is not None
                else self.weight
            )
            downcast_bias = (
                self._cast_if_autocast_enabled(self.bias)
                if self.bias is not None
                else self.bias
            )
            with torch.autocast(enabled=False, device_type=module_device.type):
                return f.layer_norm(
                    downcast_x,
                    self.normalized_shape,
                    weight=downcast_weight,
                    bias=downcast_bias,
                    eps=self.eps,
                )
        else:
            return f.layer_norm(
                x,
                self.normalized_shape,
                weight=self.weight,
                bias=self.bias,
                eps=self.eps,
            )


@use_kernel_forward_from_hub('RMSNorm')
class RMSLayerNorm(_LayerNorm):
    """RMS layer norm, a simplified :class:`LayerNorm` implementation."""

    def __init__(
        self,
        config: JinaLNormConfig,
        size: int,
        elementwise_affine: Optional[bool] = None,
        eps: float = 1e-5,
    ):
        super().__init__(
            config, size=size, elementwise_affine=elementwise_affine, eps=eps
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        with torch.autocast(enabled=False, device_type=x.device.type):
            og_dtype = x.dtype
            x = x.to(torch.float32)
            variance = x.pow(2).mean(-1, keepdim=True)
            x = x * torch.rsqrt(variance + self.eps)
            x = x.to(og_dtype)

        if self.weight is not None:
            if self.bias is not None:
                return self.weight * x + self.bias
            else:
                return self.weight * x
        else:
            return x


def build_layer_norm(config: JinaLNormConfig, size: int, **kwargs) -> _LayerNorm:
    if config.type == LayerNormType.default:
        return LayerNorm(config, size=size, low_precision=False, **kwargs)
    elif config.type == LayerNormType.low_precision:
        return LayerNorm(config, size=size, low_precision=True, **kwargs)
    return RMSLayerNorm(config, size=size, **kwargs)


"""
Multi Head Scaled Dot Product Attention module and utilities. Adapted from AllenAI Molmo
https://github.com/allenai/molmo
"""


def _create_causal_mask(seq_len: int, device: torch.device) -> torch.Tensor:
    with torch.autocast(device.type, enabled=False):
        causal_mask = torch.triu(
            torch.ones(seq_len, seq_len, device=device, dtype=torch.float),
            diagonal=1,
        )
        causal_mask.masked_fill_(causal_mask == 1, torch.finfo(causal_mask.dtype).min)
        causal_mask = causal_mask.view(1, 1, seq_len, seq_len)  # type: ignore
    return causal_mask


def _ensure_finite(
    x: torch.Tensor, check_neg_inf: bool = True, check_pos_inf: bool = False
):
    """Modify ``x`` in place to replace ``float("-inf")`` with the minimum value of the
    dtype when ``check_neg_inf`` is ``True`` and replace ``float("inf")`` with the
    maximum value of the dtype when ``check_pos_inf`` is ``True``"""
    if check_neg_inf:
        x.masked_fill_(x == float('-inf'), torch.finfo(x.dtype).min)
    if check_pos_inf:
        x.masked_fill_(x == float('inf'), torch.finfo(x.dtype).max)


def resolve_causal_mask(
    attention_mask: Optional[torch.Tensor],
    causal_mask: Optional[torch.Tensor],
    past_key_values: Optional[Cache],
    batch_size: int,
    seq_len: int,
    past_length: int,
    device,
):
    if attention_mask is not None:
        # shape: (batch_size, 1, 1, seq_len)
        if len(attention_mask.shape) == 2:
            attention_mask = attention_mask[:, : past_length + seq_len]
            attention_mask = attention_mask.to(dtype=torch.float).view(batch_size, -1)[
                :, None, None, :
            ]
        else:
            attention_mask = attention_mask.unsqueeze(1).to(dtype=torch.float)
        attention_mask = (1.0 - attention_mask) * torch.finfo(attention_mask.dtype).min

    # Merge attention mask with causal mask (attention bias)
    # NOTE: We need to initialize the attn bias in order for attn to
    # work properly with key+value cache. Otherwise
    # `f.scaled_dot_product_attention()` doesn't seem to compute scores correctly
    if (
        causal_mask is not None
        or attention_mask is not None
        or past_key_values is not None
    ):
        if causal_mask is None:
            causal_mask = _create_causal_mask(past_length + seq_len, device)
        elif causal_mask.dtype in (torch.int8, torch.bool):
            causal_mask = causal_mask.to(dtype=torch.float)
            causal_mask.masked_fill_(
                causal_mask == 0.0, torch.finfo(causal_mask.dtype).min
            )
        mask_len = seq_len
        if attention_mask is not None:
            mask_len = attention_mask.shape[-1]
        elif past_key_values is not None:
            mask_len = past_length + seq_len
        causal_mask = causal_mask[:, :, :mask_len, :mask_len].to(dtype=torch.float)
        # Add in the masking bias
        if attention_mask is not None:
            causal_mask = causal_mask + attention_mask
            # Might get -infs after adding attention mask, since
            # dtype.min + dtype.min = -inf. `f.scaled_dot_product_attention()`
            # doesn't handle -inf like you'd expect, instead it can produce NaNs
            _ensure_finite(causal_mask, check_neg_inf=True, check_pos_inf=False)
    return causal_mask


def cast_attention_mask(bias: torch.Tensor, input_dtype: torch.dtype) -> torch.Tensor:
    target_dtype = input_dtype
    # NOTE: `is_autocast_enabled()` only checks for CUDA autocast, so we use the
    # separate function `is_autocast_cpu_enabled()` for CPU autocast.
    # See https://github.com/pytorch/pytorch/issues/110966.
    if bias.device.type == 'cuda' and torch.is_autocast_enabled():
        target_dtype = torch.get_autocast_gpu_dtype()
    elif bias.device.type == 'cpu' and torch.is_autocast_cpu_enabled():
        target_dtype = torch.get_autocast_cpu_dtype()
    if bias.dtype != target_dtype:
        bias = bias.to(target_dtype)
        _ensure_finite(bias, check_neg_inf=True, check_pos_inf=False)
    return bias


def repeat_kv(hidden_states: torch.Tensor, n: int) -> torch.Tensor:
    batch, kvheads, slen, hdim = hidden_states.shape
    if n == 1:
        return hidden_states
    hidden_states = hidden_states[:, :, None, :, :].expand(
        batch, kvheads, n, slen, hdim
    )
    return hidden_states.reshape(batch, kvheads * n, slen, hdim)


def eager_attention_forward(
    module: nn.Module,
    query: torch.Tensor,
    key: torch.Tensor,
    value: torch.Tensor,
    attention_mask: Optional[torch.Tensor],
    scaling: float,
    dropout: float = 0.0,
    **_,
):
    key_states = repeat_kv(key, module.num_key_value_groups)
    value_states = repeat_kv(value, module.num_key_value_groups)

    weights = torch.matmul(query * scaling, key_states.transpose(2, 3))
    if attention_mask is not None:
        causal_mask = attention_mask[:, :, :, : key_states.shape[-2]]
        weights = weights + causal_mask

    weights = f.softmax(weights, dim=-1, dtype=torch.float32).to(query.dtype)
    weights = f.dropout(weights, p=dropout, training=module.training).to(
        value_states.dtype
    )
    out = torch.matmul(weights, value_states).to(query.dtype)
    out = out.transpose(1, 2).contiguous()

    return out, weights


def rotate_half(x: torch.Tensor):
    b, nh, t, hs = x.size()
    x = x.view(b, nh, t, 2, hs // 2)
    x1, x2 = x.unbind(dim=-2)
    return torch.cat((-x2, x1), dim=-1)


def apply_rotary_positional_embeddings(
    x: torch.Tensor,
    cos: torch.Tensor,
    sin: torch.Tensor,
) -> torch.Tensor:
    return (x * cos + rotate_half(x) * sin).to(x.dtype)


def apply_rope_to_qk(q, k, cos, sin):
    q_, k_ = q.float(), k.float()
    with torch.autocast(q.device.type, enabled=False):
        q_ = apply_rotary_positional_embeddings(q_, cos, sin)
        k_ = apply_rotary_positional_embeddings(k_, cos, sin)
    q = q_.type_as(q)
    k = k_.type_as(k)
    return q, k


class MHSDPA(nn.Module):
    """Multi Head Scaled Dot Product Attention."""

    def __init__(
        self,
        config: JinaAttentionConfig,
        hidden_size: int,
        output_size: Optional[int] = None,
        self_attn: bool = True,
        is_causal: bool = False,
        layer_idx: int = 0,
        attn_implementation: Optional[str] = None,
    ):
        super().__init__()
        self.config = config

        self.hidden_size = hidden_size
        self.n_heads = config.n_heads
        self.n_kv_heads = config.n_kv_heads or self.n_heads
        self.n_kv_groups = self.n_heads // self.n_kv_heads
        self.output_size = output_size or self.hidden_size

        # NOTE: for HF attention interface compatibility
        self.num_key_value_groups = self.n_kv_groups
        self.is_causal = is_causal
        self.layer_idx = layer_idx
        self.sliding_window = config.sliding_window

        head_dim = config.head_dim
        if head_dim is None:
            assert self.hidden_size % self.n_heads == 0
            head_dim = self.hidden_size // self.n_heads
        self.head_dim = head_dim

        self.scale = config.softmax_scale or self.head_dim**-0.5
        self.scaling = self.scale

        # Make sure QKV clip coefficient is positive, otherwise it's not well-defined
        if config.clip_qkv is not None:
            assert config.clip_qkv > 0
        self.clip_qkv = config.clip_qkv

        self.fp32_attn = config.fp32
        self.self_attn = self_attn
        self.fused_dims = (
            self.n_heads * self.head_dim,
            self.n_kv_heads * self.head_dim,
            self.n_kv_heads * self.head_dim,
        )
        if self.self_attn:
            self.qkv_w = nn.Linear(self.hidden_size, sum(self.fused_dims), bias=False)
        else:
            self.q_w = nn.Linear(
                self.hidden_size,
                self.n_heads * self.head_dim,
                bias=False,
            )
            self.kv_w = nn.Linear(
                self.hidden_size,
                sum(self.fused_dims) - self.n_heads * self.head_dim,
                bias=False,
            )
        self.out = nn.Linear(
            self.n_heads * self.head_dim,
            self.output_size,
            bias=config.o_bias,
        )
        self.q_b = nn.Parameter(
            torch.zeros(self.n_heads * self.head_dim),
            requires_grad=config.q_bias,
        )
        self.k_b = nn.Parameter(
            torch.zeros(self.n_kv_heads * self.head_dim),
            requires_grad=config.k_bias,
        )
        self.v_b = nn.Parameter(
            torch.zeros(self.n_kv_heads * self.head_dim),
            requires_grad=config.v_bias,
        )
        self.q_lnorm = nn.Identity()
        self.k_lnorm = nn.Identity()
        self.v_lnorm = nn.Identity()
        self.inner_lnorm = nn.Identity()
        self.add_q_lnorm = config.q_lnorm
        self.add_k_lnorm = config.k_lnorm
        self.add_v_lnorm = config.v_lnorm
        self.qkv_lnorm_on_heads = config.qkv_lnorm_on_heads
        q_lnorm_size = (
            self.head_dim if self.qkv_lnorm_on_heads else self.n_heads * self.head_dim
        )
        kv_lnorm_size = (
            self.head_dim
            if self.qkv_lnorm_on_heads
            else self.n_kv_heads * self.head_dim
        )
        if self.add_q_lnorm:
            self.q_lnorm = build_layer_norm(
                config.lnorm_config,
                size=q_lnorm_size,
                elementwise_affine=config.lnorm_config.with_affine,
            )
        if self.add_k_lnorm:
            self.k_lnorm = build_layer_norm(
                config.lnorm_config,
                size=kv_lnorm_size,
                elementwise_affine=config.lnorm_config.with_affine,
            )
        if self.add_v_lnorm:
            self.v_lnorm = build_layer_norm(
                config.lnorm_config,
                size=kv_lnorm_size,
                elementwise_affine=config.lnorm_config.with_affine,
            )
        if config.inner_lnorm:
            self.inner_lnorm = build_layer_norm(
                config.lnorm_config,
                size=(self.n_heads * self.head_dim),
                elementwise_affine=config.lnorm_config.with_affine,
            )
        self.drop_p = config.dropout
        self.attn_interface, *_ = self._get_attention_interface(
            attn_implementation or 'eager', None, None
        )

    def _get_attention_interface(
        self,
        attn_implementation: str,
        attn_mask: Optional[torch.Tensor] = None,
        is_causal: Optional[bool] = None,
    ) -> Tuple[Callable, Optional[torch.Tensor], Optional[bool]]:
        if 'flash' in attn_implementation and self.fp32_attn:
            raise ValueError('Flash attention does not support fp32 attention')
        if self.sliding_window != -1 and 'flash' not in attn_implementation:
            raise ValueError('Sliding window attention requires flash attention')

        attn_interface: Callable = eager_attention_forward
        if attn_implementation != 'eager':
            attn_interface = ALL_ATTENTION_FUNCTIONS[attn_implementation]

        setattr(self.config, '_attn_implementation', attn_implementation)

        if 'flash' in attn_implementation:
            # Flash attention expects attention mask to be a 2D padding only
            # mask
            # Depending on the value of is_causal, the function will
            # automatically apply causal masking or not
            if attn_mask is not None:
                # convert to 0,1 in int32
                attn_mask = (attn_mask > -1).to(torch.int32)
                # take maximum along sequence dimension
                attn_mask = attn_mask.squeeze(1).max(dim=1)[0]
        elif 'sdpa' in attn_implementation:
            if attn_mask is not None and is_causal is not None:
                is_causal = False

        elif attn_implementation == 'eager':
            if is_causal:
                assert attn_mask is not None
                assert attn_mask.ndim == 4

        return attn_interface, attn_mask, is_causal

    def forward(
        self,
        xq: torch.Tensor,
        xk: Optional[torch.Tensor] = None,
        rope_embeddings: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
        attention_mask: Optional[torch.Tensor] = None,
        past_key_values: Optional[Cache] = None,
        cache_position: Optional[torch.LongTensor] = None,
        attn_implementation: Optional[str] = None,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        if self.self_attn:
            # qkv = self.qkv_w(xq)
            qkv_b = torch.cat((self.q_b, self.k_b, self.v_b))
            # qkv += qkv_b
            qkv = f.linear(xq, self.qkv_w.weight, qkv_b)
            if self.clip_qkv is not None:
                qkv.clamp_(min=-self.clip_qkv, max=self.clip_qkv)
            q, k, v = qkv.split(self.fused_dims, dim=-1)
        else:
            assert xk is not None
            q = f.linear(xq, self.q_w.weight, self.q_b)
            kv_b = torch.cat((self.k_b, self.v_b))
            kv = f.linear(xk, self.kv_w.weight, kv_b)
            if self.clip_qkv is not None:
                q.clamp_(min=-self.clip_qkv, max=self.clip_qkv)
                kv.clamp_(min=-self.clip_qkv, max=self.clip_qkv)
            k, v = kv.split(self.fused_dims[1:], dim=-1)

        b, tq, _ = q.size()
        _, tk, __ = k.size()  # batch size, sequence length, d_model
        og_dtype = k.dtype
        if self.fp32_attn:
            dtype = torch.float32
            q = q.to(torch.float)
            k = k.to(torch.float)
        else:
            dtype = og_dtype

        # Optionally apply layer norm to keys and queries
        if not self.qkv_lnorm_on_heads:
            q = self.q_lnorm(q).to(dtype=dtype)
            k = self.k_lnorm(k).to(dtype=dtype)
            v = self.v_lnorm(v).to(dtype=dtype)

        # Move head forward to be next to the batch dim
        # shape: (bs, nh, t, hs)
        q = q.view(b, tq, self.n_heads, -1).transpose(1, 2)
        # shape: (b, n_kv_h, t, hs)
        k = k.view(b, tk, self.n_kv_heads, -1).transpose(1, 2)
        # shape: (b, n_kv_h, t, hs)
        v = v.view(b, tk, self.n_kv_heads, -1).transpose(1, 2)

        # Optionaly apply layer norm to keys and queries
        if self.qkv_lnorm_on_heads:
            q = self.q_lnorm(q).to(dtype=dtype)
            k = self.k_lnorm(k).to(dtype=dtype)
            v = self.v_lnorm(v).to(dtype=dtype)

        cache_kwargs: Dict[str, torch.Tensor] = {'cache_position': cache_position}
        if rope_embeddings is not None:
            cos, sin = rope_embeddings
            cache_kwargs['cos'] = cos
            cache_kwargs['sin'] = sin
            cos = cos.unsqueeze(1)
            sin = sin.unsqueeze(1)
            q, k = apply_rope_to_qk(q, k, cos, sin)

        if past_key_values is not None:
            k, v = past_key_values.update(k, v, self.layer_idx, cache_kwargs)

        if attention_mask is not None:
            # Resize and cast attention bias.
            # The current dtype of the attention bias might not match the dtype that the
            # SDP attn function will run in if AMP is enabled, and this can be a problem
            # if some tokens are masked out due to padding as down-casting the attention
            # bias to the autocast precision will result in -infs, which will cause the
            # SDP attn function to produce NaNs.
            qlen, klen = q.shape[-2], k.shape[-2]
            attention_mask = cast_attention_mask(
                attention_mask[:, :, klen - qlen : klen, :klen], dtype
            )

        attention_interface = self.attn_interface
        is_causal = self.is_causal
        if attn_implementation is not None:
            attention_interface, attention_mask, is_causal = (
                self._get_attention_interface(
                    attn_implementation,
                    attention_mask,
                    self.is_causal,
                )
            )

        if self.sliding_window != -1:
            kwargs['sliding_window'] = self.sliding_window
        if is_causal is not None:
            kwargs['is_causal'] = is_causal

        attn, weights = attention_interface(
            self,
            q,
            k,
            v,
            attention_mask,
            dropout=0.0 if not self.training else self.drop_p,
            scaling=self.scaling,
            **kwargs,
        )
        attn = attn.to(og_dtype)
        attn = attn.view(b, tq, -1)
        out = self.inner_lnorm(attn)
        out = self.out(out)

        return out, weights


"""
FFN module. Adapted from AllenAI Molmo https://github.com/allenai/molmo
"""


class FFN(nn.Module):
    """Feed-Forward Network."""

    def __init__(
        self,
        config: JinaFFNConfig,
        hidden_size: int,
        output_size: Optional[int] = None,
        layer_idx: int = 0,
    ):
        super().__init__()
        self.config = config
        self.hidden_size = hidden_size
        self.output_size = output_size or hidden_size
        self.intermediate_size = config.size or config.ratio * hidden_size
        self.layer_idx = layer_idx
        self.gated_activation = config.gated_activation
        self.use_bias = config.bias

        activation_type = config.activation_type.lower()
        self.act = ACT2FN[activation_type]

        intermediate_size = self.intermediate_size
        if self.gated_activation:
            intermediate_size = 2 * self.intermediate_size

        self.up = nn.Linear(self.hidden_size, intermediate_size, bias=self.use_bias)
        self.down = nn.Linear(
            self.intermediate_size, self.output_size, bias=self.use_bias
        )
        self.inner_lnorm = (
            build_layer_norm(self.config.lnorm_config, self.intermediate_size)
            if config.inner_lnorm
            else nn.Identity()
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if self.gated_activation:
            x = self.up(x)
            x, gate = x.chunk(2, dim=-1)
            return self.down(self.inner_lnorm(self.act(gate) * x))
        return self.down(self.inner_lnorm(self.act(self.up(x))))


"""
Transformer block. Adapted from AllenAI Molmo https://github.com/allenai/molmo
"""


class TransformerBlock(GradientCheckpointingLayer):
    def __init__(
        self,
        config: JinaTransformerBlockConfig,
        hidden_size: int,
        is_causal: bool = True,
        layer_idx: int = 0,
        attn_implementation: Optional[str] = None,
    ):
        super().__init__()
        self.config = config
        self.hidden_size = hidden_size
        self.is_causal = is_causal
        self.layer_idx = layer_idx
        self.drop_path = config.residual_path_dropout
        self.attn_lscale_init = config.attn_lscale_init
        self.ffn_lscale_init = config.ffn_lscale_init
        self.postnorm = config.postnorm

        self.attn = MHSDPA(
            config.attn_config,
            hidden_size=self.hidden_size,
            is_causal=is_causal,
            self_attn=True,
            layer_idx=layer_idx,
            attn_implementation=attn_implementation,
        )
        self.ffn = FFN(
            config.ffn_config, hidden_size=self.hidden_size, layer_idx=layer_idx
        )
        self.attn_drop = Dropout(
            config.residual_dropout, mask_p=config.residual_response_dropout
        )
        self.ffn_drop = Dropout(
            config.residual_dropout, mask_p=config.residual_response_dropout
        )
        self.path_drop = (
            ResidualPathDropout(self.drop_path)
            if self.drop_path > 0.0
            else nn.Identity()
        )
        self.attn_lnorm = build_layer_norm(config.lnorm_config, size=hidden_size)
        self.ffn_lnorm = build_layer_norm(config.lnorm_config, size=hidden_size)
        self.attn_lscale = nn.Identity()
        self.ffn_lscale = nn.Identity()
        if self.attn_lscale_init is not None:
            self.attn_lscale = LayerScale(self.hidden_size, self.attn_lscale_init)
        if self.ffn_lscale_init is not None:
            self.ffn_lscale = LayerScale(self.hidden_size, self.ffn_lscale_init)

    def forward(
        self,
        x: torch.Tensor,
        rope_embeddings: Optional[Tuple[torch.Tensor, torch.Tensor]] = None,
        attention_mask: Optional[torch.Tensor] = None,
        past_key_values: Optional[Cache] = None,
        cache_position: Optional[torch.LongTensor] = None,
        drop_mask: Optional[torch.Tensor] = None,
        attn_implementation: Optional[str] = None,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
        if not self.postnorm:
            x_norm = self.attn_lnorm(x)
        else:
            x_norm = x

        x_attn, x_attn_weights = self.attn(
            x_norm,
            rope_embeddings=rope_embeddings,
            attention_mask=attention_mask,
            past_key_values=past_key_values,
            cache_position=cache_position,
            attn_implementation=attn_implementation,
            **kwargs,
        )
        if self.postnorm:
            x_attn = self.attn_lnorm(x_attn)

        x_attn = self.path_drop(self.attn_lscale(x_attn))
        x = x + self.attn_drop(x_attn, drop_mask=drop_mask)

        if not self.postnorm:
            x_norm = self.ffn_lnorm(x)
        else:
            x_norm = x

        x_ffn = self.ffn(x_norm)
        if self.postnorm:
            x_ffn = self.ffn_lnorm(x)

        x_ffn = self.path_drop(self.ffn_lscale(x_ffn))
        x = x + self.ffn_drop(x_ffn, drop_mask=drop_mask)

        return x, x_attn_weights


"""
Vision Language Connector. Adapted from AllenAI Molmo https://github.com/allenai/molmo
"""


class VisionLanguageConnector(GradientCheckpointingLayer):
    """Vision-Language Connector."""

    def __init__(
        self,
        config: JinaVLConnectorConfig,
        input_size: int,
        intermediate_size: int,
        output_size: int,
        n_patches: Tuple[int, int],
        attn_implementation: Optional[str] = None,
    ):
        super().__init__()
        self.config = config
        self.input_size = input_size
        self.intermediate_size = intermediate_size
        self.output_size = output_size
        self.n_patches = n_patches

        self.padding_embed_type = config.padding_embed_type
        self.pooling_type = config.pooling_type
        self.projector_type = config.projector_type
        self.spatial_merge_size = config.spatial_merge_size
        self.pooling_h = config.pooling_h
        self.pooling_w = config.pooling_w
        self.pad_embed = None
        self.pooling = None
        self.projector: Union[nn.Linear, nn.ModuleList, FFN]

        if config.padding_embed_type is not None:
            if config.padding_embed_type in {
                ImagePaddingEmbedType.regress,
                ImagePaddingEmbedType.pad_embed,
            }:
                self.pad_embed = nn.Parameter(torch.zeros((self.input_size,)))
            else:
                self.pad_embed = nn.Parameter(torch.zeros((2, self.input_size)))

        pooling_input_size = self.input_size
        projector_input_size = self.intermediate_size
        if config.pooling_type in {
            ImagePooling2DType.attention,
            ImagePooling2DType.attention_meanq,
            ImagePooling2DType.attention_2wide,
        }:
            assert config.attn_pooling_config is not None
            if config.pooling_type == ImagePooling2DType.attention_2wide:
                pooling_input_size *= 2

            # Flash Attention can cause Inf grads in the attention pooling layer
            # because of very large batch sizes. Setting this to sdpa does not cost us
            # much since sequence lengths in the case of attention pooling are very
            # small
            attn_implementation = attn_implementation or 'eager'
            if attn_implementation.startswith('flash'):
                attn_implementation = 'sdpa'
            self.pooling = MHSDPA(
                config.attn_pooling_config,
                hidden_size=pooling_input_size,
                is_causal=False,
                self_attn=False,
                output_size=projector_input_size,
                attn_implementation=attn_implementation,
            )
        elif config.pooling_type in [
            ImagePooling2DType.stack,
            ImagePooling2DType.token_merger,
        ]:
            projector_input_size *= config.pooling_h * config.pooling_w

        if config.projector_type in {
            ImageProjectionType.mlpx2,
            ImageProjectionType.mlp,
        }:
            assert config.mlp_projector_config is not None
            mlp_projector_kwargs = dict(
                config=config.mlp_projector_config,
                hidden_size=projector_input_size,
                output_size=output_size,
            )
            if config.projector_type == ImageProjectionType.mlpx2:
                # TODO: Before there were two dropouts applied
                self.projector = nn.ModuleList(
                    [FFN(**mlp_projector_kwargs), Residual(FFN(**mlp_projector_kwargs))]
                )
            else:
                self.projector = FFN(**mlp_projector_kwargs)
        else:
            self.projector = nn.Linear(
                projector_input_size,
                output_size,
                bias=False,
            )
        self.projector_dropout = Dropout(config.projector_dropout)
        self.feature_dropout = Dropout(config.feature_dropout)

    def forward(
        self,
        image_features: torch.Tensor,
        image_masks: Optional[torch.Tensor] = None,
        attn_implementation: Optional[str] = None,
        **kwargs: Unpack[FlashAttentionKwargs],
    ) -> Tuple[torch.Tensor, Optional[torch.Tensor]]:
        # image_features:
        # (batch_size, num_crops(=num_image), num_patch, nximage_emb_dim)
        bs, ncrops = image_features.shape[:2]
        ogtype = image_features.dtype

        if self.padding_embed_type is not None:
            assert image_masks is not None
            if self.padding_embed_type == ImagePaddingEmbedType.pad_embed:
                all_pad = (image_masks == 0).to(dtype=torch.float32)
                pad_embed = self.pad_embed[None, None, None, :]
                image_features = image_features + pad_embed * torch.unsqueeze(
                    all_pad, -1
                )
            elif self.padding_embed_type == ImagePaddingEmbedType.regress:
                pad_embed = self.pad_embed[None, None, None, :]
                image_features = image_features + pad_embed * torch.unsqueeze(
                    torch.maximum(image_masks, torch.zeros_like(image_masks)), -1
                )
            else:
                pad_embed = self.pad_embed[:, None, None, None, :]
                all_pad = image_masks == 0
                partial_pad = torch.logical_and(
                    image_masks < 1, torch.logical_not(all_pad)
                ).to(dtype=torch.float32)
                all_pad = all_pad.to(dtype=torch.float32)
                image_features = image_features + pad_embed[0] * torch.unsqueeze(
                    all_pad, -1
                )
                image_features = image_features + pad_embed[1] * torch.unsqueeze(
                    partial_pad, -1
                )

        image_features = image_features.to(dtype=ogtype)
        image_features = self.feature_dropout(image_features)
        image_features = image_features.reshape((bs, ncrops) + self.n_patches + (-1,))
        pad_h = self.n_patches[0] % self.pooling_h
        pad_w = self.n_patches[1] % self.pooling_w
        if pad_h != 0 or pad_w != 0:
            # Pad so we can still pool mxn patches
            image_features = f.pad(
                image_features,
                (0, 0, 0, pad_w, 0, pad_h, 0, 0, 0, 0),
            )
        if self.pooling_type == ImagePooling2DType.token_merger:
            context_dim = image_features.shape[-1]
            hidden_size = context_dim * (self.spatial_merge_size**2)
            image_features = image_features.view([-1, hidden_size])
        else:
            image_features = einops.rearrange(
                image_features,
                'b n (h dh) (w dw) c -> (b n h w) (dh dw) c',
                dh=self.pooling_h,
                dw=self.pooling_w,
            )
            image_features = image_features.contiguous()
            if self.pooling_type == ImagePooling2DType.attention_meanq:
                query = image_features.mean(-2, keepdim=True)
                # Flash Attention can cause Inf grads in the attention pooling layer
                # because of very large batch sizes. Setting this to sdpa does not cost
                # us much since sequence lengths in the case of attention pooling are
                # very small
                attn_implementation = attn_implementation or 'eager'
                if attn_implementation.startswith('flash'):
                    attn_implementation = 'sdpa'
                if attn_implementation == 'sdpa':
                    with sdpa_kernel(backends=[SDPBackend.MATH]):
                        image_features, _ = self.pooling(
                            xq=query,
                            xk=image_features,
                            attn_implementation='sdpa',
                            **kwargs,
                        )
                else:
                    image_features, _ = self.pooling(
                        xq=query,
                        xk=image_features,
                        attn_implementation=attn_implementation,
                        **kwargs,
                    )
            elif self.pooling_type not in {
                ImagePooling2DType.none,
                ImagePooling2DType.stack,
            }:
                image_features = self.pooling(image_features[:, :1, :], image_features)

        h = self.n_patches[0] // self.pooling_h + pad_h
        w = self.n_patches[1] // self.pooling_w + pad_w

        image_features = image_features.reshape(bs, ncrops, h * w, -1)

        return self.projector(image_features)
