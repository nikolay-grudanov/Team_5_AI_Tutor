"""
Модуль для работы с эмбеддингами и векторным хранилищем.

Функции:
- Создание эмбеддингов для текстов
- Сохранение и загрузка векторного хранилища
- Поиск релевантных документов по сходству
"""

import numpy as np
from typing import List, Dict, Tuple
import logging
import json
from pathlib import Path

from sentence_transformers import SentenceTransformer

from config import (
    EMBEDDING_MODEL,
    EMBEDDING_DIMENSION,
    VECTOR_STORE_DIR,
    TOP_K_DOCUMENTS,
    SIMILARITY_THRESHOLD,
    METRIC_TYPE
)

logger = logging.getLogger(__name__)


class EmbeddingModel:
    """
    Класс для создания эмбеддингов текстов.
    
    Методы:
    - encode: создать эмбеддинг для текста или списка текстов
    - batch_encode: создать эмбеддинги для большого количества текстов
    """
    
    def __init__(self, model_name: str = EMBEDDING_MODEL):
        """
        Инициализация модели эмбеддингов.
        
        Args:
            model_name: название модели с Hugging Face
        """
        logger.info(f"Загрузка модели эмбеддингов: {model_name}")
        self.model = SentenceTransformer(model_name)
        self.dimension = EMBEDDING_DIMENSION
        logger.info(f"Модель загружена. Размерность: {self.dimension}")
    
    def encode(self, texts: str | List[str]) -> np.ndarray:
        """
        Создать эмбеддинг(и) для текста(ов).
        
        Args:
            texts: текст или список текстов
            
        Returns:
            numpy массив эмбеддингов
        """
        if isinstance(texts, str):
            texts = [texts]
        
        embeddings = self.model.encode(texts, convert_to_numpy=True)
        return embeddings
    
    def batch_encode(
        self,
        texts: List[str],
        batch_size: int = 32
    ) -> np.ndarray:
        """
        Создать эмбеддинги для списка текстов батчами.
        
        Args:
            texts: список текстов
            batch_size: размер батча
            
        Returns:
            numpy массив эмбеддингов
        """
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            convert_to_numpy=True,
            show_progress_bar=True
        )
        return embeddings


class VectorStore:
    """
    Векторное хранилище для хранения эмбеддингов и поиска.
    
    Методы:
    - add_chunks: добавить чанки в хранилище
    - search: найти релевантные чанки по текстовому запросу
    - save: сохранить хранилище на диск
    - load: загрузить хранилище с диска
    """
    
    def __init__(self, embedding_model: EmbeddingModel):
        """
        Инициализация векторного хранилища.
        
        Args:
            embedding_model: модель для создания эмбеддингов
        """
        self.embedding_model = embedding_model
        self.chunks = []
        self.embeddings = np.array([])
        self.index = None
        logger.info("VectorStore инициализирован")
    
    def add_chunks(self, chunks: List[Dict], batch_size: int = 32):
        """
        Добавить чанки в хранилище с созданием эмбеддингов.
        
        Args:
            chunks: список чанков с содержимым
            batch_size: размер батча для обработки
        """
        logger.info(f"Добавление {len(chunks)} чанков в VectorStore")
        
        # Сохранение метаинформации о чанках
        self.chunks = chunks
        
        # Извлечение текстов для эмбеддинга
        texts = [chunk['content'] for chunk in chunks]
        
        # Создание эмбеддингов батчами
        self.embeddings = self.embedding_model.batch_encode(texts, batch_size)
        
        logger.info(
            f"Эмбеддинги созданы. Форма: {self.embeddings.shape}"
        )
    
    @staticmethod
    def cosine_similarity(vec1: np.ndarray, vec2: np.ndarray) -> float:
        """
        Вычислить косинусное сходство между двумя векторами.
        
        Args:
            vec1: первый вектор
            vec2: второй вектор
            
        Returns:
            значение сходства от -1 до 1
        """
        norm1 = np.linalg.norm(vec1)
        norm2 = np.linalg.norm(vec2)
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return np.dot(vec1, vec2) / (norm1 * norm2)
    
    def search(
        self,
        query: str,
        top_k: int = TOP_K_DOCUMENTS,
        threshold: float = SIMILARITY_THRESHOLD
    ) -> List[Tuple[Dict, float]]:
        """
        Найти релевантные чанки по запросу.
        
        Args:
            query: текстовый запрос
            top_k: количество результатов
            threshold: минимальное значение сходства
            
        Returns:
            список кортежей (чанк, сходство)
        """
        # Создание эмбеддинга для запроса
        query_embedding = self.embedding_model.encode(query)
        if len(query_embedding.shape) > 1:
            query_embedding = query_embedding[0]
        
        # Вычисление сходства со всеми чанками
        similarities = []
        for idx, chunk_embedding in enumerate(self.embeddings):
            sim = self.cosine_similarity(query_embedding, chunk_embedding)
            if sim >= threshold:
                similarities.append((idx, sim))
        
        # Сортировка по сходству в убывающем порядке
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        # Возврат топ-k результатов
        results = []
        for idx, sim in similarities[:top_k]:
            chunk = self.chunks[idx]
            results.append((chunk, float(sim)))
        
        logger.debug(f"Найдено {len(results)} релевантных чанков")
        return results
    
    def save(self, save_dir: Path = VECTOR_STORE_DIR):
        """
        Сохранить векторное хранилище на диск.
        
        Args:
            save_dir: директория для сохранения
        """
        save_dir.mkdir(parents=True, exist_ok=True)
        
        # Сохранение эмбеддингов
        embeddings_path = save_dir / "embeddings.npy"
        np.save(embeddings_path, self.embeddings)
        logger.info(f"Эмбеддинги сохранены в {embeddings_path}")
        
        # Сохранение метаданных чанков
        metadata_path = save_dir / "chunks_metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.chunks, f, ensure_ascii=False, indent=2)
        logger.info(f"Метаданные сохранены в {metadata_path}")
    
    def load(self, load_dir: Path = VECTOR_STORE_DIR) -> bool:
        """
        Загрузить векторное хранилище с диска.
        
        Args:
            load_dir: директория для загрузки
            
        Returns:
            True если загрузка успешна, False иначе
        """
        embeddings_path = load_dir / "embeddings.npy"
        metadata_path = load_dir / "chunks_metadata.json"
        
        if not embeddings_path.exists() or not metadata_path.exists():
            logger.warning(
                "Файлы векторного хранилища не найдены"
            )
            return False
        
        try:
            # Загрузка эмбеддингов
            self.embeddings = np.load(embeddings_path)
            logger.info(f"Эмбеддинги загружены. Форма: {self.embeddings.shape}")
            
            # Загрузка метаданных
            with open(metadata_path, 'r', encoding='utf-8') as f:
                self.chunks = json.load(f)
            logger.info(f"Метаданные загружены. Чанков: {len(self.chunks)}")
            
            return True
            
        except Exception as e:
            logger.error(f"Ошибка при загрузке хранилища: {e}")
            return False
    
    def get_stats(self) -> Dict:
        """
        Получить статистику хранилища.
        
        Returns:
            словарь со статистикой
        """
        return {
            'total_chunks': len(self.chunks),
            'embeddings_shape': self.embeddings.shape,
            'embedding_dimension': self.embedding_model.dimension,
            'sources': list(set([c['source'] for c in self.chunks]))
        }
