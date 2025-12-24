---
source_image: page_055.png
page_number: 55
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.74
tokens: 8241
characters: 836
timestamp: 2025-12-24T02:17:17.506705
finish_reason: stop
---

Вот ответ:

(venv) $ {
    "message": "Todo added successfully."
}

Затем удалите задачу:

(venv) $ curl -X 'DELETE' \
    'http://127.0.0.1:8000/todo/1' \
    -H 'accept: application/json'

Вот ответ:

(venv) $ {
    "message": "Todo deleted successfully."
}

Давайте проверим, что задача была удалена, отправив запрос GET для получения задачи:

(venv) $ curl -X 'GET' \
    'http://127.0.0.1:8000/todo/1' \
    -H 'accept: application/json'

Вот ответ:

(venv) $ {
    "message": "Todo with supplied ID doesn't exist.
}

В этом разделе мы создали приложение с CRUD операциями, объединив уроки, извлеченные из предыдущих разделов. Подтвердив тело запроса, мы смогли убедиться, что в API отправляются правильные данные. Включение параметров пути в наши маршруты также позволило нам получить и удалить одну задачу из нашего списка задач.