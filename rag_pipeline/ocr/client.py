"""
Клиент для взаимодействия с vLLM API.

Предоставляет удобный интерфейс для отправки OCR запросов к vLLM серверу
через OpenAI-совместимый API с поддержкой специфических промптов для olmOCR.
"""

import logging
import time
from typing import Any, Dict, List, Literal, Optional

from openai import APIConnectionError, APIError, APITimeoutError, OpenAI
import requests

from .config import OCRConfig

logger = logging.getLogger(__name__)


# ============================================================================
# ПРОМПТЫ ДЛЯ РАЗНЫХ МОДЕЛЕЙ
# ============================================================================

def build_olmocr_yaml_prompt(
    language: str = "ru",
    rotation_valid: bool = True,
    rotation_correction: int = 0,
    is_table: bool = False,
    is_diagram: bool = False
) -> str:
    """Строит YAML промпт для olmOCR модели с настраиваемыми параметрами.
    
    Args:
        language: Язык контента ('ru', 'en', 'mixed')
        rotation_valid: Правильно ли ориентировано изображение
        rotation_correction: Угол поворота для коррекции (0, 90, 180, 270)
        is_table: Содержит ли страница таблицы
        is_diagram: Содержит ли страница диаграммы/графики
    
    Returns:
        YAML-форматированный промпт
    """
    return f"""---
primary_language: {language}
is_rotation_valid: {str(rotation_valid)}
rotation_correction: {rotation_correction}
is_table: {str(is_table)}
is_diagram: {str(is_diagram)}
---"""


def build_olmocr_universal_prompt() -> str:
    """Универсальный YAML промпт для технических книг.
    
    Оптимизирован для русскоязычного контента со смешанным содержимым:
    текст, код, формулы, таблицы, диаграммы.
    
    Returns:
        YAML-форматированный промпт
    """
    return """---
primary_language: ru
is_rotation_valid: True
rotation_correction: 0
is_table: auto
is_diagram: auto
---"""


def build_olmocr_technical_prompt() -> str:
    """YAML промпт для технических книг с кодом и формулами.
    
    Подходит для учебников по программированию, математике,
    где встречается код, формулы, диаграммы.
    
    Returns:
        YAML-форматированный промпт
    """
    return """---
primary_language: ru
is_rotation_valid: True
rotation_correction: 0
is_table: True
is_diagram: True
---"""


def build_simple_prompt() -> str:
    """Простой промпт для базового OCR без YAML метаданных.
    
    Returns:
        Текстовый промпт
    """
    return "Extract all text from this image, preserving formatting, formulas, symbols, and code blocks."


def build_russian_technical_prompt() -> str:
    """Промпт для русскоязычных технических текстов.
    
    Returns:
        Текстовый промпт
    """
    return """Распознай весь текст с этого изображения. Сохрани:
- Форматирование и структуру
- Код (Python, Rust, и т.д.) в блоках кода
- Математические формулы в LaTeX
- Таблицы в markdown формате
- Диаграммы и графики (описание)"""


PROMPT_TEMPLATES = {
    "olmocr_yaml": lambda: build_olmocr_yaml_prompt(language="en"),  # Оригинальный
    "olmocr_ru": lambda: build_olmocr_yaml_prompt(language="ru"),    # Русский
    "olmocr_universal": build_olmocr_universal_prompt,                # Универсальный
    "olmocr_technical": build_olmocr_technical_prompt,                # Технический (рекомендуется!)
    "simple": build_simple_prompt,
    "russian_technical": build_russian_technical_prompt,
}


class VLLMClient:
    """Клиент для работы с vLLM сервером через OpenAI API.
    
    Предоставляет методы для:
    - Проверки доступности сервера
    - Получения списка моделей
    - Отправки OCR запросов с поддержкой разных промптов
    
    Thread-safe: Да (каждый запрос создает новое соединение)
    
    Attributes:
        config (OCRConfig): Конфигурация OCR модуля
        client (OpenAI): OpenAI клиент для vLLM
        
    Пример:
        >>> from rag_pipeline.ocr import VLLMClient, OCRConfig
        >>> config = OCRConfig()
        >>> client = VLLMClient(config)
        >>> if client.check_availability():
        ...     result = client.ocr_request(
        ...         image_base64,
        ...         prompt_type="olmocr_yaml"
        ...     )
    """
    
    def __init__(self, config: Optional[OCRConfig] = None):
        """Инициализирует клиент vLLM.
        
        Args:
            config: Конфигурация OCR модуля. Если None - создается новая.
        """
        self.config = config or OCRConfig()
        
        # Создание OpenAI клиента
        self.client = OpenAI(
            api_key=self.config.api_key,
            base_url=self.config.base_url,
            timeout=self.config.timeout
        )
        
        logger.debug(f"Создан VLLMClient для {self.config.base_url}")
    
    def check_availability(self, timeout: int = 5) -> bool:
        """Проверяет доступность vLLM сервера.
        
        Отправляет простой GET запрос к /v1/models для проверки,
        что сервер отвечает.
        
        Args:
            timeout: Таймаут проверки (секунды)
            
        Returns:
            True если сервер доступен, иначе False
            
        Пример:
            >>> client = VLLMClient()
            >>> if client.check_availability():
            ...     print("Сервер доступен")
        """
        try:
            # Формируем URL для /v1/models
            models_url = self.config.base_url.rstrip('/').replace('/v1', '') + '/v1/models'
            
            response = requests.get(
                models_url,
                timeout=timeout,
                headers={"Authorization": f"Bearer {self.config.api_key}"}
            )
            
            if response.status_code == 200:
                logger.debug("vLLM сервер доступен")
                return True
            else:
                logger.warning(f"vLLM сервер вернул код {response.status_code}")
                return False
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Ошибка подключения к vLLM серверу: {e}")
            return False
    
    def get_available_models(self) -> List[str]:
        """Получает список доступных моделей на сервере.
        
        Returns:
            Список названий моделей
            
        Raises:
            APIConnectionError: Если не удалось подключиться к серверу
            
        Пример:
            >>> client = VLLMClient()
            >>> models = client.get_available_models()
            >>> print(models)
            ['/models/olmOCR-2-7B-1025']
        """
        try:
            models = self.client.models.list()
            model_ids = [model.id for model in models.data]
            
            logger.debug(f"Найдено моделей: {len(model_ids)}")
            return model_ids
            
        except APIConnectionError as e:
            logger.error(f"Не удалось получить список моделей: {e}")
            raise
        except Exception as e:
            logger.error(f"Неожиданная ошибка при получении моделей: {e}")
            return []
    
    def _build_messages(
        self,
        image_base64: str,
        prompt: Optional[str] = None,
        prompt_type: str = "olmocr_yaml"
    ) -> List[Dict[str, Any]]:
        """Строит список сообщений для Chat Completions API.
        
        Args:
            image_base64: Изображение в формате base64
            prompt: Кастомный промпт (если None - используется prompt_type)
            prompt_type: Тип промпта из PROMPT_TEMPLATES
            
        Returns:
            Список сообщений в формате OpenAI Chat API
        """
        # Выбор промпта
        if prompt is None:
            if prompt_type in PROMPT_TEMPLATES:
                prompt = PROMPT_TEMPLATES[prompt_type]()
            else:
                logger.warning(
                    f"Неизвестный prompt_type='{prompt_type}'. "
                    f"Используется 'olmocr_yaml'"
                )
                prompt = PROMPT_TEMPLATES["olmocr_yaml"]()
        
        # Формирование сообщений
        # ВАЖНО: Порядок как в официальном примере - сначала текст, потом изображение
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{image_base64}"
                        }
                    }
                ]
            }
        ]
        
        return messages
    
    def ocr_request(
        self,
        image_base64: str,
        prompt: Optional[str] = None,
        prompt_type: str = "olmocr_yaml",
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        model_name: Optional[str] = None
    ) -> Dict[str, Any]:
        """Отправляет OCR запрос к vLLM серверу.
        
        Args:
            image_base64: Изображение в формате base64
            prompt: Кастомный промпт (если указан - игнорирует prompt_type)
            prompt_type: Тип промпта ('olmocr_yaml', 'simple', 'math')
            temperature: Температура генерации (если None - из config)
            max_tokens: Максимальное количество токенов (если None - из config)
            model_name: Название модели (если None - из config)
            
        Returns:
            Словарь с результатом:
            {
                'text': str,              # Распознанный текст
                'tokens': int,            # Количество токенов
                'processing_time': float, # Время обработки (секунды)
                'model': str,             # Название модели
                'finish_reason': str,     # Причина остановки генерации
                'prompt_type': str        # Использованный тип промпта
            }
            
        Raises:
            APIError: Ошибка API (невалидный запрос, и т.д.)
            APIConnectionError: Ошибка подключения
            APITimeoutError: Превышен таймаут
            
        Пример:
            >>> client = VLLMClient()
            >>> # Использование olmOCR YAML промпта
            >>> result = client.ocr_request(
            ...     image_base64="iVBORw0KGgo...",
            ...     prompt_type="olmocr_yaml"
            ... )
            >>> print(result['text'])
            
            >>> # Использование кастомного промпта
            >>> result = client.ocr_request(
            ...     image_base64="iVBORw0KGgo...",
            ...     prompt="Extract only tables from this image"
            ... )
        """
        # Использование значений из config если не указаны
        temperature = temperature if temperature is not None else self.config.temperature
        max_tokens = max_tokens if max_tokens is not None else self.config.max_tokens
        model_name = model_name or self.config.model_name
        
        # Формирование сообщений
        messages = self._build_messages(image_base64, prompt, prompt_type)
        
        # Параметры запроса
        request_params = {
            "model": model_name,
            "messages": messages,
            "temperature": temperature,
        }
        
        # Добавляем max_tokens только если он указан
        if max_tokens is not None:
            request_params["max_tokens"] = max_tokens
        
        logger.debug(
            f"Отправка OCR запроса: model={model_name}, "
            f"prompt_type={prompt_type}, "
            f"temperature={temperature}, max_tokens={max_tokens}"
        )
        
        # Засекаем время
        start_time = time.time()
        
        try:
            # Отправка запроса
            response = self.client.chat.completions.create(**request_params)
            
            processing_time = time.time() - start_time
            
            # Извлечение результата
            text = response.choices[0].message.content
            finish_reason = response.choices[0].finish_reason
            
            # Подсчет токенов
            tokens = 0
            if response.usage:
                tokens = response.usage.total_tokens
            
            result = {
                'text': text,
                'tokens': tokens,
                'processing_time': processing_time,
                'model': model_name,
                'finish_reason': finish_reason,
                'prompt_type': prompt_type if prompt is None else 'custom'
            }
            
            logger.debug(
                f"OCR запрос выполнен за {processing_time:.2f}с, "
                f"токенов: {tokens}, символов: {len(text)}"
            )
            
            return result
            
        except APITimeoutError as e:
            logger.error(f"Таймаут OCR запроса: {e}")
            raise
            
        except APIConnectionError as e:
            logger.error(f"Ошибка подключения при OCR запросе: {e}")
            raise
            
        except APIError as e:
            logger.error(f"Ошибка API при OCR запросе: {e}")
            raise
            
        except Exception as e:
            logger.error(f"Неожиданная ошибка при OCR запросе: {e}")
            raise
    
    def health_check(self) -> Dict[str, Any]:
        """Проверяет состояние vLLM сервера.
        
        Returns:
            Словарь с информацией о сервере:
            {
                'available': bool,
                'models': List[str],
                'base_url': str,
                'model_name': str,
                'available_prompts': List[str]
            }
            
        Пример:
            >>> client = VLLMClient()
            >>> health = client.health_check()
            >>> print(health)
        """
        available = self.check_availability()
        
        models = []
        if available:
            try:
                models = self.get_available_models()
            except Exception as e:
                logger.warning(f"Не удалось получить список моделей: {e}")
        
        return {
            'available': available,
            'models': models,
            'base_url': self.config.base_url,
            'model_name': self.config.model_name,
            'available_prompts': list(PROMPT_TEMPLATES.keys())
        }
    
    def __repr__(self) -> str:
        """Строковое представление клиента."""
        return f"VLLMClient(base_url='{self.config.base_url}')"


if __name__ == "__main__":
    # Тестирование клиента
    print("=" * 70)
    print("TESTING VLLM CLIENT")
    print("=" * 70)
    
    try:
        # Создание клиента
        client = VLLMClient()
        print(f"\n✅ Клиент создан: {client}")
        
        # Показать доступные промпты
        print("\n📝 Доступные типы промптов:")
        for prompt_type in PROMPT_TEMPLATES.keys():
            print(f"   - {prompt_type}")
        
        # Примеры промптов
        print("\n📋 Пример olmOCR YAML промпта:")
        print("-" * 70)
        print(build_olmocr_yaml_prompt())
        print("-" * 70)
        
        # Health check
        print("\n🔍 Проверка состояния сервера...")
        health = client.health_check()
        
        print(f"   Доступен: {health['available']}")
        print(f"   Base URL: {health['base_url']}")
        print(f"   Модель: {health['model_name']}")
        
        if health['models']:
            print(f"   Доступные модели:")
            for model in health['models']:
                print(f"     - {model}")
        
        if health['available']:
            print("\n✅ Сервер доступен и готов к работе!")
        else:
            print("\n⚠️ Сервер недоступен. Проверьте настройки .env")
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 70)
