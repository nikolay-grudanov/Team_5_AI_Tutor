"""
Настройка логирования для OCR модуля.
"""

import logging
from pathlib import Path
from datetime import datetime


def setup_logging(log_file: Path, log_level: str = "INFO", console_level: str = "CRITICAL"):
    """Настраивает логирование в файл и консоль.
    
    Args:
        log_file: Путь к файлу логов
        log_level: Уровень логирования для ФАЙЛА (DEBUG, INFO, WARNING, ERROR)
        console_level: Уровень логирования для КОНСОЛИ (CRITICAL по умолчанию)
    """
    # Создание папки для логов если не существует
    log_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Настройка форматирования
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'
    
    # Получение root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # <- Самый низкий уровень для root
    
    # Очистка существующих handlers (на случай повторного вызова)
    root_logger.handlers.clear()
    
    # Handler для файла (все логи)
    file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
    file_handler.setLevel(getattr(logging, log_level.upper()))  # DEBUG/INFO для файла
    file_handler.setFormatter(logging.Formatter(log_format, date_format))
    
    # Handler для консоли (только важное - не мешает tqdm)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, console_level.upper()))  # WARNING/ERROR для консоли
    console_handler.setFormatter(logging.Formatter(log_format, date_format))
    
    # Добавление handlers
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)
    
    # Логирование старта (только в файл)
    logging.info("=" * 70)
    logging.info(f"Логирование настроено:")
    logging.info(f"  Файл: {log_file} (уровень: {log_level})")
    logging.info(f"  Консоль: (уровень: {console_level})")
    logging.info("=" * 70)



if __name__ == "__main__":
    # Тестирование
    import sys
    from pathlib import Path
    
    # Добавление корневой папки в путь
    sys.path.insert(0, str(Path(__file__).parent.parent.parent))
    
    from rag_pipeline.ocr.config import OCRConfig
    
    config = OCRConfig()
    setup_logging(config.log_file, config.log_level)
    
    logging.debug("Это DEBUG сообщение")
    logging.info("Это INFO сообщение")
    logging.warning("Это WARNING сообщение")
    logging.error("Это ERROR сообщение")
    
    print(f"\n✅ Логи записаны в: {config.log_file}")
