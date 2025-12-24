---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 11.21
tokens: 8158
characters: 554
timestamp: 2025-12-24T02:16:42.044730
finish_reason: stop
---

В предыдущем блоке кода, {todo_id} является параметром пути. Этот параметр позволяет приложению возвращать совпадающую задачу с переданным идентификатором.

Проверим маршрут:

(venv)$ curl -X 'GET' \
'http://127.0.0.1:8000/todo/1' \
-H 'accept: application/json'

В предыдущем запросе GET request, 1 — это параметр пути. Здесь мы говорим нашему приложению todo вернуть элемент с идентификатором 1.

Выполнение предыдущего запроса приводит к следующему ответу:

{
    "todo": {
        "id": 1,
        "item": "First Todo is to finish this book!"
    }
}