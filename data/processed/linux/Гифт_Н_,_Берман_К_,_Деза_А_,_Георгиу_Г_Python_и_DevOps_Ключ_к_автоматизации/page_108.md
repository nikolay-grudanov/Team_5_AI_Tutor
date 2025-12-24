---
source_image: page_108.png
page_number: 108
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.39
tokens: 7290
characters: 1275
timestamp: 2025-12-24T03:03:32.775187
finish_reason: stop
---

Теперь рассмотрим более сложный пример с вложенными командами. Вложение команд производится с помощью декоратора click.group, служащего для создания функций, представляющих группы. Для вложения команд в примере 3.5 мы используем пакет click с интерфейсом, очень похожим на интерфейс из примера 3.4.

Пример 3.5. click_example.py

#!/usr/bin/env python
"""
Утилита командной строки, использующая click
"""
import click

@click.group() ①
def cli(): ②
    pass

@click.group(help='Ship related commands') ③
def ships():
    pass

cli.add_command(ships) ④

@ships.command(help='Sail a ship') ⑤
def sail():
    ship_name = 'Your ship'
    print(f"{ship_name} is setting sail")

@ships.command(help='List all of the ships')
def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

@cli.command(help='Talk to a sailor') ⑥
@click.option('--greeting', default='Ahoy there', help='Greeting for sailor')
@click.argument('name')
def sailors(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    cli() ⑦

① Создаем группу верхнего уровня для прочих групп и команд.

② Создаем функцию, которая будет выступать в роли группы верхнего уровня. Метод click.group преобразует функцию в группу.