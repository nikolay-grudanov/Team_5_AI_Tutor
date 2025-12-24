---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.95
tokens: 8251
characters: 1170
timestamp: 2025-12-24T02:17:22.415187
finish_reason: stop
---

Маршрут возвращает весь контент, хранящийся в массиве todos. Чтобы указать возвращаемую информацию, нам пришлось бы либо отделить отображаемые данные, либо ввести дополнительную логику. К счастью, мы можем создать модель, содержащую поля, которые мы хотим вернуть, и добавить ее в определение нашего маршрута, используя аргумент response_model.

Давайте обновим маршрут, который извлекает все задачи, чтобы он возвращал массив только элементов задач, а не идентификаторов. Начнем с определения нового класса модели для возврата списка дел в model.py:

```python
from typing import List

class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }

class TodoItems(BaseModel):
    todos: List[TodoItem]

    class Config:
        schema_extra = {
            "example": {
                "todos": [
                    {
                        "item": "Example schema 1!"
                    },
                    {
                        "item": "Example schema 2!"
                    }
                ]
            }
        }
```