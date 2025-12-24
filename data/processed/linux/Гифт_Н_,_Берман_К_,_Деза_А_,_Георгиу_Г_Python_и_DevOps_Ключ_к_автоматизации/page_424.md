---
source_image: page_424.png
page_number: 424
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.41
tokens: 7476
characters: 1457
timestamp: 2025-12-24T03:12:04.521749
finish_reason: stop
---

Развертываем стек с помощью команды cdk deploy:

$ cdk deploy
cdk-lambda-dynamodb-fargate failed: Error:
This stack uses assets, so the toolkit stack must be deployed to the environment
(Run "cdk bootstrap aws://unknown-account/us-east-2")

Исправляем ошибку посредством выполнения cdk bootstrap:

$ cdk bootstrap
Bootstrapping environment aws://ACCOUNTID/us-east-2...
CDKToolkit: creating CloudFormation changeset...
Environment aws://ACCOUNTID/us-east-2 bootstrapped.

Снова развертываем стек CDK:

$ cdk deploy
ВЫВОД ОПУЩЕН

Outputs:
cdk-lambda-dynamodb.TodoApiEndpointC1E16B6C =
https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/

Stack ARN:
arn:aws:cloudformation:us-east-2:ACCOUNTID:stack/cdk-lambda-dynamodb/15a66bb0-cdba-11e9-aef9-0ab95d3a5528

Следующий шаг — тестирование API REST с помощью curl.

Сначала создаем новый элемент todo:

$ curl -X \
POST https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/todos \
--data '{ "text": "Learn CDK" }'
{"id": "19d55d5a-cdb4-11e9-9a8f-9ed29c44196e", "text": "Learn CDK",
"checked": false,
"createdAt": "1567450902.262834",
"updatedAt": "1567450902.262834"}%

Создаем еще один элемент todo:

$ curl -X \
POST https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/todos \
--data '{ "text": "Learn CDK with Python" }'
{"id": "58a992c6-cdb4-11e9-9a8f-9ed29c44196e", "text": "Learn CDK with Python",
"checked": false,
"createdAt": "1567451007.680936",
"updatedAt": "1567451007.680936"}%