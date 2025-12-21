from typing import List, Optional, Union

from PIL import Image
import torch
from transformers.image_processing_base import BatchFeature
from transformers.image_processing_utils_fast import (BaseImageProcessorFast,
                                                      divide_to_patches)
from transformers.image_utils import (ChannelDimension, SizeDict,
                                      get_image_size, make_list_of_images,
                                      get_image_type, ImageInput, ImageType)
from transformers.utils import TensorType


def find_closest_aspect_ratio(aspect_ratio, target_ratios, width, height, image_size):
    best_factor = float('-inf')
    best_ratio = (1, 1)
    area = width * height
    for ratio in target_ratios:
        target_aspect_ratio = ratio[0] / ratio[1]
        factor_based_on_area_n_ratio = min(
            (ratio[0]*ratio[1]*image_size*image_size)/ area, 0.6
            )* min(
                target_aspect_ratio/aspect_ratio, aspect_ratio/target_aspect_ratio)
        if factor_based_on_area_n_ratio > best_factor:
            best_factor = factor_based_on_area_n_ratio
            best_ratio = ratio
    return best_ratio


class LlamaNemotronNanoVLImageProcessor(BaseImageProcessorFast):
    model_input_names = ["pixel_values"]

    def __init__(self, image_size=512, max_num_tiles=12, use_thumbnail=True, **kwargs):
        super().__init__(**kwargs)
        self.image_size = image_size
        self.max_num_tiles = max_num_tiles
        self.use_thumbnail = use_thumbnail

    # Based on https://github.com/OpenGVLab/InternVL/blob/c62fa4f7c850165d7386bdc48ac6bc5a6fab0864/internvl_chat/internvl/train/dataset.py#L702
    def dynamic_preprocess(self, image, image_size=448, max_num_tiles=12, use_thumbnail=False):
        orig_height, orig_width = get_image_size(image, channel_dim=ChannelDimension.FIRST)
        aspect_ratio = orig_width / orig_height

        # calculate the existing image aspect ratio
        target_ratios = set(
            (i, j) for n in range(1, max_num_tiles + 1) for i in range(1, n + 1) for j in range(1, n + 1) if
            i * j <= max_num_tiles and i * j >= 1)
        target_ratios = sorted(target_ratios, key=lambda x: x[0] * x[1])

        # find the closest aspect ratio to the target
        target_aspect_ratio = find_closest_aspect_ratio(
            aspect_ratio, target_ratios, orig_width, orig_height, image_size)

        # calculate the target width and height
        target_width = image_size * target_aspect_ratio[0]
        target_height = image_size * target_aspect_ratio[1]

        resized_img = self.resize(image, SizeDict(height=target_height, width=target_width))
        patches = divide_to_patches(resized_img, image_size)
        if use_thumbnail and len(patches) != 1:
            patches.append(self.resize(image, SizeDict(height=image_size, width=image_size)))

        return patches

    def _process_image(
        self,
        image: ImageInput,
        **kwargs,
    ) -> torch.Tensor:
        image_type = get_image_type(image)
        if image_type not in [ImageType.PIL]:
            raise ValueError(f"Unsupported input image type {image_type}. Only PIL images supported")
        image = image.resize((image.width * 2, image.height * 2), Image.BILINEAR)
        return super()._process_image(image, **kwargs)

    def _preprocess(
        self,
        images: List[torch.Tensor],
        image_size: int = None,
        max_num_tiles: int = None,
        use_thumbnail: bool = None,
        do_rescale: bool = None,
        return_tensors: Optional[Union[str, TensorType]] = None,
        **kwargs,
    ) -> List[torch.Tensor]:
        image_size = image_size if image_size is not None else self.image_size
        max_num_tiles = max_num_tiles if max_num_tiles is not None else self.max_num_tiles
        use_thumbnail = use_thumbnail if use_thumbnail is not None else self.use_thumbnail
        do_rescale = do_rescale if do_rescale is not None else self.do_rescale

        images = make_list_of_images(images)

        all_patches = []
        num_patches = []
        for image in images:
            patches = self.dynamic_preprocess(
                image, image_size, max_num_tiles, use_thumbnail
            )
            all_patches.extend(patches)
            num_patches.append(len(patches))

        pixel_values = torch.stack(all_patches, dim=0)
        pixel_values = self.rescale_and_normalize(
            pixel_values,
            do_rescale,
            self.rescale_factor,
            do_normalize=self.do_normalize,
            image_mean=self.image_mean,
            image_std=self.image_std
        )

        return BatchFeature(data={"pixel_values": pixel_values, "num_patches": num_patches}, tensor_type=return_tensors)
