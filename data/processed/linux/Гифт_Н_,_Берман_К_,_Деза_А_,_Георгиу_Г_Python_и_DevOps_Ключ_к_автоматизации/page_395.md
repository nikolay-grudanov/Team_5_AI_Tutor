---
source_image: page_395.png
page_number: 395
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.66
tokens: 7264
characters: 1297
timestamp: 2025-12-24T03:11:08.359217
finish_reason: stop
---

Развертывание функции Python в AWS Lambda

Начнем с клонирования репозитория GitHub с примерами платформы Serverless:

$ git clone https://github.com/serverless/examples.git
cd examples/aws-python-simple-http-endpoint
$ export AWS_PROFILE=gheorghiu-net

Конечная точка HTTP Python описана в файле handle.py:

$ cat handler.py
import json
import datetime

def endpoint(event, context):
    current_time = datetime.datetime.now().time()
    body = {
        "message": "Hello, the current time is " + str(current_time)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

Платформа Serverless применяет декларативный подход для описания создаваемых ресурсов в YAML-файле serverless.yml. Вот пример этого файла, в котором объявлена функция currentTime, соответствующая функции Python endpoint из описанного ранее модуля handler:

$ cat serverless.yml
service: aws-python-simple-http-endpoint
frameworkVersion: ">=1.2.0 <2.0.0"

provider:
  name: aws
  runtime: python2.7 # or python3.7, supported as of November 2018

functions:
  currentTime:
    handler: handler.endpoint
    events:
      - http:
          path: ping
          method: get

Измените версию Python в файле serverless.yml на 3.7:

provider:
  name: aws
  runtime: python3.7