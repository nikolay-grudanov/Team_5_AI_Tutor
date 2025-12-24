---
source_image: page_074.png
page_number: 74
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.97
tokens: 8259
characters: 1123
timestamp: 2025-12-24T02:17:40.276739
finish_reason: stop
---

Прежде чем перейти к созданию наших шаблонов, давайте настроим Jinja в нашем приложении FastAPI:

1. Давайте изменим POST маршрут компонента API задач, todo.py:

```python
from fastapi import APIRouter, Path, HTTPException, status, Request, Depends
from fastapi.templating import Jinja2Templates
from model import Todo, TodoItem, TodoItems

todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates/")

@todo_router.post("/todo")
async def add_todo(request: Request, todo: Todo = Depends(Todo.as_form)):
    todo.id = len(todo_list) + 1
    todo_list.append(todo)
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })
```

2. Затем обновите маршруты GET:

```python
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse("todo.html", {
        "request": request,
        "todos": todo_list
    })

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(request: Request, todo_id: int = Path(..., title="The ID of the todo to retrieve.")):
```