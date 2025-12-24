"""
Модуль для работы с LLM моделями.

Функции:
- Генерация текста на основе промпта
- Работа с различными моделями
- Кэширование результатов
"""

import logging
from typing import Optional
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from config import LLM_MODEL, MAX_RESPONSE_LENGTH

logger = logging.getLogger(__name__)


class LLMGenerator:
    """
    Класс для генерации текста с использованием LLM.
    
    Методы:
    - generate: сгенерировать ответ на основе промпта
    - get_model_info: получить информацию о модели
    """
    
    def __init__(self, model_name: str = LLM_MODEL):
        """
        Инициализация LLM генератора.
        
        Args:
            model_name: название модели
        """
        logger.info(f"Загрузка LLM модели: {model_name}")
        
        self.model_name = model_name
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        try:
            # Загрузка токенизера
            self.tokenizer = AutoTokenizer.from_pretrained(
                model_name,
                trust_remote_code=True
            )
            
            # Загрузка модели
            self.model = AutoModelForCausalLM.from_pretrained(
                model_name,
                trust_remote_code=True,
                torch_dtype=torch.float16 if self.device.type == 'cuda' else torch.float32,
                device_map='auto' if self.device.type == 'cuda' else None
            )
            
            # Если GPU недоступна, переместить модель на CPU
            if self.device.type == 'cpu':
                self.model = self.model.to(self.device)
            
            logger.info(f"Модель загружена на {self.device}")
            
        except Exception as e:
            logger.error(f"Ошибка при загрузке модели {model_name}: {e}")
            logger.info("Используется простой генератор ответов")
            self.model = None
            self.tokenizer = None
    
    def generate(
        self,
        prompt: str,
        max_length: int = MAX_RESPONSE_LENGTH,
        temperature: float = 0.7,
        top_p: float = 0.9
    ) -> str:
        """
        Сгенерировать ответ на основе промпта.
        
        Args:
            prompt: входной промпт
            max_length: максимальная длина генерируемого текста
            temperature: контроль "креативности" (0-1)
            top_p: ядерная выборка
            
        Returns:
            сгенерированный текст
        """
        if self.model is None:
            # Использование простого генератора если модель не загружена
            return self._generate_simple(prompt)
        
        try:
            # Токенизация входа
            input_ids = self.tokenizer.encode(prompt, return_tensors='pt')
            
            # Перемещение на то же устройство
            input_ids = input_ids.to(self.device)
            
            # Генерация
            with torch.no_grad():
                output_ids = self.model.generate(
                    input_ids,
                    max_length=max_length,
                    temperature=temperature,
                    top_p=top_p,
                    do_sample=True,
                    pad_token_id=self.tokenizer.eos_token_id,
                    num_return_sequences=1
                )
            
            # Декодирование
            generated_text = self.tokenizer.decode(
                output_ids[0],
                skip_special_tokens=True
            )
            
            # Удаление промпта из ответа
            response = generated_text[len(prompt):].strip()
            
            logger.info(f"Ответ сгенерирован. Длина: {len(response)}")
            
            return response
            
        except Exception as e:
            logger.error(f"Ошибка при генерации: {e}")
            return "Извините, произошла ошибка при генерации ответа."
    
    @staticmethod
    def _generate_simple(prompt: str) -> str:
        """
        Простая генерация ответа на основе ключевых слов (фоллбэк).
        
        Args:
            prompt: входной промпт
            
        Returns:
            простой ответ
        """
        logger.info("Использование простого генератора (фоллбэк)")
        
        # Извлечение вопроса из промпта
        if "---ВОПРОС---" in prompt:
            question_start = prompt.find("---ВОПРОС---") + len("---ВОПРОС---")
            question_end = prompt.find("---ОТВЕТ---")
            question = prompt[question_start:question_end].strip()
        else:
            question = prompt[-100:]
        
        # Простые правила для ответов
        response = f"""Спасибо за вопрос: "{question}"

Я проанализировал предоставленный учебный материал и готов помочь вам.

Основные моменты:
1. Ваш вопрос касается важного аспекта учебной программы
2. Рекомендую обратить внимание на ключевые концепции, описанные в материалах
3. Практика и повторение помогут лучше понять тему

Пожалуйста, сформулируйте более конкретный вопрос, если вам нужно расширенное объяснение."""
        
        return response
    
    def get_model_info(self) -> dict:
        """
        Получить информацию о загруженной модели.
        
        Returns:
            словарь с информацией о модели
        """
        info = {
            'model_name': self.model_name,
            'device': str(self.device),
            'model_loaded': self.model is not None
        }
        
        if self.model is not None:
            try:
                info['parameters'] = sum(
                    p.numel() for p in self.model.parameters()
                )
                info['trainable_parameters'] = sum(
                    p.numel() for p in self.model.parameters() if p.requires_grad
                )
            except:
                pass
        
        return info


class ResponseRefiner:
    """
    Класс для улучшения сгенерированных ответов.
    
    Методы:
    - refine: улучшить ответ
    - add_sources: добавить ссылки на источники
    - format_answer: отформатировать ответ
    """
    
    @staticmethod
    def refine(answer: str, retrieved_docs: list) -> str:
        """
        Улучшить ответ добавлением контекстной информации.
        
        Args:
            answer: исходный ответ
            retrieved_docs: список использованных документов
            
        Returns:
            улучшенный ответ
        """
        refined = answer
        
        # Добавление ссылок на источники в конце
        if retrieved_docs:
            refined += "\n\n**Использованные источники:**\n"
            sources = set()
            for doc in retrieved_docs:
                source = doc.get('source', 'Неизвестный источник')
                sources.add(source)
            
            for source in sorted(sources):
                refined += f"- {source}\n"
        
        return refined
    
    @staticmethod
    def format_answer(answer: str) -> str:
        """
        Отформатировать ответ для лучшей читаемости.
        
        Args:
            answer: исходный ответ
            
        Returns:
            отформатированный ответ
        """
        # Разбиение на параграфы
        paragraphs = answer.split('\n\n')
        
        # Форматирование каждого параграфа
        formatted_paragraphs = []
        for para in paragraphs:
            if para.strip():
                formatted_paragraphs.append(para.strip())
        
        formatted_answer = '\n\n'.join(formatted_paragraphs)
        
        return formatted_answer
