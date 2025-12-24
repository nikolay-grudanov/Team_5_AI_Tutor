#!/usr/bin/env python3
"""
Тестовый скрипт для проверки функциональности извлечения текста из PDF.
Этот скрипт использует упрощенную версию для проверки конвертации PDF в изображения.
"""

import os
import sys
from pathlib import Path
from PIL import Image
from pdf2image import convert_from_path
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def test_pdf_conversion():
    """Тестирование конвертации PDF в изображения."""
    pdf_dir = Path("pdf-for-test")
    
    if not pdf_dir.exists():
        logger.error(f"Директория {pdf_dir} не существует")
        return False
    
    # Поиск PDF файлов
    pdf_files = list(pdf_dir.glob("*.pdf"))
    
    if not pdf_files:
        logger.error(f"В директории {pdf_dir} не найдено PDF файлов")
        return False
    
    logger.info(f"Найдено {len(pdf_files)} PDF файлов")
    
    # Создание директории для тестовых изображений
    test_images_dir = Path("test_images")
    test_images_dir.mkdir(exist_ok=True)
    
    for pdf_file in pdf_files:
        try:
            logger.info(f"Обработка файла: {pdf_file}")
            
            # Конвертация PDF в изображения
            images = convert_from_path(str(pdf_file), dpi=150)  # Используем меньшее разрешение для теста
            
            logger.info(f"Получено {len(images)} изображений из {pdf_file.name}")
            
            # Сохранение первых двух страниц каждого PDF для проверки
            for i, image in enumerate(images[:2]):  # Только первые 2 страницы для теста
                output_path = test_images_dir / f"{pdf_file.stem}_page_{i+1}.png"
                image.save(output_path, "PNG")
                logger.info(f"Сохранено изображение: {output_path}")
            
            logger.info(f"Успешно обработан файл: {pdf_file}")
            
        except Exception as e:
            logger.error(f"Ошибка при обработке файла {pdf_file}: {e}")
            return False
    
    logger.info("Тестирование конвертации PDF завершено успешно")
    logger.info(f"Изображения сохранены в директории: {test_images_dir}")
    return True

def check_dependencies():
    """Проверка наличия необходимых зависимостей."""
    try:
        import pdf2image
        logger.info("✓ pdf2image установлен")
    except ImportError:
        logger.error("✗ pdf2image не установлен. Установите с помощью: pip install pdf2image")
        return False
    
    try:
        from PIL import Image
        logger.info("✓ Pillow установлен")
    except ImportError:
        logger.error("✗ Pillow не установлен. Установите с помощью: pip install pillow")
        return False
    
    # Проверка наличия poppler
    try:
        import subprocess
        result = subprocess.run(['pdftoppm', '-v'], capture_output=True, text=True)
        if result.returncode == 0:
            logger.info("✓ Poppler установлен")
        else:
            logger.error("✗ Poppler не установлен или не работает корректно")
            logger.error("Установите Poppler согласно инструкциям в README.md")
            return False
    except FileNotFoundError:
        logger.error("✗ Poppler не найден")
        logger.error("Установите Poppler согласно инструкциям в README.md")
        return False
    
    return True

def main():
    """Основная функция."""
    logger.info("Начало тестирования извлечения текста из PDF")
    
    # Проверка зависимостей
    if not check_dependencies():
        logger.error("Проверка зависимостей не пройдена")
        sys.exit(1)
    
    # Тестирование конвертации PDF
    if not test_pdf_conversion():
        logger.error("Тестирование конвертации PDF не пройдено")
        sys.exit(1)
    
    logger.info("Все тесты пройдены успешно!")
    logger.info("Теперь вы можете запустить основной скрипт:")
    logger.info("python pdf_text_extractor.py")

if __name__ == "__main__":
    main()