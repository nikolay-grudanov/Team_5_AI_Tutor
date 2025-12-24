"""
Модуль для веб-интерфейса AI-репетитора.

Функции:
- Инициализация Flask приложения
- Создание маршрутов API
- Подача HTML интерфейса
- Управление сессиями пользователей
"""

import os
import sys

# Исправление проблемы с кодировкой на Windows
os.environ['PYTHONIOENCODING'] = 'utf-8'
if sys.platform == 'win32':
    os.system('chcp 65001 > nul 2>&1')

from flask import Flask, render_template, request, jsonify, session
from datetime import datetime
import logging
from typing import Dict, List
import uuid

from config import HOST, PORT, DEBUG, MAX_QUESTION_LENGTH
from document_processor import process_documents_pipeline
from vector_store import EmbeddingModel, VectorStore
from rag_pipeline import RAGPipeline
from llm_generator import LLMGenerator, ResponseRefiner

# ============================================================================
# КОНФИГУРАЦИЯ ЛОГИРОВАНИЯ
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================================
# ИНИЦИАЛИЗАЦИЯ FLASK ПРИЛОЖЕНИЯ
# ============================================================================

app = Flask(__name__)
app.secret_key = 'ai_tutor_secret_key_2025'

# ============================================================================
# ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ
# ============================================================================

# Хранилище компонентов системы
SYSTEM_COMPONENTS = {
    'processor': None,
    'embedding_model': None,
    'vector_store': None,
    'rag_pipeline': None,
    'llm_generator': None,
    'response_refiner': None,
    'is_initialized': False
}

# Хранилище сессий пользователей
USER_SESSIONS = {}


def initialize_system():
    """
    Инициализация всех компонентов AI-репетитора.
    """
    try:
        logger.info("=" * 60)
        logger.info("ИНИЦИАЛИЗАЦИЯ AI-РЕПЕТИТОРА")
        logger.info("=" * 60)
        
        # Шаг 1: Обработка документов
        logger.info("[1/6] Загрузка и обработка документов...")
        processor, chunks = process_documents_pipeline()
        SYSTEM_COMPONENTS['processor'] = processor
        
        # Шаг 2: Инициализация модели эмбеддингов
        logger.info("[2/6] Инициализация модели эмбеддингов...")
        embedding_model = EmbeddingModel()
        SYSTEM_COMPONENTS['embedding_model'] = embedding_model
        
        # Шаг 3: Создание векторного хранилища
        logger.info("[3/6] Создание векторного хранилища...")
        vector_store = VectorStore(embedding_model)
        vector_store.add_chunks(chunks)
        SYSTEM_COMPONENTS['vector_store'] = vector_store
        
        # Сохранение хранилища
        vector_store.save()
        stats = vector_store.get_stats()
        logger.info(f"VectorStore создан: {stats}")
        
        # Шаг 4: Инициализация RAG пайплайна
        logger.info("[4/6] Инициализация RAG пайплайна...")
        rag_pipeline = RAGPipeline(vector_store)
        SYSTEM_COMPONENTS['rag_pipeline'] = rag_pipeline
        
        # Шаг 5: Инициализация LLM генератора
        logger.info("[5/6] Инициализация LLM генератора...")
        llm_generator = LLMGenerator()
        SYSTEM_COMPONENTS['llm_generator'] = llm_generator
        
        # Шаг 6: Инициализация рефайнера ответов
        logger.info("[6/6] Инициализация рефайнера ответов...")
        response_refiner = ResponseRefiner()
        SYSTEM_COMPONENTS['response_refiner'] = response_refiner
        
        SYSTEM_COMPONENTS['is_initialized'] = True
        
        logger.info("=" * 60)
        logger.info("✓ СИСТЕМА УСПЕШНО ИНИЦИАЛИЗИРОВАНА")
        logger.info("=" * 60)
        
        return True
        
    except Exception as e:
        logger.error(f"✗ Ошибка при инициализации системы: {e}")
        import traceback
        traceback.print_exc()
        return False


def get_or_create_session():
    """
    Получить или создать сессию пользователя.
    
    Returns:
        ID сессии
    """
    if 'user_id' not in session:
        user_id = str(uuid.uuid4())
        session['user_id'] = user_id
        USER_SESSIONS[user_id] = {
            'created_at': datetime.now(),
            'questions_count': 0,
            'history': []
        }
        logger.info(f"Создана новая сессия: {user_id}")
    
    return session['user_id']


# ============================================================================
# МАРШРУТЫ API
# ============================================================================

@app.route('/')
def index():
    """Главная страница интерфейса."""
    get_or_create_session()
    return render_template('index.html')


@app.route('/api/status', methods=['GET'])
def get_status():
    """
    API эндпоинт для получения статуса системы.
    
    Returns:
        JSON с информацией о статусе
    """
    if SYSTEM_COMPONENTS['is_initialized']:
        vector_store = SYSTEM_COMPONENTS['vector_store']
        stats = vector_store.get_stats()
        
        return jsonify({
            'status': 'ready',
            'message': 'AI-репетитор готов к работе',
            'vector_store_stats': stats
        })
    else:
        return jsonify({
            'status': 'initializing',
            'message': 'Система инициализируется...'
        }), 202


@app.route('/api/ask', methods=['POST'])
def ask_question():
    """
    API эндпоинт для обработки вопроса студента.
    
    Request JSON:
    {
        'question': 'Текст вопроса'
    }
    
    Returns:
        JSON с ответом и метаинформацией
    """
    try:
        # Валидация системы
        if not SYSTEM_COMPONENTS['is_initialized']:
            return jsonify({
                'error': 'Система еще не инициализирована',
                'status': 'error'
            }), 503
        
        # Получение данных из запроса
        data = request.get_json()
        question = data.get('question', '').strip()
        
        # Валидация вопроса
        if not question:
            return jsonify({
                'error': 'Вопрос не может быть пустым',
                'status': 'error'
            }), 400
        
        if len(question) > MAX_QUESTION_LENGTH:
            return jsonify({
                'error': f'Вопрос слишком длинный (макс {MAX_QUESTION_LENGTH} символов)',
                'status': 'error'
            }), 400
        
        # Получение ID сессии
        user_id = get_or_create_session()
        
        logger.info(f"[{user_id}] Вопрос: {question[:100]}")
        
        # Запуск RAG пайплайна
        rag_pipeline = SYSTEM_COMPONENTS['rag_pipeline']
        llm_generator = SYSTEM_COMPONENTS['llm_generator']
        response_refiner = SYSTEM_COMPONENTS['response_refiner']
        
        result = rag_pipeline.generate_pipeline(
            query=question,
            llm_generator=llm_generator
        )
        
        # Улучшение ответа
        refined_answer = response_refiner.refine(
            result['answer'],
            result['retrieved_documents']
        )
        
        # Сохранение в историю
        USER_SESSIONS[user_id]['questions_count'] += 1
        USER_SESSIONS[user_id]['history'].append({
            'question': question,
            'answer': refined_answer,
            'timestamp': datetime.now().isoformat(),
            'sources_count': result['num_retrieved']
        })
        
        # Подготовка ответа
        response_data = {
            'status': 'success',
            'question': question,
            'answer': refined_answer,
            'sources': result['retrieved_documents'],
            'num_sources': result['num_retrieved'],
            'session_id': user_id
        }
        
        logger.info(f"[{user_id}] Ответ сгенерирован ({result['num_retrieved']} источников)")
        
        return jsonify(response_data), 200
        
    except Exception as e:
        logger.error(f"Ошибка при обработке вопроса: {e}")
        import traceback
        traceback.print_exc()
        
        return jsonify({
            'error': f'Ошибка при обработке: {str(e)}',
            'status': 'error'
        }), 500


@app.route('/api/history', methods=['GET'])
def get_history():
    """
    API эндпоинт для получения истории вопросов.
    
    Returns:
        JSON с историей
    """
    user_id = get_or_create_session()
    
    if user_id in USER_SESSIONS:
        history = USER_SESSIONS[user_id]['history']
        return jsonify({
            'status': 'success',
            'history': history,
            'total_questions': len(history)
        }), 200
    
    return jsonify({
        'status': 'error',
        'error': 'Сессия не найдена'
    }), 404


@app.route('/api/session-info', methods=['GET'])
def get_session_info():
    """
    API эндпоинт для получения информации о сессии.
    
    Returns:
        JSON с информацией о сессии
    """
    user_id = get_or_create_session()
    
    if user_id in USER_SESSIONS:
        session_data = USER_SESSIONS[user_id]
        return jsonify({
            'status': 'success',
            'user_id': user_id,
            'created_at': session_data['created_at'].isoformat(),
            'questions_count': session_data['questions_count']
        }), 200
    
    return jsonify({
        'status': 'error',
        'error': 'Сессия не найдена'
    }), 404


@app.route('/api/clear-history', methods=['POST'])
def clear_history():
    """
    API эндпоинт для очистки истории.
    
    Returns:
        JSON с результатом
    """
    user_id = get_or_create_session()
    
    if user_id in USER_SESSIONS:
        USER_SESSIONS[user_id]['history'] = []
        USER_SESSIONS[user_id]['questions_count'] = 0
        
        return jsonify({
            'status': 'success',
            'message': 'История очищена'
        }), 200
    
    return jsonify({
        'status': 'error',
        'error': 'Сессия не найдена'
    }), 404


# ============================================================================
# ОБРАБОТКА ОШИБОК
# ============================================================================

@app.errorhandler(404)
def page_not_found(e):
    """Обработка ошибки 404."""
    return jsonify({
        'error': 'Страница не найдена',
        'status': 'error'
    }), 404


@app.errorhandler(500)
def internal_error(e):
    """Обработка ошибки 500."""
    logger.error(f"Внутренняя ошибка сервера: {e}")
    return jsonify({
        'error': 'Внутренняя ошибка сервера',
        'status': 'error'
    }), 500


# ============================================================================
# ТОЧКА ВХОДА
# ============================================================================

if __name__ == '__main__':
    # Инициализация системы
    if initialize_system():
        # Запуск Flask приложения
        logger.info(f"Запуск сервера на {HOST}:{PORT}")
        app.run(host=HOST, port=PORT, debug=DEBUG)
    else:
        logger.error("Не удалось инициализировать систему")
