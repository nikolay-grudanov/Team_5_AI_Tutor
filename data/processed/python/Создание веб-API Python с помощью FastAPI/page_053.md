---
source_image: page_053.png
page_number: 53
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.99
tokens: 8211
characters: 696
timestamp: 2025-12-24T02:17:08.029192
finish_reason: stop
---

"item": "Example Schema!"
}
Вот ответ:

(venv) $ {
    "message": "Todo added successfully."
}

Далее давайте обновим задачу, отправив запрос PUT:

(venv) $ curl -X 'PUT' \
    'http://127.0.0.1:8000/todo/1' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{'
    "item": "Read the next chapter of the book."
}'
Вот ответ:

(venv) $ {
    "message": "Todo updated successfully."
}

Давайте проверим, что наша задача действительно была обновлена:

(venv) $ curl -X 'GET' \
    'http://127.0.0.1:8000/todo/1' \
    -H 'accept: application/json'

Вот ответ:

(venv) $ {
    "todo": {
        "id": 1,
        "item": "Read the next chapter of the book"
    }
}