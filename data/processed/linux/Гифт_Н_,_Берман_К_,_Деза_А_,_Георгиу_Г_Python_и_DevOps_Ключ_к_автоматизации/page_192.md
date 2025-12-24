---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.82
tokens: 7268
characters: 1350
timestamp: 2025-12-24T03:05:52.828226
finish_reason: stop
---

Осталось только инициализировать каркас приложения Hugo и установить тему:

hugo new site quickstart

Эта команда создает новый сайт quickstart. Можно произвести его повторную сборку, очень быстро выполнив команду hugo, которая компилирует файлы в формате Markdown в HTML и CSS.

Преобразование WordPress в посты Hugo

Далее я преобразовал базу данных WordPress в формат JSON через неформатированный дамп. Затем написал сценарий Python для преобразования этих данных в посты Hugo в формате Markdown. Вот его код:

"""Код преобразования полей старой базы данных в формат Markdown

Если вы выполнили дамп базы данных WordPress и затем преобразовали его в JSON, можете приспособить этот код под свои нужды"""

import os
import shutil
from category import CAT
from new_picture_products import PICTURES

def check_all_category():
    ares = {}
    REC = []
    for pic in PICTURES:
        res = check_category(pic)
        if not res:
            pic["categories"] = "Other"
            REC.append(pic)
            continue

        title, key = res
        if key:
            print("FOUND MATCH: TITLE--[%s], CATEGORY--[%s]" %\n    (title, key))
            ares[title] = key
            pic["categories"] = key
            REC.append(pic)
    return ares, REC

def check_category(rec):
    title = str(rec['title'])
    for key, values in CAT.items():