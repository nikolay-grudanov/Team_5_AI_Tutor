---
source_image: page_416.png
page_number: 416
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.83
tokens: 7444
characters: 1715
timestamp: 2025-12-24T03:11:52.008589
finish_reason: stop
---

Следующий пример будет полноценнее. Мы продемонстрируем, как выделить с помощью AWS CDK сразу несколько функций Lambda, работающих за API Gateway, обеспечивающих (CRUD) REST-доступ для создания/чтения/обновления/удаления хранимых в таблице DynamoDB элементов todo. Мы также покажем, как выполнить нагрузочное тестирование нашего API REST с помощью развернутых в AWS Fargate контейнеров, а также утилиты нагрузочного тестирования Locust. Контейнеры Fargate мы также выделим с помощью AWS CDK.

Выделение таблиц DynamoDB, функций Lambda и методов API Gateway с помощью AWS CDK

Мы уже мельком упоминали AWS CDK в главе 10. AWS CDK — программный продукт, с помощью которого можно описывать желаемое состояние инфраструктуры в виде настоящего кода (в настоящее время поддерживаются языки программирования TypeScript и Python) вместо файлов описаний в формате YAML (как в платформе Serverless).

Установите интерфейс командной строки CDK на глобальном уровне (в зависимости от вашей операционной системы может потребоваться выполнить следующую команду с sudo):

$ npm install cdk -g

Создайте каталог для приложения CDK:

$ mkdir cdk-lambda-dynamodb-fargate
$ cd cdk-lambda-dynamodb-fargate

Создайте пример Python-приложения с помощью cdk init:

$ cdk init app --language=python
Applying project template app for python
Executing Creating virtualenv...

# Welcome to your CDK Python project!
This is a blank project for Python development with CDK.
The `cdk.json` file tells the CDK Toolkit how to execute your app.

Выводим список созданных файлов:

$ ls -la
total 40
drwxr-xr-x   9 ggheo  staff   288 Sep  2 10:10 .
drwxr-xr-x  12 ggheo  staff   384 Sep  2 10:10 ..
drwxr-xr-x   6 ggheo  staff   192 Sep  2 10:10 .env