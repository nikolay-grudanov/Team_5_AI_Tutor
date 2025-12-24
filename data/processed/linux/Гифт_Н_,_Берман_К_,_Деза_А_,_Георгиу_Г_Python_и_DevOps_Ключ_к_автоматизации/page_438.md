---
source_image: page_438.png
page_number: 438
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.71
tokens: 7394
characters: 1627
timestamp: 2025-12-24T03:12:24.988756
finish_reason: stop
---

Как и ожидалось, значения обеих метрик — длительности выполнения функции Lambda и количества единиц пропускной способности по чтению DynamoDB — выросли, поскольку мы теперь моделируем \(5 \cdot 10 = 50\) работающих конкурентно пользователей.

Для моделирования большего числа пользователей можно увеличить как значение параметра concurrency в файле конфигурации taurus.yaml, так и значение параметра desired_count для контейнера Fargate. Благодаря сочетанию этих двух параметров можно легко увеличивать нагрузку на конечные точки нашего API REST.

Удаляем стеки CDK:

$ cdk destroy cdk-fargate
$ cdk destroy cdk-lambda-dynamodb

Стоит отметить, что развернутая нами бессерверная архитектура (API Gateway + 5 функций AWS Lambda + таблица DynamoDB) неплохо подошла для приложения API CRUD REST. Мы также следовали всем рекомендуемым практикам и описали всю инфраструктуру в коде Python с помощью AWS CDK.

Упражнения

• Запустите простую конечную точку HTTP с помощью платформы CaaS Google: Cloud Run (https://cloud.google.com/run).

• Запустите простые конечные точки HTTP на других упоминавшихся платформах, основанных на Kubernetes: Kubeless (https://kubeless.io), Fn Project (https://fnproject.io) и Fission (https://fission.io).

• Установите и настройте Apache OpenWhisk (https://openwhisk.apache.org) в кластере Kubernetes, подходящем для промышленной эксплуатации, например Amazon EKS, Google GKE или Azure AKS.

• Портируйте наш пример API REST для AWS на GCP и Azure. Для работы с несколькими API GCP предоставляет Cloud Endpoints (https://cloud.google.com/endpoints), а Azure — API Management (https://oreil.ly/tmDh7).