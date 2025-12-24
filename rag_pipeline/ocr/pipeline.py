"""
OCR Pipeline для параллельной обработки папки с изображениями.

Основные возможности:
- Параллельная обработка изображений (ThreadPoolExecutor)
- Автоматическое сканирование папки
- Прогресс-бар (tqdm)
- Детальная статистика
- Resume: пропуск уже обработанных файлов
- Обработка ошибок и логирование
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import logging
from pathlib import Path
import time
from typing import Any, Dict, List, Optional

from .logging_setup import setup_logging

try:
    from tqdm import tqdm
    TQDM_AVAILABLE = True
except ImportError:
    TQDM_AVAILABLE = False
    print("⚠️  tqdm не установлен. Установите: pip install tqdm")

from .config import OCRConfig
from .processor import ImageProcessor
from .utils import create_output_path, get_image_files

logger = logging.getLogger(__name__)


class OCRPipeline:
    """Pipeline для параллельной OCR обработки папки с изображениями.
    
    Особенности:
    - Автоматическое сканирование изображений (.png, .jpg, .jpeg)
    - Параллельная обработка с ThreadPoolExecutor
    - Прогресс-бар с tqdm
    - Resume: пропуск уже обработанных файлов
    - Детальная статистика и отчет
    - Обработка ошибок
    
    Attributes:
        config (OCRConfig): Конфигурация OCR
        processor (ImageProcessor): Процессор изображений
        stats (dict): Статистика обработки
        
    Пример:
        >>> pipeline = OCRPipeline()
        >>> results = pipeline.process_directory(
        ...     "data/raw/math/Книга",
        ...     max_workers=4,
        ...     resume=True
        ... )
        >>> pipeline.print_summary()
    """
    
    def __init__(
        self,
        config: Optional[OCRConfig] = None,
        processor: Optional[ImageProcessor] = None
    ):
        """Инициализирует pipeline.
        
        Args:
            config: Конфигурация OCR (если None - создается новая)
            processor: Процессор изображений (если None - создается новый)
        """
        self.config = config or OCRConfig()
        self.processor = processor or ImageProcessor(self.config)
        
        # Настройка логирования
        # Файл: DEBUG/INFO (все логи)
        # Консоль: WARNING (только важное, не мешает tqdm)
        setup_logging(
            self.config.log_file, 
            self.config.log_level,      # DEBUG/INFO в файл
            console_level="CRITICAL"    # только CRITICAL в консоль
        )
        
        self.stats = {
            'total_files': 0,
            'processed': 0,
            'skipped': 0,
            'failed': 0,
            'total_tokens': 0,
            'total_chars': 0,
            'total_time': 0.0,
            'errors': []
        }
        
        logger.info("OCRPipeline инициализирован")
    
    def process_directory(
        self,
        input_dir: Path,
        max_workers: Optional[int] = None,
        resume: bool = True,
        extensions: Optional[List[str]] = None
    ) -> List[Dict[str, Any]]:
        """Обрабатывает все изображения в папке параллельно.
        
        Args:
            input_dir: Путь к папке с изображениями
            max_workers: Количество параллельных потоков (None = из config)
            resume: Пропускать уже обработанные файлы
            extensions: Расширения файлов (по умолчанию: ['.png', '.jpg', '.jpeg'])
            
        Returns:
            Список результатов обработки
            
        Пример:
            >>> pipeline = OCRPipeline()
            >>> results = pipeline.process_directory(
            ...     "data/raw/math/Книга",
            ...     max_workers=4,
            ...     resume=True
            ... )
            Processing: 100%|██████| 234/234 [42:15<00:00, 10.8с/img]
        """
        input_dir = Path(input_dir)
        
        if not input_dir.exists():
            raise ValueError(f"Папка не найдена: {input_dir}")
        
        max_workers = max_workers or self.config.max_workers
        logger.info(f"Используется воркеров: {max_workers}")
        extensions = extensions or ['.png', '.jpg', '.jpeg']
        
        logger.info(f"=" * 70)
        logger.info(f"Запуск OCR Pipeline")
        logger.info(f"Входная папка: {input_dir}")
        logger.info(f"Параллельных потоков: {max_workers}")
        logger.info(f"Resume: {resume}")
        logger.info(f"=" * 70)
        
        # Сканирование файлов
        image_files = get_image_files(input_dir, extensions=extensions)
        
        if not image_files:
            logger.warning(f"Не найдено изображений в {input_dir}")
            return []
        
        logger.info(f"Найдено изображений: {len(image_files)}")
        
        # Фильтрация уже обработанных файлов
        if resume:
            image_files = self._filter_processed(image_files)
            logger.info(f"К обработке (после фильтрации): {len(image_files)}")
        
        if not image_files:
            logger.info("Все файлы уже обработаны!")
            return []
        
        self.stats['total_files'] = len(image_files)
        
        # Параллельная обработка
        start_time = time.time()
        results = self._process_parallel(image_files, max_workers)
        self.stats['total_time'] = time.time() - start_time
        
        # Подсчет статистики
        self._update_stats(results)
        
        # Вывод итоговой статистики
        self.print_summary()
        
        return results
    
    def _filter_processed(self, image_files: List[Path]) -> List[Path]:
        """Фильтрует уже обработанные файлы.
        
        Args:
            image_files: Список путей к изображениям
            
        Returns:
            Список путей к необработанным изображениям
        """
        unprocessed = []
        skipped_count = 0
        
        for image_path in image_files:
            output_path = create_output_path(
                image_path,
                self.config.data_raw_dir,
                self.config.data_processed_dir,
                extension=".md"
            )
            
            if output_path.exists():
                skipped_count += 1
                logger.debug(f"Пропуск (уже обработан): {image_path.name}")
            else:
                unprocessed.append(image_path)
        
        if skipped_count > 0:
            logger.info(f"Пропущено (уже обработаны): {skipped_count} файлов")
        
        self.stats['skipped'] = skipped_count
        
        return unprocessed
    
    def _process_parallel(
        self,
        image_files: List[Path],
        max_workers: int
    ) -> List[Dict[str, Any]]:
        """Параллельно обрабатывает список изображений.
        
        Args:
            image_files: Список путей к изображениям
            max_workers: Количество параллельных потоков
            
        Returns:
            Список результатов обработки
        """
        results = []
        
        # Создание прогресс-бара
        if TQDM_AVAILABLE:
            pbar = tqdm(
                total=len(image_files),
                desc="⚡ Обработка",
                unit="img",
                ncols=100,
                bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}, {rate_fmt}]'
            )
        else:
            pbar = None
            logger.info(f"Начало обработки {len(image_files)} файлов...")
        
        # Параллельная обработка
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Отправка всех задач
            future_to_path = {
                executor.submit(self.processor.process_image, img_path): img_path
                for img_path in image_files
            }
            
            # Сбор результатов по мере завершения
            for future in as_completed(future_to_path):
                image_path = future_to_path[future]
                
                try:
                    result = future.result()
                    results.append(result)
                    
                    # Обновление прогресс-бара
                    if pbar:
                        pbar.update(1)
                        # Краткая информация о последнем файле
                        if result['success']:
                            pbar.set_postfix_str(
                                f"✓ {result['image_path'].name} "
                                f"({result['processing_time']:.1f}с)"
                            )
                    else:
                        # Без tqdm - простой лог
                        if result['success']:
                            logger.info(
                                f"✓ {result['image_path'].name}: "
                                f"{result['processing_time']:.2f}с"
                            )
                        else:
                            logger.error(
                                f"✗ {result['image_path'].name}: "
                                f"{result['error']}"
                            )
                
                except Exception as e:
                    error_msg = f"Неожиданная ошибка для {image_path.name}: {e}"
                    logger.error(error_msg)
                    
                    results.append({
                        'success': False,
                        'image_path': image_path,
                        'error': str(e)
                    })
                    
                    if pbar:
                        pbar.update(1)
        
        if pbar:
            pbar.close()
        
        return results
    
    def _update_stats(self, results: List[Dict[str, Any]]) -> None:
        """Обновляет статистику обработки.
        
        Args:
            results: Список результатов обработки
        """
        for result in results:
            if result['success']:
                self.stats['processed'] += 1
                self.stats['total_tokens'] += result.get('tokens', 0)
                self.stats['total_chars'] += len(result.get('text', ''))
            else:
                self.stats['failed'] += 1
                self.stats['errors'].append({
                    'file': result['image_path'].name,
                    'error': result.get('error', 'Unknown error')
                })
    
    def print_summary(self) -> None:
        """Выводит итоговую статистику обработки."""
        logger.info("\n" + "=" * 70)
        logger.info("📊 СТАТИСТИКА ОБРАБОТКИ")
        logger.info("=" * 70)
        
        total = self.stats['total_files']
        processed = self.stats['processed']
        skipped = self.stats['skipped']
        failed = self.stats['failed']
        
        logger.info(f"Всего файлов:           {total}")
        logger.info(f"Успешно обработано:     {processed}")
        logger.info(f"Пропущено (уже есть):   {skipped}")
        logger.info(f"Ошибок:                 {failed}")
        
        if total > 0:
            success_rate = (processed / total) * 100
            logger.info(f"Процент успеха:         {success_rate:.1f}%")
        
        if processed > 0:
            logger.info(f"\nВсего токенов:          {self.stats['total_tokens']:,}")
            logger.info(f"Всего символов:         {self.stats['total_chars']:,}")
            
            avg_time = self.stats['total_time'] / processed
            logger.info(f"\nОбщее время:            {self.stats['total_time']:.1f}с")
            logger.info(f"Среднее время/файл:     {avg_time:.2f}с")
        
        # Вывод ошибок (если есть)
        if self.stats['errors']:
            logger.info("\n" + "-" * 70)
            logger.info("❌ ОШИБКИ:")
            logger.info("-" * 70)
            for error in self.stats['errors'][:10]:  # Первые 10 ошибок
                logger.info(f"  • {error['file']}: {error['error']}")
            
            if len(self.stats['errors']) > 10:
                logger.info(f"  ... и еще {len(self.stats['errors']) - 10} ошибок")
        
        logger.info("=" * 70 + "\n")
    
    def get_stats(self) -> Dict[str, Any]:
        """Возвращает статистику обработки.
        
        Returns:
            Словарь со статистикой
        """
        return self.stats.copy()
    
    def __repr__(self) -> str:
        """Строковое представление pipeline."""
        return (
            f"OCRPipeline("
            f"model='{self.config.model_name}', "
            f"config_max_workers={self.config.max_workers})"
        )


if __name__ == "__main__":
    # Тестирование pipeline
    import sys
    
    print("=" * 70)
    print("TESTING OCR PIPELINE")
    print("=" * 70)
    
    if len(sys.argv) < 2:
        print("\nИспользование:")
        print("  python -m rag_pipeline.ocr.pipeline <путь_к_папке>")
        print("\nПример:")
        print("  python -m rag_pipeline.ocr.pipeline data/raw/math/Книга")
        print("\nОпции через переменные окружения:")
        print("  MAX_WORKERS=8 python -m rag_pipeline.ocr.pipeline data/raw/math/Книга")
        sys.exit(1)
    
    input_dir = Path(sys.argv[1])
    
    if not input_dir.exists():
        print(f"\n❌ Папка не найдена: {input_dir}")
        sys.exit(1)
    
    try:
        # Создание pipeline
        pipeline = OCRPipeline()
        print(f"\n✅ Pipeline создан: {pipeline}")
        
        # Проверка доступности сервера
        print("\n🔍 Проверка vLLM сервера...")
        if not pipeline.processor.client.check_availability():
            print("❌ vLLM сервер недоступен!")
            print("   Запустите vLLM сервер и попробуйте снова.")
            sys.exit(1)
        
        print("✅ Сервер доступен")
        
        # Обработка папки
        print(f"\n📁 Обработка папки: {input_dir}")
        print("-" * 70)
        
        results = pipeline.process_directory(
            input_dir=input_dir,
            resume=True
        )
        
        print("\n✅ Обработка завершена!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Прервано пользователем")
        if 'pipeline' in locals():
            pipeline.print_summary()
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 70)
