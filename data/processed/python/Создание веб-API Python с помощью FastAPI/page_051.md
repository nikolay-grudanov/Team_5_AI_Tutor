---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.39
tokens: 8195
characters: 887
timestamp: 2025-12-24T02:17:07.521251
finish_reason: stop
---

Создание простого CRUD-приложения

Мы создали маршруты для создания и получения задач. Построим маршруты для обновления и удаления добавленных задач. Начнем с создания модели тела запроса для маршрута UPDATE в model.py:

```python
class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                "item": "Read the next chapter of the book"
            }
        }
```

Далее давайте напишем маршрут для обновления задачи в todo.py:

```python
from fastapi import APIRouter, Path
from model import Todo, TodoItem

todo_router = APIRouter()

todo_list = []

@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }

@todo_router.get("/todo")
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }
```