---
source_image: page_129.png
page_number: 129
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.83
tokens: 8177
characters: 600
timestamp: 2025-12-24T02:19:06.317326
finish_reason: stop
---

4. Обновим локацию события на Hybrid:

(venv)$ curl -X 'PUT' \
'http://0.0.0.0:8080/event/624daab1585059e8a3fa77ac' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
    "location": "Hybrid"
}'

{
    "_id": "624daab1585059e8a3fa77ac",
    "title": "FastAPI Book Launch",
    "image": "https://linktomyimage.com/image.png",
    "description": "We will be discussing the contents of the FastAPI book in this event. Ensure to come with your own copy to win gifts!",
    "tags": [
        "python","fastapi",
        "book",
        "launch"
    ],
    "location": "Hybrid"
}