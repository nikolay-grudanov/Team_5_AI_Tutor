---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.38
tokens: 8168
characters: 572
timestamp: 2025-12-24T02:17:29.942838
finish_reason: stop
---

Рисунок 4.1 – Макет нашего шаблона домашней страницы

1. Во-первых, давайте установим пакет Jinja и создадим папку templates:

    (venv) $ pip install jinja2
    (venv) $ mkdir templates

2. Во вновь созданной папке создайте два новых файла, home.html и todo.html:

    (venv) $ cd templates
    (venv) $ touch {home,todo}.html

В предыдущем командном блоке мы создали два файла шаблона:
▪ home.html для главной страницы приложения
▪ todo.html для страницы задач

В макете на Рисунке 4.1, внутреннее поле обозначает шаблон todo, а большее поле — шаблон домашней страницы.