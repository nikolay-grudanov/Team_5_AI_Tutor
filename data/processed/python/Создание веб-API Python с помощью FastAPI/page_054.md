---
source_image: page_054.png
page_number: 54
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.71
tokens: 8234
characters: 987
timestamp: 2025-12-24T02:17:14.106755
finish_reason: stop
---

Из возвращенного ответа мы видим, что задача успешно обновлена. Теперь давайте создадим маршрут для удаления задачи и всех задач.

В todo.py, обновите маршруты:

```python
@todo_router.delete("/todo/{todo_id}")
async def delete_single_todo(todo_id: int) -> dict:
    for index in range(len(todo_list)):
        todo = todo_list[index]
        if todo.id == todo_id:
            todo_list.pop(index)
            return {
                "message": "Todo deleted successfully."
            }
    return {
        "message": "Todo with supplied ID doesn't exist."
    }

@todo_router.delete("/todo")
async def delete_all_todo() -> dict:
    todo_list.clear()
    return {
        "message": "Todos deleted successfully."
    }
```

Давайте протестируем маршрут удаления. Сначала мы добавляем задачу:

```bash
(venv)$ curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "id": 1,
    "item": "Example Schema!"
}'
```