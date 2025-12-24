---
source_image: page_098.png
page_number: 98
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.17
tokens: 8189
characters: 742
timestamp: 2025-12-24T02:18:17.393952
finish_reason: stop
---

"fastapi",
"book",
"launch"
],
"location": "Google Meet"
}
'
Вот ответ:
{
    "message": "Event created successfully"
}

Эта операция прошла успешно, судя по полученному ответу. Теперь давайте попробуем получить конкретное событие, которое мы только что создали:

• Маршрут GET:

(venv)$ curl -X 'GET' \
'http://0.0.0.0:8080/event/1' \
-H 'accept: application/json'

Вот ответ:
{
    "id": 1,
    "title": "FastAPI BookLaunch",
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