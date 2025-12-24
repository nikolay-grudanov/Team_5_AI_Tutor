---
license: other
license_name: nvidia-open-model-license
license_link: >-
  https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/
pipeline_tag: image-text-to-text
library_name: transformers
tags:
  - nvidia
  - VLM
  - llama3.1
---

# Llama-3.1-Nemotron-Nano-VL-8B-V1

## Model Overview

### Description

 Llama Nemotron Nano VL is a leading document intelligence vision language model (VLMs) that enables the ability to query and summarize images from the physical or virtual world. Llama Nemotron Nano VL is deployable in the data center, cloud and at the edge, including Jetson Orin and laptop by AWQ 4bit quantization through TinyChat framework. We find: (1) image-text pairs are not enough, interleaved image-text is essential; (2) unfreezing LLM during interleaved image-text pre-training enables in-context learning; (3)re-blending text-only instruction data is crucial to boost both VLM and text-only performance.

This model was trained on commercial images for all three stages of training and supports single image inference.

<b>Note:</b> NVIDIA Nemotron Nano v2 12B VL is now available on Huggingface in the [BF16](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-BF16), [FP8](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-FP8) and [NVFP4-QAD](https://huggingface.co/nvidia/NVIDIA-Nemotron-Nano-12B-v2-VL-NVFP4-QAD) formats.


### License/Terms of Use
**Governing Terms:**  

Your use of the model is governed by the [NVIDIA Open License Agreement](https://www.nvidia.com/en-us/agreements/enterprise-software/nvidia-open-model-license/). Additional Information: Llama 3.1 Community Model License; Built with Llama.

**Additional Information:**

[Llama 3.1 Community Model License](https://www.llama.com/llama3_1/license/); Built with Llama.


### Deployment Geography:

Global

### Use Case:

Customers: AI foundry enterprise customers

Use Cases: Image summarization. Text-image analysis, Optical Character Recognition, Interactive Q&A on images, Text Chain-of-Thought reasoning
  

## Release Date:  

- Build.Nvidia.com [June 3rd, 2025] via [nvidia/llama-3.1-nemotron-nano-vl-8b-v1](https://build.nvidia.com/nvidia/llama-3.1-nemotron-nano-vl-8b-v1)
- Hugging Face [June 3rd, 2025]

## Model Architecture:

**Network Type:** Transformer 

**Network Architecture:** 

Vision Encoder: [C-RADIOv2-H](https://huggingface.co/nvidia/C-RADIOv2-VLM-H)

Language Encoder: Llama-3.1-8B-Instruct

### Input

Input Type(s): Image, Text
- Input Images
- Language Supported: English only

Input Format(s): Image (Red, Green, Blue (RGB)), and Text (String)

Input Parameters: Image (2D), Text (1D)

Other Properties Related to Input:

- Input + Output Token: 16K
- Maximum Resolution: Determined by a 12-tile layout constraint, with each tile being 512 × 512 pixels. This supports aspect ratios such as:
  - 4 × 3 layout: up to 2048 × 1536 pixels
  - 3 × 4 layout: up to 1536 × 2048 pixels
  - 2 × 6 layout: up to 1024 × 3072 pixels
  - 6 × 2 layout: up to 3072 × 1024 pixels
  - Other configurations allowed, provided total tiles ≤ 12
- Channel Count: 3 channels (RGB)
- Alpha Channel: Not supported (no transparency)

### Output
Output Type(s): Text

Output Formats: String

Output Parameters: 1D

Other Properties Related to Output: Input + Output Token: 16K



Our AI models are designed and/or optimized to run on NVIDIA GPU-accelerated systems. By leveraging NVIDIA’s hardware (e.g. GPU cores) and software frameworks (e.g., CUDA libraries), the model achieves faster training and inference times compared to CPU-only solutions.

### Software Integration
Runtime Engine(s): TensorRT-LLM<br>
Supported Hardware Microarchitecture Compatibility: H100 SXM 80GB<br>
Supported Operating System(s): Linux<br>

### Model Versions:
Llama-3.1-Nemotron-Nano-VL-8B-V1 

## Quick Start

### Install Dependencies
```
pip install transformers accelerate timm einops open-clip-torch
```

### Usage
```python
from PIL import Image
from transformers import AutoImageProcessor, AutoModel, AutoTokenizer

path = "nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1"
model = AutoModel.from_pretrained(path, trust_remote_code=True, device_map="cuda").eval()
tokenizer = AutoTokenizer.from_pretrained(path)
image_processor = AutoImageProcessor.from_pretrained(path, trust_remote_code=True, device="cuda")

image1 = Image.open("images/example1a.jpeg")
image2 = Image.open("images/example1b.jpeg")
image_features = image_processor([image1, image2])

generation_config = dict(max_new_tokens=1024, do_sample=False, eos_token_id=tokenizer.eos_token_id)

question = 'Describe the two images.'
response = model.chat(
    tokenizer=tokenizer, question=question, generation_config=generation_config,
    **image_features)

print(f'User: {question}\nAssistant: {response}')
```


## Training/Evaluation Dataset:
NV-Pretraining and NV-CosmosNemotron-SFT were used for training and evaluation

Data Collection Method by dataset (Training and Evaluation):  <br>
* Hybrid: Human, Synthetic <br>

Labeling Method by dataset (Training and Evaluation):  <br>
* Hybrid: Human, Synthetic <br>


Additionally, the dataset collection (for training and evaluation) consists of a mix of internal and public datasets designed for training and evaluation across various tasks. It includes: <br>
• Internal datasets built with public commercial images and internal labels, supporting tasks like conversation modeling and document analysis.<br>
• Public datasets sourced from publicly available images and annotations, adapted for tasks such as image captioning and visual question answering.<br>
• Synthetic datasets generated programmatically for specific tasks like tabular data understanding.<br>
• Specialized datasets for safety alignment, function calling, and domain-specific tasks (e.g., science diagrams, financial question answering).<br>



## Evaluation Benchmarks:

| Benchmark | Score |
| --- | --- |
| MMMU Val with chatGPT as a judge | 48.2% |
| AI2D | 85.0% |
| ChartQA  | 86.3% |
| InfoVQA Val | 77.4% |
| OCRBench | 839 |
| OCRBenchV2 English | 60.1% |
| OCRBenchV2 Chinese | 37.9% |
| DocVQA val | 91.2% |
| VideoMME<sup>*</sup>  | 54.7% |

<sup>*</sup>Calculated with 1 tile per image



# Inference:
**Engine:** TTensorRT-LLM <br>
**Test Hardware:** <br>
* 1x NVIDIA H100 SXM 80GB


## Ethical Considerations:
NVIDIA believes Trustworthy AI is a shared responsibility and we have established policies and practices to enable development for a wide array of AI applications.  When downloaded or used in accordance with our terms of service, developers should work with their internal model team to ensure this model meets requirements for the relevant industry and use case and addresses unforeseen product misuse.  For more detailed information on ethical considerations for this model, please see the Model Card++ [Explainability](explainability.md), [Bias](bias.md), [Safety & Security](safety.md), and [Privacy](privacy.md) Subcards.  Please report security vulnerabilities or NVIDIA AI Concerns [here](https://www.nvidia.com/en-us/support/submit-security-vulnerability/).

Users are responsible for model inputs and outputs. Users are responsible for ensuring safe integration of this model, including implementing guardrails as well as other safety mechanisms, prior to deployment. 

Outputs generated by these models may contain political content or other potentially misleading information, issues with content security and safety, or unwanted bias that is independent of our oversight.


 