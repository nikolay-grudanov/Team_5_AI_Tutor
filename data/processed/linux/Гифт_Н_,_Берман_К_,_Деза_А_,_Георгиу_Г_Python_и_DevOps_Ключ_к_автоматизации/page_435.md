---
source_image: page_435.png
page_number: 435
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.31
tokens: 7271
characters: 1032
timestamp: 2025-12-24T03:12:16.363202
finish_reason: stop
---

Развертываем стек cdk-fargate:

$ cdk deploy cdk-fargate

Перейдите в консоль AWS и взгляните на кластер ECS с запущенным там контейнером Fargate (рис. 13.5).

![Кластер ECS с запущенным там контейнером Fargate](../images/13_5.png)

Рис. 13.5. Кластер ECS с запущенным там контейнером Fargate

Посмотрите на инструментальной панели CloudWatch длительность выполнения функции Lambda (рис. 13.6), а также выделяемых и потребляемых единиц пропускной способности по чтению/записи DynamoDB (рис. 13.7). Как видите, задержка вполне удовлетворительная.

Увеличиваем количество контейнеров Fargate в cdk_lambda_dynamodb_fargate/cdk_fargate_stack.py до 5:

aws_ecs.FargateService(self, 'service',
    cluster=cluster,
    task_definition=task_definition,
    desired_count=5)

Снова развертываем стек cdk-fargate:

$ cdk deploy cdk-fargate

Смотрим на инструментальной панели CloudWatch длительность выполнения функции Lambda (рис. 13.8), а также выделяемых и потребляемых единиц пропускной способности по чтению/записи DynamoDB (рис. 13.9).