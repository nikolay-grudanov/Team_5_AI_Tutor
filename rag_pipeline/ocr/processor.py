"""
Процессор для обработки одного изображения.

Отвечает за:
- Загрузку и конвертацию изображения
- Отправку OCR запроса
- Немедленное сохранение результата в .md файл
"""

import logging
from pathlib import Path
from typing import Optional, Dict, Any
from datetime import datetime

from .config import OCRConfig
from .client import VLLMClient
from .utils import (
    image_to_base64,
    create_output_path,
    extract_page_number,
    get_image_info
)

logger = logging.getLogger(__name__)


class ImageProcessor:
    """Процессор для OCR обработки одного изображения.
    
    Выполняет полный цикл обработки:
    1. Загрузка изображения
    2. Конвертация в base64
    3. OCR через vLLM
    4. Форматирование результата
    5. Сохранение в .md файл
    
    Thread-safe: Да (не использует shared state)
    
    Attributes:
        config (OCRConfig): Конфигурация OCR модуля
        client (VLLMClient): Клиент для vLLM API
        
    Пример:
        >>> processor = ImageProcessor()
        >>> result = processor.process_image(
        ...     "data/raw/math/Книга/page_001.png"
        ... )
        >>> print(result['output_path'])
        data/processed/math/Книга/page_001.md
    """
    
    def __init__(
        self,
        config: Optional[OCRConfig] = None,
        client: Optional[VLLMClient] = None
    ):
        """Инициализирует процессор.
        
        Args:
            config: Конфигурация OCR модуля (если None - создается новая)
            client: vLLM клиент (если None - создается новый)
        """
        self.config = config or OCRConfig()
        self.client = client or VLLMClient(self.config)
        
        logger.debug("ImageProcessor инициализирован")
    
    def process_image(
        self,
        image_path: Path,
        save_immediately: bool = True
    ) -> Dict[str, Any]:
        """Обрабатывает одно изображение через OCR.
        
        Args:
            image_path: Путь к изображению
            save_immediately: Сохранять результат сразу после обработки
            
        Returns:
            Словарь с результатом обработки:
            {
                'success': bool,           # Успешность обработки
                'image_path': Path,        # Исходное изображение
                'output_path': Path,       # Путь к сохраненному .md файлу
                'text': str,               # Распознанный текст
                'tokens': int,             # Количество токенов
                'processing_time': float,  # Время обработки (секунды)
                'page_number': int,        # Номер страницы
                'error': Optional[str]     # Ошибка (если есть)
            }
            
        Пример:
            >>> processor = ImageProcessor()
            >>> result = processor.process_image(
            ...     Path("data/raw/math/Книга/page_001.png")
            ... )
            >>> if result['success']:
            ...     print(f"Сохранено: {result['output_path']}")
        """
        image_path = Path(image_path)
        start_time = datetime.now()
        
        result = {
            'success': False,
            'image_path': image_path,
            'output_path': None,
            'text': '',
            'tokens': 0,
            'processing_time': 0.0,
            'page_number': extract_page_number(image_path.name),
            'error': None
        }
        
        try:
            logger.info(f"Обработка: {image_path.name}")
            
            # 1. Получение информации об изображении
            try:
                img_info = get_image_info(image_path)
                logger.debug(
                    f"Изображение: {img_info['width']}x{img_info['height']}, "
                    f"{img_info['mode']}, {img_info['file_size']}"
                )
            except Exception as e:
                logger.warning(f"Не удалось получить информацию об изображении: {e}")
            
            # 2. Конвертация в base64
            logger.debug("Конвертация в base64...")
            image_base64 = image_to_base64(
                image_path,
                resize=self.config.resize_image,
                max_size=self.config.max_image_size
            )
            logger.debug(f"Base64 размер: {len(image_base64):,} символов")
            
            # 3. OCR запрос
            logger.debug("Отправка OCR запроса...")
            ocr_result = self.client.ocr_request(
                image_base64=image_base64,
                prompt_type=self.config.prompt_type
            )
            
            # 4. Обновление результата
            result['text'] = ocr_result['text']
            result['tokens'] = ocr_result['tokens']
            result['processing_time'] = ocr_result['processing_time']
            result['success'] = True
            
            logger.info(
                f"✓ {image_path.name}: {result['processing_time']:.2f}с, "
                f"{result['tokens']} токенов, {len(result['text'])} символов"
            )
            
            # 5. Сохранение результата
            if save_immediately:
                output_path = self._save_result(image_path, result, ocr_result)
                result['output_path'] = output_path
                logger.debug(f"Сохранено: {output_path}")
            
            return result
            
        except Exception as e:
            error_msg = str(e)
            logger.error(f"✗ Ошибка обработки {image_path.name}: {error_msg}")
            
            result['error'] = error_msg
            result['processing_time'] = (datetime.now() - start_time).total_seconds()
            
            return result
    
    def _save_result(
        self,
        image_path: Path,
        result: Dict[str, Any],
        ocr_result: Dict[str, Any]
    ) -> Path:
        """Сохраняет результат OCR в .md файл.
        
        Args:
            image_path: Путь к исходному изображению
            result: Результат обработки
            ocr_result: Результат OCR запроса
            
        Returns:
            Путь к сохраненному .md файлу
        """
        # Создание пути для сохранения
        output_path = create_output_path(
            image_path,
            self.config.data_raw_dir,
            self.config.data_processed_dir,
            extension=".md"
        )
        
        # Формирование содержимого .md файла
        content = self._format_markdown(image_path, result, ocr_result)
        
        # Сохранение
        output_path.write_text(content, encoding='utf-8')
        
        return output_path
    
    def _format_markdown(
        self,
        image_path: Path,
        result: Dict[str, Any],
        ocr_result: Dict[str, Any]
    ) -> str:
        """Форматирует результат в markdown с YAML frontmatter.
        
        Args:
            image_path: Путь к исходному изображению
            result: Результат обработки
            ocr_result: Результат OCR запроса
            
        Returns:
            Отформатированная markdown строка
        """
        # YAML frontmatter с метаданными
        timestamp = datetime.now().isoformat()
        
        frontmatter = f"""---
source_image: {image_path.name}
page_number: {result['page_number']}
model: {ocr_result['model']}
prompt_type: {ocr_result['prompt_type']}
processing_time: {result['processing_time']:.2f}
tokens: {result['tokens']}
characters: {len(result['text'])}
timestamp: {timestamp}
finish_reason: {ocr_result.get('finish_reason', 'unknown')}
---

"""
        
        # Тело документа с распознанным текстом
        body = result['text']
        
        return frontmatter + body
    
    def process_batch(
        self,
        image_paths: list,
        save_immediately: bool = True
    ) -> list:
        """Последовательно обрабатывает список изображений.
        
        Примечание: Для параллельной обработки используйте OCRPipeline.
        
        Args:
            image_paths: Список путей к изображениям
            save_immediately: Сохранять результаты сразу
            
        Returns:
            Список результатов обработки
            
        Пример:
            >>> processor = ImageProcessor()
            >>> paths = [Path("page_001.png"), Path("page_002.png")]
            >>> results = processor.process_batch(paths)
            >>> success_count = sum(1 for r in results if r['success'])
        """
        results = []
        
        for image_path in image_paths:
            result = self.process_image(image_path, save_immediately)
            results.append(result)
        
        return results
    
    def __repr__(self) -> str:
        """Строковое представление процессора."""
        return f"ImageProcessor(model='{self.config.model_name}')"


if __name__ == "__main__":
    # Тестирование процессора
    import sys
    
    print("=" * 70)
    print("TESTING IMAGE PROCESSOR")
    print("=" * 70)
    
    if len(sys.argv) < 2:
        print("\nИспользование:")
        print("  python -m rag_pipeline.ocr.processor <путь_к_изображению>")
        print("\nПример:")
        print("  python -m rag_pipeline.ocr.processor data/raw/math/Книга/page_001.png")
        sys.exit(1)
    
    image_path = Path(sys.argv[1])
    
    if not image_path.exists():
        print(f"\n❌ Файл не найден: {image_path}")
        sys.exit(1)
    
    try:
        # Создание процессора
        processor = ImageProcessor()
        print(f"\n✅ Процессор создан: {processor}")
        
        # Проверка доступности сервера
        print("\n🔍 Проверка vLLM сервера...")
        if not processor.client.check_availability():
            print("❌ vLLM сервер недоступен!")
            print("   Запустите vLLM сервер и попробуйте снова.")
            sys.exit(1)
        
        print("✅ Сервер доступен")
        
        # Обработка изображения
        print(f"\n📷 Обработка: {image_path.name}")
        print("-" * 70)
        
        result = processor.process_image(image_path)
        
        print("-" * 70)
        
        if result['success']:
            print(f"\n✅ УСПЕШНО!")
            print(f"   Время обработки: {result['processing_time']:.2f}с")
            print(f"   Токенов: {result['tokens']}")
            print(f"   Символов: {len(result['text'])}")
            print(f"   Сохранено: {result['output_path']}")
            
            print(f"\n📝 Первые 300 символов:")
            print("-" * 70)
            print(result['text'][:300])
            print("-" * 70)
        else:
            print(f"\n❌ ОШИБКА: {result['error']}")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Прервано пользователем")
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 70)
