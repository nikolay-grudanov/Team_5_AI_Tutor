---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.30
tokens: 8318
characters: 1079
timestamp: 2025-12-24T02:16:42.044189
finish_reason: stop
---

Ответ от приложения, в консоли:

```json
{"message": "Hello World"}
```

Далее мы проверяем работоспособность todo-маршрутов:

```bash
(venv)$ curl -X 'GET' \
    'http://127.0.0.1:8000/todo' \
    -H 'accept: application/json'
```

Ответ от приложения в консоли должна быть следующим:

```json
{
    "todos": []
}
```

Маршрут todo сработал! Давайте проверим операцию POST, отправив запрос на добавление элемента в наш список задач:

```bash
(venv)$ curl -X 'POST' \
    'http://127.0.0.1:8000/todo' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
        "id": 1,
        "item": "First Todo is to finish this book!"
    }'
```

Имеем следующий ответ:

```json
{
    "message": "Todo added successfully."
}
```

Мы узнали, как работает класс APIRouter и как включить его в основной экземпляр приложения, чтобы разрешить использование определенных операций пути. В маршрутах todo, построенных в этом разделе, отсутствовали модели, также известные как схемы. В следующем разделе мы рассмотрим модели Pydantic и варианты их использования.