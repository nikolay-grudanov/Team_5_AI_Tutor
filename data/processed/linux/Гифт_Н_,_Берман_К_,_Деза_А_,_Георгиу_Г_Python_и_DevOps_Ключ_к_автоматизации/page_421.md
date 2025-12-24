---
source_image: page_421.png
page_number: 421
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.81
tokens: 7534
characters: 1691
timestamp: 2025-12-24T03:12:04.961993
finish_reason: stop
---

Следующий этап — добавление в стек функций Lambda и ресурса API Gateway.

В каталоге кода CDK создайте каталог lambda и скопируйте туда модули Python из примера API REST на Python для платформы Serverless для AWS (https://oreil.ly/mRSjn):

$ pwd
~/code/devops/serverless/cdk-lambda-dynamodb-fargate

$ mkdir lambda
$ cp ~/code/examples/aws-python-rest-api-with-dynamodb/todos/* lambda
$ ls -la lambda
total 48
drwxr-xr-x   9 ggheo  staff   288 Sep  2 10:41 .
drwxr-xr-x  10 ggheo  staff   320 Sep  2 10:19 ..
-rw-r--r--   1 ggheo  staff     0 Sep  2 10:41 __init__.py
-rw-r--r--   1 ggheo  staff   822 Sep  2 10:41 create.py
-rw-r--r--   1 ggheo  staff   288 Sep  2 10:41 decimalencoder.py
-rw-r--r--   1 ggheo  staff   386 Sep  2 10:41 delete.py
-rw-r--r--   1 ggheo  staff   535 Sep  2 10:41 get.py
-rw-r--r--   1 ggheo  staff   434 Sep  2 10:41 list.py
-rw-r--r--   1 ggheo  staff  1240 Sep  2 10:41 update.py

Добавляем требуемые модули в файл requirements.txt и установим их с помощью системы управления пакетами pip:

$ cat requirements.txt
-e .
aws-cdk.core
aws-cdk.aws-dynamodb
aws-cdk.aws-lambda
aws-cdk.aws-apigateway

$ pip install -r requirements.txt

Создаем конструкции Lambda и API Gateway в модуле стека:

$ cat cdk_lambda_dynamodb_fargate/cdk_lambda_dynamodb_stack.py
from aws_cdk import core
from aws_cdk.core import App, Construct, Duration
from aws_cdk import aws_dynamodb, aws_lambda, aws_apigateway

class CdkLambdaDynamodbStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Описываем таблицу для хранения элементов Todo
        table = aws_dynamodb.Table(self, "Table",