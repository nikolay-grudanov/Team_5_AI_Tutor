---
source_image: page_403.png
page_number: 403
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.69
tokens: 7467
characters: 1608
timestamp: 2025-12-24T03:11:31.410190
finish_reason: stop
---

2019-08-23T03:35:12.419846316Z: Function execution took 20 ms, finished with status code: 200
2019-08-23T03:35:12.400499207Z: Function execution started
2019-08-23T03:34:27.133107221Z: Function execution took 11 ms, finished with status code: 200
2019-08-23T03:34:27.122244864Z: Function execution started

Проверяем работу конечной точки функции с помощью curl:

$ curl \
https://undefined-pythonfordevops-cloudfunction.cloudfunctions.net/endpoint
<!DOCTYPE html>
<html lang=en>
  <p><b>404.</b> <ins>That's an error.</ins>
  <p>The requested URL was not found on this server.
  <ins>That's all we know.</ins>

Поскольку мы не задали в файле serverless.yml регион, URL конечной точки начинается с undefined и возвращается ошибка.

Задаем в файле serverless.yml регион us-central1:

provider:
  name: google
  runtime: python37
  region: us-central1
  project: pythonfordevops-cloudfunction
  credentials: /Users/ggheo/.gcloud/pythonfordevops-cloudfunction.json

Развертываем новую версию с помощью команды serverless deploy и тестируем конечную точку функции, применяя curl:

$ curl \
https://us-central1-pythonfordevops-cloudfunction.cloudfunctions.net/endpoint
{
    "statusCode": 200,
    "body": {
        "message": "Received a GET request at 03:51:02.560756"
    }
}%

Развертывание функции на Python в Azure

Платформа Serverless пока что не поддерживает Azure Functions (https://oreil.ly/4WQKG)¹ на Python. Поэтому мы покажем, как развернуть функцию Python Azure с помощью нативных утилит Azure.

¹ Уже поддерживает, см. https://www.serverless.com/blog/serverless-azure-functions-v2/. — Примеч. пер.