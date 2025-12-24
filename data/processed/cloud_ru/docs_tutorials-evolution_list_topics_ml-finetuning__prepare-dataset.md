---
source_image: docs_tutorials-evolution_list_topics_ml-finetuning__prepare-dataset.jpg
page_number: 0
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.79
tokens: 9789
characters: 6387
timestamp: 2025-12-24T06:03:28.071836
finish_reason: stop
---

### Подготовка датасета Alpaca для использования в ML Finetuning

С помощью этого руководства вы подготовите датасет GitHub Issue в формате Alpaca для использования в сервисе ML Finetuning.

Датасет предназначен для дообучения моделей, которые решают задачу генерации заголовка на основе текстового описания проблемы.

В качестве исходного используется датасет mlfoundations-dev/github-issues. В результате получится набор данных в формате Alpaca, опубликованный на HuggingFace Hub.

Вы будете использовать следующие сервисы:

• Notebooks — сервис для запуска сред ML и работы DS-специалистов в ноутбуках на платформе Evolution.
• Huggingface — платформа для публикации и использования моделей машинного обучения.

Шаги:

1. Подготовьте среду.
2. Загрузите и исследуйте исходный датасет.
3. Отфильтруйте датасет.
4. Преобразуйте датасет в формат Alpaca.
5. Загрузите датасет на HuggingFace Hub.

Перед началом работы

1. Зарегистрируйтесь в личном кабинете Cloud.ru.
   Если вы уже зарегистрированы, войдите под своей учетной записью.
2. Убедитесь, что в личном кабинете Cloud.ru подключен сервис Notebooks.
3. Создайте токен Huggingface.
   а. Войдите или зарегистрируйтесь на https://huggingface.co.
   б. Перейдите в раздел Access Tokens.
   c. Нажмите Create new token.
   d. Выберите тип Write.
   e. Введите название токена.
   f. Нажмите Create token.
   g. Скопируйте токен и сохраните его, например в блокнот. После закрытия страницы он будет недоступен.

1. Подготовьте среду
1. Создайте ноутбук со следующими параметрами:
   • Конфигурация — ncpu.medium.4.
   • Образ — Cloud.ru Jupyter (Conda) 0.3.2.
Затем по той же инструкции настройте окружение ноутбука.
2. На главной странице сервиса Notebooks в строке нужного ноутбука нажмите JupyterLab — вы перейдете в среду разработки.
3. Установите библиотеки, выполнив код:

```python
pip install matplotlib numpy datasets huggingface_hub langdetect
```

4. Импортируйте прочие библиотеки, добавив код:

```python
import matplotlib.pyplot as plt
import numpy as np
from datasets import load_dataset
from huggingface_hub import login
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException

# HuggingFace Authentication
# Specify your HuggingFace Token
login()
```

2. Загрузите и исследуйте исходный датасет
1. Для загрузки датасета Github Issue добавьте следующий код:

```python
dataset = load_dataset("mlfoundations-dev/github-issues", split="train")
```

2. Чтобы понять структуру данных, ознакомьтесь с примерами записей в датасете:

```python
def show_samples(dataset, num_samples=1):
    """Просмотр примеров записей из набора данных."""
    sample = dataset.shuffle().select(range(num_samples))
    for example in sample:
        print(f"--> Заголовок: {example['title']}")
        print(f"--> Тело: {example['body']}")
        print(f"--> Язык: {detect(example['body'])}")
        print()

show_samples(dataset)
```

3. Постройте распределение длин поля body — текстовых описаний проблем:

```python
# Выводим длины тел всех записей
body_lengths = [len(str(item['body'])) for item in dataset]
body_lengths = np.array(body_lengths)

# Статистика
print("Минимальная длина тела:")
print(f"Минимальная длина тела: {body_lengths.min()}")
print("Максимальная длина тела:")
print(f"Максимальная длина тела: {body_lengths.max()}")
print("Средняя длина тела:")
print(f"Средняя длина тела: {body_lengths.mean():.2f}")
print("90-й процентиль:")
print(f"90-й процентиль: {np.percentile(body_lengths, 90):.2f}")
print("95-й процентиль:")
print(f"95-й процентиль: {np.percentile(body_lengths, 95):.2f}")
print("99-й процентиль:")
print(f"99-й процентиль: {np.percentile(body_lengths, 99):.2f}")

plt.figure(figsize=(10, 6))
plt.hist(body_lengths, bins=50, log=True)
plt.xlabel('Длина тела')
plt.ylabel('Количество примеров')
plt.title('Распределение длин тел проблем')
plt.show()
```

3. Отфильтруйте датасет
1. Оставьте только те строки, где значение body находится в диапазоне от 100 до 5 000 символов:

```python
def filter_by_body_length(example):
    """Фильтрация проблем по длине тела (100-5000 символов)."""
    length = len(str(example['body']))
    return 100 <= length <= 5000

filtered_dataset = dataset.filter(filter_by_body_length)
print(f"Общее количество проблем после фильтрации по длине: {len(filtered_dataset)}")
```

2. Оставьте только записи на английском языке:

```python
def is_english(example):
    """Checking whether the title and body are written in English"""
    try:
        return detect(example["title"]) == "en" and detect(example["body"]) == "en"
    except LangDetectException:
        return False

# For faster processing, you can apply filtering to a subset of the dataset
# english_ds = filtered_dataset.select(range(100000)).filter(is_english, num_proc=4)
english_ds = filtered_dataset.filter(is_english, num_proc=4)
print(f"Количество английских примеров: {len(english_ds)}")
```

4. Преобразуйте датасет в формат Alpaca
Преобразуйте датасет в формат Alpaca, в котором каждый пример — это словарь с тремя полями:

• instruction — текстовое задание для модели;
• input — входные данные;
• output — целевой ответ.

```python
def convert_to_alpaca_format(example):
    return {
        "instruction": "Write short and clear GitHub issue title that captures main problem.",
        "input": example["body"],
        "output": example["title"],
    }

alpaca_dataset = english_ds.map(convert_to_alpaca_format)
alpaca_dataset = alpaca_dataset.remove_columns([col for col in alpaca_dataset.column_names if col not in ["instruction", "input", "output"]])
```

5. Загрузите датасет на HuggingFace Hub
Опубликуйте итоговый датасет в ваш репозиторий на HuggingFace Hub, подставив свои данные:

```python
alpaca_dataset.push_to_hub("your_login/hf-repository_name")
```

Подсказка
Вы можете скачать готовый ноутбук, содержащий код и инструкции для обработки датасета из этого практического руководства.

Результат
Вы подготовили очищенный и структурированный датасет для задач генерации заголовков GitHub Issue по их описанию, преобразовали его в формат Alpaca и опубликовали на HuggingFace Hub для использования в сервисе ML Finetuning. Теперь вы можете дообучить модель из Huggingface, используя подготовленный датасет.

Узнавайте больше о прикладных сценариях и примерах решения бизнес-задач, получайте навыки управления облаком, выполняя практические руководства.