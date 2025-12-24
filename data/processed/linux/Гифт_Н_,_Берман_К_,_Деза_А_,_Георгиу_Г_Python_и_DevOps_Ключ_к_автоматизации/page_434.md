---
source_image: page_434.png
page_number: 434
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.38
tokens: 7355
characters: 1543
timestamp: 2025-12-24T03:12:16.519086
finish_reason: stop
---

task_definition = aws_ecs.FargateTaskDefinition(self,
    'LoadTestTask')
task_definition.add_container('TaurusLoadTest',
    image=aws_ecs.ContainerImage.from_asset("loadtest"),
    environment={'BASE_URL':
        "https://k6ygy4xw24.execute-api.us-east-2.amazonaws.com/prod/"})

# Описываем сервис fargate. TPS определяет количество требуемых
# экземпляров задания (каждая задача соответствует одной TPS)
aws_ecs.FargateService(self, 'service',
    cluster=cluster,
    task_definition=task_definition,
    desired_count=1)

В коде класса FargateStack необходимо отметить несколько нюансов.

• С помощью конструкции aws_ec2.Vpc создается новое VPC.
• В этом новом VPC создается кластер ECS.
• Описание задачи Fargate создается на основе Dockerfile из каталога loadtest, CDK достаточно интеллектуален для того, чтобы собрать образ Docker на основе этого Dockerfile и затем поместить его в реестр Docker ECR.
• Для запуска контейнеров Fargate, основанных на помещенном в реестр ECR образе, создается сервис ECS, параметр desired_count определяет количество запускаемых контейнеров.

Вызываем в app.py конструктор класса FargateStack:

$ cat app.py
#!/usr/bin/env python3

from aws_cdk import core

from cdk_lambda_dynamodb_fargate.cdk_lambda_dynamodb_stack \
import CdkLambdaDynamodbStack
from cdk_lambda_dynamodb_fargate.cdk_fargate_stack import FargateStack

app = core.App()
app_env = {
    "region": "us-east-2",
}

CdkLambdaDynamodbStack(app, "cdk-lambda-dynamodb", env=app_env)
FargateStack(app, "cdk-fargate", env=app_env)

app.synth()