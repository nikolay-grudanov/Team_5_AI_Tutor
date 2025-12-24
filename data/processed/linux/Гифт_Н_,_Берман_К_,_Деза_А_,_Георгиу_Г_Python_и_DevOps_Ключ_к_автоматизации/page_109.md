---
source_image: page_109.png
page_number: 109
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.25
tokens: 7318
characters: 1532
timestamp: 2025-12-24T03:03:45.469199
finish_reason: stop
---

3 Создаем группу для команд ships.

4 Добавляем в группу верхнего уровня группу ships в качестве команды. Обратите внимание на то, что функция cli теперь представляет собой группу с методом add_command.

5 Добавляем команду в группу ships. Обратите внимание на то, что вместо click.command мы используем ships.command.

6 Добавляем команду в группу cli.

7 Вызываем группу верхнего уровня.

Справочные сообщения верхнего уровня, сгенерированные click, выглядят так:

./click_example.py --help
Usage: click_example.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help    Show this message and exit.

Commands:
  sailors   Talk to a sailor
  ships     Ship related commands

А вот так можно посмотреть справку для подгруппы:

$ ./click_example.py ships --help
Usage: click_example.py ships [OPTIONS] COMMAND [ARGS]...

  Ship related commands

Options:
  --help    Show this message and exit.

Commands:
  list-ships  List all of the ships
  sail        Sail a ship

Если сравнить примеры 3.4 и 3.5, можно заметить различия между argparse и click. Подход click определенно требует меньшего объема кода — почти в два раза. Код пользовательского интерфейса (UI) разбросан по всей программе, что особенно важно при создании функций, работающих исключительно в качестве групп. В сложной программе с запутанным интерфейсом следует стремиться как можно сильнее изолировать различную функциональность, упрощая тем самым тестирование и отладку отдельных ее частей. В подобном случае имеет смысл применять argparse, чтобы отделить код интерфейса.