---
source_image: page_045.png
page_number: 45
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.45
tokens: 8304
characters: 1149
timestamp: 2025-12-24T02:17:08.029177
finish_reason: stop
---

POST и UPDATE
Метод POST используется, когда необходимо выполнить вставку на сервер, а метод UPDATE используется, когда необходимо обновить существующие данные на сервере.

Давайте взглянем на запрос POST ранее в этой главе:

(venv)$ curl -X 'POST' \
'http://127.0.0.1:8000/todo' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"id": 2,
"item": "Validation models help with input types"
}'

В предыдущем запросе тело запроса выглядит следующим образом:

{
    "id": 2,
    "item": "Validation models help with input types.."
}

Совет
FastAPI также предоставляет класс Body() для дополнительной проверки.

Мы узнали о моделях в FastAPI. Они также служат дополнительной цели в документировании наших конечных точек API и типов тела запроса. В следующем подразделе мы узнаем о страницах документации, генерируемых по умолчанию в приложениях FastAPI.

Автоматические документы FastAPI
FastAPI генерирует определения схемы JSON для наших моделей и автоматически документирует наши маршруты, включая их тип тела запроса, параметры пути и запроса, а также модели ответов. Эта документация бывает двух типов:

• Swagger
• ReDoc