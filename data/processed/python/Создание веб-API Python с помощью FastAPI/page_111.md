---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.30
tokens: 8246
characters: 952
timestamp: 2025-12-24T02:18:38.767252
finish_reason: stop
---

)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Event with supplied ID does not exist"
    )
Модель ответа для обоих маршрутов была установлена в классе модели. Давайте протестируем оба маршрута, сначала отправив запрос GET для получения списка событий:

(venv)$ curl -X 'GET' \
    'http://0.0.0.0:8080/event/' \
    -H 'accept: application/json'

Мы получаем ответ:

[
    {
        "id": 1,
        "title": "FastAPI Book Launch",
        "image": "fastapi-book.jpeg",
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

Далее давайте извлечем событие по его ID:

(venv)$ curl -X 'GET' \
    'http://0.0.0.0:8080/event/1' \
    -H 'accept: application/json'