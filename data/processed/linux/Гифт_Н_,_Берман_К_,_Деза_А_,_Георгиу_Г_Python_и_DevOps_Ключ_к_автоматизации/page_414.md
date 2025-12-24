---
source_image: page_414.png
page_number: 414
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.95
tokens: 7404
characters: 1691
timestamp: 2025-12-24T03:11:44.228625
finish_reason: stop
---

Помещаем образ в Docker Hub с помощью команды faas-cli push:

$ faas-cli push -f ./hello-python.yml
[0] > Pushing hello-python [griggheo/hello-python:latest].
The push refers to repository [docker.io/griggheo/hello-python]
latest: digest:
sha256:27e1fbb7f68bb920a6ff8d3baf1fa3599ae92e0b3c607daac3f8e276aa7f3ae3
size: 4074
[0] < Pushing hello-python [griggheo/hello-python:latest] done.
[0] worker done.

Выполняем развертывание функции OpenFaaS на Python в удаленном кластере k3s с помощью команды faas-cli deploy:

$ faas-cli deploy -f ./hello-python.yml
Deploying: hello-python.
WARNING! Communication is not secure, please consider using HTTPS.
Letsencrypt.org offers free SSL/TLS certificates.
Handling connection for 8080

unauthorized access, run "faas-cli login"
to setup authentication for this server

Function 'hello-python' failed to deploy with status code: 401

Получаем учетные данные аутентификации с помощью команды faas-cli login:

$ echo -n $PASSWORD | faas-cli login -g http://localhost:8080 \
-u admin --password-stdin
Calling the OpenFaaS server to validate the credentials...
Handling connection for 8080
WARNING! Communication is not secure, please consider using HTTPS.
Letsencrypt.org offers free SSL/TLS certificates.
credentials saved for admin http://localhost:8080

Вносим следующие изменения в файл hello-python.yml:

gateway: http://localhost:8080

Поскольку наш обработчик возвращает JSON, добавьте в файл hello-python.yml следующие строки кода:

    environment:
        content_type: application/json

Содержимое файла hello-python.yml теперь выглядит так:

$ cat hello-python.yml
version: 1.0
provider:
    name: openfaas
    gateway: http://localhost:8080