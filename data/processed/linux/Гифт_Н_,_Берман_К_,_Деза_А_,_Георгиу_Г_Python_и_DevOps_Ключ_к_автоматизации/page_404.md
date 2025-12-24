---
source_image: page_404.png
page_number: 404
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.57
tokens: 7339
characters: 1497
timestamp: 2025-12-24T03:11:27.953210
finish_reason: stop
---

Создайте учетную запись Microsoft Azure и установите среду выполнения Microsoft Azure для своей операционной системы в соответствии с официальной документацией Microsoft (https://oreil.ly/GHS4c). Если вы работаете на macOS, воспользуйтесь brew:

$ brew tap azure/functions
$ brew install azure-functions-core-tools
Создайте новый каталог для кода функции Python:
$ mkdir azure-functions-python
$ cd azure-functions-python

Установите Python 3.6, поскольку Azure Functions не поддерживают версию 3.7¹. Создайте и активируйте виртуальную среду:

$ brew unlink python
$ brew install \
https://raw.githubusercontent.com/Homebrew/homebrew-core/
f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb \
--ignore-dependencies

$ python3 -V
Python 3.6.5

$ python3 -m venv .venv
$ source .venv/bin/activate

С помощью утилиты func Azure создайте локальный проект функции Azure с названием python-simple-http-endpoint:

$ func init python-simple-http-endpoint
Select a worker runtime:
1. dotnet
2. node
3. python
4. powershell (preview)
Choose option: 3

Перейдите в только что созданный каталог python-simple-http-endpoint и создайте Azure HTTP Trigger Function с помощью команды func new:

$ cd python-simple-http-endpoint
$ func new
Select a template:
1. Azure Blob Storage trigger
2. Azure Cosmos DB trigger
3. Azure Event Grid trigger

¹ На момент выпуска русскоязычного издания этой книги Azure Functions поддерживали Python вплоть до версии 3.9 (официальные дистрибутивы CPython). — Примеч. пер.