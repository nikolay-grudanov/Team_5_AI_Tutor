---
source_image: page_087.png
page_number: 87
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.13
tokens: 8220
characters: 992
timestamp: 2025-12-24T02:18:05.470990
finish_reason: stop
---

Как показано на предыдущей диаграмме модели, у каждого пользователя будет поле Events, представляющее собой список событий, на которые он имеет право собственности.

2. Определим модель Event в models/events.py:

```python
from pydantic import BaseModel
from typing import List

class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str
```

3. Давайте определим подкласс Config в классе Event, чтобы показать пример того, как будут выглядеть данные модели, когда мы посетим документацию:

```python
class Config:
    schema_extra = {
        "example": {
            "title": "FastAPI Book Launch",
            "image": "https://linktomyimage.com/image.png",
            "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
            "tags": ["python", "fastapi", "book", "launch"]
            "location": "Google Meet"
        }
    }
```