---
source_image: page_279.png
page_number: 279
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.85
tokens: 7346
characters: 1618
timestamp: 2025-12-24T03:08:06.104939
finish_reason: stop
---

Python 2.7, Python 3.6 или Python 3.7. Все эти поставщики поддерживают среды выполнения Python и в некоторых случаях — возможности пользовательской настройки базовой среды выполнения посредством настраиваемого под свои нужды контейнера Docker. Далее приведен пример простой лямбда-функции AWS, предназначенной для получения главной страницы «Википедии».

Следует отметить несколько особенностей этой лямбда-функции. Собственно, ее логика заключается в lambda_handler, принимающей два аргумента. Первый аргумент, event, передается вызывающей стороной, которая может быть чем угодно, от таймера событий Amazon Cloud Watch до запуска ее со сформированным в AWS Lambda Console содержимым. Второй аргумент, context, содержит методы и свойства, обеспечивающие информацию о вызове, функции и среде выполнения:

import json
import wikipedia

print('Loading function')

def lambda_handler(event, context):
    """Средство реферирования Википедии"""

    entity = event["entity"]
    res = wikipedia.summary(entity, sentences=1)
    print(f"Response from wikipedia API: {res}")
    response = {
        "statusCode": "200",
        "headers": { "Content-type": "application/json" },
        "body": json.dumps({"message": res})
    }
    return response

Для использования этой лямбда-функции мы передаем следующее JSON-содержимое:

{"entity":"google"}

Выдаваемые этой лямбда-функцией результаты также представляют собой JSON-содержимое:

Response
{
    "statusCode": "200",
    "headers": {
        "Content-type": "application/json"
    },
    "body": "{\"message\": \"Google LLC is an American multinational technology\"}"
}