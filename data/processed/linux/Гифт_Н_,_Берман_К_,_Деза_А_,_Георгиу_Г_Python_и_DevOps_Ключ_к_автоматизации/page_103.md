---
source_image: page_103.png
page_number: 103
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.74
tokens: 7318
characters: 1421
timestamp: 2025-12-24T03:03:30.596434
finish_reason: stop
---

6 Обращается к значениям аргументов по названиям. -- из названия необязательного аргумента убрано.

Если запустить эту программу с флагом --twice, введенное сообщение будет повторено дважды:

$ ./simple_parse.py hello --twice
hello
hello

Пакет argparse автоматически выдает справочные сообщения в зависимости от указанных вами справки и описаний:

$ ./simple_parse.py --help
usage: simple_parse.py [-h] [--twice] message

Echo your input

positional arguments:
    message      Message to echo

optional arguments:
    -h, --help   show this help message and exit
    --twice, -t  Do it twice

Во многих утилитах командной строки используется несколько уровней команд для группировки команд по контролируемым сферам. Возьмем для примера git. В нем есть команды верхнего уровня, например git stash, у которых есть отдельные подкоманды, например git stash pop. С помощью пакета argparse можно создавать подкоманды путем создания субанализаторов главного синтаксического анализатора. С их помощью можно создать иерархию команд. В примере 3.4 мы реализуем приложение для судоходства с командами для кораблей и моряков. К главному синтаксическому анализатору добавили два субанализатора, каждый со своими командами.

Пример 3.4. argparse_example.py

#!/usr/bin/env python
"""
Утилита командной строки, использующая argparse
"""
import argparse
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")