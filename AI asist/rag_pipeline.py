"""
Модуль для RAG-пайплайна (Retrieval-Augmented Generation).

Функции:
- Объединение релевантных документов в контекст
- Построение промпта для LLM модели
- Управление пайплайном генерации ответа
"""

from typing import List, Dict, Tuple
import logging

from config import MAX_CONTEXT_LENGTH, TOP_K_DOCUMENTS

logger = logging.getLogger(__name__)


class RAGPipeline:
    """
    RAG-пайплайн для поиска и генерации.
    
    Методы:
    - retrieve: получить релевантные документы
    - format_context: форматировать контекст для модели
    - build_prompt: построить промпт для LLM
    """
    
    def __init__(self, vector_store):
        """
        Инициализация RAG-пайплайна.
        
        Args:
            vector_store: объект VectorStore для поиска документов
        """
        self.vector_store = vector_store
        logger.info("RAGPipeline инициализирован")
    
    def retrieve(
        self,
        query: str,
        top_k: int = TOP_K_DOCUMENTS
    ) -> List[Tuple[Dict, float]]:
        """
        Получить релевантные документы из хранилища.
        
        Args:
            query: текстовый запрос
            top_k: количество документов для возврата
            
        Returns:
            список релевантных документов с оценками сходства
        """
        logger.info(f"Поиск релевантных документов для запроса: {query[:100]}")
        
        retrieved_docs = self.vector_store.search(query, top_k=top_k)
        
        logger.info(f"Найдено {len(retrieved_docs)} релевантных документов")
        
        return retrieved_docs
    
    @staticmethod
    def format_context(
        retrieved_docs: List[Tuple[Dict, float]],
        max_length: int = MAX_CONTEXT_LENGTH
    ) -> str:
        """
        Форматировать релевантные документы в контекст.
        
        Args:
            retrieved_docs: список релевантных документов
            max_length: максимальная длина контекста
            
        Returns:
            отформатированная строка контекста
        """
        context_parts = []
        current_length = 0
        
        for doc, similarity in retrieved_docs:
            # Форматирование информации о документе
            doc_text = f"""
            
Источник: {doc['source']} (сходство: {similarity:.2f})
---
{doc['content']}
---
"""
            
            # Проверка, не превышена ли максимальная длина
            if current_length + len(doc_text) <= max_length:
                context_parts.append(doc_text)
                current_length += len(doc_text)
            else:
                # Если добавить весь документ не получается,
                # добавить частично
                remaining_length = max_length - current_length
                if remaining_length > 100:
                    truncated = doc_text[:remaining_length] + "..."
                    context_parts.append(truncated)
                break
        
        context = "".join(context_parts)
        logger.debug(f"Контекст отформатирован. Длина: {len(context)}")
        
        return context
    
    @staticmethod
    def build_prompt(
        query: str,
        context: str,
        system_prompt: str = None
    ) -> str:
        """
        Построить промпт для LLM модели.
        
        Args:
            query: вопрос пользователя
            context: релевантный контекст из документов
            system_prompt: системный промпт (опционально)
            
        Returns:
            готовый промпт для модели
        """
        if system_prompt is None:
            system_prompt = """Ты — профессиональный AI-репетитор. 
Твоя задача — помочь студентам разобраться с учебным материалом, 
ответить на их вопросы четко и понятно, используя предоставленный контекст.

Инструкции:
1. Отвечай на основе предоставленного контекста
2. Если ответа нет в контексте, скажи об этом честно
3. Давай пояснения и примеры где необходимо
4. Будь дружелюбным и поддерживающим"""
        
        prompt = f"""{system_prompt}

---РЕЛЕВАНТНЫЙ КОНТЕКСТ---
{context}

---ВОПРОС---
{query}

---ОТВЕТ---
Подробный и понятный ответ:"""
        
        logger.debug(f"Промпт построен. Длина: {len(prompt)}")
        
        return prompt
    
    def generate_pipeline(
        self,
        query: str,
        llm_generator,
        top_k: int = TOP_K_DOCUMENTS
    ) -> Dict:
        """
        Полный пайплайн RAG: поиск -> форматирование -> генерация.
        
        Args:
            query: вопрос пользователя
            llm_generator: объект для генерации текста
            top_k: количество документов для поиска
            
        Returns:
            словарь с результатами
        """
        logger.info("Запуск RAG пайплайна")
        
        # Шаг 1: Поиск релевантных документов
        retrieved_docs = self.retrieve(query, top_k=top_k)
        
        # Шаг 2: Форматирование контекста
        context = self.format_context(retrieved_docs)
        
        # Шаг 3: Построение промпта
        prompt = self.build_prompt(query, context)
        
        # Шаг 4: Генерация ответа
        answer = llm_generator.generate(prompt)
        
        # Подготовка результата
        result = {
            'query': query,
            'answer': answer,
            'context_used': context,
            'retrieved_documents': [
                {
                    'source': doc['source'],
                    'similarity': sim,
                    'preview': doc['content'][:200]
                }
                for doc, sim in retrieved_docs
            ],
            'num_retrieved': len(retrieved_docs)
        }
        
        logger.info("RAG пайплайн завершен")
        
        return result
