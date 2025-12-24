"""
Вспомогательные функции для OCR модуля.

Функции:
    - image_to_base64: Конвертация изображения в base64
    - create_output_path: Создание пути для сохранения результата
    - format_duration: Форматирование времени
    - setup_logging: Настройка логирования
"""

import base64
from datetime import timedelta
from io import BytesIO
import logging
from pathlib import Path
import sys
from typing import List, Optional, Union

from PIL import Image


def image_to_base64(
    image_path: Union[str, Path],
    resize: bool = True,
    max_size: int = 1920
) -> str:
    """Конвертирует изображение в base64 строку.
    
    Загружает изображение, опционально изменяет размер и конвертирует в base64.
    Автоматически оптимизирует формат (PNG для RGBA, JPEG для RGB).
    
    Args:
        image_path: Путь к изображению
        resize: Флаг изменения размера (если True и изображение > max_size)
        max_size: Максимальный размер по большей стороне (px)
        
    Returns:
        Base64 строка изображения
        
    Raises:
        FileNotFoundError: Если файл не найден
        PIL.UnidentifiedImageError: Если файл не является изображением
        
    Пример:
        >>> base64_str = image_to_base64("page_001.png", resize=True, max_size=1920)
        >>> print(len(base64_str))
        245678
    """
    image_path = Path(image_path)
    
    if not image_path.exists():
        raise FileNotFoundError(f"Изображение не найдено: {image_path}")
    
    # Загрузка изображения
    image = Image.open(image_path)
    
    # Изменение размера если нужно
    if resize and max(image.size) > max_size:
        # Вычисление нового размера с сохранением пропорций
        ratio = max_size / max(image.size)
        new_size = (int(image.width * ratio), int(image.height * ratio))
        
        # Resize с высоким качеством
        image = image.resize(new_size, Image.Resampling.LANCZOS)
    
    # Конвертация в base64
    buffered = BytesIO()
    
    # Выбор формата в зависимости от режима изображения
    if image.mode in ('RGBA', 'LA', 'P'):
        # Изображения с прозрачностью -> PNG
        image.save(buffered, format="PNG", optimize=True)
    else:
        # Конвертация в RGB если нужно
        if image.mode != 'RGB':
            image = image.convert('RGB')
        # Обычные изображения -> JPEG (меньше размер)
        image.save(buffered, format="JPEG", quality=95, optimize=True)
    
    # Кодирование в base64
    img_bytes = buffered.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode('utf-8')
    
    return img_base64


def create_output_path(
    input_path: Union[str, Path],
    raw_dir: Union[str, Path],
    processed_dir: Union[str, Path],
    extension: str = ".md"
) -> Path:
    """Создает путь для сохранения обработанного файла.
    
    Преобразует путь из data/raw/... в data/processed/...
    с сохранением структуры подпапок.
    
    Args:
        input_path: Путь к исходному файлу (например, page_001.png)
        raw_dir: Корневая директория с исходными файлами (data/raw)
        processed_dir: Корневая директория для обработанных файлов (data/processed)
        extension: Расширение выходного файла (по умолчанию .md)
        
    Returns:
        Путь для сохранения обработанного файла
        
    Пример:
        >>> input_path = Path("data/raw/math/Книга/page_001.png")
        >>> output_path = create_output_path(
        ...     input_path,
        ...     raw_dir="data/raw",
        ...     processed_dir="data/processed"
        ... )
        >>> print(output_path)
        data/processed/math/Книга/page_001.md
    """
    input_path = Path(input_path)
    raw_dir = Path(raw_dir)
    processed_dir = Path(processed_dir)
    
    # Получаем относительный путь от raw_dir
    try:
        relative_path = input_path.relative_to(raw_dir)
    except ValueError:
        # Если input_path не внутри raw_dir, используем только имя файла
        relative_path = input_path.name
    
    # Заменяем расширение
    output_filename = relative_path.stem + extension
    
    # Формируем полный путь
    if relative_path.parent != Path("."):
        output_path = processed_dir / relative_path.parent / output_filename
    else:
        output_path = processed_dir / output_filename
    
    # Создаем директории если не существуют
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    return output_path


def extract_page_number(filename: str) -> int:
    """Извлекает номер страницы из имени файла.
    
    Поддерживаемые форматы:
        - page_001.png -> 1
        - page_042.jpg -> 42
        - 0001.png -> 1
        - img_123.png -> 123
        
    Args:
        filename: Имя файла
        
    Returns:
        Номер страницы (int). Если не найден - возвращает 0
        
    Пример:
        >>> extract_page_number("page_001.png")
        1
        >>> extract_page_number("page_042.jpg")
        42
    """
    import re
    
    # Паттерн для поиска чисел в имени файла
    match = re.search(r'(\d+)', filename)
    
    if match:
        return int(match.group(1))
    
    return 0


def format_duration(seconds: float) -> str:
    """Форматирует длительность в человекочитаемый вид.
    
    Args:
        seconds: Количество секунд
        
    Returns:
        Отформатированная строка
        
    Пример:
        >>> format_duration(65.5)
        '1m 5.5s'
        >>> format_duration(3665.0)
        '1h 1m 5s'
        >>> format_duration(5.234)
        '5.2s'
    """
    if seconds < 60:
        return f"{seconds:.1f}s"
    
    delta = timedelta(seconds=seconds)
    
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    secs = delta.seconds % 60
    
    parts = []
    if hours > 0:
        parts.append(f"{hours}h")
    if minutes > 0:
        parts.append(f"{minutes}m")
    if secs > 0 or not parts:
        parts.append(f"{secs}s")
    
    return " ".join(parts)


def format_size(size_bytes: int) -> str:
    """Форматирует размер файла в человекочитаемый вид.
    
    Args:
        size_bytes: Размер в байтах
        
    Returns:
        Отформатированная строка
        
    Пример:
        >>> format_size(1024)
        '1.0 KB'
        >>> format_size(1536000)
        '1.5 MB'
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    
    return f"{size_bytes:.1f} PB"


def setup_logging(
    log_level: str = "INFO",
    log_file: Union[str, Path, None] = None
) -> logging.Logger:
    """Настраивает логирование для OCR модуля.
    
    Создает logger с выводом в консоль и опционально в файл.
    
    Args:
        log_level: Уровень логирования (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Путь к файлу логов (опционально)
        
    Returns:
        Настроенный logger
        
    Пример:
        >>> logger = setup_logging("INFO", "logs/ocr.log")
        >>> logger.info("OCR processing started")
    """
    # Конвертируем строку уровня в константу logging
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)
    
    # Создаем logger
    logger = logging.getLogger("rag_pipeline.ocr")
    logger.setLevel(numeric_level)
    
    # Очищаем существующие handlers (избегаем дублирования)
    logger.handlers.clear()
    
    # Формат логов
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(numeric_level)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (если указан путь)
    if log_file:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(numeric_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger


def count_tokens_estimate(text: str) -> int:
    """Примерная оценка количества токенов в тексте.
    
    Использует простую эвристику: ~4 символа = 1 токен для английского,
    ~2 символа = 1 токен для русского.
    
    Args:
        text: Текст для подсчета
        
    Returns:
        Примерное количество токенов
        
    Примечание:
        Это грубая оценка. Для точного подсчета используйте tiktoken.
        
    Пример:
        >>> count_tokens_estimate("Hello world!")
        3
    """
    # Грубая эвристика: среднее между английским и русским
    chars_per_token = 3
    return len(text) // chars_per_token


def validate_image_path(image_path: Union[str, Path]) -> bool:
    """Проверяет, является ли файл поддерживаемым изображением.
    
    Args:
        image_path: Путь к файлу
        
    Returns:
        True если файл - поддерживаемое изображение, иначе False
        
    Пример:
        >>> validate_image_path("page_001.png")
        True
        >>> validate_image_path("document.pdf")
        False
    """
    image_path = Path(image_path)
    
    # Проверка существования
    if not image_path.exists():
        return False
    
    # Проверка расширения
    supported_extensions = {'.png', '.jpg', '.jpeg', '.webp', '.bmp', '.tiff'}
    if image_path.suffix.lower() not in supported_extensions:
        return False
    
    # Проверка что это файл, а не директория
    if not image_path.is_file():
        return False
    
    return True


def get_image_info(image_path: Union[str, Path]) -> dict:
    """Получает информацию об изображении.
    
    Args:
        image_path: Путь к изображению
        
    Returns:
        Словарь с информацией: size, mode, format, file_size
        
    Пример:
        >>> info = get_image_info("page_001.png")
        >>> print(info)
        {'size': (1920, 2560), 'mode': 'RGB', 'format': 'PNG', 'file_size': '2.3 MB'}
    """
    image_path = Path(image_path)
    
    with Image.open(image_path) as img:
        info = {
            'size': img.size,
            'width': img.width,
            'height': img.height,
            'mode': img.mode,
            'format': img.format,
            'file_size': format_size(image_path.stat().st_size)
        }
    
    return info

def get_image_files(
    directory: Path,
    extensions: Optional[List[str]] = None,
    recursive: bool = False
) -> List[Path]:
    """Сканирует папку и возвращает список изображений.
    
    Args:
        directory: Путь к папке для сканирования
        extensions: Список расширений файлов (по умолчанию: ['.png', '.jpg', '.jpeg'])
        recursive: Рекурсивный поиск в подпапках
        
    Returns:
        Отсортированный список путей к изображениям
        
    Пример:
        >>> files = get_image_files(Path("data/raw/math/Книга"))
        >>> print(f"Найдено: {len(files)} изображений")
        Найдено: 234 изображений
    """
    directory = Path(directory)
    
    if not directory.exists():
        raise ValueError(f"Папка не найдена: {directory}")
    
    if not directory.is_dir():
        raise ValueError(f"Путь не является папкой: {directory}")
    
    # Расширения по умолчанию
    if extensions is None:
        extensions = ['.png', '.jpg', '.jpeg']
    
    # Приведение к нижнему регистру для сравнения
    extensions = [ext.lower() if ext.startswith('.') else f'.{ext.lower()}' 
                for ext in extensions]
    
    # Сканирование файлов
    image_files = []
    
    if recursive:
        # Рекурсивный поиск
        for ext in extensions:
            image_files.extend(directory.rglob(f'*{ext}'))
    else:
        # Только в текущей папке
        for ext in extensions:
            image_files.extend(directory.glob(f'*{ext}'))
    
    # Сортировка по имени файла
    image_files = sorted(image_files, key=lambda p: p.name)
    
    return image_files



if __name__ == "__main__":
    # Тестирование функций
    print("=" * 70)
    print("TESTING OCR UTILS")
    print("=" * 70)
    
    # Тест format_duration
    print("\n1. format_duration:")
    print(f"   65.5s -> {format_duration(65.5)}")
    print(f"   3665s -> {format_duration(3665)}")
    
    # Тест format_size
    print("\n2. format_size:")
    print(f"   1024 bytes -> {format_size(1024)}")
    print(f"   1536000 bytes -> {format_size(1536000)}")
    
    # Тест extract_page_number
    print("\n3. extract_page_number:")
    print(f"   'page_001.png' -> {extract_page_number('page_001.png')}")
    print(f"   'page_042.jpg' -> {extract_page_number('page_042.jpg')}")
    
    # Тест count_tokens_estimate
    print("\n4. count_tokens_estimate:")
    text = "Hello world! Привет мир!"
    print(f"   '{text}' -> ~{count_tokens_estimate(text)} tokens")
    
    # Тест create_output_path
    print("\n5. create_output_path:")
    input_path = Path("data/raw/math/Книга/page_001.png")
    output_path = create_output_path(input_path, "data/raw", "data/processed")
    print(f"   {input_path}")
    print(f"   -> {output_path}")
    
    print("\n" + "=" * 70)
