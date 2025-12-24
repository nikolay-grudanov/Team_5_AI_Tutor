"""
Скрипт для инициализации и проверки AI-репетитора.

Этот скрипт выполняет:
- Проверку зависимостей
- Инициализацию всех компонентов
- Выполнение базовых тестов
- Запуск демонстрационного примера
"""

import logging
import sys
from pathlib import Path

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def check_dependencies():
    """
    Проверка наличия всех необходимых зависимостей.
    
    Returns:
        True если все зависимости установлены, False иначе
    """
    logger.info("Проверка зависимостей...")
    
    required_packages = {
        'torch': 'torch',
        'transformers': 'transformers',
        'sentence_transformers': 'sentence-transformers',
        'flask': 'flask',
        'numpy': 'numpy'
    }
    
    missing_packages = []
    
    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
            logger.info(f"✓ {package_name} установлен")
        except ImportError:
            logger.warning(f"✗ {package_name} НЕ установлен")
            missing_packages.append(package_name)
    
    if missing_packages:
        logger.error(f"\nОтсутствующие пакеты: {', '.join(missing_packages)}")
        logger.error("Установите их с помощью:")
        logger.error(f"pip install {' '.join(missing_packages)}")
        return False
    
    logger.info("✓ Все зависимости установлены")
    return True


def test_components():
    """
    Тестирование основных компонентов системы.
    
    Returns:
        True если все тесты пройдены, False иначе
    """
    logger.info("\n" + "=" * 60)
    logger.info("ТЕСТИРОВАНИЕ КОМПОНЕНТОВ")
    logger.info("=" * 60)
    
    try:
        # Тест 1: DocumentProcessor
        logger.info("\n[1/4] Тестирование DocumentProcessor...")
        from document_processor import DocumentProcessor
        processor = DocumentProcessor()
        processor.load_sample_materials()
        processor.create_chunks()
        logger.info(f"✓ Создано {len(processor.get_chunks())} чанков")
        
        # Тест 2: EmbeddingModel
        logger.info("\n[2/4] Тестирование EmbeddingModel...")
        from vector_store import EmbeddingModel
        embedding_model = EmbeddingModel()
        test_embedding = embedding_model.encode("Тестовый текст")
        logger.info(f"✓ Эмбеддинг создан, размерность: {test_embedding.shape}")
        
        # Тест 3: VectorStore
        logger.info("\n[3/4] Тестирование VectorStore...")
        from vector_store import VectorStore
        vector_store = VectorStore(embedding_model)
        vector_store.add_chunks(processor.get_chunks()[:10])  # Первые 10 чанков
        search_results = vector_store.search("математика", top_k=3)
        logger.info(f"✓ Поиск выполнен, найдено {len(search_results)} результатов")
        
        # Тест 4: RAGPipeline
        logger.info("\n[4/4] Тестирование RAGPipeline...")
        from rag_pipeline import RAGPipeline
        rag_pipeline = RAGPipeline(vector_store)
        retrieved = rag_pipeline.retrieve("Как решить квадратное уравнение?")
        logger.info(f"✓ RAG пайплайн работает, найдено {len(retrieved)} документов")
        
        logger.info("\n" + "=" * 60)
        logger.info("✓ ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО")
        logger.info("=" * 60)
        
        return True
        
    except Exception as e:
        logger.error(f"\n✗ Ошибка при тестировании: {e}")
        import traceback
        traceback.print_exc()
        return False


def demo():
    """
    Демонстрационный пример работы системы.
    """
    logger.info("\n" + "=" * 60)
    logger.info("ДЕМОНСТРАЦИЯ РАБОТЫ СИСТЕМЫ")
    logger.info("=" * 60)
    
    try:
        from document_processor import process_documents_pipeline
        from vector_store import EmbeddingModel, VectorStore
        from rag_pipeline import RAGPipeline
        from llm_generator import LLMGenerator, ResponseRefiner
        
        # Инициализация
        logger.info("\nИнициализация системы...")
        processor, chunks = process_documents_pipeline()
        embedding_model = EmbeddingModel()
        vector_store = VectorStore(embedding_model)
        vector_store.add_chunks(chunks)
        rag_pipeline = RAGPipeline(vector_store)
        llm_generator = LLMGenerator()
        response_refiner = ResponseRefiner()
        
        # Примеры вопросов
        questions = [
            "Что такое теорема Пифагора?",
            "Как работает первый закон Ньютона?",
            "Объясни стехиометрию в химии"
        ]
        
        # Обработка вопросов
        for i, question in enumerate(questions, 1):
            logger.info(f"\n--- Вопрос {i} ---")
            logger.info(f"Q: {question}")
            
            # RAG пайплайн
            result = rag_pipeline.generate_pipeline(question, llm_generator)
            
            # Улучшение ответа
            refined_answer = response_refiner.refine(
                result['answer'],
                result['retrieved_documents']
            )
            
            logger.info(f"A: {refined_answer[:200]}...")
            logger.info(f"Использовано источников: {result['num_retrieved']}")
        
        logger.info("\n" + "=" * 60)
        logger.info("✓ ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"Ошибка при демонстрации: {e}")
        import traceback
        traceback.print_exc()


def main():
    """
    Главная функция инициализации.
    """
    logger.info("=" * 60)
    logger.info("ИНИЦИАЛИЗАЦИЯ AI-РЕПЕТИТОРА")
    logger.info("=" * 60)
    
    # Проверка зависимостей
    if not check_dependencies():
        logger.error("\nУстановите отсутствующие зависимости и попробуйте снова.")
        return False
    
    # Тестирование компонентов
    if not test_components():
        logger.error("\nНекоторые компоненты не работают корректно.")
        return False
    
    # Демонстрация
    demo()
    
    logger.info("\n" + "=" * 60)
    logger.info("ЗАПУСК ВЕБ-ИНТЕРФЕЙСА")
    logger.info("=" * 60)
    logger.info("\nДля запуска веб-интерфейса выполните:")
    logger.info("python app.py")
    logger.info("\nЗатем откройте в браузере: http://localhost:5000")
    
    return True


if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
