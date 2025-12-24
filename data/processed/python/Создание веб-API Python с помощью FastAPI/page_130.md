---
source_image: page_130.png
page_number: 130
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.63
tokens: 8281
characters: 1003
timestamp: 2025-12-24T02:19:15.281986
finish_reason: stop
---

5. Наконец, давайте удалим событие:

    (venv)$ curl -X 'DELETE' \
        'http://0.0.0.0:8080/event/624daab1585059e8a3fa77ac' \
        -H 'accept: application/json'

Вот ответ, полученный на запрос:

    {
        "message": "Event deleted successfully."
    }

6. Теперь, когда мы протестировали маршруты для событий, давайте создадим нового пользователя, а затем войдем в систему:

    (venv)$ curl -X 'POST' \
        'http://0.0.0.0:8080/user/signup' \
        -H 'accept: application/json' \
        -H 'Content-Type: application/json' \
        -d '{'
        "email": "fastapi@packt.com",
        "password": "strong!!!",
        "events": []
    '

Запрос возвращает ответ:

    {
        "message": "User created successfully"
    }

Повторный запуск запроса возвращает ошибку HTTP 409, указывающую на конфликт:

    {
        "detail": "User with email provided exists already."
    }

Изначально мы разработали маршрут для проверки существующих пользователей, чтобы избежать дублирования.