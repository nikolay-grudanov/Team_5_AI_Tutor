# PDF Text Extractor с использованием HunyuanOCR

Этот скрипт предназначен для извлечения текста из PDF файлов с использованием модели HunyuanOCR от Tencent.

## Требования

- Python 3.8+
- PyTorch
- Transformers
- Pillow
- pdf2image
- Poppler (для pdf2image)

## Установка зависимостей

### 1. Установка Python пакетов

```bash
pip install torch torchvision transformers pillow pdf2image
```

### 2. Установка Poppler (требуется для pdf2image)

#### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install poppler-utils
```

#### CentOS/RHEL/Fedora:
```bash
sudo yum install poppler-utils
# или для Fedora:
sudo dnf install poppler-utils
```

#### macOS:
```bash
brew install poppler
```

#### Windows:
1. Скачайте Poppler с [официального сайта](http://blog.alivate.com.au/poppler-windows/)
2. Распакуйте архив и добавьте путь к `bin` директории в системную переменную PATH

## Использование

### Базовое использование

Для обработки всех PDF файлов в директории `pdf-for-test`:

```bash
python pdf_text_extractor.py
```

### Расширенные опции

```bash
# Обработка конкретного PDF файла
python pdf_text_extractor.py --input path/to/your/file.pdf

# Указание выходной директории
python pdf_text_extractor.py --input pdf-for-test --output extracted_texts

# Использование другой модели
python pdf_text_extractor.py --model "Tencent/HunyuanOCR"
```

### Аргументы командной строки

- `--input`: Путь к PDF файлу или директории с PDF файлами (по умолчанию: `pdf-for-test`)
- `--output`: Директория для сохранения результатов (по умолчанию: та же, что и входная)
- `--model`: Название модели (по умолчанию: `Tencent/HunyuanOCR`)

## Структура проекта

```
notebooks/vlm-ingestion-pipeline/
├── pdf_text_extractor.py  # Основной скрипт
├── README.md              # Этот файл
├── pdf-for-test/          # Директория с тестовыми PDF файлами
│   ├── o-predelnom-mnogomernom-raspredelenii.pdf
│   └── standartizatsiya-i-kachestvo-zhizni.pdf
└── extracted_texts/       # Директория для результатов (создается автоматически)
```

## Как это работает

1. **Конвертация PDF в изображения**: Скрипт использует библиотеку `pdf2image` для конвертации каждой страницы PDF в изображение высокого качества (300 DPI).

2. **Обработка изображений с помощью HunyuanOCR**: Каждое изображение обрабатывается моделью HunyuanOCR для извлечения текста.

3. **Сохранение результатов**: Извлеченный текст сохраняется в текстовый файл с тем же именем, что и исходный PDF.

## Логирование

Скрипт создает лог-файл `pdf_extraction.log` с подробной информацией о процессе обработки, включая:
- Время начала и окончания обработки
- Информацию о каждой обработанной странице
- Сообщения об ошибках

## Производительность

- Для оптимальной производительности рекомендуется использовать GPU (CUDA)
- При использовании CPU обработка может занять значительное время
- Модель автоматически определяет наличие CUDA и использует его при доступности

## Устранение неполадок

### Ошибка: "poppler-utils not found"
Установите Poppler согласно инструкциям для вашей операционной системы.

### Ошибка: "CUDA out of memory"
Если у вас недостаточно видеопамяти, скрипт автоматически переключится на CPU, или вы можете принудительно использовать CPU, изменив код.

### Ошибка: "Model not found"
Убедитесь, что у вас есть доступ к интернету для загрузки модели с Hugging Face Hub.

## Пример использования

```python
from pdf_text_extractor import HunyuanOCRExtractor

# Создание экземпляра экстрактора
extractor = HunyuanOCRExtractor()

# Извлечение текста из одного PDF файла
text = extractor.extract_text_from_pdf("pdf-for-test/document.pdf")

# Обработка всех PDF файлов в директории
extractor.process_directory("pdf-for-test", "extracted_texts")
```

## Лицензия

Этот скрипт предоставляется для образовательных целей. Пожалуйста, соблюдайте лицензии используемых библиотек и моделей.