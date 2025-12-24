"""
Примеры использования AI-репетитора и документация по API.

Этот файл содержит:
- Примеры использования компонентов
- Документацию по API
- Примеры интеграции
"""

import json
from datetime import datetime


# ============================================================================
# ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ КОМПОНЕНТОВ
# ============================================================================

def example_basic_usage():
    """
    Пример 1: Базовое использование системы.
    """
    print("=" * 60)
    print("ПРИМЕР 1: Базовое использование")
    print("=" * 60)
    
    from document_processor import process_documents_pipeline
    from vector_store import EmbeddingModel, VectorStore
    from rag_pipeline import RAGPipeline
    from llm_generator import LLMGenerator, ResponseRefiner
    
    # Шаг 1: Обработка документов
    print("\n1. Обработка документов...")
    processor, chunks = process_documents_pipeline()
    print(f"   Создано чанков: {len(chunks)}")
    
    # Шаг 2: Инициализация эмбеддингов
    print("\n2. Инициализация эмбеддингов...")
    embedding_model = EmbeddingModel()
    print("   Модель загружена")
    
    # Шаг 3: Создание векторного хранилища
    print("\n3. Создание векторного хранилища...")
    vector_store = VectorStore(embedding_model)
    vector_store.add_chunks(chunks)
    print("   Хранилище создано")
    
    # Шаг 4: RAG пайплайн
    print("\n4. Запуск RAG пайплайна...")
    rag_pipeline = RAGPipeline(vector_store)
    llm_generator = LLMGenerator()
    response_refiner = ResponseRefiner()
    
    # Обработка вопроса
    question = "Как решить квадратное уравнение?"
    print(f"\n   Вопрос: {question}")
    
    result = rag_pipeline.generate_pipeline(question, llm_generator)
    refined = response_refiner.refine(result['answer'], result['retrieved_documents'])
    
    print(f"\n   Ответ: {refined[:200]}...")
    print(f"   Источников: {result['num_retrieved']}")


def example_custom_documents():
    """
    Пример 2: Использование собственных документов.
    """
    print("\n" + "=" * 60)
    print("ПРИМЕР 2: Использование собственных документов")
    print("=" * 60)
    
    from document_processor import DocumentProcessor
    from pathlib import Path
    
    processor = DocumentProcessor()
    
    # Создание примера документа
    print("\n1. Создание примера документа...")
    docs_dir = Path("data/documents")
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    sample_doc = docs_dir / "sample.txt"
    sample_doc.write_text("""
    ПРОГРАММИРОВАНИЕ НА PYTHON
    
    Python - это интерпретируемый язык программирования.
    Он известен своей простотой и читаемостью кода.
    
    Основные типы данных:
    - int (целые числа)
    - float (числа с плавающей точкой)
    - str (строки)
    - list (списки)
    - dict (словари)
    
    Функции определяются с помощью ключевого слова def.
    """)
    
    print(f"   Документ создан: {sample_doc}")
    
    # Загрузка документа
    print("\n2. Загрузка документа...")
    docs = processor.load_documents(docs_dir)
    print(f"   Загружено документов: {len(docs)}")
    
    # Создание чанков
    print("\n3. Создание чанков...")
    chunks = processor.create_chunks()
    print(f"   Создано чанков: {len(chunks)}")
    
    for chunk in chunks[:3]:
        print(f"\n   Чанк {chunk['id']}:")
        print(f"   Содержимое: {chunk['content'][:100]}...")


def example_search_similarity():
    """
    Пример 3: Поиск по сходству.
    """
    print("\n" + "=" * 60)
    print("ПРИМЕР 3: Поиск по сходству")
    print("=" * 60)
    
    from document_processor import DocumentProcessor
    from vector_store import EmbeddingModel, VectorStore
    
    # Подготовка
    processor = DocumentProcessor()
    processor.load_sample_materials()
    chunks = processor.create_chunks()
    
    embedding_model = EmbeddingModel()
    vector_store = VectorStore(embedding_model)
    vector_store.add_chunks(chunks[:20])  # Первые 20 чанков для скорости
    
    # Примеры поисков
    queries = [
        "теорема Пифагора",
        "закон Ньютона",
        "функции Python"
    ]
    
    for query in queries:
        print(f"\nПоиск: '{query}'")
        results = vector_store.search(query, top_k=2)
        
        for i, (doc, similarity) in enumerate(results, 1):
            print(f"  {i}. Сходство: {similarity:.3f}")
            print(f"     Источник: {doc['source']}")
            print(f"     Текст: {doc['content'][:80]}...")


def example_session_management():
    """
    Пример 4: Управление сессиями пользователей.
    """
    print("\n" + "=" * 60)
    print("ПРИМЕР 4: Управление сессиями")
    print("=" * 60)
    
    import uuid
    from datetime import datetime
    
    # Симуляция нескольких пользователей
    sessions = {}
    
    # Создание сессий
    print("\n1. Создание сессий:")
    for i in range(3):
        user_id = str(uuid.uuid4())
        session = {
            'created_at': datetime.now(),
            'questions': [],
            'answers': []
        }
        sessions[user_id] = session
        print(f"   Пользователь {i+1}: {user_id[:8]}...")
    
    # Добавление вопросов
    print("\n2. Добавление вопросов:")
    user_ids = list(sessions.keys())
    
    for idx, user_id in enumerate(user_ids):
        session = sessions[user_id]
        session['questions'].append(f"Вопрос {idx+1}")
        session['answers'].append(f"Ответ {idx+1}")
        print(f"   {user_id[:8]}...: {len(session['questions'])} вопросов")
    
    # Статистика
    print("\n3. Статистика сессий:")
    for user_id, session in sessions.items():
        print(f"   {user_id[:8]}...")
        print(f"      Создана: {session['created_at'].strftime('%H:%M:%S')}")
        print(f"      Вопросов: {len(session['questions'])}")


# ============================================================================
# ДОКУМЕНТАЦИЯ ПО REST API
# ============================================================================

class APIDocumentation:
    """Документация по REST API."""
    
    @staticmethod
    def print_api_docs():
        """Вывести документацию API."""
        
        docs = {
            "API_BASE_URL": "http://localhost:5000",
            "API_VERSION": "1.0",
            "ENDPOINTS": {
                "GET /": {
                    "description": "Главная страница веб-интерфейса",
                    "response": "HTML",
                    "example": "http://localhost:5000/"
                },
                "GET /api/status": {
                    "description": "Получить статус системы",
                    "response": {
                        "status": "ready",
                        "message": "AI-репетитор готов к работе",
                        "vector_store_stats": {
                            "total_chunks": 15,
                            "embeddings_shape": [15, 384]
                        }
                    }
                },
                "POST /api/ask": {
                    "description": "Отправить вопрос",
                    "request": {
                        "question": "Как решить квадратное уравнение?"
                    },
                    "response": {
                        "status": "success",
                        "question": "Как решить квадратное уравнение?",
                        "answer": "Квадратное уравнение решается...",
                        "sources": [
                            {
                                "source": "math.txt",
                                "similarity": 0.95,
                                "preview": "Квадратное уравнение формы ax²..."
                            }
                        ],
                        "num_sources": 1
                    }
                },
                "GET /api/history": {
                    "description": "Получить историю вопросов",
                    "response": {
                        "status": "success",
                        "history": [
                            {
                                "question": "Вопрос 1",
                                "answer": "Ответ 1",
                                "timestamp": "2024-01-01T12:00:00",
                                "sources_count": 2
                            }
                        ],
                        "total_questions": 1
                    }
                },
                "GET /api/session-info": {
                    "description": "Получить информацию о сессии",
                    "response": {
                        "status": "success",
                        "user_id": "uuid-string",
                        "created_at": "2024-01-01T12:00:00",
                        "questions_count": 5
                    }
                },
                "POST /api/clear-history": {
                    "description": "Очистить историю",
                    "response": {
                        "status": "success",
                        "message": "История очищена"
                    }
                }
            }
        }
        
        print("\n" + "=" * 60)
        print("REST API ДОКУМЕНТАЦИЯ")
        print("=" * 60)
        print(json.dumps(docs, ensure_ascii=False, indent=2))


# ============================================================================
# ПРИМЕРЫ ИНТЕГРАЦИИ
# ============================================================================

def example_integration_with_flask():
    """
    Пример 5: Интеграция с Flask.
    """
    print("\n" + "=" * 60)
    print("ПРИМЕР 5: Интеграция с Flask")
    print("=" * 60)
    
    example_code = """
    # Пример кастомного эндпоинта
    from flask import Blueprint, request, jsonify
    from app import SYSTEM_COMPONENTS
    
    # Создание Blueprint
    custom_bp = Blueprint('custom', __name__, url_prefix='/api/custom')
    
    @custom_bp.route('/advanced-search', methods=['POST'])
    def advanced_search():
        '''Продвинутый поиск с фильтрацией.'''
        data = request.get_json()
        query = data['query']
        subject = data.get('subject')
        
        # Поиск с использованием RAG
        rag = SYSTEM_COMPONENTS['rag_pipeline']
        results = rag.retrieve(query)
        
        # Фильтрация по предмету
        if subject:
            results = [r for r in results if r[0].get('subject') == subject]
        
        return jsonify({
            'status': 'success',
            'results': results
        })
    
    # Регистрация Blueprint
    app.register_blueprint(custom_bp)
    """
    
    print(example_code)


def example_error_handling():
    """
    Пример 6: Обработка ошибок.
    """
    print("\n" + "=" * 60)
    print("ПРИМЕР 6: Обработка ошибок")
    print("=" * 60)
    
    error_examples = {
        "400 Bad Request": "Пустой или слишком длинный вопрос",
        "503 Service Unavailable": "Система еще инициализируется",
        "500 Internal Server Error": "Ошибка при обработке вопроса",
        "404 Not Found": "Эндпоинт не найден"
    }
    
    print("\nВозможные ошибки и их коды:")
    for error_code, description in error_examples.items():
        print(f"\n{error_code}:")
        print(f"  Описание: {description}")


# ============================================================================
# ГЛАВНАЯ ФУНКЦИЯ
# ============================================================================

def main():
    """Запуск всех примеров."""
    
    print("\n╔════════════════════════════════════════════════════════════════╗")
    print("║             ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ AI-РЕПЕТИТОРА             ║")
    print("╚════════════════════════════════════════════════════════════════╝")
    
    # Отключим это, чтобы не заниматься долгой инициализацией
    # example_basic_usage()
    # example_custom_documents()
    # example_search_similarity()
    
    example_session_management()
    
    APIDocumentation.print_api_docs()
    
    example_integration_with_flask()
    example_error_handling()
    
    print("\n" + "=" * 60)
    print("Для дополнительной информации смотрите README.md")
    print("=" * 60)


if __name__ == '__main__':
    main()
