---
source_image: page_400.png
page_number: 400
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.53
tokens: 7233
characters: 1217
timestamp: 2025-12-24T03:11:11.542962
finish_reason: stop
---

Попробуем развернуть функцию снова:

$ serverless deploy

    Error -------------------------------------------------------------
    Error: ENOENT: no such file or directory,
    open '/Users/ggheo/.gcloud/keyfile.json'

Для генерации ключа учетных данных создайте новую учетную запись сервиса sa на странице учетной записи сервиса IAM GCP. В данном случае для новой учетной записи сервиса был задан адрес электронной почты sa-255@pythonfordevops-cloudfunction.iam.gserviceaccount.com.

Создайте ключ учетных данных и скачайте его в файл ~/.gcloud/pythonfordevops-cloudfunction.json.

Укажите проект и путь к ключу в файле serverless.yml:

$ cat serverless.yml

service: python-simple-http-endpoint

frameworkVersion: ">=1.2.0 <2.0.0"

package:
  exclude:
    - node_modules/**
    - .gitignore
    - .git/**

plugins:
  - serverless-google-cloudfunctions

provider:
  name: google
  runtime: python37
  project: pythonfordevops-cloudfunction
  credentials: ~/.gcloud/pythonfordevops-cloudfunction.json

functions:
  currentTime:
    handler: endpoint
    events:
      - http: path

Перейдите на страницу менеджера развертывания (deployment manager) GCP и включите его API, а также биллинг для Google Cloud Storage.