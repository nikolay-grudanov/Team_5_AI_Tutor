import argparse
import glob
import os
import warnings
from time import perf_counter
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import urlparse

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TOKENIZERS_PARALLELISM'] = 'false'

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoProcessor,
    GenerationConfig,
    TextStreamer,
)
from transformers.utils import is_flash_attn_2_available

TEST_IMAGE = './assets/the_persistence_of_memory.jpg'


class Timer:
    def __enter__(self):
        self.start = perf_counter()
        self.readout = None
        return self

    def __exit__(self, *_, **__):
        self.time = perf_counter() - self.start
        self.readout = f'{self.time:.3f}'


def _resolve_device_dtype_and_attn() -> Tuple[torch.device, torch.dtype, str]:
    if torch.cuda.is_available():
        device = torch.device('cuda')
        if is_flash_attn_2_available():
            dtype = torch.bfloat16
            attn_implementation = 'flash_attention_2'
        else:
            dtype = torch.float16
            attn_implementation = 'sdpa'
    else:
        if torch.backends.mps.is_available():
            device = torch.device('mps')
        else:
            device = torch.device('cpu')
        dtype = torch.float32
        attn_implementation = 'sdpa'

    return device, dtype, attn_implementation


def _build_conversations(
    images: Optional[List[str]],
    prompts: Optional[List[str]],
    map_mode: bool = False,
    prompt_first: bool = False,
    image_labels: bool = False,
):
    def _is_url(_path: str) -> bool:
        try:
            result = urlparse(_path)
            return result.scheme in ('http', 'https')
        except Exception as e:
            _ = str(e)
            return False

    images = images or []
    expanded_image_paths = []
    for path in images:
        if _is_url(path):
            expanded_image_paths.append(path)
        elif any(char in path for char in ['*', '?', '[', ']']):
            matched_files = glob.glob(path)
            if matched_files:
                expanded_image_paths.extend(sorted(matched_files))
            else:
                warnings.warn(f'No files matched pattern "{path}"')
        else:
            expanded_image_paths.append(path)
    images = expanded_image_paths
    n_images = len(images)
    if prompts is None:
        if len(images) == 0:
            images = [TEST_IMAGE]
            n_images = len(images)
        prompts = (
            ['Describe the image in 100 words']
            if n_images == 1 or map_mode
            else ['Describe the images in 100 words']
        )
    n_prompts = len(prompts)

    if n_images == 0:
        examples = [([], prompt) for prompt in prompts]
    elif n_images > 1 and n_images == n_prompts:
        examples = [([image], prompt) for image, prompt in zip(images, prompts)]
    elif map_mode:
        if n_images > 1 and n_prompts == 1:
            prompt = prompts[0]
            print(f'Map mode: Applying 1 prompt to {n_images} images')
            examples = [([image], prompt) for image in images]
        elif n_images == 1 and n_prompts > 1:
            image = images[0]
            print(f'Map mode: Applying {n_prompts} prompts to 1 image')
            examples = [([image], prompt) for prompt in prompts]
        else:
            raise ValueError(
                'Map mode requires either (multiple images + 1 prompt) or '
                '(1 image + multiple prompts). Got '
                f'{n_images} images and {n_prompts} prompts'
            )
    else:
        if n_prompts > 1:
            raise ValueError(
                'Non-map mode requires 1+ images and 1 prompt. Got '
                f'{n_images} images and {n_prompts} prompts'
            )
        examples = [(images, prompts[0])]

    conversations = []
    allimages = []
    allprompts = []
    ordinals = [
        'first',
        'second',
        'third',
        'fourth',
        'fifth',
        'sixth',
        'seventh',
        'eighth',
        'ninth',
        'tenth',
    ]
    for images, prompt in examples:
        content = []
        allimages.append(images)
        allprompts.append(prompt)
        if prompt_first:
            content.append({'type': 'text', 'text': prompt})
        if len(images) > 1 and image_labels:
            for idx, img in enumerate(images):
                ordinal = ordinals[idx] if idx < len(ordinals) else f'{idx + 1}th'
                image = images[idx]
                descriptor = f'url: {image}'
                if os.path.isfile(image):
                    descriptor = f'filename: {os.path.basename(image)}'
                content.append(
                    {
                        'type': 'text',
                        'text': f'(this is the {ordinal} image, {descriptor})',
                    }
                )
                content.append({'type': 'image', 'image': img})
        else:
            content.extend([{'type': 'image', 'image': image} for image in images])
        if not prompt_first:
            content.append({'type': 'text', 'text': prompt})
        conversations.append([{'role': 'user', 'content': content}])

    return conversations, allimages, allprompts


def _token_usage_report(
    inputs: Dict[str, Any],
    n_images: int,
    max_sequence_length: int,
    special_image_token_ids: Dict[str, int],
):
    """Report token usage statistics in tree format."""
    input_ids = inputs['input_ids']
    attention_mask = inputs['attention_mask']

    # Total tokens in sequence (non-padding)
    total_tokens = attention_mask.sum().item()

    # Count ALL image-related tokens directly from input_ids
    image_patch_id = special_image_token_ids['image_patch_token_id']
    image_start_id = special_image_token_ids['image_start_token_id']
    image_end_id = special_image_token_ids['image_end_token_id']
    image_column_token_id = special_image_token_ids['image_column_token_id']

    num_patch = (input_ids == image_patch_id).sum().item()
    num_start = (input_ids == image_start_id).sum().item()
    num_end = (input_ids == image_end_id).sum().item()
    num_col = (input_ids == image_column_token_id).sum().item()

    # Total image tokens = all image-related special tokens
    total_image_tokens = num_patch + num_start + num_end + num_col

    # Pure text tokens (excluding all image-related tokens)
    text_token_count = total_tokens - total_image_tokens

    report = [
        f'Input Context Window Layout (max: {max_sequence_length} tokens):',
        f'├── Total: {total_tokens} tokens '
        f'({((total_tokens / max_sequence_length) * 100):.1f}%)',
    ]
    # Count tokens per image by finding img_start and img_end boundaries
    # Each image is delimited by img_start and img_end tokens
    tokens_per_image_list = []

    # Find all img_start and img_end positions in input_ids
    start_positions = (input_ids == image_start_id).nonzero(as_tuple=True)[0].tolist()
    end_positions = (input_ids == image_end_id).nonzero(as_tuple=True)[0].tolist()

    if len(start_positions) > 0 and len(end_positions) > 0:
        # Each image typically has 2 start and 2 end tokens
        # Determine actual number of images in context
        n_starts_per_image = 2  # typical case
        n_images_in_context = len(start_positions) // n_starts_per_image

        # Warn if not all images fit in context
        if n_images_in_context < n_images:
            warnings.warn(
                f'Only {n_images_in_context}/{n_images} images fit in context window'
            )

        for idx in range(n_images):
            if idx < n_images_in_context:
                # Get the start and end indices for this image
                start_idx_begin = idx * n_starts_per_image
                end_idx_end = (idx + 1) * n_starts_per_image
                if start_idx_begin < len(start_positions) and end_idx_end <= len(
                    end_positions
                ):
                    # First start position and last end position define the image span
                    first_start = start_positions[start_idx_begin]
                    last_end = end_positions[end_idx_end - 1]
                    # Count tokens from first start to last end (inclusive)
                    num_tokens = last_end - first_start + 1
                    tokens_per_image_list.append(num_tokens)
                else:
                    tokens_per_image_list.append(0)
            else:
                # Image didn't fit in context
                tokens_per_image_list.append(0)
    else:
        # Fallback to uniform division if we can't find boundaries
        tokens_per_image = total_image_tokens // n_images if n_images > 0 else 0
        tokens_per_image_list = [tokens_per_image] * n_images

    for idx in range(n_images):
        n_tokens = tokens_per_image_list[idx] if idx < len(tokens_per_image_list) else 0
        pct = n_tokens / max_sequence_length * 100
        report.append(f'├── Image {idx + 1} → {n_tokens} tokens ({pct:.1f}%)')

    text_pct = text_token_count / max_sequence_length * 100
    report.append(f'└── Text: {text_token_count} tokens ({text_pct:.1f}%)')

    return '\n'.join(report)


def test_jvlm():
    parser = argparse.ArgumentParser(
        description='jina-vlm vision-language model inference.'
    )
    default_model = '.' if os.path.exists('./config.json') else 'jinaai/jina-vlm'
    parser.add_argument(
        '-m',
        '--model',
        default=default_model,
        help=(
            'Model path. Auto-detects local repo (if config.json exists) or '
            'falls back to "jinaai/jina-vlm" from HuggingFace.'
        ),
    )
    parser.add_argument(
        '-i',
        '--image',
        action='append',
        help=(
            'Image path, URL, or glob pattern (can specify multiple times, default: '
            '`[]`).'
        ),
    )
    parser.add_argument(
        '-p',
        '--prompt',
        action='append',
        help=(
            'Text prompt (can specify multiple times, default: '
            '`"Describe the image for me in 100 words"` or `"Describe the images for '
            'me in 100 words"` if multiple images are provided).'
        ),
    )
    parser.add_argument(
        '--max-crops',
        type=int,
        default=12,
        help='Maximum crops (default: `12`).',
    )
    parser.add_argument(
        '--max-tokens',
        type=int,
        default=1024,
        help='Maximum output tokens (default: `1024`).',
    )
    parser.add_argument(
        '--max-pixels',
        type=int,
        default=None,
        help=(
            'Max pixels per image, larger images are resized and the aspect ratio is '
            'preserved (default: `None`)'
        ),
    )
    parser.add_argument(
        '--stream',
        action='store_true',
        help='Enable streaming (default: `False`).',
    )
    parser.add_argument(
        '--image-labels',
        action='store_true',
        help=(
            'Enable ordinal text labels after each image (default: `False` -> '
            'no image labels for multi-image).'
        ),
    )
    parser.add_argument(
        '--prompt-first',
        action='store_true',
        help=(
            'Place prompt before images instead of after (default: `False` -> '
            'prompt after images).'
        ),
    )
    parser.add_argument(
        '--map',
        action='store_true',
        help=(
            'Map mode - apply single prompt to multiple images OR multiple prompts to '
            'single image (default: `False` -> no mapping)'
        ),
    )
    args = parser.parse_args()

    print()
    print('Welcome to the jinaai/jina-vlm playground ✨')
    print('Use this script to test our model!')
    print('- Jina AI')
    print()
    print('--- Loading the model ...')
    print('Specifying device, dtype and attention implementation ...')
    device, dtype, attn_implementation = _resolve_device_dtype_and_attn()
    print(f'Using attention implementation: {attn_implementation}')
    print(f'Using device: {device}')
    print(f'Using dtype: {dtype}')
    print('Model path: ', args.model)
    processor = AutoProcessor.from_pretrained(
        args.model,
        trust_remote_code=True,
        use_fast=False,
    )
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        trust_remote_code=True,
        dtype=dtype,
        low_cpu_mem_usage=True,
        device_map=device.type,
        attn_implementation=attn_implementation,
    )
    max_sequence_length = getattr(model.config, 'max_sequence_length', 40960)
    n_params = sum(p.numel() for p in model.parameters())
    print(f'Max sequence length: {max_sequence_length}')
    print(f'Number of parameters: {n_params}')
    print('Done ✅')
    print()

    print("--- Let's create some conversations ...")
    conversations, images, prompts = _build_conversations(
        args.image,
        args.prompt,
        map_mode=args.map,
        prompt_first=args.prompt_first,
        image_labels=args.image_labels,
    )
    n_conversations = len(conversations)
    print(f'Built {n_conversations} conversations 🚀')
    print()

    print('--- Transforming conversations to numbers ...')
    timer = Timer()
    with timer:
        texts = processor.apply_chat_template(conversations, add_generation_prompt=True)
        inputs = processor(
            text=texts,
            images=images,
            padding='longest',
            max_length=max_sequence_length,
            max_crops=args.max_crops,
            max_pixels=args.max_pixels,
            do_resize=True if args.max_pixels is not None else False,
            return_tensors='pt',
        )
        texts = texts if isinstance(texts, list) else [texts]
        device_inputs = {}
        for k, v in inputs.items():
            if k == 'labels':
                continue
            if isinstance(v, torch.Tensor):
                if v.is_floating_point():
                    device_inputs[k] = v.to(device, dtype=dtype, non_blocking=True)
                else:
                    device_inputs[k] = v.to(device, non_blocking=True)
            else:
                device_inputs[k] = v

    processing_time = timer.readout
    special_image_token_ids = {
        'image_patch_token_id': processor.image_patch_token_id,
        'image_start_token_id': processor.image_start_token_id,
        'image_end_token_id': processor.image_end_token_id,
        'image_column_token_id': processor.image_column_token_id,
    }
    token_usage_reports = []
    for idx in range(n_conversations):
        ith_inputs = {k: v[idx] for k, v in inputs.items()}
        token_usage_report = _token_usage_report(
            ith_inputs,
            len(images[idx]),
            max_sequence_length=max_sequence_length,
            special_image_token_ids=special_image_token_ids,
        )
        token_usage_reports.append(token_usage_report)
    print(f'Processed {n_conversations} conversations in {processing_time}s')
    print('All done 🪄')
    print()

    print('--- Running inference ...')
    generated_tokens = 0
    input_prompts = inputs['input_ids']

    if args.stream:
        print('Streaming mode')
        print('Inference will run sequentially')
        print()

        streamer = TextStreamer(
            processor.tokenizer, skip_prompt=True, skip_special_tokens=True
        )
        generation_time = 0.0
        for idx in range(n_conversations):
            print(f'* Conversation {idx + 1}/{n_conversations}')
            print(f'├── 🖼️Images: {images[idx]}')
            print(f'├── 📜Prompt: {prompts[idx]}')
            print(f'├── 💬Chat:{texts[idx]}')
            print('└── 🧠Response:', end='')
            ith_inputs = {k: v[idx].unsqueeze(0) for k, v in device_inputs.items()}
            with (
                timer,
                torch.no_grad(),
                torch.autocast(
                    device.type, enabled=(device.type != 'mps'), dtype=dtype
                ),
            ):
                output = model.generate(
                    **ith_inputs,
                    streamer=streamer,
                    generation_config=GenerationConfig(
                        max_new_tokens=args.max_tokens,
                        do_sample=False,
                    ),
                    return_dict_in_generate=True,
                    use_model_defaults=True,
                )
            generation_time += timer.time

            out = output.sequences[0][len(input_prompts[idx].tolist()) :]
            generated_tokens += len(out)
            print('Token usage report:')
            print(token_usage_reports[idx])
            print()
    else:
        print('Non-streaming mode')
        print('Inference will run in a batch')
        print()

        with (
            timer,
            torch.no_grad(),
            torch.autocast(device.type, enabled=(device.type != 'mps'), dtype=dtype),
        ):
            output = model.generate(
                **device_inputs,
                generation_config=GenerationConfig(
                    max_new_tokens=args.max_tokens,
                    do_sample=False,
                ),
                return_dict_in_generate=True,
                use_model_defaults=True,
            )
        generation_time = timer.time

        for idx in range(n_conversations):
            out = output.sequences[idx][len(input_prompts[idx].tolist()) :]
            generated_tokens += len(out)
            response = processor.tokenizer.decode(out, skip_special_tokens=True)
            print(f'* Conversation {idx + 1}/{n_conversations}')
            print(f'├── 🖼️Images: {images[idx]}')
            print(f'├── 📜Prompt: {prompts[idx]}')
            print(f'├── 💬Chat:{texts[idx]}')
            print(f'└── 🧠Response:{response}')
            print('Token usage report:')
            print(token_usage_reports[idx])
            print()

    res_per_sec = n_conversations / generation_time if generation_time > 0 else 0
    tok_per_sec = generated_tokens / generation_time if generation_time > 0 else 0
    print(f'Generated {n_conversations} responses in {generation_time:.3f}s')
    print(f'{res_per_sec:.2f} res/s {tok_per_sec:.2f} tok/s')
    print('Done ✅')


if __name__ == '__main__':
    test_jvlm()
