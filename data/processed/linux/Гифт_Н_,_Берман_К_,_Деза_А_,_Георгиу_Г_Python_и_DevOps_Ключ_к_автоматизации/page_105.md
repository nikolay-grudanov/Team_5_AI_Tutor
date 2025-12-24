---
source_image: page_105.png
page_number: 105
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.93
tokens: 7348
characters: 1513
timestamp: 2025-12-24T03:03:31.908539
finish_reason: stop
---

6 Добавляем субанализатор для sailors.

7 Добавляем обязательный позиционно зависимый аргумент в субанализатор sailors.

8 Проверяем, какой субанализатор используется, по значению func.

В примере 3.4 есть один необязательный аргумент верхнего уровня (twice) и два субанализатора, каждый со своими командами и флагами. Пакет argparse автоматически создает иерархию справочных сообщений и отображает их при использовании флага --help.

Команды верхнего уровня, включая субанализаторы и аргумент верхнего уровня twice, снабжены документацией:

$ ./argparse_example.py --help
usage: argparse_example.py [-h] [--twice] {ships,sailors} ...

Maritime control

positional arguments:
  {ships,sailors}
    ships      Ship related commands
    sailors    Talk to a sailor

optional arguments:
  -h, --help    show this help message and exit
  --twice, -t   Do it twice

Можно узнать больше о подкомандах (субанализаторах), указав флаг help после соответствующей команды:

$ ./argparse_example.py ships --help
usage: argparse_example.py ships [-h] {list,sail}

positional arguments:
  {list,sail}

optional arguments:
  -h, --help    show this help message and exit

Как видите, пакет argparse предоставляет широкие возможности управления интерфейсом утилиты командной строки. При желании можно создать специально подогнанный под конкретную архитектуру многоуровневый интерфейс со встроенной документацией и множеством опций. Впрочем, это потребовало бы немалых усилий, так что взглянем на некоторые более простые варианты.