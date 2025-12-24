---
source_image: page_040.png
page_number: 40
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.20
tokens: 8186
characters: 713
timestamp: 2025-12-24T02:16:42.044969
finish_reason: stop
---

Отправка запроса с правильными данными возвращает успешный ответ:

(venv)$ curl -X 'POST' \
    'http://127.0.0.1:8000/todo' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "id": 2,
        "item": "Validation models help with input types"
    }'

Вот ответ:

{
    "message": "Todo added successfully."
}

Вложенные модели

Модели Pydantic также могут быть вложенными, например, следующие:

class Item(BaseModel)
    item: str
    status: str

class Todo(BaseModel)
    id: int
    item: Item

В результате задача типа Todo будет представлена следующим образом:

{
    "id": 1,
    "item": {
        "item": "Nested models",
        "Status": "completed"
    }
}