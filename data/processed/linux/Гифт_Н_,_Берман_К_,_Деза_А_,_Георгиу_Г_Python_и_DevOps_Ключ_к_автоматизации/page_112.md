---
source_image: page_112.png
page_number: 112
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.73
tokens: 7293
characters: 1268
timestamp: 2025-12-24T03:03:48.764525
finish_reason: stop
---

fire
    The Python fire module.

COMMANDS
    COMMAND is one of the following:

        greet

        goodbye
(END)

Это очень удобно, если нужно разобраться в чужом коде или отладить свой. Одной дополнительной строки кода достаточно, чтобы получить возможность работать со всеми функциями модуля из командной строки. Весьма впечатляюще. Поскольку библиотека fire определяет интерфейс на основе структуры самой программы, то она сильнее связана с не относящимся к интерфейсу кодом, чем argparse или click. Для моделирования интерфейса с вложенными командами необходимо описать классы, отражающие структуру требуемого интерфейса. Пример 3.6 иллюстрирует подобный подход.

Пример 3.6. fire_example.py
#!/usr/bin/env python
"""
Утилита командной строки, использующая библиотеку fire
"""
import fire

class Ships(): ①
    def sail(self):
        ship_name = 'Your ship'
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {','.join(ships)}")

def sailors(greeting, name): ②
    message = f'{greeting} {name}'
    print(message)

class Cli(): ③

    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()

if __name__ == '__main__': ④
    fire.Fire(Cli)