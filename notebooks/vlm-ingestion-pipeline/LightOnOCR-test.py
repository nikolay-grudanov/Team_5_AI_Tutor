"""
Правильная загрузка LightOnOCR с кастомным процессором
"""

from transformers import AutoModel, AutoTokenizer, AutoImageProcessor
from PIL import Image
import torch
import sys

model_path = "models/LightOnOCR-1B-1025"

print("="*70)
print("🔧 ПРАВИЛЬНАЯ ЗАГРУЗКА LightOnOCR")
print("="*70)

try:
    # Шаг 1: Загрузить модель с trust_remote_code
    print(f"\n📦 Загрузка модели...")
    model = AutoModel.from_pretrained(
        model_path,
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )
    print(f"✅ Модель: {type(model)}")
    
    # Шаг 2: Загрузить токенизатор
    print(f"\n📦 Загрузка токенизатора...")
    tokenizer = AutoTokenizer.from_pretrained(
        model_path,
        trust_remote_code=True
    )
    print(f"✅ Токенизатор: {type(tokenizer)}")
    
    # Шаг 3: Загрузить image processor
    print(f"\n📦 Загрузка image processor...")
    try:
        image_processor = AutoImageProcessor.from_pretrained(
            model_path,
            trust_remote_code=True
        )
        print(f"✅ Image Processor: {type(image_processor)}")
    except Exception as e:
        print(f"⚠️  AutoImageProcessor не сработал: {e}")
        print(f"   Попытка загрузить из preprocessor_config.json...")
        
        # Попробовать загрузить вручную
        from transformers import PreTrainedImageProcessor
        import json
        
        with open(f"{model_path}/preprocessor_config.json", "r") as f:
            config = json.load(f)
        
        print(f"   Preprocessor config: {config}")
    
    # Шаг 4: ТЕСТ - Обработка изображения
    print(f"\n🧪 ТЕСТ: Обработка изображения...")
    
    test_image = list(IMAGE_PATHS)[0]
    image = Image.open(test_image)
    print(f"   Изображение: {test_image.name} ({image.size})")
    
    # Попробовать разные способы обработки
    print(f"\n   Способ 1: Через модель напрямую...")
    if hasattr(model, 'forward'):
        # Подготовить inputs
        # LightOnOCR ожидает pixel_values
        from torchvision import transforms
        
        # Простая нормализация
        transform = transforms.Compose([
            transforms.Resize((512, 512)),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.48145466, 0.4578275, 0.40821073],
                std=[0.26862954, 0.26130258, 0.27577711]
            )
        ])
        
        pixel_values = transform(image).unsqueeze(0).to(model.device)
        print(f"   ✅ pixel_values shape: {pixel_values.shape}")
        
        # Генерация
        with torch.no_grad():
            outputs = model.generate(
                pixel_values=pixel_values,
                max_new_tokens=512,
                temperature=0.2,
                top_p=0.9,
                do_sample=True
            )
        
        # Декодирование
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        print(f"\n📝 РЕЗУЛЬТАТ:")
        print(f"   Символов: {len(text)}")
        print(f"\n{text[:500]}")
        
        if len(text) > 50:
            print(f"\n🎉 УСПЕХ! Модель распознала текст!")
        else:
            print(f"\n⚠️  Результат слишком короткий")
    
except Exception as e:
    print(f"\n❌ ОШИБКА: {e}")
    import traceback
    traceback.print_exc()

print(f"\n{'='*70}")

