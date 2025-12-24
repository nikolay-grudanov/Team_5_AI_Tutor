---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.89
tokens: 8203
characters: 844
timestamp: 2025-12-24T02:16:44.345808
finish_reason: stop
---

```python
@todo_router.get("/todo")
async def retrieve_todos() -> dict:
    return {"todos": todo_list}
```

Давайте проверим новый валидатор тела запроса, отправив пустой словарь в качестве тела запроса:

```bash
(venv)$ curl -X 'POST' \
    'http://127.0.0.1:8000/todo' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{ }'
```

Получаем ответ, указывающий на отсутствие поля id и item в теле запроса:

```json
{
    "detail": [
        {
            "loc": [
                "body",
                "id"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        },
        {
            "loc": [
                "body",
                "item"
            ],
            "msg": "field required",
            "type": "value_error.missing"
        }
    ]
}
```