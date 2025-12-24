"""
Конфигурация OCR модуля.

Загружает настройки из .env файла и предоставляет удобный доступ к параметрам.

Для теста с текущим .env запустите из корня проекта команду 

python -m rag_pipeline.ocr.config

"""

import logging
import os
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Загружаем .env файл
load_dotenv()

logger = logging.getLogger(__name__)


class OCRConfig:
    """Конфигурация для OCR обработки.
    
    Загружает параметры из переменных окружения (.env файл).
    Предоставляет валидированные значения с fallback на значения по умолчанию.
    
    Attributes:
        base_url (str): URL vLLM API сервера
        model_name (str): Название модели для OCR
        api_key (str): API ключ (обычно "EMPTY" для vLLM)
        max_workers (int): Количество параллельных потоков
        resize_image (bool): Флаг ресайза изображений
        max_image_size (int): Максимальный размер изображения (px)
        timeout (int): Таймаут запроса (секунды)
        temperature (float): Температура генерации
        max_tokens (Optional[int]): Максимальное количество токенов в ответе
        data_raw_dir (Path): Директория с исходными изображениями
        data_processed_dir (Path): Директория для сохранения результатов
        log_level (str): Уровень логирования
        log_file (Path): Путь к файлу логов
    
    Пример:
        >>> config = OCRConfig()
        >>> print(config.base_url)
        'http://localhost:8000/v1'
    """
    
    def __init__(self):
        """Инициализирует конфигурацию из переменных окружения."""
        
        # =================================================================
        # vLLM СЕРВЕР
        # =================================================================
        self.base_url = os.getenv("VLLM_BASE_URL", "http://localhost:8000/v1")
        self.model_name = os.getenv("VLLM_MODEL_NAME", "/models/olmOCR-2-7B-1025")
        self.api_key = os.getenv("VLLM_API_KEY", "EMPTY")
        
        # =================================================================
        # ПАРАМЕТРЫ ОБРАБОТКИ
        # =================================================================
        self.max_workers = self._parse_int("MAX_WORKERS", 4)
        
        # =================================================================
        # ПАРАМЕТРЫ ИЗОБРАЖЕНИЙ
        # =================================================================
        self.resize_image = self._parse_bool("RESIZE_IMAGE", True)
        self.max_image_size = self._parse_int("MAX_IMAGE_SIZE", 1920)
        
        # =================================================================
        # ПАРАМЕТРЫ ГЕНЕРАЦИИ
        # =================================================================
        self.timeout = self._parse_int("TIMEOUT", 180)
        self.temperature = self._parse_float("TEMPERATURE", 0.0)
        self.max_tokens = self._parse_max_tokens("MAX_TOKENS", 8192)
        self.prompt_type = os.getenv("PROMPT_TYPE", "olmocr_technical")

        # Параметры YAML (по умолчанию для русских технических книг)
        self.yaml_language = os.getenv("YAML_LANGUAGE", "ru")
        self.yaml_is_table = self._parse_bool("YAML_IS_TABLE", True)
        self.yaml_is_diagram = self._parse_bool("YAML_IS_DIAGRAM", True)
                
        # =================================================================
        # ПУТИ К ДАННЫМ
        # =================================================================
        self.data_raw_dir = Path(os.getenv("DATA_RAW_DIR", "data/raw"))
        self.data_processed_dir = Path(os.getenv("DATA_PROCESSED_DIR", "data/processed"))
        
        # =================================================================
        # ЛОГИРОВАНИЕ
        # =================================================================
        self.log_level = os.getenv("LOG_LEVEL", "INFO").upper()
        self.console_log_level = os.getenv("CONSOLE_LOG_LEVEL", "CRITICAL").upper()
        self.log_file = Path(os.getenv("LOG_FILE", "logs/ocr_processing.log"))
        
        # Валидация конфигурации
        self._validate()
    
    def _parse_int(self, env_var: str, default: int) -> int:
        """Парсит целое число из переменной окружения.
        
        Args:
            env_var: Название переменной окружения
            default: Значение по умолчанию
            
        Returns:
            Целое число
        """
        value = os.getenv(env_var)
        if value is None:
            return default
        
        try:
            return int(value)
        except ValueError:
            logger.warning(
                f"Некорректное значение {env_var}='{value}'. "
                f"Используется значение по умолчанию: {default}"
            )
            return default
    
    def _parse_float(self, env_var: str, default: float) -> float:
        """Парсит float из переменной окружения.
        
        Args:
            env_var: Название переменной окружения
            default: Значение по умолчанию
            
        Returns:
            Float число
        """
        value = os.getenv(env_var)
        if value is None:
            return default
        
        try:
            return float(value)
        except ValueError:
            logger.warning(
                f"Некорректное значение {env_var}='{value}'. "
                f"Используется значение по умолчанию: {default}"
            )
            return default
    
    def _parse_bool(self, env_var: str, default: bool) -> bool:
        """Парсит boolean из переменной окружения.
        
        Принимает: true/false, yes/no, 1/0 (регистронезависимо)
        
        Args:
            env_var: Название переменной окружения
            default: Значение по умолчанию
            
        Returns:
            Boolean значение
        """
        value = os.getenv(env_var)
        if value is None:
            return default
        
        value_lower = value.lower().strip()
        
        if value_lower in ("true", "yes", "1", "on"):
            return True
        elif value_lower in ("false", "no", "0", "off"):
            return False
        else:
            logger.warning(
                f"Некорректное значение {env_var}='{value}'. "
                f"Используется значение по умолчанию: {default}"
            )
            return default
    
    def _parse_max_tokens(self, env_var: str, default: int) -> Optional[int]:
        """Парсит MAX_TOKENS из переменной окружения.
        
        Поддерживает:
        - "auto" или "none" -> None (автоматический расчет vLLM)
        - Число -> int
        
        Args:
            env_var: Название переменной окружения
            default: Значение по умолчанию
            
        Returns:
            int или None
        """
        value = os.getenv(env_var)
        if value is None:
            return default
        
        value_lower = value.lower().strip()
        
        if value_lower in ("auto", "none", "null"):
            return None
        
        try:
            return int(value)
        except ValueError:
            logger.warning(
                f"Некорректное значение {env_var}='{value}'. "
                f"Используется значение по умолчанию: {default}"
            )
            return default
    
    def _validate(self):
        """Валидирует корректность конфигурации."""
        
        # Проверка URL
        if not self.base_url.startswith(("http://", "https://")):
            raise ValueError(
                f"VLLM_BASE_URL должен начинаться с http:// или https://. "
                f"Получено: {self.base_url}"
            )
        
        # Проверка max_workers
        if self.max_workers < 1:
            raise ValueError(f"MAX_WORKERS должен быть >= 1. Получено: {self.max_workers}")
        
        # Проверка max_image_size
        if self.max_image_size < 100:
            raise ValueError(
                f"MAX_IMAGE_SIZE должен быть >= 100. Получено: {self.max_image_size}"
            )
        
        # Проверка timeout
        if self.timeout < 10:
            raise ValueError(f"TIMEOUT должен быть >= 10. Получено: {self.timeout}")
        
        # Проверка temperature
        if not 0.0 <= self.temperature <= 2.0:
            raise ValueError(
                f"TEMPERATURE должна быть в диапазоне [0.0, 2.0]. "
                f"Получено: {self.temperature}"
            )
        
        # Проверка max_tokens
        if self.max_tokens is not None and self.max_tokens < 1:
            raise ValueError(f"MAX_TOKENS должен быть >= 1. Получено: {self.max_tokens}")
        
        # Создание директорий для логов
        self.log_file.parent.mkdir(parents=True, exist_ok=True)
    
    def to_dict(self) -> dict:
        """Конвертирует конфигурацию в словарь.
        
        Returns:
            Словарь с параметрами конфигурации
        """
        return {
            "vllm": {
                "base_url": self.base_url,
                "model_name": self.model_name,
                "api_key": "***" if self.api_key != "EMPTY" else "EMPTY",
            },
            "processing": {
                "max_workers": self.max_workers,
            },
            "image": {
                "resize_image": self.resize_image,
                "max_image_size": self.max_image_size,
            },
            "generation": {
                "timeout": self.timeout,
                "temperature": self.temperature,
                "max_tokens": self.max_tokens,
                "prompt_type": self.prompt_type, 
            },
            "yaml_params": {
                "language": self.yaml_language,
                "is_table": self.yaml_is_table,
                "is_diagram": self.yaml_is_diagram,
            },
            "paths": {
                "data_raw_dir": str(self.data_raw_dir),
                "data_processed_dir": str(self.data_processed_dir),
            },
            "logging": {
                "log_level": self.log_level,
                "log_file": str(self.log_file),
            }
        }
    
    def __repr__(self) -> str:
        """Строковое представление конфигурации."""
        return f"OCRConfig(base_url='{self.base_url}', model='{self.model_name}')"
    
    def __str__(self) -> str:
        """Человекочитаемое представление конфигурации."""
        import json
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)


# Создаем глобальный экземпляр конфигурации для удобства
config = OCRConfig()


if __name__ == "__main__":
    # Тестирование конфигурации
    print("=" * 70)
    print("OCR CONFIGURATION")
    print("=" * 70)
    print(config)
    print("=" * 70)
