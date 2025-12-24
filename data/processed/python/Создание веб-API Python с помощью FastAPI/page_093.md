---
source_image: page_093.png
page_number: 93
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.73
tokens: 8288
characters: 1036
timestamp: 2025-12-24T02:18:14.102642
finish_reason: stop
---

INFO:     Started server process [6550]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

6. Теперь, когда наше приложение успешно запустилось, давайте проверим реализованные нами пользовательские маршруты. Начнем с регистрации пользователя:

(venv)$ curl -X 'POST' \
    'http://0.0.0.0:8080/user/signup' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{'
    "email": "fastapi@packt.com",
    "password": "Stro0ng!",
    "username": "FastPackt"
}'

Предыдущий запрос возвращает ответ:

{
    "message": "User successfully registered!"
}

7. Предыдущий ответ указывает на успешность выполненной операции. Давайте проверим маршрут входа:

(venv)$ curl -X 'POST' \
    'http://0.0.0.0:8080/user/signin' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{'
    "email": "fastapi@packt.com",
    "password": "Stro0ng!"
}'

Предыдущий ответ на запрос выглядит следующим образом:

{
    "message": "User signed in successfully"
}