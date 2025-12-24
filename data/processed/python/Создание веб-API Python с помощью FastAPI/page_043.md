---
source_image: page_043.png
page_number: 43
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.56
tokens: 8216
characters: 978
timestamp: 2025-12-24T02:17:00.625502
finish_reason: stop
---

FastAPI также предоставляет класс Path, который отличает параметры пути от других аргументов, присутствующих в функции маршрута. Класс Path также помогает дать параметрам маршрута больше контекста во время документации, автоматически предоставляемой OpenAPI через Swagger и ReDoc, и действует как валидатор.

Давайте изменим определение маршрута:

```python
from fastAPI import APIRouter, Path

from model import Todo

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

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
```