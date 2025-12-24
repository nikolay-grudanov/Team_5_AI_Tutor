"""
Файл быстрого старта (Quick Start).

Для быстрого запуска используйте этот файл.
"""

import os
import sys
import subprocess
from pathlib import Path

# Исправление проблемы с кодировкой на Windows
os.environ['PYTHONIOENCODING'] = 'utf-8'
if sys.platform == 'win32':
    os.system('chcp 65001 > nul 2>&1')


def check_python_version():
    """Проверить версию Python."""
    if sys.version_info < (3, 8):
        print("[ERROR] Требуется Python 3.8 или выше")
        print(f"Ваша версия: {sys.version}")
        return False
    
    print(f"[OK] Python версия: {sys.version_info.major}.{sys.version_info.minor}")
    return True


def create_virtual_env():
    """Создать виртуальное окружение."""
    if (Path("venv") / ("Scripts" if os.name == "nt" else "bin")).exists():
        print("[OK] Виртуальное окружение уже существует")
        return True
    
    print("\n[INFO] Создание виртуального окружения...")
    try:
        subprocess.check_call([sys.executable, "-m", "venv", "venv"])
        print("[OK] Виртуальное окружение создано")
        return True
    except Exception as e:
        print(f"[ERROR] Ошибка: {e}")
        return False


def install_dependencies():
    """Установить зависимости."""
    print("\n[INFO] Установка зависимостей...")
    
    if os.name == "nt":  # Windows
        pip_path = Path("venv/Scripts/pip.exe")
    else:  # Unix
        pip_path = Path("venv/bin/pip")
    
    if not pip_path.exists():
        print("[ERROR] pip не найден")
        return False
    
    try:
        subprocess.check_call([str(pip_path), "install", "-r", "requirements.txt"])
        print("[OK] Зависимости установлены")
        return True
    except Exception as e:
        print(f"[ERROR] Ошибка при установке: {e}")
        return False


def run_application():
    """Запустить приложение."""
    print("\n[INFO] Запуск приложения...")
    
    if os.name == "nt":  # Windows
        python_path = Path("venv/Scripts/python.exe")
    else:  # Unix
        python_path = Path("venv/bin/python")
    
    if not python_path.exists():
        print("[ERROR] Python в виртуальном окружении не найден")
        return False
    
    try:
        subprocess.call([str(python_path), "run.py"])
        return True
    except KeyboardInterrupt:
        print("\n\n[INFO] Приложение остановлено")
        return True
    except Exception as e:
        print(f"[ERROR] Ошибка при запуске: {e}")
        return False


def print_banner():
    """Вывести баннер."""
    banner = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║              AI-REPEPITOR BYSTRUJ START (v1.0)                ║
    ║                                                                ║
    ║            Intelligent Learning System v1.0                    ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    try:
        print(banner)
    except UnicodeEncodeError:
        print("=" * 65)
        print("AI-REPEPITOR BYSTRUJ START (v1.0)")
        print("Intelligent Learning System v1.0")
        print("=" * 65)


def print_instructions():
    """Vyvesti instrukcii."""
    instructions = """
    
    ====== INSTRUCTIONS FOR QUICK START ======
    
    1. REQUIREMENTS:
       - Python 3.8 or higher
       - Internet connection (for downloading models)
       - 2+ GB RAM (recommended)
    
    2. AUTOMATIC START:
       - Run this script: python quickstart.py
       - Script automatically:
         * Creates virtual environment
         * Installs all dependencies
         * Launches application
    
    3. MANUAL START:
       
       # Windows
       python -m venv venv
       .\\venv\\Scripts\\activate
       pip install -r requirements.txt
       python run.py
       
       # Linux/Mac
       python3 -m venv venv
       source venv/bin/activate
       pip install -r requirements.txt
        python run.py
    
    4. OPEN INTERFACE:
       - After startup, open in browser:
       - http://localhost:5000
    
    5. RUN COMMANDS:
       python run.py              # Web interface (default)
       python run.py --mode test  # Component testing
       python run.py --mode demo  # Demo
       python run.py --mode debug # Debug mode
    
    6. TROUBLESHOOTING:
       
       Error: "ModuleNotFoundError"
       -> Make sure virtual environment is activated
       -> Reinstall dependencies: pip install -r requirements.txt
       
       Error: "CUDA not found"
       -> This is normal, system will use CPU
       -> Responses will be slower, but functionality remains the same
       
       Error: "Model not loaded"
       -> Check internet connection
       -> Model downloads from Hugging Face on first run
       -> Takes time (depends on network speed)
    
    7. DOCUMENTATION:
       - Full documentation: README.md
       - Usage examples: examples.py
       - Code with comments in English
    
    ==========================================
    """
    try:
        print(instructions)
    except UnicodeEncodeError:
        print("Quick Start Instructions printed (encoding issue)")


def main():
    """Главная функция."""
    print_banner()
    print_instructions()
    
    # Проверка Python
    if not check_python_version():
        sys.exit(1)
    
    # Создание виртуального окружения
    if not create_virtual_env():
        sys.exit(1)
    
    # Установка зависимостей
    if not install_dependencies():
        sys.exit(1)
    
    # Запуск приложения
    if run_application():
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == '__main__':
    main()
