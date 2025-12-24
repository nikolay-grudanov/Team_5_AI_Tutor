---
source_image: page_426.png
page_number: 426
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.86
tokens: 7461
characters: 1444
timestamp: 2025-12-24T03:12:07.805615
finish_reason: stop
---

"checked": false,
"createdAt": "1567451007.680936",
"text": "Learn CDK with Python",
"id": "58a992c6-cdb4-11e9-9a8f-9ed29c44196e",
"updatedAt": "1567451007.680936"
}
]

Удаляем элемент todo и убеждаемся, что в списке его больше нет:

$ curl -X DELETE \
https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/todos/
19d55d5a-cdb4-11e9-9a8f-9ed29c44196e
$ curl https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/todos | jq
[
{
    "checked": false,
    "createdAt": "1567451007.680936",
    "text": "Learn CDK with Python",
    "id": "58a992c6-cdb4-11e9-9a8f-9ed29c44196e",
    "updatedAt": "1567451007.680936"
}
]

А теперь проверяем обновление существующего элемента todo с помощью curl:

$ curl -X \
PUT https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/todos/
58a992c6-cdb4-11e9-9a8f-9ed29c44196e \
--data '{ "text": "Learn CDK with Python by reading the PyForDevOps book" }'
{"message": "Internal server error"%}

Смотрим журнал CloudWatch для связанной с этой конечной точкой функции Lambda:

[ERROR] Exception: Couldn't update the todo item.
Traceback (most recent call last):
    File "/var/task/update.py", line 15, in update
        raise Exception("Couldn't update the todo item.")

Меняем код проверочного теста в lambda/update.py на следующий:

    data = json.loads(event['body'])
    if 'text' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't update the todo item.")