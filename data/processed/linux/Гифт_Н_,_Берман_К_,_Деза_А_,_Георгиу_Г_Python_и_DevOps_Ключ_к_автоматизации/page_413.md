---
source_image: page_413.png
page_number: 413
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.79
tokens: 7304
characters: 1368
timestamp: 2025-12-24T03:11:38.330994
finish_reason: stop
---

Args:
    req (str): тело запроса
"""

current_time = datetime.datetime.now().time()
body = {
    "message": "Received a {} at {}".format(req, str(current_time))
}

response = {
    "statusCode": 200,
    "body": body
}
return json.dumps(response, indent=4)

Следующий шаг — сборка Python-функции OpenFaaS. Выполним сборку образа Docker на основе сгенерированного автоматически Dockerfile с помощью команды сборки faas-cli:

$ faas-cli build -f ./hello-python.yml
[0] > Building hello-python.
Clearing temporary build folder: ./build/hello-python/
Preparing ./hello-python/ ./build/hello-python//function
Building: hello-python:latest with python template. Please wait..
Sending build context to Docker daemon 8.192kB
Step 1/29 : FROM openfaas/classic-watchdog:0.15.4 as watchdog

ВЫВОД КОМАНДЫ СБОРКИ DOCKER ОПУЩЕН

Successfully tagged hello-python:latest
Image: hello-python:latest built.
[0] < Building hello-python done.
[0] worker done.

Проверяем, появился ли на локальной машине образ Docker:

$ docker images | grep hello-python
hello-python        latest
05b2c37407e1   29 seconds ago   75.5MB

Помечаем полученный образ Docker тегом и помещаем в реестр Docker Hub для использования на удаленном кластере Kubernetes:

$ docker tag hello-python:latest griggheo/hello-python:latest

Вносим изменения в файл hello-python.yml:

image: griggheo/hello-python:latest