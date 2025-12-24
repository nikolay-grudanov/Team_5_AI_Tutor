---
source_image: page_418.png
page_number: 418
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.21
tokens: 7410
characters: 1755
timestamp: 2025-12-24T03:11:52.385090
finish_reason: stop
---

Активируем виртуальную среду:

$ source .env/bin/activate

Мы возьмем средство сокращения URL из примеров CDK (https://oreil.ly/q2dDF) и модифицируем его, воспользовавшись кодом из примера API REST на Python для платформы Serverless для AWS (https://oreil.ly/o_gxS), и получим в результате API REST для создания и вывода списка, а также обновления и удаления элементов todo. Для хранения данных применим DynamoDB от Amazon.

Изучаем содержимое файла serverless.yml из examples/aws-python-rest-api-with-dynamodb и развертываем его с помощью команды serverless, чтобы посмотреть, какие ресурсы AWS будут созданы:

$ pwd
~/code/examples/aws-python-rest-api-with-dynamodb

$ serverless deploy
Serverless: Stack update finished...
Service Information
service: serverless-rest-api-with-dynamodb
stage: dev
region: us-east-1
stack: serverless-rest-api-with-dynamodb-dev
resources: 34
api keys:
  None
endpoints:
POST - https://tbst34m2b7.execute-api.us-east-1.amazonaws.com/dev/todos
GET - https://tbst34m2b7.execute-api.us-east-1.amazonaws.com/dev/todos
GET - https://tbst34m2b7.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
PUT - https://tbst34m2b7.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
DELETE - https://tbst34m2b7.execute-api.us-east-1.amazonaws.com/dev/todos/{id}
functions:
  create: serverless-rest-api-with-dynamodb-dev-create
  list: serverless-rest-api-with-dynamodb-dev-list
  get: serverless-rest-api-with-dynamodb-dev-get
  update: serverless-rest-api-with-dynamodb-dev-update
  delete: serverless-rest-api-with-dynamodb-dev-delete
layers:
  None
Serverless: Run the "serverless" command to setup monitoring, troubleshooting and testing.

Предыдущая команда создала пять функций AWS Lambda, один API Gateway и одну таблицу DynamoDB.