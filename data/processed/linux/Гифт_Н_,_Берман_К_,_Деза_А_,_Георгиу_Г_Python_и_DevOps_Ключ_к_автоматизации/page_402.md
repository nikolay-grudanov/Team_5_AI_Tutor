---
source_image: page_402.png
page_number: 402
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.49
tokens: 7391
characters: 1789
timestamp: 2025-12-24T03:11:28.124464
finish_reason: stop
---

Переходим в Deployment Manager в консоли GCP и изучаем сообщения об ошибках:

sls-python-simple-http-endpoint-dev failed to deploy

sls-python-simple-http-endpoint-dev has resource warnings
sls-python-simple-http-endpoint-dev-1566510445295:
{
"ResourceType":"storage.v1.bucket",
"ResourceErrorCode":"403",
"ResourceErrorMessage":{"code":403,
"errors":[{"domain":"global","location":"Authorization",
"locationType":"header",
"message":"The project to be billed is associated with an absent billing account.",
"reason":"accountDisabled"}],
"message":"The project to be billed is associated with an absent billing account.",
"statusMessage":"Forbidden",
"requestPath":"https://www.googleapis.com/storage/v1/b",
"httpMethod":"POST"}}
Удаляем развертывание sls-python-simple-http-endpoint-dev в консоли GCP и снова выполняем команду serverless deploy:

$ serverless deploy

Deployed functions
first
    https://us-central1-pythonfordevops-cloudfunction.cloudfunctions.net/http

Команда serverless deploy вновь завершилась неудачно, поскольку изначально мы не включили биллинг для Google Cloud Storage. Развертывание было помечено как завершившееся неудачно для указанного в файле serverless.yml сервиса, так что последующие команды serverless deploy завершались неудачно даже после включения биллинга Cloud Storage. После удаления неудачного развертывания в консоли GCP команда serverless deploy начала работать.

Вызываем непосредственно развернутую функцию Google Cloud:

$ serverless invoke --function currentTime
Serverless: v1os7ptg9o48 {
    "statusCode": 200,
    "body": {
        "message": "Received a POST request at 03:46:39.027230"
    }
}

Изучаем журнал с помощью команды serverless logs:

$ serverless logs --function currentTime
Serverless: Displaying the 4 most recent log(s):