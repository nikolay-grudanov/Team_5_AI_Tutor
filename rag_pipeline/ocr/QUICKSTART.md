# 🚀 Быстрый старт OCR модуля

## 1️⃣ Установка

```
# Клонирование репозитория
git clone <your-repo-url>
cd Team_5_AI_Tutor

# Установка зависимостей
pip install -r requirements.txt
```

## 2️⃣ Конфигурация

```
# Копирование примера конфигурации
cp .env.example .env

# Редактирование (укажите ваш vLLM сервер)
nano .env
```

Минимальные настройки:
```
VLLM_BASE_URL=https://your-vllm-server.cloud.ru/v1
VLLM_MODEL_NAME=model-run-olm-ocr
MAX_WORKERS=4
```

## 3️⃣ Проверка

```
# Проверка конфигурации
python -m rag_pipeline.ocr.config

# Проверка vLLM сервера
python -m rag_pipeline.ocr.client
```

## 4️⃣ Обработка

### Одно изображение (тест)
```
python -m rag_pipeline.ocr.processor data/raw/math/Книга/page_001.png
```

### Одна книга
```
python scripts/run_ocr.py --input data/raw/math/Книга_1 --workers 4
```

### Все книги
```
python scripts/run_ocr.py --input data/raw/math --recursive --workers 4
```

## 5️⃣ Проверка результатов

```
# Результаты в data/processed/
ls -la data/processed/math/Книга_1/

# Просмотр одного файла
cat data/processed/math/Книга_1/page_001.md
```

## 🎯 Оптимизация производительности

### Для быстрой обработки (если сервер мощный)
```
MAX_WORKERS=8 python scripts/run_ocr.py --input data/raw/math --recursive
```

### Для стабильности (если сервер загружен)
```
MAX_WORKERS=2 TIMEOUT=600 python scripts/run_ocr.py --input data/raw/math --recursive
```

## 📊 Мониторинг

```
# Логи в реальном времени
tail -f logs/ocr_processing.log

# Статистика после обработки
grep "СТАТИСТИКА" logs/ocr_processing.log
```
