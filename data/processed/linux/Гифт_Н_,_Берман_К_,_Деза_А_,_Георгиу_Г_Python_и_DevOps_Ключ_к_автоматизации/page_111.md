---
source_image: page_111.png
page_number: 111
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.62
tokens: 7196
characters: 1020
timestamp: 2025-12-24T03:03:38.248344
finish_reason: stop
---

def greet(greeting='Hiya', name='Tammy'):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    fire.Fire(greet)

Далее библиотека fire создает UI на основе названия и аргументов метода:

$ ./simple_fire.py --help

NAME
    simple_fire.py

SYNOPSIS
    simple_fire.py <flags>

FLAGS
    --greeting=GREETING
    --name=NAME

В простых случаях можно автоматически сделать доступными в командной строке несколько методов путем вызова fire без аргументов:

#!/usr/bin/env python
"""
Простой пример использования fire
"""
import fire

def greet(greeting='Hiya', name='Tammy'):
    print(f"{greeting} {name}")

def goodbye(goodbye='Bye', name='Tammy'):
    print(f"{goodbye} {name}")

if __name__ == '__main__':
    fire.Fire()

fire автоматически делает из каждой функции команду и создает документацию для нее:

$ ./simple_fire.py --help
INFO: Showing help with the command 'simple_fire.py -- --help'.

NAME
    simple_fire.py

SYNOPSIS
    simple_fire.py GROUP | COMMAND

GROUPS
    GROUP is one of the following: