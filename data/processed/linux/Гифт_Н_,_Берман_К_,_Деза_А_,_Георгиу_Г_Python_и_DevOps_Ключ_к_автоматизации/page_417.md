---
source_image: page_417.png
page_number: 417
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.26
tokens: 7529
characters: 1820
timestamp: 2025-12-24T03:11:57.236564
finish_reason: stop
---

Выделение таблиц DynamoDB, функций Lambda и методов API Gateway с помощью AWS CDK

-rw-r--r--   1 ggheo staff   1651 Sep  2 10:10 README.md
-rw-r--r--   1 ggheo staff    252 Sep  2 10:10 app.py
-rw-r--r--   1 ggheo staff     32 Sep  2 10:10 cdk.json
drwxr-xr-x   4 ggheo staff   128 Sep  2 10:10 cdk_lambda_dynamodb_fargate
-rw-r--r--   1 ggheo staff      5 Sep  2 10:10 requirements.txt
-rw-r--r--   1 ggheo staff   1080 Sep  2 10:10 setup.py

Изучаем содержимое основного файла app.py:

$ cat app.py
#!/usr/bin/env python3

from aws_cdk import core

from cdk_lambda_dynamodb_fargate.cdk_lambda_dynamodb_fargate_stack \
import CdkLambdaDynamodbFargateStack

app = core.App()
CdkLambdaDynamodbFargateStack(app, "cdk-lambda-dynamodb-fargate")

app.synth()

Программа CDK состоит из приложения (app), которое может содержать один или несколько стеков (stacks). Стек соответствует объекту стека CloudFormation.

Изучаем модуль с описанием стека CDK:

$ cat cdk_lambda_dynamodb_fargate/cdk_lambda_dynamodb_fargate_stack.py
from aws_cdk import core

class CdkLambdaDynamodbFargateStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Место для кода с описанием вашего стека

Поскольку у нас будет два стека, один для ресурсов DynamoDB/Lambda/API Gateway, а второй для ресурсов Fargate, переименовываем cdk_lambda_dynamodb_fargate/cdk_lambda_dynamodb_fargate_stack.py в cdk_lambda_dynamodb_fargate/cdk_lambda_dynamodb_stack.py, а класс CdkLambdaDynamodbFargateStack — в CdkLambdaDynamodbStack.

Кроме того, необходимо, чтобы файл app.py ссылался на измененные названия модуля и класса:

from cdk_lambda_dynamodb_fargate.cdk_lambda_dynamodb_stack \
import CdkLambdaDynamodbStack

CdkLambdaDynamodbStack(app, "cdk-lambda-dynamodb")