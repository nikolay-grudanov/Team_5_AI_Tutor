---
source_image: page_415.png
page_number: 415
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.53
tokens: 7323
characters: 1406
timestamp: 2025-12-24T03:11:41.276893
finish_reason: stop
---

functions:
    hello-python:
        lang: python
        handler: ./hello-python
        image: griggheo/hello-python:latest
        environment:
            content_type: application/json

Снова запустите команду faas-cli deploy:

$ faas-cli deploy -f ./hello-python.yml
Deploying: hello-python.
WARNING! Communication is not secure, please consider using HTTPS.
Letsencrypt.org offers free SSL/TLS certificates.
Handling connection for 8080
Handling connection for 8080

Deployed. 202 Accepted.
URL: http://localhost:8080/function/hello-python

При необходимости изменения кода собрать и заново развернуть функцию можно с помощью следующих команд (обратите внимание на то, что команда faas-cli remove удаляет текущую версию функции):

$ faas-cli build -f ./hello-python.yml
$ faas-cli push -f ./hello-python.yml
$ faas-cli remove -f ./hello-python.yml
$ faas-cli deploy -f ./hello-python.yml

Проверим работу развернутой функции с помощью curl:

$ curl localhost:8080/function/hello-python --data-binary 'hello'
Handling connection for 8080
{
    "body": {
        "message": "Received a hello at 22:55:05.225295"
    },
    "statusCode": 200
}

Проверяем еще и непосредственным вызовом нашей функции с помощью faas-cli:

$ echo -n "hello" | faas-cli invoke hello-python
Handling connection for 8080
{
    "body": {
        "message": "Received a hello at 22:56:23.549509"
    },
    "statusCode": 200
}