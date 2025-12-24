"""
Утилиты для работы с AI-репетитором.

Содержит вспомогательные функции:
- Работа с конфигурацией
- Логирование
- Утилиты для отладки
"""

import logging
from pathlib import Path
from datetime import datetime
import json

from config import LOG_FILE, LOG_LEVEL, DATA_DIR


class Logger:
    """
    Настраиваемый логгер для приложения.
    
    Логирует в консоль и в файл одновременно.
    """
    
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance
    
    def _initialize(self):
        """Инициализация логгера."""
        # Создание директории для логов
        LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        # Создание логгера
        self.logger = logging.getLogger('AI-Tutor')
        self.logger.setLevel(getattr(logging, LOG_LEVEL))
        
        # Форматер
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # Обработчик для консоли
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # Обработчик для файла
        try:
            file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except Exception as e:
            self.logger.warning(f"Не удалось создать файл логов: {e}")
    
    def get_logger(self, name=None):
        """Получить логгер."""
        if name:
            return logging.getLogger(name)
        return self.logger


def get_logger(name=None):
    """
    Получить логгер приложения.
    
    Args:
        name: название модуля (опционально)
        
    Returns:
        объект логгера
    """
    logger_instance = Logger()
    return logger_instance.get_logger(name)


class ProgressTracker:
    """
    Отслеживание прогресса выполнения операций.
    
    Полезно для отслеживания долгих операций.
    """
    
    def __init__(self, total_steps: int, title: str = "Выполнение"):
        """
        Инициализация трекера прогресса.
        
        Args:
            total_steps: всего шагов
            title: название операции
        """
        self.total_steps = total_steps
        self.current_step = 0
        self.title = title
        self.logger = get_logger(__name__)
    
    def step(self, message: str = ""):
        """
        Перейти к следующему шагу.
        
        Args:
            message: сообщение о текущем шаге
        """
        self.current_step += 1
        progress = (self.current_step / self.total_steps) * 100
        
        msg = f"{self.title} [{self.current_step}/{self.total_steps}] {progress:.0f}%"
        if message:
            msg += f" - {message}"
        
        self.logger.info(msg)
    
    def complete(self, message: str = "Завершено"):
        """
        Завершить операцию.
        
        Args:
            message: финальное сообщение
        """
        self.logger.info(f"{self.title}: {message}")


class ConfigManager:
    """
    Менеджер конфигурации приложения.
    
    Позволяет загружать и сохранять настройки.
    """
    
    CONFIG_FILE = DATA_DIR / "config.json"
    
    @classmethod
    def load_config(cls) -> dict:
        """
        Загрузить конфигурацию из файла.
        
        Returns:
            словарь с конфигурацией
        """
        if cls.CONFIG_FILE.exists():
            try:
                with open(cls.CONFIG_FILE, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                get_logger(__name__).warning(f"Ошибка при загрузке конфига: {e}")
        
        return cls.get_default_config()
    
    @classmethod
    def save_config(cls, config: dict):
        """
        Сохранить конфигурацию в файл.
        
        Args:
            config: словарь с конфигурацией
        """
        cls.CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(cls.CONFIG_FILE, 'w', encoding='utf-8') as f:
                json.dump(config, f, ensure_ascii=False, indent=2)
            get_logger(__name__).info(f"Конфигурация сохранена: {cls.CONFIG_FILE}")
        except Exception as e:
            get_logger(__name__).error(f"Ошибка при сохранении конфига: {e}")
    
    @staticmethod
    def get_default_config() -> dict:
        """
        Получить конфигурацию по умолчанию.
        
        Returns:
            словарь с конфигурацией
        """
        return {
            'app_name': 'AI-Tutor',
            'version': '1.0.0',
            'created_at': datetime.now().isoformat(),
            'model': 'gpt-2',
            'embedding_model': 'sentence-transformers/all-MiniLM-L6-v2',
            'top_k': 5,
            'similarity_threshold': 0.3
        }


class SystemStats:
    """
    Сбор статистики работы системы.
    """
    
    def __init__(self):
        """Инициализация."""
        self.start_time = datetime.now()
        self.questions_count = 0
        self.documents_count = 0
        self.total_response_time = 0
    
    def add_question(self, response_time: float):
        """
        Добавить обработанный вопрос.
        
        Args:
            response_time: время обработки в секундах
        """
        self.questions_count += 1
        self.total_response_time += response_time
    
    def set_documents_count(self, count: int):
        """
        Установить количество документов.
        
        Args:
            count: количество документов
        """
        self.documents_count = count
    
    def get_stats(self) -> dict:
        """
        Получить статистику.
        
        Returns:
            словарь со статистикой
        """
        uptime = (datetime.now() - self.start_time).total_seconds()
        avg_response_time = (
            self.total_response_time / self.questions_count
            if self.questions_count > 0 else 0
        )
        
        return {
            'uptime_seconds': uptime,
            'questions_processed': self.questions_count,
            'documents_indexed': self.documents_count,
            'average_response_time': avg_response_time,
            'total_response_time': self.total_response_time
        }
    
    def print_stats(self):
        """Вывести статистику."""
        stats = self.get_stats()
        logger = get_logger(__name__)
        
        logger.info("=" * 60)
        logger.info("СТАТИСТИКА СИСТЕМЫ")
        logger.info("=" * 60)
        logger.info(f"Время работы: {stats['uptime_seconds']:.0f} сек")
        logger.info(f"Обработано вопросов: {stats['questions_processed']}")
        logger.info(f"Индексировано документов: {stats['documents_indexed']}")
        logger.info(f"Среднее время ответа: {stats['average_response_time']:.2f} сек")
        logger.info("=" * 60)


class TimerContext:
    """
    Контекстный менеджер для отслеживания времени выполнения.
    
    Использование:
        with TimerContext("Операция"):
            # код
    """
    
    def __init__(self, operation_name: str):
        """
        Инициализация.
        
        Args:
            operation_name: название операции
        """
        self.operation_name = operation_name
        self.start_time = None
        self.logger = get_logger(__name__)
    
    def __enter__(self):
        """Начало отслеживания."""
        self.start_time = datetime.now()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Конец отслеживания."""
        elapsed = (datetime.now() - self.start_time).total_seconds()
        
        if exc_type is None:
            self.logger.info(f"✓ {self.operation_name}: {elapsed:.2f} сек")
        else:
            self.logger.error(
                f"✗ {self.operation_name} завершился с ошибкой: {exc_type.__name__}"
            )
        
        return False


def print_banner():
    """Вывести баннер приложения."""
    banner = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║              🎓 AI-РЕПЕТИТОР НА ОСНОВЕ RAG 🎓                ║
    ║                                                                ║
    ║            Интеллектуальная система обучения v1.0             ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    print(banner)


def debug_info():
    """Вывести информацию для отладки."""
    logger = get_logger(__name__)
    
    logger.info("=" * 60)
    logger.info("ИНФОРМАЦИЯ ДЛЯ ОТЛАДКИ")
    logger.info("=" * 60)
    logger.info(f"Директория данных: {DATA_DIR}")
    logger.info(f"Файл логов: {LOG_FILE}")
    logger.info(f"Уровень логирования: {LOG_LEVEL}")
    
    # Проверка файлов
    logger.info("\nФайлы конфигурации:")
    logger.info(f"  - config.json: {'✓' if ConfigManager.CONFIG_FILE.exists() else '✗'}")
    
    logger.info("=" * 60)


if __name__ == '__main__':
    print_banner()
    debug_info()
