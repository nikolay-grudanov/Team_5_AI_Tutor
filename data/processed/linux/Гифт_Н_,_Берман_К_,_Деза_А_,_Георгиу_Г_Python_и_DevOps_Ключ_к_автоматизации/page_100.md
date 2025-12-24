---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.39
tokens: 7413
characters: 1725
timestamp: 2025-12-24T03:03:34.248456
finish_reason: stop
---

Пример 3.2. Синтаксический разбор с использованием sys.argv

#!/usr/bin/env python
"""
Простая утилита командной строки, использующая sys.argv
"""
import sys

def say_it(greeting, target):
    message = f'{greeting} {target}'
    print(message)

if __name__ == '__main__':
    greeting = 'Hello'  # В этих двух строках задаются значения по умолчанию.
    target = 'Joe'

    if '--help' in sys.argv:
        help_message = f"Usage: {sys.argv[0]} --name <NAME> --greeting <GREETING>"
        print(help_message)
        sys.exit()  # Выход из программы после вывода справки.

    if '--name' in sys.argv:
        # Выясняем позицию значения, следующего за флагом name
        name_index = sys.argv.index('--name') + 1  # Нам нужно знать позицию значения, следующего за флагом, к которому оно должно относиться.
        if name_index < len(sys.argv):
            name = sys.argv[name_index]

    if '--greeting' in sys.argv:
        # Выясняем позицию значения, следующего за флагом greeting
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    say_it(greeting, name)  # Вызываем функцию с указанными в аргументах значениями.

① Проверяем, запущен ли сценарий из командной строки.

② В этих двух строках задаются значения по умолчанию.

③ Проверяем, присутствует ли в списке аргументов строковое значение --help.

④ Выход из программы после вывода справки.

⑤ Нам нужно знать позицию значения, следующего за флагом, к которому оно должно относиться.

⑥ Проверяем, достаточно ли длинный список аргументов. Если нет, значит, не было указано значение для какого-то флага.

⑦ Вызываем функцию с указанными в аргументах значениями.