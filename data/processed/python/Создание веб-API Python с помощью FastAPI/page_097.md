---
source_image: page_097.png
page_number: 97
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.57
tokens: 8272
characters: 988
timestamp: 2025-12-24T02:18:26.309911
finish_reason: stop
---

import uvicorn
app = FastAPI()

# Register routes

app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)

Приложение автоматически перезагружается при каждом изменении. Проверим маршруты:

• Маршрут GET — следующая операция возвращает пустой массив, сообщая нам об отсутствии данных:

(venv)$ curl -X 'GET' \
'http://0.0.0.0:8080/event/' \
-H 'accept: application/json'
[]

Далее добавим данные в наш массив.

• Маршрут POST — в терминале выполните следующую команду:

(venv)$ curl -X 'POST' \
'http://0.0.0.0:8080/event/new' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 1,
"title": "FastAPI Book Launch",
"image": "https://linktomyimage.com/image.png",
"description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
"tags": [
"python",