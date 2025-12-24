---
source_image: page_150.png
page_number: 150
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.40
tokens: 8434
characters: 1388
timestamp: 2025-12-24T02:19:54.717678
finish_reason: stop
---

Теперь давайте создадим новое событие из командной строки:

```bash
$ curl -X 'POST' \
    'http://0.0.0.0:8080/event/new' \
    -H 'accept: application/json' \
    -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlc2VyIjoicmVhZGVyQHBhY2t0LmNvbSIsImV4cGlyZXMiOjE2NTA4MjkxODMuNTg3NjAyfQ.MOXjI5GXnyzGNftdlxDGyM119_L11uPq8yCxBHepf04' \
    -H 'Content-Type: application/json' \
    -d '{
        "title": "FastAPI Book Launch CLI",
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
```

В отправленном здесь запросе также отправляется заголовок Authorization: Bearer, чтобы сообщить приложению, что мы уполномочены выполнять это действие. Полученный ответ следующий:

```json
{
    "message": "Event created successfully"
}
```

Если мы попытаемся создать событие без передачи заголовка авторизации с действительным токеном, будет возвращена ошибка HTTP 401 Unauthorized:

```bash
$ curl -X 'POST' \
    'http://0.0.0.0:8080/event/new' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "title": "FastAPI BookLaunch",
```