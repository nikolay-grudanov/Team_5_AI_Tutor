---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 15.78
tokens: 8265
characters: 1005
timestamp: 2025-12-24T02:20:46.860878
finish_reason: stop
---

Команда возвращает список контейнеров, работающих вместе с портами, через которые к ним можно получить доступ. Давайте проверим рабочее состояние, отправив запрос GET развернутому приложению:

(venv)$ curl -X 'GET' \
    'http://localhost:8080/event/' \
    -H 'accept: application/json'

Получаем следующий ответ:

[]

Замечательно! Развернутое приложение работает корректно. Давайте проверим, что база данных также работает, создав пользователя:

(venv)$ curl -X 'POST' \
    'http://localhost:8080/user/signup' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "email": "fastapi@packt.com",
        "password": "strong!!!"
    }'

Мы также получаем положительный ответ:

{
    "message": "User created successfully"
}

Теперь, когда мы протестировали оба маршрута, вы можете приступить к тестированию других маршрутов. Чтобы остановить сервер развертывания после проверки, из корневого каталога запускается следующая команда:

(venv)$ docker-compose down