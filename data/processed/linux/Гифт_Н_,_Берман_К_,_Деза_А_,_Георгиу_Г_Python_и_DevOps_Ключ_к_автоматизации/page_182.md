---
source_image: page_182.png
page_number: 182
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.57
tokens: 7382
characters: 1580
timestamp: 2025-12-24T03:05:34.324674
finish_reason: stop
---

Мы воспользуемся маленьким сервером HTTP API, в основе которого лежит веб-фреймворк Pecan (https://www.pecanpy.org/).

Ничего связанного конкретно с Pecan в этом разделе нет, так что примеры подходят и для других фреймворков или долгоживущих процессов.

Настройка

Выберем постоянное месторасположение по адресу /opt/http для создания каталога проекта, после чего создадим новую виртуальную среду и устанавливаем фреймворк Pecan:

$ mkdir -p /opt/http
$ cd /opt/http
$ python3 -m venv .
$ source bin/activate
(http) $ pip install "pecan==1.3.3"

У Pecan есть встроенные вспомогательные функции для создания необходимых файлов и каталогов для нашего примера проекта. С помощью Pecan можно создать простейший базовый проект API HTTP, способный привязываться к systemd. У версии 1.3.3 есть две опции — base и rest-api:

$ pecan create api rest-api
Creating /opt/http/api
Recursing into +package+
    Creating /opt/http/api/api
...
Copying scaffolds/rest-api/config.py_tmpl to /opt/http/api/config.py
Copying scaffolds/rest-api/setup.cfg_tmpl to /opt/http/api/setup.cfg
Copying scaffolds/rest-api/setup.py_tmpl to /opt/http/api/setup.py

Важно использовать один и тот же путь, поскольку в дальнейшем он будет применяться при настройке сервиса с помощью systemd.

Благодаря включению туда скаффолдинга проекта мы без всяких усилий получаем полнофункциональный проект. Он даже содержит файл setup.py со всем необходимым, готовый к созданию нативного пакета Python! Установим проект¹, чтобы можно было его запустить:

¹ Перед этим необходимо перейти в каталог api:cd api/. — Примеч. пер.