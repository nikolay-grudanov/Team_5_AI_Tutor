---
source_image: page_433.png
page_number: 433
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.19
tokens: 7282
characters: 1132
timestamp: 2025-12-24T03:12:09.918817
finish_reason: stop
---

Длительность выполнения
Различные единицы

![Длительность выполнения функции Lambda](../images/13_3.png)

Рис. 13.3. Длительность выполнения функции Lambda

Количество

![Выделяемые и потребляемые единицы пропускной способности по чтению/записи DynamoDB](../images/13_4.png)

Рис. 13.4. Выделяемые и потребляемые единицы пропускной способности по чтению/записи DynamoDB

Далее мы создаем стек CDK Fargate для запуска контейнеров, основанных на сформированном ранее образе Docker:

$ cat cdk_lambda_dynamodb_fargate/cdk_fargate_stack.py
from aws_cdk import core
from aws_cdk import aws_ecs, aws_ec2

class FargateStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = aws_ec2.Vpc(
            self, "MyVpc",
            cidr= "10.0.0.0/16",
            max_azs=3
        )

        # Описываем кластер ECS, хостируемый в запрошенном нами VPC
        cluster = aws_ecs.Cluster(self, 'cluster', vpc=vpc)

        # Описываем нашу задачу в рамках одного контейнера
        # образ собирается и публикуется из локального каталога ресурсов