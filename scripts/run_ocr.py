#!/usr/bin/env python3
"""
Скрипт для запуска OCR обработки папки с изображениями.

Использование:
    # Обработка одной папки
    python scripts/run_ocr.py --input data/raw/math/Книга_1
    
    # С указанием количества потоков
    python scripts/run_ocr.py --input data/raw/math/Книга_1 --workers 8
    
    # Без resume (обработать все заново)
    python scripts/run_ocr.py --input data/raw/math/Книга_1 --no-resume
    
    # Обработка всех подпапок в math/
    python scripts/run_ocr.py --input data/raw/math --recursive
"""

import argparse
import sys
from pathlib import Path

# Добавление корневой папки в PYTHONPATH
sys.path.insert(0, str(Path(__file__).parent.parent))

from rag_pipeline.ocr import OCRPipeline


def main():
    parser = argparse.ArgumentParser(
        description="OCR обработка изображений через vLLM",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры:
  # Обработка одной книги
  python scripts/run_ocr.py --input data/raw/math/o-predelnom-mnogomernom-raspredelenii
  
  # С 8 потоками
  python scripts/run_ocr.py --input data/raw/math/Книга --workers 8
  
  # Обработать все заново
  python scripts/run_ocr.py --input data/raw/math/Книга --no-resume
  
  # Обработка всех подпапок
  python scripts/run_ocr.py --input data/raw/math --recursive
        """
    )
    
    parser.add_argument(
        '--input', '-i',
        type=Path,
        required=True,
        help='Путь к папке с изображениями'
    )
    
    parser.add_argument(
        '--workers', '-w',
        type=int,
        default=None,
        help='Количество параллельных потоков (по умолчанию: из config)'
    )
    
    parser.add_argument(
        '--no-resume',
        action='store_true',
        help='Обработать все файлы заново (без пропуска обработанных)'
    )
    
    parser.add_argument(
        '--recursive', '-r',
        action='store_true',
        help='Обработать все подпапки рекурсивно'
    )
    
    parser.add_argument(
        '--extensions',
        nargs='+',
        default=['.png', '.jpg', '.jpeg'],
        help='Расширения файлов для обработки (по умолчанию: .png .jpg .jpeg)'
    )
    
    args = parser.parse_args()
    
    # Проверка входной папки
    if not args.input.exists():
        print(f"❌ Папка не найдена: {args.input}")
        sys.exit(1)
    
    # Создание pipeline
    try:
        pipeline = OCRPipeline()
        print(f"✅ Pipeline создан: {pipeline}")
        print(f"📝 Логи: {pipeline.config.log_file}") 
        effective_workers = args.workers or pipeline.config.max_workers
        print(f"⚙️  Используется воркеров: {effective_workers}") 
    except Exception as e:
        print(f"❌ Ошибка создания pipeline: {e}")
        sys.exit(1)
    
    # Проверка доступности сервера
    print("\n🔍 Проверка vLLM сервера...")
    if not pipeline.processor.client.check_availability():
        print("❌ vLLM сервер недоступен!")
        print("   Запустите vLLM сервер и попробуйте снова.")
        sys.exit(1)
    print("✅ Сервер доступен\n")
    
    # Обработка
    try:
        if args.recursive:
            # Рекурсивная обработка всех подпапок
            subdirs = [d for d in args.input.iterdir() if d.is_dir()]
            
            if not subdirs:
                print(f"⚠️  Подпапок не найдено в {args.input}")
                sys.exit(0)
            
            print(f"📁 Найдено папок для обработки: {len(subdirs)}\n")
            
            for i, subdir in enumerate(subdirs, 1):
                print(f"\n{'='*70}")
                print(f"📚 Папка {i}/{len(subdirs)}: {subdir.name}")
                print(f"{'='*70}")
                
                pipeline.process_directory(
                    input_dir=subdir,
                    max_workers=args.workers,
                    resume=not args.no_resume,
                    extensions=args.extensions
                )
        else:
            # Обработка одной папки
            pipeline.process_directory(
                input_dir=args.input,
                max_workers=args.workers,
                resume=not args.no_resume,
                extensions=args.extensions
            )
        
        print("\n✅ Все операции завершены!")
        
    except KeyboardInterrupt:
        print("\n\n⚠️ Прервано пользователем")
        if 'pipeline' in locals():
            pipeline.print_summary()
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
