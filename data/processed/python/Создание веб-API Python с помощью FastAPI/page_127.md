---
source_image: page_127.png
page_number: 127
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.62
tokens: 8250
characters: 948
timestamp: 2025-12-24T02:19:06.753414
finish_reason: stop
---

Далее в другом окне запускаем приложение:

(venv)$ python main.py
INFO:    Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
INFO:    Started reloader process [3744] using statreload
INFO:    Started server process [3747]
INFO:    Waiting for application startup.
INFO:    Application startup complete.

Давайте протестируем маршруты событий:

1. Создайте событие:

(venv)$ curl -X 'POST' \
'http://0.0.0.0:8080/event/new' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
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
}'

Вот ответ от предыдущей операции:

{
    "message": "Event created successfully"
}