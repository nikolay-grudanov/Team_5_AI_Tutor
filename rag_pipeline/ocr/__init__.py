"""
OCR модуль для распознавания текста с изображений через vLLM API.

Основные компоненты:
    - OCRConfig: Конфигурация модуля (из .env)
    - VLLMClient: Клиент для подключения к vLLM серверу
    - ImageProcessor: Обработка одного изображения
    - OCRPipeline: Параллельная обработка папки с книгой

Пример использования:
    >>> from rag_pipeline.ocr import OCRPipeline
    >>> pipeline = OCRPipeline()
    >>> pipeline.process_directory("data/raw/math/Книга")

Запуск через CLI:
    $ python scripts/run_ocr.py --input data/raw/math/Книга
"""

__version__ = "0.1.0"

# Ленивый импорт для избежания циклических зависимостей
# и ускорения загрузки модуля

def __getattr__(name):
    """Ленивый импорт классов при первом обращении."""
    
    if name == "OCRConfig":
        from .config import OCRConfig
        return OCRConfig
    
    elif name == "VLLMClient":
        from .client import VLLMClient
        return VLLMClient
    
    elif name == "ImageProcessor":
        from .processor import ImageProcessor
        return ImageProcessor
    
    elif name == "OCRPipeline":
        from .pipeline import OCRPipeline
        return OCRPipeline
    
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Публичный API модуля
__all__ = [
    "OCRConfig",
    "VLLMClient", 
    "ImageProcessor",
    "OCRPipeline",
]
