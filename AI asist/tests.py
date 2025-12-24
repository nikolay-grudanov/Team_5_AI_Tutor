"""
Тестирование компонентов AI-репетитора.

Этот модуль содержит тесты для проверки функциональности всех компонентов:
- document_processor
- vector_store
- rag_pipeline
- llm_generator
"""

import unittest
from pathlib import Path
import tempfile
import numpy as np

from config import SAMPLE_MATERIALS
from document_processor import DocumentProcessor
from vector_store import EmbeddingModel, VectorStore
from rag_pipeline import RAGPipeline
from llm_generator import LLMGenerator, ResponseRefiner


class TestDocumentProcessor(unittest.TestCase):
    """Тесты для обработчика документов."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.processor = DocumentProcessor()
    
    def test_clean_text(self):
        """Тест очистки текста."""
        dirty_text = "  Привет   мир!   "
        clean_text = DocumentProcessor.clean_text(dirty_text)
        self.assertEqual(clean_text, "Привет мир!")
    
    def test_split_into_chunks(self):
        """Тест разбиения текста на чанки."""
        text = "Первое предложение. Второе предложение. Третье предложение."
        chunks = DocumentProcessor.split_into_chunks(text, max_length=30, overlap=5)
        self.assertTrue(len(chunks) > 0)
        self.assertTrue(all(isinstance(c, str) for c in chunks))
    
    def test_load_sample_materials(self):
        """Тест загрузки примеров материалов."""
        docs = self.processor.load_sample_materials()
        self.assertTrue(len(docs) > 0)
        self.assertTrue(all('source' in d for d in docs))
        self.assertTrue(all('content' in d for d in docs))


class TestVectorStore(unittest.TestCase):
    """Тесты для векторного хранилища."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore(self.embedding_model)
    
    def test_add_chunks(self):
        """Тест добавления чанков."""
        chunks = [
            {'id': 'test_1', 'content': 'Тестовый текст первый', 'source': 'test'},
            {'id': 'test_2', 'content': 'Тестовый текст второй', 'source': 'test'}
        ]
        self.vector_store.add_chunks(chunks)
        
        self.assertEqual(len(self.vector_store.chunks), 2)
        self.assertEqual(self.vector_store.embeddings.shape[0], 2)
    
    def test_similarity_search(self):
        """Тест поиска по сходству."""
        chunks = [
            {'id': '1', 'content': 'Это математика', 'source': 'math'},
            {'id': '2', 'content': 'Физика и законы', 'source': 'physics'},
            {'id': '3', 'content': 'Математические формулы', 'source': 'math'}
        ]
        self.vector_store.add_chunks(chunks)
        
        results = self.vector_store.search('математика', top_k=2)
        self.assertTrue(len(results) > 0)


class TestRAGPipeline(unittest.TestCase):
    """Тесты для RAG пайплайна."""
    
    def setUp(self):
        """Подготовка к тестам."""
        self.embedding_model = EmbeddingModel()
        self.vector_store = VectorStore(self.embedding_model)
        
        chunks = [
            {'id': '1', 'content': 'Алгебра изучает числа и их свойства', 'source': 'math'},
            {'id': '2', 'content': 'Геометрия изучает фигуры и пространство', 'source': 'math'}
        ]
        self.vector_store.add_chunks(chunks)
        
        self.rag = RAGPipeline(self.vector_store)
    
    def test_retrieve(self):
        """Тест поиска документов."""
        results = self.rag.retrieve('алгебра')
        self.assertTrue(len(results) > 0)
    
    def test_format_context(self):
        """Тест форматирования контекста."""
        docs = [
            ({'source': 'math.txt', 'content': 'Тест контекста'}, 0.9)
        ]
        context = RAGPipeline.format_context(docs)
        self.assertTrue('Источник' in context)
        self.assertTrue('math.txt' in context)
    
    def test_build_prompt(self):
        """Тест построения промпта."""
        query = "Что такое алгебра?"
        context = "Алгебра - это раздел математики"
        
        prompt = RAGPipeline.build_prompt(query, context)
        
        self.assertTrue(query in prompt)
        self.assertTrue(context in prompt)


class TestResponseRefiner(unittest.TestCase):
    """Тесты для рефайнера ответов."""
    
    def test_format_answer(self):
        """Тест форматирования ответа."""
        answer = "Первый параграф\n\nВторой параграф"
        formatted = ResponseRefiner.format_answer(answer)
        
        self.assertTrue(len(formatted) > 0)
    
    def test_add_sources(self):
        """Тест добавления источников."""
        answer = "Ответ на вопрос"
        docs = [
            {'source': 'math.txt', 'similarity': 0.95},
            {'source': 'physics.txt', 'similarity': 0.87}
        ]
        
        refined = ResponseRefiner.refine(answer, docs)
        
        self.assertTrue('Источники' in refined or 'источники' in refined.lower())
        self.assertTrue('math.txt' in refined)


class TestCosineSimilarity(unittest.TestCase):
    """Тесты для вычисления косинусного сходства."""
    
    def test_cosine_similarity_identical_vectors(self):
        """Тест сходства одинаковых векторов."""
        vec1 = np.array([1, 0, 0])
        vec2 = np.array([1, 0, 0])
        
        sim = VectorStore.cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(sim, 1.0, places=5)
    
    def test_cosine_similarity_orthogonal_vectors(self):
        """Тест сходства ортогональных векторов."""
        vec1 = np.array([1, 0, 0])
        vec2 = np.array([0, 1, 0])
        
        sim = VectorStore.cosine_similarity(vec1, vec2)
        self.assertAlmostEqual(sim, 0.0, places=5)


def run_tests():
    """Запуск всех тестов."""
    # Создание набора тестов
    test_suite = unittest.TestSuite()
    
    # Добавление тестов
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDocumentProcessor))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestVectorStore))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestRAGPipeline))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestResponseRefiner))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestCosineSimilarity))
    
    # Запуск
    runner = unittest.TextTestRunner(verbosity=2)
    return runner.run(test_suite)


if __name__ == '__main__':
    run_tests()
