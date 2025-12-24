---
source_image: page_084.png
page_number: 84
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.62
tokens: 8240
characters: 913
timestamp: 2025-12-24T02:18:00.515448
finish_reason: stop
---

Технические требования

Код, использованный в этой главе, можно найти по адресу https://github.com/PacktPublishing/Building-Python-Web-APIs-with-FastAPI/tree/main/ch05/planner.

Структурирование в приложениях FastAPI

В этой главе мы создадим планировщик событий. Давайте разработаем структуру приложения, чтобы она выглядела так:

planner/
    main.py
    database/
        __init__.py
        connection.py
    routes/
        __init__.py
        events.py
        users.py
    models/
        __init__.py
        events.py
        users.py

Первый шаг — создать новую папку для приложения. Он будет называться планировщик:

$ mkdir planner && cd planner

Во вновь созданной папке планировщика, создайте файл ввода, main.py, и три подпапки
– database, routes, and models:

$ touch main.py
$ mkdir database routes models

Затем создайте __init__.py в каждой папке:

$ touch {database, routes, models}/__init__.py