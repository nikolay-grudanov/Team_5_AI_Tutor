import torch
from transformers import AutoTokenizer, AutoModel, AutoImageProcessor
from PIL import Image

path = "nvidia/Llama-3.1-Nemotron-Nano-VL-8B-V1"
model = AutoModel.from_pretrained(
    path,
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True,
    device_map="cuda",).eval()

tokenizer = AutoTokenizer.from_pretrained(path)
image_processor = AutoImageProcessor.from_pretrained(path, device="cuda", trust_remote_code=True)

generation_config = dict(max_new_tokens=1024, do_sample=False, eos_token_id=tokenizer.eos_token_id)

# pure-text conversation
question = 'What happened in 1986?'
response, history = model.chat(
    tokenizer, None, question, generation_config, history=None, return_history=True
)
print(f'User: {question}\nAssistant: {response}')

# single-image single-round conversation
image_path = 'images/table.png'
image_features = image_processor(Image.open(image_path))
question = '<image>\nExtract the table in this image as HTML.'
response = model.chat(
    tokenizer=tokenizer, question=question, generation_config=generation_config,
    **image_features
)
print(f'User: {question}\nAssistant: {response}')

# single-image single-round conversation
image_path = 'images/tech.png'
image_features = image_processor(Image.open(image_path))
question = '<image>\nList in bullet point the most important Technological breakthrough of Nvidia Hopper.'
response = model.chat(
    tokenizer=tokenizer, question=question, generation_config=generation_config,
    **image_features
)
print(f'User: {question}\nAssistant: {response}')

# two image single-round conversation
image_features = image_processor([
    Image.open('images/example1a.jpeg'),
    Image.open('images/example1b.jpeg')
])

question = '<image-1>: <image>\n<image-2>: <image>\nBriefly describe the two images.'
response = model.chat(
    tokenizer=tokenizer, question=question, generation_config=generation_config,
    **image_features
)
print(f'User: {question}\nAssistant: {response}')