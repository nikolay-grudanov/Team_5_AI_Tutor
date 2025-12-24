---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.50
tokens: 8224
characters: 801
timestamp: 2025-12-24T02:17:24.026176
finish_reason: stop
---

В предыдущем блоке кода мы определили новую модель, TodoItems, которая возвращает список переменных, содержащихся в модели TodoItem. Давайте обновим наш маршрут в todo.py добавив в него модель ответа:

```python
from model import Todo, TodoItem, TodoItems

...
@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }
```

Активируйте виртуальную среду и запустите приложение:

```bash
$ source venv/bin/activate
(venv)$ uvicorn api:app --host=0.0.0.0 --port 8000 --reload
```

Затем добавьте новую задачу:

```bash
(venv)$ curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 1,
"item": "This todo will be retrieved without exposing my ID!"
}'
```