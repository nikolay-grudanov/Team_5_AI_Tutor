---
source_image: page_128.png
page_number: 128
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.67
tokens: 8317
characters: 1094
timestamp: 2025-12-24T02:19:12.942906
finish_reason: stop
---

2. Получить все события:

(venv)$ curl -X 'GET' \
    'http://0.0.0.0:8080/event/' \
    -H 'accept: application/json'

Предыдущий запрос возвращает список событий:

[
    {
        "_id": "624daab1585059e8a3fa77ac",
        "title": "FastAPI Book Launch",
        "image": "https://linktomyimage.com/image.png",
        "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
        "tags": [
            "python",
            "fastapi",
            "book",
            "launch"
        ],
        "location": "Google Meet"
    }
]

3. Получить событие:

(venv)$ curl -X 'GET' \
    'http://0.0.0.0:8080/event/624daab1585059e8a3fa77ac' \
    -H 'accept: application/json'

Эта операция возвращает событие, соответствующее предоставленному ID:

{
    "_id": "624daab1585059e8a3fa77ac",
    "title": "FastAPI Book Launch",
    "image": "https://linktomyimage.com/image.png",
    "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",