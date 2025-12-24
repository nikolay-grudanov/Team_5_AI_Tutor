---
source_image: page_396.png
page_number: 396
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.39
tokens: 7367
characters: 1647
timestamp: 2025-12-24T03:11:14.287405
finish_reason: stop
---

Развертываем эту функцию в AWS Lambda с помощью команды serverless deploy:

$ serverless deploy
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless:
Uploading service aws-python-simple-http-endpoint.zip file to S3 (1.95 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
.............
Serverless: Stack update finished...
Service Information
service: aws-python-simple-http-endpoint
stage: dev
region: us-east-1
stack: aws-python-simple-http-endpoint-dev
resources: 10
api keys:
  None
endpoints:
  GET - https://3a88jzlxm0.execute-api.us-east-1.amazonaws.com/dev/ping
functions:
  currentTime: aws-python-simple-http-endpoint-dev-currentTime
layers:
  None
Serverless:
Run the "serverless" command to setup monitoring, troubleshooting and testing.

Проверяем развернутую функцию AWS Lambda, выполняя запрос к ее конечной точке с помощью curl:

$ curl https://3a88jzlxm0.execute-api.us-east-1.amazonaws.com/dev/ping
{"message": "Hello, the current time is 23:16:30.479690"%}

Вызываем функцию Lambda напрямую с помощью команды serverless invoke:

$ serverless invoke --function currentTime
{
    "statusCode": 200,
    "body": "{\"message\": \"Hello, the current time is 23:18:38.101006\"}"
}

Вызываем функцию Lambda напрямую с одновременным выводом журнала (он отправляется в AWS CloudWatch Logs):

$ serverless invoke --function currentTime --log
{
    "statusCode": 200,
    "body": "{\"message\": \"Hello, the current time is 23:17:11.182463\"}"
}