---
source_image: page_107.png
page_number: 107
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.54
tokens: 7372
characters: 1715
timestamp: 2025-12-24T03:03:41.031565
finish_reason: stop
---

Это значит, что можно привязывать флаги и опции непосредственно к параметрам соответствующих функций. Указав функции command и option библиотеки click перед своей функцией в качестве декораторов, можно сделать из нее простую утилиту командной строки:

#!/usr/bin/env python
"""
Простой пример использования библиотеки Click
"""
import click

@click.command()
@click.option('--greeting', default='Hiya', help='How do you want to greet?')
@click.option('--name', default='Tammy', help='Who do you want to greet?')
def greet(greeting, name):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    greet()

Декоратор click.command указывает, что функция должна быть доступна для вызова из командной строки. Декоратор click.option служит для добавления аргумента командной строки с автоматической привязкой его к параметру функции с соответствующим именем (--greeting к greet, --name к name). Библиотека click выполняет часть работы «за кулисами», благодаря чему мы можем вызывать метод greet в блоке main без указания параметров, уже охваченных декораторами option.

Эти декораторы производят синтаксический разбор аргументов командной строки и автоматически выдают справочные сообщения:

$ ./simple_click.py --greeting Privet --name Peggy
Privet Peggy

$ ./simple_click.py --help
Usage: simple_click.py [OPTIONS]

Options:
  --greeting TEXT    How do you want to greet?
  --name TEXT        Who do you want to greet?
  --help             Show this message and exit.

Как видите, благодаря библиотеке click для применения функции в командной строке требуется гораздо меньше кода, чем при использовании argparse. Это позволяет разработчику сосредоточиться на бизнес-логике кода вместо проектирования интерфейса.