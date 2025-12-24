---
source_image: page_419.png
page_number: 419
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.68
tokens: 7260
characters: 1287
timestamp: 2025-12-24T03:11:48.679634
finish_reason: stop
---

В каталоге CDK добавляем в создаваемый стек таблицу DynamoDB:

$ pwd
~/code/devops/serverless/cdk-lambda-dynamodb-fargate

$ cat cdk_lambda_dynamodb_fargate/cdk_lambda_dynamodb_stack.py
from aws_cdk import core
from aws_cdk import aws_dynamodb

class CdkLambdaDynamodbStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        # Описываем таблицу для хранения элементов Todo
        table = aws_dynamodb.Table(self, "Table",
            partition_key=aws_dynamodb.Attribute(
                name="id",
                type=aws_dynamodb.AttributeType.STRING),
            read_capacity=10,
            write_capacity=5)

Установим нужные модули Python:

$ cat requirements.txt
-e .
aws-cdk.core
aws-cdk.aws-dynamodb

$ pip install -r requirements.txt

С помощью команды cdk synth создадим стек CloudFormation:

$ export AWS_PROFILE=gheorghiu-net
$ cdk synth

Передаем конструктору CdkLambdaDynamodbStack в app.py переменную variable, содержащую значение для региона:

app_env = {"region": "us-east-2"}
CdkLambdaDynamodbStack(app, "cdk-lambda-dynamodb", env=app_env)

Снова выполняем команду cdk synth:

$ cdk synth
Resources:
    TableCD117FA1:
        Type: AWS::DynamoDB::Table
        Properties: