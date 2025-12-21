# Copyright 2025 Jina AI. All rights reserved.

from collections import defaultdict
from typing import Dict, List, Optional, Sequence, Tuple, TypedDict, Union

import numpy as np
from transformers import PreTrainedTokenizer
from transformers.feature_extraction_utils import BatchFeature
from transformers.image_utils import ImageInput
from transformers.processing_utils import (
    AllKwargsForChatTemplate,
    CommonKwargs,
    MultiModalData,
    ProcessorMixin,
    Unpack,
)
from transformers.tokenization_utils_base import (
    PaddingStrategy,
    PreTokenizedInput,
    TextInput,
)

from .image_processing_jvlm import JinaVLMImageProcessor, JinaVLMImagesKwargs


class JinaVLMTextKwargs(TypedDict, total=False):
    """
    Attributes:
        padding (`bool`, `str` or [`~utils.PaddingStrategy`], *optional*)
            Activates and controls padding.
        max_length (`int`, *optional*):
            Controls the maximum length to use by one of the truncation/padding
            parameters.
        is_split_into_words (`bool`, *optional*):
            Whether or not the input is already pre-tokenized.
    """

    padding: Union[bool, str, PaddingStrategy]
    padding_side: Optional[str]
    max_length: Optional[int]
    is_split_into_words: Optional[bool]


class JinaVLMProcessingKwargs(JinaVLMTextKwargs, JinaVLMImagesKwargs, CommonKwargs):
    return_labels: Optional[bool]


class JinaVLMProcessor(ProcessorMixin):
    r"""Constructs a JinaVLM processor which wraps a JinaVLM image processor and a
    tokenizer into a single processor.

    Args:
        image_processor ([`JinaVLMImageProcessor`], *optional*):
            The image processor is a required input.
        tokenizer ([`AutoTokenizer`], *optional*):
            The tokenizer is a required input.
        chat_template (`str`, *optional*):
            A Jinja template which will be used to convert lists of messages in a chat
            into a tokenizable string.
    """

    attributes = ['image_processor', 'tokenizer']
    image_processor_class = 'AutoImageProcessor'
    tokenizer_class = 'AutoTokenizer'

    IMAGE_PATCH_TOKEN = '<im_patch>'
    IMAGE_START_TOKEN = '<im_start>'
    IMAGE_END_TOKEN = '<im_end>'
    IMAGE_COLUMN_TOKEN = '<im_col>'
    IMAGE_PROMPT_TOKEN = '<|image|>'
    IMAGE_SLICE_TOKEN = '<im_slice>'
    EXTRA_TOKENS = (
        IMAGE_PATCH_TOKEN,
        IMAGE_START_TOKEN,
        IMAGE_END_TOKEN,
        IMAGE_COLUMN_TOKEN,
        IMAGE_PROMPT_TOKEN,
        IMAGE_SLICE_TOKEN,
    )

    TEXT_KEYS = [
        'input_ids',
        'labels',
    ]
    IMAGE_KEYS = [
        'images',
        'image_masks',
        'image_input_idx',
    ]

    def __init__(
        self,
        image_processor: JinaVLMImageProcessor,
        tokenizer: PreTrainedTokenizer,
        chat_template=None,
        always_start_with_space: bool = False,
        **_,
    ):
        self.image_processor: JinaVLMImageProcessor = image_processor
        self.tokenizer: PreTrainedTokenizer = tokenizer
        super().__init__(image_processor, tokenizer, chat_template=chat_template)

        self.special_token_ids = self.get_special_token_ids()
        self.image_patch_token_id = self.special_token_ids[self.IMAGE_PATCH_TOKEN]
        self.image_start_token_id = self.special_token_ids[self.IMAGE_START_TOKEN]
        self.image_end_token_id = self.special_token_ids[self.IMAGE_END_TOKEN]
        self.image_column_token_id = self.special_token_ids[self.IMAGE_COLUMN_TOKEN]
        self.image_prompt_token_id = self.special_token_ids[self.IMAGE_PROMPT_TOKEN]
        self.image_slice_token_id = self.special_token_ids[self.IMAGE_SLICE_TOKEN]
        self.image_processor.set_special_token_ids(
            patch_token_id=self.image_patch_token_id,
            start_token_id=self.image_start_token_id,
            end_token_id=self.image_end_token_id,
            column_token_id=self.image_column_token_id,
        )
        self.max_sequence_length = self.tokenizer.model_max_length or 4096
        self.max_crops = self.image_processor.max_crops
        self.always_start_with_space = always_start_with_space

    def get_special_token_ids(self) -> Dict[str, int]:
        special_token_ids = {}
        for token in self.EXTRA_TOKENS:
            if token not in self.tokenizer.get_vocab():
                raise ValueError(
                    f'Image token {token} not found in the tokenizer vocabulary. '
                    'Make sure the tokenizer is trained with extra tokens '
                    f'{self.EXTRA_TOKENS}.'
                )
            token_ids = self.tokenizer.encode(token, add_special_tokens=False)
            assert len(token_ids) == 1
            special_token_ids[token] = token_ids[0]

        return special_token_ids

    @staticmethod
    def _pad_np_sequences(
        tensors: Sequence[Optional[np.ndarray]],
        max_sequence_length: int,
        dtype: Optional[np.dtype] = None,
        pad: Union[
            PaddingStrategy.MAX_LENGTH, PaddingStrategy.LONGEST
        ] = PaddingStrategy.MAX_LENGTH,
        pad_value: int = -1,
        padding_side: str = 'right',
    ) -> Tuple[np.ndarray, np.ndarray]:
        if pad == PaddingStrategy.MAX_LENGTH:
            max_len = max_sequence_length
            tensor = [x for x in tensors if x is not None][0]
            arr = np.full(
                [len(tensors), max_sequence_length] + list(tensor.shape[1:]),
                pad_value,
                dtype=dtype or tensor.dtype,
            )
        else:
            max_len = max((0 if x is None else x.shape[0]) for x in tensors)
            max_len = min(max_len, max_sequence_length)
            arr = np.full(
                [len(tensors), max_len] + list(tensors[0].shape[1:]),
                pad_value,
                dtype=dtype or tensors[0].dtype,
            )

        padlens = np.zeros(len(tensors), dtype=np.int32)
        for ix, tensor in enumerate(tensors):
            if tensor is not None and len(tensor) > 0:
                padlens[ix] = max_len - min(len(tensor), max_len)
                if padding_side == 'left':
                    arr[ix, -len(tensor) :] = tensor[:max_len]
                else:
                    arr[ix, : len(tensor)] = tensor[:max_len]

        return arr, padlens

    def _collate(
        self,
        batch: Dict[str, List[Optional[np.ndarray]]],
        text_max_sequence_length: Optional[int] = None,
        image_max_sequence_length: Optional[int] = None,
        padding: Union[
            PaddingStrategy.MAX_LENGTH, PaddingStrategy.LONGEST
        ] = PaddingStrategy.MAX_LENGTH,
        padding_side: str = 'right',
        pad_value: int = -1,
    ):
        out = {}
        padlens = {}
        for key, value in batch.items():
            _padding_side = 'right'
            if key in self.TEXT_KEYS:
                _padding_side = padding_side
                max_len = text_max_sequence_length
                dtype = np.int64
            elif key in self.IMAGE_KEYS:
                max_len = image_max_sequence_length
                dtype = np.int64
                if key == 'images':
                    dtype = np.float32
            else:
                continue
            out[key], padlens[key] = self._pad_np_sequences(
                value,
                max_len,
                dtype=dtype,
                pad=padding,
                pad_value=pad_value,
                padding_side=_padding_side,
            )

        input_ids: np.ndarray = out['input_ids']
        attention_mask = input_ids != -1
        out['attention_mask'] = attention_mask

        input_ids_padlens = padlens['input_ids']
        image_input_idx = out.get('image_input_idx', None)
        if image_input_idx is not None and padding_side == 'left':
            n_crops, n_image_tokens = image_input_idx.shape[1:3]
            shift = input_ids_padlens[:, np.newaxis, np.newaxis]
            shift = np.repeat(shift, n_image_tokens, axis=2)
            shift = np.repeat(shift, n_crops, axis=1)
            image_input_idx[image_input_idx < 0] = -text_max_sequence_length
            image_input_idx = image_input_idx + shift
            out['image_input_idx'] = image_input_idx

        if text_max_sequence_length is not None:
            image_input_idx = out.get('image_input_idx', [])
            n = len(image_input_idx)
            for i in range(n):
                arr = image_input_idx[i]
                if arr.ndim > 0 and arr.size > 0:
                    n_image_tokens = arr.max()
                    if n_image_tokens > text_max_sequence_length - 3:
                        raise RuntimeError(
                            'Image tokens truncation at sequence boundary. Max '
                            f'sequence length ({text_max_sequence_length}) is too '
                            'small to fit the generated image tokens '
                            f'({n_image_tokens}). Consider increasing the max '
                            'sequence length or tweaking the image processing '
                            'parameters (`max_crops`, `max_pixels`) to reduce the '
                            'number of image tokens.'
                        )

        return out

    def apply_chat_template(
        self,
        conversation: Union[List[Dict[str, str]], List[List[Dict[str, str]]]],
        chat_template: Optional[str] = None,
        **kwargs: Unpack[AllKwargsForChatTemplate],
    ) -> str:
        return super().apply_chat_template(
            conversation,
            chat_template=chat_template,
            always_start_with_space=self.always_start_with_space,
            image_prompt_token=self.IMAGE_PROMPT_TOKEN,
            **kwargs,
        )

    def _interleave_text_and_image_tokens(
        self,
        token_ids: np.ndarray,
        image_crops: List[np.ndarray],
        image_tokens: List[np.ndarray],
        image_input_idx: List[np.ndarray],
        image_padding_mask: List[np.ndarray],
        return_labels: bool = False,
        add_empty_image_features: bool = False,
    ):
        """Interleave images and text tokens into multi-modal features for the model."""
        if len(image_crops) == 0:
            input_ids = token_ids
            target_tokens = input_ids
            ends_with_eos = input_ids[-1] == self.tokenizer.eos_token_id
            bos = self.tokenizer.bos_token_id or self.tokenizer.eos_token_id
            # noinspection PyTypeChecker
            input_ids = np.pad(input_ids, [[1, 0]], constant_values=bos)
            if ends_with_eos:
                input_ids = input_ids[:-1]
            else:
                # We are presumably doing inference since the messages end with user
                # response instead of a target response, so these fields should not be
                # used, but pad them anyway just so everything is a consistent length
                # noinspection PyTypeChecker
                target_tokens = np.pad(target_tokens, [[0, 1]], constant_values=-1)

            position_ids = np.arange(len(input_ids), dtype=np.int64)
            data = {
                'input_ids': input_ids,
                'position_ids': position_ids,
            }
            if return_labels:
                data['labels'] = target_tokens
            if add_empty_image_features:
                # Add size-zero image features, this can be useful to make sure all
                # devices get an image input when the image ViT is FSDP wrapped
                tokens_per_image = self.image_processor.tokens_per_image
                patch_size = self.image_processor.patch_size
                n_pixels = patch_size**2 * 3
                h, w = self.image_processor.base_input_size
                n_patches = (h // patch_size) * (w // patch_size)
                crops = np.zeros((0, n_patches, n_pixels), dtype=np.float32)
                image_idx = np.zeros((0, tokens_per_image), np.int32)
                image_masks = np.zeros((0, n_patches), dtype=np.float32)
                data.update(
                    dict(
                        images=crops,
                        image_input_idx=image_idx,
                        image_masks=image_masks,
                    )
                )
            return data

        n = len(image_crops)
        assert n == len(image_tokens) == len(image_input_idx) == len(image_padding_mask)
        image_idx = np.argwhere(token_ids == self.image_prompt_token_id)
        if len(image_idx) == 0:
            image_idx = [-1] * n
        else:
            image_idx = image_idx[:, 0]
            assert len(image_idx) == n

        all_tokens = []
        all_image_crops = []
        all_image_input_idx = []
        all_image_padding_masks = []
        cumulative_image_idx = 0

        for ix in range(n):
            token_ix = image_idx[ix]
            if token_ix == -1:  # -1 is an image inserted at the very start
                start = 0
                token_ix = 0
            else:
                start = 0 if ix == 0 else image_idx[ix - 1] + 1

            _img_crops = image_crops[ix]
            _img_tokens = image_tokens[ix]
            _img_input_idx = image_input_idx[ix]
            _img_padding_mask = image_padding_mask[ix]
            all_image_input_idx.append(_img_input_idx + token_ix + cumulative_image_idx)
            all_image_crops.append(_img_crops)
            all_image_padding_masks.append(_img_padding_mask)
            all_tokens.append(token_ids[start:token_ix])
            all_tokens.append(_img_tokens)

            # -1 because the first token is already in the input as general image token
            # and is replace by the img_start token
            cumulative_image_idx += len(_img_tokens) - 1

        end = image_idx[-1] + 1
        all_tokens.append(token_ids[end:])

        input_ids = np.concatenate(all_tokens, 0)
        images = np.concatenate(all_image_crops, 0)
        image_input_idx = np.concatenate(all_image_input_idx, 0)
        image_masks = np.concatenate(all_image_padding_masks, 0)

        target_tokens = input_ids
        ends_with_eos = input_ids[-1] == self.tokenizer.eos_token_id
        bos = self.tokenizer.bos_token_id or self.tokenizer.eos_token_id
        # noinspection PyTypeChecker
        input_ids = np.pad(input_ids, [[1, 0]], constant_values=bos)
        if ends_with_eos:
            input_ids = input_ids[:-1]
        else:
            # We are presumably doing inference since the messages end with user
            # response instead of a target response, so these fields should not be used,
            # but pad them anyway just so everything is a consistent length
            # noinspection PyTypeChecker
            target_tokens = np.pad(target_tokens, [[0, 1]], constant_values=-1)

        image_input_idx = np.where(
            image_input_idx < 0, image_input_idx, image_input_idx + 1
        )
        position_ids = np.arange(len(input_ids), dtype=np.int64)
        data = {
            'input_ids': input_ids,
            'position_ids': position_ids,
            'images': images,
            'image_input_idx': image_input_idx,
            'image_masks': image_masks,
        }
        if return_labels:
            data['labels'] = target_tokens
        return data

    def __call__(
        self,
        images: Union[None, ImageInput, List[ImageInput]] = None,
        text: Union[
            None, TextInput, PreTokenizedInput, list[TextInput], list[PreTokenizedInput]
        ] = None,
        **kwargs: Unpack[JinaVLMProcessingKwargs],
    ) -> BatchFeature:
        """Main method to prepare for the model one or several sequences(s) and
        image(s). This method forwards the `text` and `kwargs` arguments to  the
        tokenizr if `text` is not `None` to encode the text. To prepare the vision
        inputs, this method forwards the `images` and `kwargs` arguments the image
        processor if `images` is not `None`.

        Args:
            images (
                `PIL.Image.Image`,
                `np.ndarray`,
                `torch.Tensor`,
                `list[PIL.Image.Image]`,
                `list[np.ndarray]`,
                `list[torch.Tensor]`
                `list[list[PIL.Image.Image]]`,
                `list[list[np.ndarray]]`,
                `list[list[torch.Tensor]]`
            ):
                The image or batch of images to be prepared. Each image can be a PIL
                image, NumPy array or PyTorch tensor. Both channels-first and
                channels-last formats are supported.
            text (`str`, `list[str]`, `list[list[str]]`):
                The sequence or batch of sequences to be encoded. Each sequence can be
                a string or a list of strings (pretokenized string). If the sequences
                are provided as list of strings (pretokenized), you must set
                `is_split_into_words=True` (to lift the ambiguity with a batch of
                sequences).
            return_tensors (`str` or [`~utils.TensorType`], *optional*):
                If set, will return tensors of a particular framework. Acceptable values
                are:
                - `'pt'`: Return PyTorch `torch.Tensor` objects.
                - `'np'`: Return NumPy `np.ndarray` objects.

        Returns:
            [`BatchFeature`]: A [`BatchFeature`] with the fields required for
            inference.
        """
        if text is None:
            raise ValueError('Processor requires text input.')

        return_tensors = kwargs.pop('return_tensors', None)
        return_labels = kwargs.pop('return_labels', False)
        padding = kwargs.pop('padding', PaddingStrategy.LONGEST)
        padding_side = kwargs.pop('padding_side', 'left')
        max_length = kwargs.pop('max_length', None)
        max_crops = kwargs.get('max_crops', None)

        images_kwargs = {}
        text_kwargs = {}
        unexpected_kwargs = {}
        for k, v in kwargs.items():
            if k in JinaVLMImagesKwargs.__annotations__:
                images_kwargs[k] = v
            elif k in JinaVLMTextKwargs.__annotations__:
                text_kwargs[k] = v
            else:
                unexpected_kwargs[k] = v

        text_inputs = self.tokenizer(
            text,
            truncation=None,
            padding=PaddingStrategy.DO_NOT_PAD,
            max_length=None,
            return_tensors='np',
            return_attention_mask=False,
            add_special_tokens=False,
            **text_kwargs,
        )
        token_ids = text_inputs['input_ids']
        batch_size = token_ids.shape[0]
        images = images or [[] for _ in range(batch_size)]

        if batch_size == 1:
            if isinstance(images, list):
                if isinstance(images[0], list):
                    if len(images) != 1:
                        raise ValueError(
                            'When given a single text, the processor expects a nested '
                            'list of images to have outer length of 1 '
                            f'(got {len(images)})'
                        )
                else:
                    images = [images]
            else:
                images = [[images]]
        else:
            if isinstance(images, list):
                if len(images) != batch_size:
                    raise ValueError(
                        f'When given multiple ({batch_size}) texts, the processor '
                        f'expects a list of images or a list of list of images with '
                        f'outer length {batch_size} (got {len(images)})'
                    )
                images = [elm if isinstance(elm, list) else [elm] for elm in images]
            else:
                raise ValueError(
                    'When given multiple texts, the processor expects a list of '
                    f'images or a list of list of images, got {type(images)} instead'
                )

        outputs = defaultdict(list)
        n_images = []
        for idx in range(batch_size):
            _token_ids = token_ids[idx]
            _images = images[idx]
            n_images.append(len(_images))
            image_inputs = self.image_processor(_images, **images_kwargs)
            image_crops = image_inputs['image_crops']
            image_tokens = image_inputs['image_tokens']
            image_input_idx = image_inputs['image_input_idx']
            image_padding_mask = image_inputs.get('image_padding_mask')
            output = self._interleave_text_and_image_tokens(
                _token_ids,
                image_crops,
                image_tokens,
                image_input_idx,
                image_padding_mask if image_padding_mask is not None else [],
                add_empty_image_features=(batch_size > 1),
                return_labels=return_labels,
            )
            for k, v in output.items():
                outputs[k].append(v)

        if padding != PaddingStrategy.DO_NOT_PAD:
            text_max_sequence_length = max_length or self.max_sequence_length
            max_crops = max_crops or self.max_crops
            max_n_images = max(n_images)
            image_max_sequence_length = (max_crops + 1) * max_n_images
            outputs = self._collate(
                outputs,
                text_max_sequence_length=text_max_sequence_length,
                image_max_sequence_length=image_max_sequence_length,
                padding=padding,
                padding_side=padding_side,
            )
        return BatchFeature(data=outputs, tensor_type=return_tensors)

    def _get_num_multimodal_tokens(
        self,
        image_sizes: Optional[List[List[int]]] = None,
        **kwargs: Unpack[JinaVLMImagesKwargs],
    ) -> MultiModalData:
        """Computes the number of placeholder tokens needed for multimodal inputs with
        the given sizes.

        Args:
            image_sizes (`list[list[int]]`, *optional*):
                The input sizes formatted as (height, width) per each image.
        Returns:
            `MultiModalData`: A `MultiModalData` object holding number of tokens per
            each of the provided input modalities, along with other useful data.
        """
        data = {}
        if image_sizes is not None:
            n_patches = [
                self.image_processor.get_n_image_patches(h, w, **kwargs)
                for h, w in image_sizes
            ]
            data.update({'num_image_tokens': n_patches, 'num_image_patches': n_patches})
        return MultiModalData(**data)


JinaVLMProcessor.register_for_auto_class()
