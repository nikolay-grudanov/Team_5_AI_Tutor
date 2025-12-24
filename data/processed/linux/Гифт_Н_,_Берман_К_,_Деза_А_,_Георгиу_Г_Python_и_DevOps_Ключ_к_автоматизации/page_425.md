---
source_image: page_425.png
page_number: 425
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.75
tokens: 7410
characters: 1365
timestamp: 2025-12-24T03:12:00.243152
finish_reason: stop
---

Пытаемся получить подробные сведения о только что созданном элементе по его ID:

$ curl \
https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/
prod/todos/58a992c6-cdb4-11e9-9a8f-9ed29c44196e
{"message": "Internal server error"%}

Просматриваем журнал CloudWatch Logs для функции Lambda TodoGetFunction:

[ERROR] Runtime.ImportModuleError:
Unable to import module 'get': No module named 'todos'

Чтобы исправить эту проблему, измените в файле lambda/get.py строку:

from todos import decimalencoder

на следующую:

import decimalencoder

Снова развертываем стек с помощью команды cdk deploy.

Опять пытаемся получить сведения об элементе todo с помощью curl:

$ curl \
https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/
prod/todos/58a992c6-cdb4-11e9-9a8f-9ed29c44196e
{"checked": false, "createdAt": "1567451007.680936",
"text": "Learn CDK with Python",
"id": "58a992c6-cdb4-11e9-9a8f-9ed29c44196e",
"updatedAt": "1567451007.680936"}

Производим замену на import decimalencoder во всех модулях из каталога lambda, в которых требуется модуль decimalencoder, и развертываем стек заново с помощью cdk deploy.

Выводим список всех todo, форматируя выводимые результаты с помощью утилиты jq:

$ curl \
https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/todos | jq
[
  {
    "checked": false,
    "createdAt": "1567450902.262834",
    "text": "Learn CDK",