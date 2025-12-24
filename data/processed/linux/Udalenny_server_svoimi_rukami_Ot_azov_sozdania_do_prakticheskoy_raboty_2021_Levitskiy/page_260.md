---
source_image: page_260.png
page_number: 260
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.12
tokens: 6174
characters: 585
timestamp: 2025-12-24T04:01:44.382409
finish_reason: stop
---

Внимательные читатели заметили два факта. Первый — какая версия 7.0 будет установлена в Ubuntu по умолчанию? Ведь нужна версия 7.0.13 или более новая? Все в порядке, по умолчанию на данный момент устанавливается версия 7.0.32. Узнать версию можно командой:

php -v

![Скриншот терминала с выводом информации о версии PHP](../images/chapter15_02.png)

Рис. 15.2. Версия PHP

Что делать, если вам нужна версия 7.2, но ее нет в вашем дистрибутиве? Тогда введите следующие команды:

sudo apt-get install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update