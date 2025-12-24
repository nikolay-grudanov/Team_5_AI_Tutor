---
source_image: page_118.png
page_number: 118
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.54
tokens: 8276
characters: 1253
timestamp: 2025-12-24T02:18:58.370532
finish_reason: stop
---

В этом блоке кода мы начинаем с импорта зависимостей, необходимых для инициализации базы данных. Затем мы определяем класс Settings, который имеет значение DATABASE_URL, которое считывается из среды env, определенной в подклассе Config. Мы также определяем метод initialize_database для инициализации базы данных.

Метод init_beanie принимает клиент базы данных, который представляет собой версию движка mongo, созданную в разделе SQLModel, и список документов.

3. Давайте обновим файлы модели в каталоге моделей, чтобы включить документы MongoDB. В models/events.py, замените содержимое следующим:

```python
from beanie import Document
from typing import Optional, List

class Event(Document):
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "https://linktomyimage.com/image.png",
                "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Google Meet"
            }
        }
```