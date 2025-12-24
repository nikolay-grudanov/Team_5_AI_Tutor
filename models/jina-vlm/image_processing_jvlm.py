# Copyright 2025 Jina AI. All rights reserved.

import math
from typing import Any, Dict, List, Optional, Tuple, TypedDict, Union

import numpy as np
import PIL
import PIL.Image
import torch
import torchvision.transforms
from PIL import ImageFile
from torchvision.transforms import InterpolationMode as TVInterpolationMode
from torchvision.transforms.functional import convert_image_dtype
from transformers.image_processing_utils import BaseImageProcessor
from transformers.image_transforms import convert_to_rgb
from transformers.image_utils import (
    OPENAI_CLIP_MEAN,
    OPENAI_CLIP_STD,
    ChannelDimension,
    ImageInput,
    get_image_size,
    infer_channel_dimension_format,
    make_flat_list_of_images,
    to_numpy_array,
    valid_images,
)
from transformers.processing_utils import Unpack

from .configuration_jvlm import StrEnum

"""
Image processing utils. Based on the following: 
https://github.com/allenai/molmo
https://github.com/OpenBMB/MiniCPM-V
https://github.com/QwenLM/Qwen3-VL/tree/main/qwen-vl-utils
"""


def setup_pil():
    PIL.Image.MAX_IMAGE_PIXELS = None
    ImageFile.LOAD_TRUNCATED_IMAGES = True


def smart_resize(
    height: int,
    width: int,
    factor: int = 28,
    min_pixels: int = 56 * 56,
    max_pixels: int = 14 * 14 * 4 * 1280,
    max_absolute_aspect_ratio: int = 200,
) -> Tuple[int, int]:
    """
    Resizes the image so that the following conditions are met:

    1. Both dimensions (height and width) are divisible by 'factor'.
    2. The total number of pixels is within the range ['min_pixels', 'max_pixels'].
    3. The aspect ratio of the image is maintained as closely as possible.
    """
    abs_aspect_ratio = max(height, width) / min(height, width)
    if abs_aspect_ratio > max_absolute_aspect_ratio:
        raise ValueError(
            f'Absolute aspect ratio must be < {max_absolute_aspect_ratio}, '
            f'got {abs_aspect_ratio}'
        )
    h_bar = round(height / factor) * factor
    w_bar = round(width / factor) * factor
    if h_bar * w_bar > max_pixels:
        beta = math.sqrt((height * width) / max_pixels)
        h_bar = max(factor, math.floor(height / beta / factor) * factor)
        w_bar = max(factor, math.floor(width / beta / factor) * factor)
    elif h_bar * w_bar < min_pixels:
        beta = math.sqrt(min_pixels / (height * width))
        h_bar = math.ceil(height * beta / factor) * factor
        w_bar = math.ceil(width * beta / factor) * factor

    return h_bar, w_bar


def patchify(array: np.ndarray, patch_size: int, batched: bool = False) -> np.ndarray:
    """Reshape an image of [bs, h, w, 3] -> [bs, n_patches, pixels_per_patch]"""
    if len(array.shape) == 2:
        w, h = array.shape
        h_patches = h // patch_size
        w_patches = w // patch_size
        array = np.reshape(array, [h_patches, patch_size, w_patches, patch_size])
        array = np.transpose(array, [0, 2, 1, 3])
        return np.reshape(array, [h_patches * w_patches, patch_size * patch_size])
    elif len(array.shape) == 3:
        if batched:
            bs, w, h = array.shape
            h_patches = h // patch_size
            w_patches = w // patch_size
            array = np.reshape(
                array, [bs, h_patches, patch_size, w_patches, patch_size]
            )
            array = np.transpose(array, [0, 1, 3, 2, 4])
            return np.reshape(
                array, [bs, h_patches * w_patches, patch_size * patch_size]
            )
        w, h, c = array.shape
        h_patches = h // patch_size
        w_patches = w // patch_size
        array = np.reshape(array, [h_patches, patch_size, w_patches, patch_size, c])
        array = np.transpose(array, [0, 2, 1, 3, 4])
        return np.reshape(array, [h_patches * w_patches, patch_size * patch_size * c])
    bs, w, h, c = array.shape
    h_patches = h // patch_size
    w_patches = w // patch_size
    array = np.reshape(array, [bs, h_patches, patch_size, w_patches, patch_size, c])
    array = np.transpose(array, [0, 1, 3, 2, 4, 5])
    return np.reshape(array, [bs, h_patches * w_patches, patch_size * patch_size * c])


class NormalizationMethod(StrEnum):
    GAUSSIAN = 'gaussian'
    MINMAX = 'minmax'


class CroppingMethod(StrEnum):
    RESIZE = 'resize'
    OVERLAP_AND_RESIZE = 'overlap-and-resize'
    ADAPTIVE_SLICING = 'adaptive-slicing'
    ADAPTIVE_SLICING_WITH_THUMBNAIL = 'adaptive-slicing-with-thumbnail'


class InterpolationMode(StrEnum):
    NEAREST = 'nearest'
    NEAREST_EXACT = 'nearest-exact'
    BILINEAR = 'bilinear'
    BICUBIC = 'bicubic'
    BOX = 'box'
    HAMMING = 'hamming'
    LANCZOS = 'lanczos'


class JinaVLMImagesKwargs(TypedDict, total=False):
    r"""
    Attributes:
        do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`):
            Whether to convert the image to RGB.
        do_resize (`bool`, *optional*, defaults to `self.do_resize`):
            Whether to resize the image before any additional processing.
        size (`dict[str, int]`, *optional*, defaults to `self.size`):
            Size of the image after resizing. Shortest edge of the image is resized
            to size["shortest_edge"], with the longest edge resized to keep the
            input aspect ratio.
        min_pixels (`int`, *optional*, defaults to `self.min_pixels`):
            The min pixels of the image to resize the image.
        max_pixels (`int`, *optional*, defaults to `self.max_pixels`):
            The max pixels of the image to resize the image.
        max_crops (`int`, *optional*, defaults to 6):
            The maximum number of image crops to generate.
    """

    do_convert_rgb: Optional[bool]
    do_resize: Optional[bool]
    min_pixels: Optional[int]
    max_pixels: Optional[int]
    size: Optional[dict[str, int]]
    max_crops: Optional[int]
    input_data_format: Optional[Union[str, ChannelDimension]]


class JinaVLMImageProcessor(BaseImageProcessor):
    r"""Constructs a JinaVLM Image Processor that prepares images for the JinaVLM model.

    Args:
        do_resize (`bool`, *optional*, defaults to `self.do_resize`):
            Whether to resize the image before any additional processing.
        size (`dict[str, int]`, *optional*, defaults to `self.size`):
            Size of the image after resizing. Shortest edge of the image is resized
            to size["shortest_edge"], with the longest edge resized to keep the
            input aspect ratio.
        min_pixels (`int`, *optional*, defaults to `self.min_pixels`):
            The min pixels of the image to resize the image.
        max_pixels (`int`, *optional*, defaults to `self.max_pixels`):
            The max pixels of the image to resize the image.
        do_convert_rgb (`bool`, *optional*, defaults to `self.do_convert_rgb`):
            Whether to convert the image to RGB.
        cropping_method (`str`, *optional*, defaults to `'resize'`):
            The image cropping method to use.
        normalization_method (`str`, *optional*, defaults to `'gaussian'`):
            The image normalization method to use.
        image_mean (`float` or `list[float]`, *optional*, defaults to
        `OPENAI_CLIP_MEAN`):
            The image mean to use for normalization. If a single float is provided,
            the same value is used for all channels.
        image_std (`float` or `list[float]`, *optional*, defaults to
        `OPENAI_CLIP_STD`):
            The image standard deviation to use for normalization. If a single float
            is provided, the same value is used for all channels.
        image_min (`float`, *optional*, defaults to -1.0):
            The minimum image value to use for min-max normalization.
        image_max (`float`, *optional*, defaults to 1.0):
            The maximum image value to use for min-max normalization.
        interpolation (`str`, *optional*, defaults to `'bicubic'`):
            The interpolation method to use when resizing the image.
        random_interpolation (`bool`, *optional*, defaults to `False`):
            Whether to use random interpolation when resizing the image.
        antialias (`bool`, *optional*, defaults to `True`):
            Whether to use antialiasing when resizing the image.
        preserve_aspect_ratio (`bool`, *optional*, defaults to `False`):
            Whether to preserve the aspect ratio when resizing the image.
        resize_in_float32 (`bool`, *optional*, defaults to `True`):
            Whether to perform resizing in float32 precision. If `False`, the
            resizing is performed in the original image precision.
        max_crops (`int`, *optional*, defaults to 6):
            The maximum number of image crops to generate.
        base_input_size (`int` or `Tuple[int, int]`, *optional*, defaults to
        (336, 336)):
            The base input size of the vision encoder.
        patch_size (`int`, *optional*, defaults to 14):
            The patch size of the vision encoder.
        overlap_margins (`Tuple[int, int]`, *optional*, defaults to (4, 4)):
            The overlap margins (width, height) between image crops.
        ...
    """

    model_input_names = [
        'image_crops',
        'image_tokens',
        'image_input_idx',
        'image_padding_mask',
    ]

    def __init__(
        self,
        do_resize: bool = True,
        size: Optional[dict[str, int]] = None,
        min_pixels: Optional[int] = None,
        max_pixels: Optional[int] = None,
        do_convert_rgb: bool = True,
        cropping_method: str = 'resize',
        normalization_method: str = 'gaussian',
        image_mean: Optional[Union[float, list[float]]] = None,
        image_std: Optional[Union[float, list[float]]] = None,
        image_min: Optional[float] = None,
        image_max: Optional[float] = None,
        interpolation: str = 'bicubic',
        random_interpolation: bool = False,
        antialias: bool = True,
        preserve_aspect_ratio: bool = False,
        resize_in_float32: bool = True,
        max_crops: int = 6,
        base_input_size: Tuple[int, int] = (336, 336),
        patch_size: int = 14,
        overlap_margins: Tuple[int, int] = (4, 4),
        use_column_tokens: bool = True,
        pooling_w: int = 2,
        pooling_h: int = 2,
        token_length_w: int = 12,
        token_length_h: int = 12,
        padding_mask: Union[bool, int] = False,
        padding_value: float = 0.0,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        if size is not None and (
            'shortest_edge' not in size or 'longest_edge' not in size
        ):
            raise ValueError(
                "Agument size must contain 'shortest_edge' and 'longest_edge' keys."
            )
        else:
            size = {'shortest_edge': 56 * 56, 'longest_edge': 28 * 28 * 1280}
        if min_pixels is not None:
            size['shortest_edge'] = min_pixels
        if max_pixels is not None:
            size['longest_edge'] = max_pixels
        self.min_pixels = size['shortest_edge']
        self.max_pixels = size['longest_edge']
        self.size = size

        self.do_resize = do_resize
        self.do_convert_rgb = do_convert_rgb

        _cropping_method = cropping_method.upper().replace('-', '_')
        if not hasattr(CroppingMethod, _cropping_method):
            raise ValueError(
                f'Cropping method {cropping_method} not recognized. Choose from '
                f'{list(CroppingMethod)}.'
            )
        self.cropping_method = getattr(CroppingMethod, _cropping_method)

        _normalization_method = normalization_method.upper().replace('-', '_')
        if not hasattr(NormalizationMethod, _normalization_method):
            raise ValueError(
                f'Normalization method {normalization_method} not recognized. Choose '
                f'from {list(NormalizationMethod)}.'
            )
        self.normalization_method = getattr(NormalizationMethod, _normalization_method)

        self.image_mean = image_mean or OPENAI_CLIP_MEAN
        self.image_std = image_std or OPENAI_CLIP_STD
        self.image_min = image_min or -1.0
        self.image_max = image_max or 1.0
        self.image_mean = (
            [self.image_mean] * 3
            if isinstance(self.image_mean, float)
            else self.image_mean
        )
        self.image_std = (
            [self.image_std] * 3
            if isinstance(self.image_std, float)
            else self.image_std
        )
        _interpolation = interpolation.upper().replace('-', '_')
        if not hasattr(InterpolationMode, _interpolation):
            raise ValueError(
                f'Interpolation method {interpolation} not recognized. Choose from '
                f'{list(InterpolationMode)}.'
            )
        self.interpolation = getattr(InterpolationMode, _interpolation)
        self.random_interpolation = random_interpolation
        self.antialias = antialias
        self.preserve_aspect_ratio = preserve_aspect_ratio
        self.resize_in_float32 = resize_in_float32
        self.max_crops = max_crops
        self.overlap_margins = overlap_margins
        if isinstance(base_input_size, int):
            base_input_size = (base_input_size, base_input_size)
        self.base_input_size = base_input_size
        self.patch_size = patch_size
        self.use_column_tokens = use_column_tokens
        self.pooling_w = pooling_w
        self.pooling_h = pooling_h
        self.token_length_w = token_length_w
        self.token_length_h = token_length_h
        self.patch_token_id = 0
        self.column_token_id = 1
        self.start_token_id = 2
        self.end_token_id = 3
        self.padding_mask = padding_mask
        self.padding_value = padding_value
        self.tokens_per_image = self.token_length_w * self.token_length_h
        self.image_base_patch_w = self.base_input_size[1] // patch_size
        self.image_base_patch_h = self.base_input_size[0] // patch_size
        self.crop_size = self.base_input_size[0]

    """ Normalization and resizing """

    def _gaussian_normalize(self, x: np.ndarray, dtype: np.dtype) -> np.ndarray:
        x -= np.array(self.image_mean, dtype=dtype)[None, None, :]
        x /= np.array(self.image_std, dtype=dtype)[None, None, :]
        return x

    def _minmax_normalize(self, x: np.ndarray, dtype: np.dtype) -> np.ndarray:
        return np.asarray(self.image_min, dtype=dtype) + x * np.asarray(
            self.image_max - self.image_min, dtype=dtype
        )

    def normalize_image(
        self,
        x: np.ndarray,
        dtype: Optional[np.dtype] = None,
    ) -> np.ndarray:
        dtype = dtype or x.dtype
        if self.normalization_method == NormalizationMethod.GAUSSIAN:
            return self._gaussian_normalize(x, dtype)
        return self._minmax_normalize(x, dtype)

    def resize_image(
        self,
        x: np.ndarray,
        size: List[int],
        rng: Any = np.random,
        mode: Optional[InterpolationMode] = None,
    ) -> Tuple[np.ndarray, np.ndarray]:
        x = torch.permute(torch.from_numpy(x), [2, 0, 1])

        pad = False
        padding = [[0, 0], [0, 0], [0, 0]]
        if self.preserve_aspect_ratio:
            desired_height, desired_width = size
            height, width = x.shape[:2]
            np_desired_height = np.array(desired_height, np.float32)
            np_desired_width = np.array(desired_width, np.float32)
            np_height = np.array(height, np.float32)
            np_width = np.array(width, np.float32)
            image_scale_y = np_desired_height / np_height
            image_scale_x = np_desired_width / np_width
            image_scale = np.array(
                min(float(image_scale_x), float(image_scale_y)), np.float32
            )
            scaled_height = int(height * image_scale)
            scaled_width = int(width * image_scale)
            size = [scaled_height, scaled_width]
            pad = True
            top_pad = (desired_height - scaled_height) // 2
            left_pad = (desired_width - scaled_width) // 2
            padding = [
                [top_pad, desired_height - scaled_height - top_pad],
                [left_pad, desired_width - scaled_width - left_pad],
                [0, 0],
            ]

        if self.resize_in_float32:
            x = convert_image_dtype(x)

        mode = mode or self.interpolation
        if self.random_interpolation:
            options = [
                InterpolationMode.BILINEAR,
                InterpolationMode.NEAREST_EXACT,
                InterpolationMode.BICUBIC,
                InterpolationMode.LANCZOS,
                InterpolationMode.HAMMING,
            ]
            mode = options[rng.randint(len(options))]

        mode = getattr(TVInterpolationMode, mode.upper())
        dtype = x.dtype
        in_min = 0.0
        if torch.is_floating_point(x):
            in_max = 1.0
            x = torchvision.transforms.Resize(size, mode, antialias=self.antialias)(x)
            x = torch.clip(x, 0.0, 1.0).to(dtype)
        else:
            assert dtype == torch.uint8, (
                'Expected float images or uint8 images, but got {}'.format(x.dtype)
            )
            in_max = 255.0
            x = torchvision.transforms.Resize(size, mode, antialias=self.antialias)(x)
            x = torch.clip(x, 0, 255).to(dtype)

        x = x.to(torch.float32)
        x = (x - in_min) / (in_max - in_min)
        x = torch.permute(x, [1, 2, 0]).numpy()
        mask = np.ones_like(x[:, :, 0], dtype=np.bool_)

        if pad:
            # noinspection PyTypeChecker
            x = np.pad(x, padding, constant_values=self.padding_value)
            # noinspection PyTypeChecker
            mask = np.pad(mask, padding[:2])
        return x, mask

    """ Base cropping via resizing """

    def base_get_n_image_patches(
        self,
        height: int,
        width: int,
        max_crops: int,
    ) -> int:
        raise NotImplementedError(
            'Function `get_n_image_patches` is not implemented for cropping method '
            f'{CroppingMethod.RESIZE}'
        )

    def base_resize_cropping(self, image: np.ndarray):
        resized, mask = self.resize_image(image, list(self.base_input_size))
        resized = self.normalize_image(resized)
        patches = patchify(resized, self.patch_size, batched=False)
        mask = patchify(mask, self.patch_size, batched=False)
        perrow = np.full((self.token_length_w,), self.patch_token_id, dtype=np.int32)
        if self.use_column_tokens:
            perrow = np.concatenate([perrow, [self.column_token_id]], 0, dtype=np.int32)
        extra_tokens = np.tile(perrow, [self.token_length_h])
        joint = [
            [self.start_token_id],
            extra_tokens,
            [self.end_token_id],
        ]
        # noinspection PyTypeChecker
        joint = np.concatenate(joint, 0, dtype=np.int32)

        return np.expand_dims(patches, 0), joint, None, mask

    """ Molmo cropping via overlapping and resizing """

    @staticmethod
    def _molmo_select_tiling(h: int, w: int, patch_size: int, max_num_crops: int):
        """Divide an image of size [w, h] in up to max_num_patches of size
        patch_size."""
        tilings = []
        for i in range(1, max_num_crops + 1):
            for j in range(1, max_num_crops + 1):
                if i * j <= max_num_crops:
                    tilings.append((i, j))

        # sort so argmin and argmax favour smaller tilings in the event of a tie
        tilings.sort(key=lambda x: (x[0] * x[1], x[0]))
        candidate_tilings = np.array(tilings, dtype=np.int32)  # [n_resolutions, 2]
        candidate_resolutions = candidate_tilings * patch_size  # [n_resolutions, 2]

        # How much we would need to scale the image to fit exactly in each tiling
        original_size = np.stack([h, w], dtype=np.float32)  # [1, 2]

        # The original size can be zero in rare cases if the image is smaller than the
        # margin. In those cases letting the scale become infinite means the tiling is
        # based on the other side, or falls back to the smallest tiling
        with np.errstate(divide='ignore'):
            required_scale_d = (
                candidate_resolutions.astype(np.float32) / original_size,
            )

        # [n_resolutions, 1]
        required_scale = np.min(required_scale_d, axis=-1, keepdims=True)
        if np.all(required_scale < 1):
            # We are forced to downscale, so try to minimize the amount of downscaling
            ix = np.argmax(required_scale)
        else:
            # Pick the resolution that required the least upscaling so that it most
            # closely fits the image
            required_scale = np.where(required_scale < 1.0, 10e9, required_scale)
            ix = np.argmin(required_scale)

        return candidate_tilings[ix]

    @staticmethod
    def _molmo_get_patches_from_tiling(
        num_tiles,
        pooling_size,
        crop_patches,
        crop_window_patches,
        left_margin,
        right_margin,
    ) -> np.int32:
        if num_tiles > 1:
            left_crop_window_patches = (
                (crop_window_patches + left_margin + pooling_size - 1)
                // pooling_size
                * pooling_size
            )
            middle_crop_window_patches = (
                (crop_window_patches + pooling_size - 1) // pooling_size * pooling_size
            )
            right_crop_window_patches = (
                (crop_window_patches + right_margin + pooling_size - 1)
                // pooling_size
                * pooling_size
            )
            return (
                left_crop_window_patches
                + (num_tiles - 2) * middle_crop_window_patches
                + right_crop_window_patches
            )
        else:
            single_crop_window_patches = (
                (crop_patches + pooling_size - 1) // pooling_size * pooling_size
            )
            return single_crop_window_patches

    def molmo_get_n_image_patches(
        self,
        height: int,
        width: int,
        max_crops: int,
    ) -> int:
        # Discard this many patches from the (left/top, right/bottom) of crops
        left_margin, right_margin = self.overlap_margins
        # Required for compatibility with image pooling
        assert left_margin % self.pooling_w == 0 and right_margin % self.pooling_w == 0
        assert left_margin % self.pooling_h == 0 and right_margin % self.pooling_h == 0
        # pixels removed per dim
        total_margin_pixels = self.patch_size * (right_margin + left_margin)
        # patches per crop dim
        crop_patches = self.base_input_size[0] // self.patch_size

        # usable patches
        crop_window_patches = crop_patches - (right_margin + left_margin)
        crop_window_size = crop_window_patches * self.patch_size

        # We assume hxw pooling, but can allow padding the right/bottom with extra
        # patches if the number of patches per side is not divisible by h/w
        assert (
            crop_patches + self.pooling_h - 1
        ) // self.pooling_h == self.token_length_h
        assert (
            crop_patches + self.pooling_w - 1
        ) // self.pooling_w == self.token_length_w

        # Decide how to tile the image, to account for the overlap margins we
        # compute the tiling as if we had an image without the margins and were
        # using a crop size without the margins
        tiling = self._molmo_select_tiling(
            height - total_margin_pixels,
            width - total_margin_pixels,
            crop_window_size,
            max_crops,
        )

        # Now build the output tokens
        h = self._molmo_get_patches_from_tiling(
            tiling[0],
            self.pooling_h,
            crop_patches,
            crop_window_patches,
            left_margin,
            right_margin,
        )
        w = self._molmo_get_patches_from_tiling(
            tiling[1],
            self.pooling_w,
            crop_patches,
            crop_window_patches,
            left_margin,
            right_margin,
        )
        # for each row of patches, add a patch token per patch
        n_tokens = w.item() // self.pooling_w
        if self.use_column_tokens:
            # after each row, one column token is added
            n_tokens += 1
        # replicate each row of patch tokens by number of rows, i.e.
        # proportional to image height
        n_tokens *= h.item() // self.pooling_h
        # add start and end image tokens
        n_tokens += 2

        # Global image goes first, so the order of patches in previous crops gets
        # increased
        n_thumbnail_tokens = self.token_length_w
        if self.use_column_tokens:
            n_thumbnail_tokens += 1
        n_thumbnail_tokens *= self.token_length_h
        n_thumbnail_tokens += 2

        return n_tokens + n_thumbnail_tokens

    def molmo_overlap_and_resize_cropping(self, image: np.ndarray):
        # Discard this many patches from the (left/top, right/bottom) of crops
        left_margin, right_margin = self.overlap_margins

        # Required for compatibility with image pooling
        assert left_margin % self.pooling_w == 0 and right_margin % self.pooling_w == 0
        assert left_margin % self.pooling_h == 0 and right_margin % self.pooling_h == 0

        # pixels removed per dim
        total_margin_pixels = self.patch_size * (right_margin + left_margin)

        # patches per crop dim
        crop_patches = self.base_input_size[0] // self.patch_size

        # usable patches
        crop_window_patches = crop_patches - (right_margin + left_margin)
        crop_window_size = crop_window_patches * self.patch_size

        # Decide how to tile the image, to account for the overlap margins we
        # compute the tiling as if we had an image without the margins and were
        # using a crop size without the margins
        original_image_h, original_image_w = image.shape[:2]
        tiling = self._molmo_select_tiling(
            original_image_h - total_margin_pixels,
            original_image_w - total_margin_pixels,
            crop_window_size,
            self.max_crops,
        )
        # noinspection PyTypeChecker
        src, img_mask = self.resize_image(
            image,
            [
                tiling[0] * crop_window_size + total_margin_pixels,
                tiling[1] * crop_window_size + total_margin_pixels,
            ],
        )
        src = self.normalize_image(src)

        # Now we have to split the image into crops, while keeping track of how each
        # patch in each crop should be ordered in the global image, this require a
        # lot of tricky booking
        _ = tiling[0] * tiling[1]
        patches_arr = []
        mask_arr = []
        patch_ordering_arr = []

        # We assume hxw pooling, but can allow padding the right/bottom with extra
        # patches if the number of patches per side is not divisible by h/w
        assert (
            crop_patches + self.pooling_h - 1
        ) // self.pooling_h == self.token_length_h
        assert (
            crop_patches + self.pooling_w - 1
        ) // self.pooling_w == self.token_length_w
        image_base_patch_w = self.base_input_size[1] // self.patch_size
        image_base_patch_h = self.base_input_size[0] // self.patch_size
        crop_size = self.base_input_size[0]
        on = 0
        on_patch = 0
        for i in range(tiling[0]):
            y0 = i * crop_window_size
            if i == 0:
                crop_y0 = 0
            else:
                crop_y0 = left_margin // self.pooling_h
            crop_h = image_base_patch_h - (right_margin + left_margin)
            if i == 0:
                crop_h += left_margin
            if i == (tiling[0] - 1):
                crop_h += right_margin
            for j in range(tiling[1]):
                x0 = j * crop_window_size
                if j == 0:
                    crop_x0 = 0
                else:
                    crop_x0 = left_margin // self.pooling_w
                crop_w = image_base_patch_w - (right_margin + left_margin)
                if j == 0:
                    crop_w += left_margin
                if j == (tiling[1] - 1):
                    crop_w += right_margin
                pooled_w = (crop_w + self.pooling_w - 1) // self.pooling_w
                pooled_h = (crop_h + self.pooling_h - 1) // self.pooling_h
                after_padding_width = self.token_length_w - pooled_w - crop_x0
                after_padding_height = self.token_length_h - pooled_h - crop_y0
                # noinspection PyTypeChecker
                patch_ordering_arr.append(
                    np.pad(
                        np.reshape(
                            np.arange(on, on + pooled_h * pooled_w, dtype=np.int32),
                            (pooled_h, pooled_w),
                        ),
                        [
                            [crop_y0, after_padding_height],
                            [crop_x0, after_padding_width],
                        ],
                        constant_values=-1,
                        mode='constant',
                    )
                )
                patches_arr.append(src[y0 : y0 + crop_size, x0 : x0 + crop_size])
                mask_arr.append(img_mask[y0 : y0 + crop_size, x0 : x0 + crop_size])
                on += pooled_h * pooled_w
                on_patch += 1

        # [n_crops, base_image_h, base_image_w, n_channels]
        patches = np.stack(patches_arr)
        patch_ordering = np.stack(patch_ordering_arr)
        img_mask = np.stack(mask_arr)
        patches = patchify(patches, self.patch_size, batched=True)
        img_mask = patchify(img_mask, self.patch_size, batched=True)
        img_mask = img_mask.astype(np.float32).mean(axis=-1)
        patch_ordering = np.reshape(patch_ordering, [-1])
        valid = patch_ordering >= 0

        # Path order numbers the patches crop-by-crop, here we transpose
        # it to get left-to-right order
        patch_ordering_rh = np.reshape(
            patch_ordering,
            [tiling[0], tiling[1], self.token_length_h, self.token_length_w],
        )
        patch_ordering_rh = np.transpose(patch_ordering_rh, [0, 2, 1, 3])
        patch_ordering_rh = np.reshape(patch_ordering_rh, [-1])

        # The transpose will screw up which patches are masked, project the
        # new order into sparse structure of `patch_ordering` to fix it
        patch_ordering[valid] = patch_ordering_rh[patch_ordering_rh >= 0]

        # Now build the output tokens
        h = self._molmo_get_patches_from_tiling(
            tiling[0],
            self.pooling_h,
            crop_patches,
            crop_window_patches,
            left_margin,
            right_margin,
        )
        w = self._molmo_get_patches_from_tiling(
            tiling[1],
            self.pooling_w,
            crop_patches,
            crop_window_patches,
            left_margin,
            right_margin,
        )
        # for each row of patches, add a patch token per patch
        per_row = np.full((w // self.pooling_w,), self.patch_token_id, dtype=np.int32)
        if self.use_column_tokens:
            # after each row, one column token is added
            per_row = np.concatenate([per_row, [self.column_token_id]], 0)

        # replicate each row of patch tokens by number of rows, i.e.
        # proportional to image height
        joint = np.tile(per_row, [h // self.pooling_h])
        # add start and end image tokens
        joint = [[self.start_token_id], joint, [self.end_token_id]]

        # Finally do the same for the global image
        resized, _ = self.resize_image(image, list(self.base_input_size))
        resized = self.normalize_image(resized)
        resized = patchify(resized, self.patch_size, batched=False)
        # prepend the global image
        patches = np.concatenate([np.expand_dims(resized, 0), patches], 0)

        # Global image goes first, so the order of patches in previous crops gets
        # increased
        patch_ordering = np.where(
            patch_ordering >= 0, patch_ordering + self.tokens_per_image, -1
        )
        patch_ordering = np.concatenate(
            [np.arange(0, self.tokens_per_image), patch_ordering], 0
        )
        per_row = np.full((self.token_length_w,), self.patch_token_id, dtype=np.int32)
        if self.use_column_tokens:
            per_row = np.concatenate([per_row, [self.column_token_id]], 0)
        extra_tokens = np.tile(per_row, [self.token_length_h])
        joint = [
            [self.start_token_id],
            extra_tokens,
            [self.end_token_id],
        ] + joint

        # noinspection PyTypeChecker
        joint = np.concatenate(joint, 0)
        # noinspection PyTypeChecker
        img_mask = np.pad(img_mask, [[0, 1], [0, 0]], constant_values=-1)

        return patches, joint, patch_ordering, img_mask

    """ MiniCPM adaptive slicing functions """

    @staticmethod
    def _minicpm_get_refine_size(grid: List[int], scale_resolution: int):
        grid_x, grid_y = grid
        return grid_x * scale_resolution, grid_y * scale_resolution

    @staticmethod
    def _minicpm_split_to_slices(image: np.ndarray, grid: List[int]):
        slices = []
        width, height = image.shape[:2]
        grid_x = int(width / grid[0])
        grid_y = int(height / grid[1])
        has_channels = True if len(image) == 3 else False
        for i in range(0, height, grid_y):
            images = []
            for j in range(0, width, grid_x):
                if has_channels:
                    _slice = image[j : j + grid_x, i : i + grid_y, :]
                else:
                    _slice = image[j : j + grid_x, i : i + grid_y]
                images.append(_slice)
            slices.append(images)

        return slices

    def _minicpm_refine_image_for_slicing(
        self,
        image: np.ndarray,
        max_slice_nums: int = 9,
        scale_resolution: int = 448,
    ):
        original_size = image.shape[:2]
        original_width, original_height = original_size
        log_ratio = math.log(original_width / original_height)
        ratio = original_width * original_height / (scale_resolution * scale_resolution)
        multiple = min(math.ceil(ratio), max_slice_nums)
        best_grid = [1, 1]
        if multiple > 1:
            candidate_split_grids_nums = []
            for i in [multiple - 1, multiple, multiple + 1]:
                if i == 1 or i > max_slice_nums:
                    continue
                candidate_split_grids_nums.append(i)

            candidate_grids = []
            # find best grid
            for split_grids_nums in candidate_split_grids_nums:
                m = 1
                while m <= split_grids_nums:
                    if split_grids_nums % m == 0:
                        candidate_grids.append([m, split_grids_nums // m])
                    m += 1

            min_error = float('inf')
            for grid in candidate_grids:
                error = abs(log_ratio - math.log(grid[0] / grid[1]))
                if error < min_error:
                    best_grid = grid
                    min_error = error

        refine_size = self._minicpm_get_refine_size(best_grid, scale_resolution)
        refine_image, image_mask = self.resize_image(
            x=image, size=list(refine_size), mode=InterpolationMode.BICUBIC
        )
        return refine_image, image_mask, best_grid

    def _minicpm_slice_image(
        self,
        image: np.ndarray,
        mask: np.ndarray,
        best_grid: List[int],
        scale_resolution: int = 448,
    ):
        num_patches_h = num_patches_w = scale_resolution // self.patch_size
        num_patches_h = num_patches_h // self.pooling_h
        num_patches_w = num_patches_w // self.pooling_w
        patch_ordering_arr = []

        # Returns hierarchical list of list slices.
        # Scanning is over width first. Then over height.
        # List of best_grid_y*(list of best_grid_x slices)
        slices = self._minicpm_split_to_slices(image, best_grid)
        image_masks = self._minicpm_split_to_slices(mask, best_grid)

        # Flatten the inner slices
        slices = [item for sublist in slices for item in sublist]
        image_masks = [item for sublist in image_masks for item in sublist]
        first_slice = slices[0]
        on = 0
        on_patch = 0
        for j in range(best_grid[1]):
            for i in range(best_grid[0]):
                # Assure all slices are the same size
                if i != 0 and j != 0:
                    index = i + j
                    assert slices[index].shape == first_slice.shape
                patch_ordering_arr.append(
                    np.reshape(
                        np.arange(
                            on, on + num_patches_h * num_patches_w, dtype=np.int32
                        ),
                        (num_patches_h, num_patches_w),
                    ),
                )
                on += num_patches_h * num_patches_w
                on_patch += 1

        return slices, image_masks, patch_ordering_arr, best_grid

    def minicpm_get_n_image_patches(
        self, height: int, width: int, max_crops: int, with_thumbnail: bool = False
    ) -> int:
        raise NotImplementedError(
            'Function `get_n_image_patches` is not implemented for cropping method '
            f'{CroppingMethod.ADAPTIVE_SLICING}'
        )

    def minicpm_adaptive_slicing(self, image: np.ndarray, with_thumbnail: bool = True):
        scale_resolution = self.base_input_size[0]
        refine_image, image_mask, best_grid = self._minicpm_refine_image_for_slicing(
            image, self.max_crops, scale_resolution
        )
        refine_image = self.normalize_image(refine_image)
        slices, image_masks, patch_ordering_arr, best_grid = self._minicpm_slice_image(
            refine_image,
            image_mask,
            best_grid,
            scale_resolution,
        )
        # [n_crops, base_image_h, base_image_w, n_channels]
        patches = np.stack(slices)
        patch_ordering = np.stack(patch_ordering_arr)
        # [n_crops, n_patches, n_pixels_per_patch]
        patches = patchify(patches, self.patch_size, batched=True)
        patch_ordering = np.reshape(patch_ordering, [-1])
        img_mask = np.stack(image_masks)
        img_mask = patchify(img_mask, self.patch_size, batched=True)
        img_mask = img_mask.astype(np.float32).mean(axis=-1)

        # Add special tokens
        # Molmo uses special patch token ids for mapping patches to token ids
        per_row = np.full(
            (best_grid[0] * self.token_length_w,),
            self.patch_token_id,
            dtype=np.int32,
        )
        # replicate each row of patch tokens by number of rows, i.e.
        # proportional to image height
        joint = np.tile(per_row, [best_grid[1] * self.token_length_h])
        # add start and end image tokens
        joint = [[self.start_token_id], joint, [self.end_token_id]]
        if with_thumbnail:
            resized, _ = self.resize_image(image, list(self.base_input_size))
            resized = self.normalize_image(resized)
            resized = patchify(resized, self.patch_size, batched=False)
            patches = np.concatenate(
                [np.expand_dims(resized, 0), patches], 0
            )  # prepend the global image

            # Global image goes first, so the order of patches in previous crops
            # gets increased
            patch_ordering = np.concatenate(
                [np.arange(0, self.tokens_per_image), patch_ordering], 0
            )
            per_row = np.full(
                (self.token_length_w,), self.patch_token_id, dtype=np.int32
            )
            extra_tokens = np.tile(per_row, [self.token_length_h])
            joint = [
                [self.start_token_id],
                extra_tokens,
                [self.end_token_id],
            ] + joint

        # noinspection PyTypeChecker
        joint = np.concatenate(joint, 0)
        # noinspection PyTypeChecker
        mask = np.pad(img_mask, [[0, 1], [0, 0]], constant_values=-1)

        return patches, joint, patch_ordering, mask

    """ Image input idx builder """

    def build_image_input_idx(self, image_tokens: np.ndarray, patch_order: np.ndarray):
        """Converts `patch_order` into an array mapping patch_id -> token_position."""
        tokens_per_image = self.token_length_w * self.token_length_h
        image_input_idx = image_tokens == self.patch_token_id
        # noinspection PyTypeChecker
        image_input_idx = np.nonzero(image_input_idx)[0].astype(np.int32)

        if patch_order is not None:
            patch_order = np.reshape(patch_order, [-1])
            _ = patch_order.shape[0]
            valid = patch_order >= 0
            n_valid_patches = valid.sum()
            assert len(image_input_idx) == n_valid_patches

            sorted_patch_ixs = np.zeros([image_input_idx.shape[0]], np.int32)
            sorted_patch_ixs[patch_order[valid]] = np.arange(
                n_valid_patches, dtype=np.int32
            )
            sorted_patch_ixs_ex = np.full(np.shape(patch_order), -1)
            sorted_patch_ixs_ex[valid] = sorted_patch_ixs

            valid = (sorted_patch_ixs_ex >= 0).astype(np.int32)
            image_input_idx = image_input_idx[sorted_patch_ixs_ex * valid]
            image_input_idx = image_input_idx * valid - 10000 * (1 - valid)

        return np.reshape(image_input_idx, [-1, tokens_per_image])

    def crop(self, image: np.ndarray):
        """Crops a single image.

        Returns:
            crops: (n_crops, n_patches, patch_dim) individual crops, `n_crops` might
                change between images but the other dimension are fixed
            tokens: (n_tokens,) int32 tokens, pad tokens indicate where to insert the
                patch features, might include other special tokens as well
            image_idx: (n_crops, n_patches) index in `tokens` to put the patch features
                from the crops after pooling, negative values indicates patches features
                to exclude
            padding_mask: (n_crops, n_patches) what percent of each crop is padding,
                can be None if the image mask is not being used.
        """
        if self.cropping_method == CroppingMethod.RESIZE:
            crops, tokens, patch_ordering, mask = self.base_resize_cropping(image)
        elif self.cropping_method == CroppingMethod.OVERLAP_AND_RESIZE:
            crops, tokens, patch_ordering, mask = (
                self.molmo_overlap_and_resize_cropping(image)
            )
        elif self.cropping_method == CroppingMethod.ADAPTIVE_SLICING:
            crops, tokens, patch_ordering, mask = self.minicpm_adaptive_slicing(
                image, with_thumbnail=False
            )
        else:
            crops, tokens, patch_ordering, mask = self.minicpm_adaptive_slicing(
                image, with_thumbnail=True
            )
        image_input_idx = self.build_image_input_idx(tokens, patch_ordering)
        return crops, tokens, image_input_idx, mask

    def set_special_token_ids(
        self,
        patch_token_id: int,
        column_token_id: int,
        start_token_id: int,
        end_token_id: int,
    ):
        self.patch_token_id = patch_token_id
        self.column_token_id = column_token_id
        self.start_token_id = start_token_id
        self.end_token_id = end_token_id

    def _resolve_images_kwargs(
        self, **kwargs: Unpack[JinaVLMImagesKwargs]
    ) -> JinaVLMImagesKwargs:
        max_crops = self.max_crops
        if 'max_crops' in kwargs and kwargs['max_crops'] is not None:
            max_crops = kwargs['max_crops']

        min_pixels = self.min_pixels
        if 'min_pixels' in kwargs and kwargs['min_pixels'] is not None:
            min_pixels = kwargs['min_pixels']
        max_pixels = self.max_pixels
        if 'max_pixels' in kwargs and kwargs['max_pixels'] is not None:
            max_pixels = kwargs['max_pixels']
        size = None
        if 'size' in kwargs:
            size = kwargs['size']

        if size is not None and (
            'shortest_edge' not in size or 'longest_edge' not in size
        ):
            raise ValueError(
                "Agument size must contain 'shortest_edge' and 'longest_edge' keys."
            )
        elif min_pixels is not None and max_pixels is not None:
            size = {'shortest_edge': min_pixels, 'longest_edge': max_pixels}
        else:
            size = {**self.size}
        min_pixels = size['shortest_edge']
        max_pixels = size['longest_edge']
        do_resize = self.do_resize
        if 'do_resize' in kwargs and kwargs['do_resize'] is not None:
            do_resize = kwargs['do_resize']
        do_convert_rgb = self.do_convert_rgb
        if 'do_convert_rgb' in kwargs and kwargs['do_convert_rgb'] is not None:
            do_convert_rgb = kwargs['do_convert_rgb']
        input_data_format = None
        if 'input_data_format' in kwargs:
            input_data_format = kwargs['input_data_format']

        return JinaVLMImagesKwargs(
            do_convert_rgb=do_convert_rgb,
            do_resize=do_resize,
            min_pixels=min_pixels,
            max_pixels=max_pixels,
            size=size,
            max_crops=max_crops,
            input_data_format=input_data_format,
        )

    def get_n_image_patches(
        self,
        height: int,
        width: int,
        **kwargs: Unpack[JinaVLMImagesKwargs],
    ) -> int:
        """A utility that returns number of image patches for a given image size.

        Args:
            height (`int`):
                Height of the input image.
            width (`int`):
                Width of the input image.
            **kwargs (`dict`, *optional*)
                Any kwargs to override defaults of the image processor.
        Returns:
            `int`: Number of image patches
        """
        if self.cropping_method != CroppingMethod.OVERLAP_AND_RESIZE:
            raise NotImplementedError(
                'Function is only implemented for cropping method '
                f'{CroppingMethod.OVERLAP_AND_RESIZE}'
            )
        kwargs = self._resolve_images_kwargs(**kwargs)
        do_resize = kwargs['do_resize']
        size = kwargs['size']
        max_crops = kwargs['max_crops']
        if do_resize:
            height, width = smart_resize(
                height,
                width,
                factor=self.patch_size,
                min_pixels=size['shortest_edge'],
                max_pixels=size['longest_edge'],
            )

        if self.cropping_method == CroppingMethod.RESIZE:
            return self.base_get_n_image_patches(height, width, max_crops)
        elif self.cropping_method == CroppingMethod.OVERLAP_AND_RESIZE:
            return self.molmo_get_n_image_patches(height, width, max_crops)
        elif self.cropping_method == CroppingMethod.ADAPTIVE_SLICING:
            return self.minicpm_get_n_image_patches(height, width, max_crops)
        return self.minicpm_get_n_image_patches(
            height, width, max_crops, with_thumbnail=True
        )

    def preprocess(
        self,
        images: ImageInput,
        **kwargs: Unpack[JinaVLMImagesKwargs],
    ) -> Dict[str, List[np.ndarray]]:
        """Preprocess an image or batch of images."""
        if images is None or len(images) == 0:
            return {
                'image_crops': [],
                'image_tokens': [],
                'image_input_idx': [],
                'image_padding_mask': [],
            }
        kwargs = self._resolve_images_kwargs(**kwargs)
        do_convert_rgb = kwargs['do_convert_rgb']
        do_resize = kwargs['do_resize']
        input_data_format = kwargs['input_data_format']
        size = kwargs['size']
        self.max_crops = kwargs['max_crops']

        # noinspection PyTypeChecker
        images = self.fetch_images(images)
        images = make_flat_list_of_images(images)
        if not valid_images(images):
            raise ValueError(
                'Invalid image type. Must be of type PIL.Image.Image, numpy.ndarray '
                'or torch.Tensor'
            )
        if do_convert_rgb:
            images = [convert_to_rgb(image) for image in images]

        # All transformations expect numpy arrays
        images = [to_numpy_array(image) for image in images]
        if input_data_format is None:
            # We assume that all images have the same channel dimension format.
            input_data_format = infer_channel_dimension_format(images[0])

        data = []
        for image in images:
            if do_resize:
                height, width = get_image_size(image, channel_dim=input_data_format)
                resized_height, resized_width = smart_resize(
                    height,
                    width,
                    factor=self.patch_size,
                    min_pixels=size['shortest_edge'],
                    max_pixels=size['longest_edge'],
                )
                image, _ = self.resize_image(image, [resized_height, resized_width])

            crops, tokens, image_input_idx, mask = self.crop(image)
            data.append(
                {
                    'image_crops': crops,
                    'image_tokens': tokens,
                    'image_input_idx': image_input_idx,
                    'image_padding_mask': mask,
                }
            )

        return {
            'image_crops': [d['image_crops'] for d in data],
            'image_tokens': [d['image_tokens'] for d in data],
            'image_input_idx': [d['image_input_idx'] for d in data],
            'image_padding_mask': [d['image_padding_mask'] for d in data],
        }


JinaVLMImageProcessor.register_for_auto_class()
