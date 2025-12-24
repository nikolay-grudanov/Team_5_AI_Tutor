---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.31
tokens: 7361
characters: 1609
timestamp: 2025-12-24T03:03:13.443524
finish_reason: stop
---

config_path = os.path.join(parent_path, rc_name)
print(f"Checking {config_path}")
if os.path.exists(config_path):
    return config_path

print(f"File {rc_name} has not been found")

① Проверяем, существует ли такая переменная в активной среде.

② Формируем путь с указанием названия переменной среды. Он будет выглядеть примерно так: $EXAMPLERC_DIR/.examplerc.

③ Дополняем переменную среды для вставки ее значения в формируемый путь.

④ Проверяем, существует ли такой файл.

⑤ Формируем путь на основе рабочего каталога.

⑥ Получаем путь к домашнему каталогу пользователя с помощью функции expanduser.

⑦ Дополняем хранящийся в file относительный путь до абсолютного.

⑧ Получаем путь к содержащему текущий файл каталогу с помощью dirname.

Подмодуль path также позволяет получить характеристики пути. С его помощью можно выяснить, чем является путь — файлом, каталогом, ссылкой или точкой монтирования. Можно также узнать такие его характеристики, как размер и время последнего обращения/изменения. В примере 2.3 мы выполним с помощью path обход дерева каталогов и выведем информацию о размере и последнем времени доступа ко всем содержащимся в них файлам.

Пример 2.3. os_path_walk.py
#!/usr/bin/env python

import fire
import os

def walk_path(parent_path):
    print(f"Checking: {parent_path}")
    childs = os.listdir(parent_path) ①

    for child in childs:
        child_path = os.path.join(parent_path, child) ②
        if os.path.isfile(child_path): ③
            last_access = os.path.getatime(child_path) ④
            size = os.path.getsize(child_path) ⑤
            print(f"File: {child_path}")