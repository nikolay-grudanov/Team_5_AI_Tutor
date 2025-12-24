"""
RAG Pipeline - модуль для построения пайплайна обработки документов.

Модули:
    - pdf_conversion: Конвертация PDF в PNG изображения
    - check_server: Проверка доступности vLLM сервера
    - ocr: OCR распознавание текста с изображений

Пример использования:
    # Шаг 1: Конвертация PDF
    python rag_pipeline/pdf_conversion.py
    
    # Шаг 2: OCR обработка
    python scripts/run_ocr.py --input data/raw/math/Книга
"""

__version__ = "0.1.0"

# Экспорты из OCR модуля (для использования в коде)
try:
    from .ocr.pipeline import OCRPipeline
    from .ocr.client import VLLMClient
    from .ocr.config import OCRConfig
    
    __all__ = [
        "OCRPipeline",
        "VLLMClient",
        "OCRConfig",
    ]
except ImportError:
    # OCR модуль еще не создан
    __all__ = []
