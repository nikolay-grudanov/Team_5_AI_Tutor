---
source_image: page_397.png
page_number: 397
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.86
tokens: 7534
characters: 2009
timestamp: 2025-12-24T03:11:24.932319
finish_reason: stop
---

---------------------------------------------
START RequestId: 5ac3c9c8-f8ca-4029-84fa-fcf5157b1404 Version: $LATEST
END RequestId: 5ac3c9c8-f8ca-4029-84fa-fcf5157b1404
REPORT RequestId: 5ac3c9c8-f8ca-4029-84fa-fcf5157b1404
Duration: 1.68 ms Billed Duration: 100 ms   Memory Size: 1024 MB
Max Memory Used: 56 MB

Обратите внимание на то, что Billed Duration (включенная в счет длительность использования) в предыдущем выводе составляет 100 миллисекунд, демонстрируя тем самым одно из преимуществ FaaS — счет выставляется за очень дробные промежутки времени.

Кроме того, мы хотели бы обратить ваше внимание на то, что весь большой объем работ по созданию ресурсов AWS, необходимых для функции Lambda, берет на себя «за кулисами» платформа Serverless. Она создает стек CloudFormation под названием в данном случае aws-python-simple-http-endpoint-dev. Просмотреть его можно с помощью утилиты командной строки aws:

$ aws cloudformation describe-stack-resources \
  --stack-name aws-python-simple-http-endpoint-dev
  --region us-east-1 | jq '.StackResources[].ResourceType'
"AWS::ApiGateway::Deployment"
"AWS::ApiGateway::Method"
"AWS::ApiGateway::Resource"
"AWS::ApiGateway::RestApi"
"AWS::Lambda::Function"
"AWS::Lambda::Permission"
"AWS::Lambda::Version"
"AWS::Logs::LogGroup"
"AWS::IAM::Role"
"AWS::S3::Bucket"

Отметим, что стек CloudFormation включает не менее десяти типов ресурсов, которые в противном случае пришлось бы создавать или связывать друг с другом вручную.

Развертывание функции Python в Google Cloud Functions

В этом разделе мы воспользуемся примером кода из каталога google-python-simple-http-endpoint репозитория GitHub с примерами платформы Serverless:

$ gcloud projects list
PROJECT_ID                NAME                                 PROJECT_NUMBER
pulumi-gke-testing        Pulumi GKE Testing                  705973980178
pythonfordevops-gke-pulumi pythonfordevops-gke-pulumi         787934032650

Создаем новый проект GCP:

$ gcloud projects create pythonfordevops-cloudfunction