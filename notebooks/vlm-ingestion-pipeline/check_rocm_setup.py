"""
Проверка настройки ROCm окружения для vLLM.
"""

import sys
import os

print("=" * 60)
print("Проверка ROCm окружения")
print("=" * 60)

# 1. Проверка NumPy
print("\n1. Проверка NumPy:")
try:
    import numpy as np
    print(f"   ✅ NumPy версия: {np.__version__}")
    if np.__version__.startswith('2.'):
        print("   ⚠️  ПРЕДУПРЕЖДЕНИЕ: NumPy 2.x может вызвать проблемы!")
        print("   Выполните: pip install 'numpy<2.0' --force-reinstall")
except Exception as e:
    print(f"   ❌ Ошибка NumPy: {e}")

# 2. Проверка PyTorch
print("\n2. Проверка PyTorch:")
try:
    import torch
    print(f"   ✅ PyTorch версия: {torch.__version__}")
    print(f"   ROCm доступен: {torch.cuda.is_available()}")
    print(f"   Количество GPU: {torch.cuda.device_count()}")
    
    if torch.cuda.is_available():
        print(f"   Имя GPU: {torch.cuda.get_device_name(0)}")
        print(f"   CUDA версия (ROCm): {torch.version.cuda}")
    else:
        print("   ⚠️  ПРЕДУПРЕЖДЕНИЕ: PyTorch не видит GPU!")
        print("   Переустановите: pip install torch --index-url https://download.pytorch.org/whl/rocm6.2")
except Exception as e:
    print(f"   ❌ Ошибка PyTorch: {e}")

# 3. Проверка переменных окружения
print("\n3. Проверка переменных окружения:")
env_vars = {
    'ROCM_PATH': '/opt/rocm',
    'HIP_VISIBLE_DEVICES': '0',
    'HSA_OVERRIDE_GFX_VERSION': '11.0.0'
}

for var, expected in env_vars.items():
    value = os.environ.get(var, 'НЕ УСТАНОВЛЕНА')
    if value == 'НЕ УСТАНОВЛЕНА':
        print(f"   ⚠️  {var}: {value}")
        print(f"      Добавьте: export {var}={expected}")
    else:
        print(f"   ✅ {var}: {value}")

# 4. Проверка vLLM
print("\n4. Проверка vLLM:")
try:
    import vllm
    print(f"   ✅ vLLM установлен")
    
    # Проверяем, может ли vLLM импортировать основные классы
    from vllm import LLM, SamplingParams
    print(f"   ✅ vLLM импорт успешен")
except Exception as e:
    print(f"   ❌ Ошибка vLLM: {e}")
    print("   Переустановите: pip install vllm")

# 5. Проверка зависимостей
print("\n5. Проверка зависимостей:")
packages = ['transformers', 'pillow', 'pdf2image', 'pyarrow', 'pandas']
for pkg in packages:
    try:
        module = __import__(pkg)
        version = getattr(module, '__version__', 'unknown')
        print(f"   ✅ {pkg}: {version}")
    except ImportError:
        print(f"   ❌ {pkg}: НЕ УСТАНОВЛЕН")

print("\n" + "=" * 60)
print("Проверка завершена")
print("=" * 60)
