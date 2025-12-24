---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.92
tokens: 7330
characters: 1652
timestamp: 2025-12-24T03:03:30.826028
finish_reason: stop
---

def list_ships():
    ships = ['John B', 'Yankee Clipper', 'Pequod']
    print(f"Ships: {','.join(ships)}")

def greet(greeting, name):
    message = f'{greeting} {name}'
    print(message)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Maritime control') ①

    parser.add_argument('--twice', '-t', ②
                        help='Do it twice',
                        action='store_true')

    subparsers = parser.add_subparsers(dest='func') ③

    ship_parser = subparsers.add_parser('ships', ④
                                        help='Ship related commands')
    ship_parser.add_argument('command', ⑤
                            choices=['list', 'sail'])

    sailor_parser = subparsers.add_parser('sailors', ⑥
                                        help='Talk to a sailor')
    sailor_parser.add_argument('name', ⑦
                            help='Sailors name')
    sailor_parser.add_argument('--greeting', '-g',
                            help='Greeting',
                            default='Ahoy there')

    args = parser.parse_args()
    if args.func == 'sailors': ⑧
        greet(args.greeting, args.name)
    elif args.command == 'list':
        list_ships()
    else:
        sail()

① Создаем синтаксический анализатор верхнего уровня.

② Добавляем аргумент верхнего уровня, который можно использовать с любыми командами из иерархии этого синтаксического анализатора.

③ Создаем объект для субанализаторов. Для выбора субанализатора служит атрибут dest.

④ Добавляем субанализатор для ships.

⑤ Добавляем команду в субанализатор ships. Список возможных вариантов подкоманд выводит параметр choices.