#!/usr/bin/env python3
"""
Главный скрипт запуска AI-репетитора.

Этот файл запускает полное приложение с веб-интерфейсом.
Используйте: python run.py
"""

import sys
import os
import argparse
from pathlib import Path

# Исправление проблемы с кодировкой на Windows
os.environ['PYTHONIOENCODING'] = 'utf-8'
if sys.platform == 'win32':
    os.system('chcp 65001 > nul 2>&1')

# Добавление текущей директории в путь
sys.path.insert(0, str(Path(__file__).parent))

from utils import print_banner, get_logger, debug_info, TimerContext
from init import check_dependencies, test_components, demo


def main():
    """Главная функция приложения."""
    
    # Парсинг аргументов командной строки
    parser = argparse.ArgumentParser(
        description='AI-Репетитор: Система обучения на основе RAG'
    )
    parser.add_argument(
        '--mode',
        choices=['web', 'test', 'demo', 'debug'],
        default='web',
        help='Режим запуска (по умолчанию: web)'
    )
    parser.add_argument(
        '--no-init',
        action='store_true',
        help='Пропустить инициализацию'
    )
    parser.add_argument(
        '--debug',
        action='store_true',
        help='Режим отладки'
    )
    
    args = parser.parse_args()
    
    # Баннер
    print_banner()
    
    logger = get_logger(__name__)
    
    # Режим отладки
    if args.debug:
        debug_info()
    
    # Проверка зависимостей
    logger.info("Проверка окружения...")
    if not check_dependencies():
        logger.error("Отсутствуют необходимые зависимости")
        sys.exit(1)
    
    # Режим теста
    if args.mode == 'test':
        logger.info("\n>>> Режим тестирования")
        if test_components():
            logger.info("✓ Все тесты пройдены успешно")
            sys.exit(0)
        else:
            logger.error("✗ Тесты не пройдены")
            sys.exit(1)
    
    # Режим демонстрации
    elif args.mode == 'demo':
        logger.info("\n>>> Режим демонстрации")
        demo()
        sys.exit(0)
    
    # Режим отладки
    elif args.mode == 'debug':
        logger.info("\n>>> Режим отладки")
        debug_info()
        sys.exit(0)
    
    # Веб-режим (по умолчанию)
    else:
        logger.info("\n>>> Запуск веб-интерфейса")
        
        # Инициализация системы (если не пропущена)
        if not args.no_init:
            from app import initialize_system
            
            logger.info("Инициализация системы...")
            if not initialize_system():
                logger.error("Ошибка при инициализации системы")
                sys.exit(1)
        
        # Запуск Flask приложения
        try:
            from config import HOST, PORT, DEBUG
            from app import app
            
            logger.info(f"\n{'='*60}")
            logger.info("ВЕБА-ИНТЕРФЕЙС ГОТОВ К РАБОТЕ")
            logger.info(f"{'='*60}")
            logger.info(f"URL: http://{HOST}:{PORT}")
            logger.info(f"Отладка: {'Включена' if DEBUG else 'Отключена'}")
            logger.info(f"{'='*60}\n")
            
            logger.info("Нажмите Ctrl+C для остановки сервера")
            
            # Запуск приложения
            app.run(
                host=HOST,
                port=PORT,
                debug=DEBUG,
                use_reloader=False  # Отключаем перезагрузчик для избежания двойной инициализации
            )
            
        except KeyboardInterrupt:
            logger.info("\n\nСервер остановлен пользователем")
            sys.exit(0)
        except Exception as e:
            logger.error(f"Ошибка при запуске сервера: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)


if __name__ == '__main__':
    with TimerContext("Выполнение приложения"):
        main()
