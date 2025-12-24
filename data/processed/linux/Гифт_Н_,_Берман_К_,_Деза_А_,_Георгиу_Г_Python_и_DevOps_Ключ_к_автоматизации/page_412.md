---
source_image: page_412.png
page_number: 412
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.67
tokens: 7353
characters: 1354
timestamp: 2025-12-24T03:11:41.206044
finish_reason: stop
---

Зайдите в браузере на веб-UI OpenFaaS по адресу http://localhost:8080/ и войдите в систему с именем пользователя admin и паролем $PASSWORD.

Далее мы создаем функцию OpenFaaS на Python. Для создания новой функции OpenFaaS hello-python задействуем утилиту faas-cli:

$ faas-cli new --lang python hello-python
Folder: hello-python created.
Function created in folder: hello-python
Stack file written: hello-python.yml

Заглянем в файл конфигурации функции hello-python:

$ cat hello-python.yml
version: 1.0
provider:
  name: openfaas
  gateway: http://127.0.0.1:8080
functions:
  hello-python:
    lang: python
    handler: ./hello-python
    image: hello-python:latest

Смотрим на содержимое автоматически созданного каталога hello-python:

$ ls -la hello-python
total 8
drwx------ 4 ggheo staff 128 Aug 24 15:16 .
drwxr-xr-x 8 ggheo staff 256 Aug 24 15:16 ..
-rw-r--r-- 1 ggheo staff 123 Aug 24 15:16 handler.py
-rw-r--r-- 1 ggheo staff 0 Aug 24 15:16 requirements.txt

$ cat hello-python/handler.py
def handle(req):
    """Обрабатывает запрос к функции
    Args:
        req (str): тело запроса
    """
    return req

Отредактируем файл handler.py, слегка изменив код, выводящий текущее время, из simple-http-example платформы Serverless:

$ cat hello-python/handler.py
import json
import datetime

def handle(req):
    """Обрабатывает запрос к функции