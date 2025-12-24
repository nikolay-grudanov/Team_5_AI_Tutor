---
source_image: page_113.png
page_number: 113
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.08
tokens: 7172
characters: 1041
timestamp: 2025-12-24T03:03:41.478613
finish_reason: stop
---

1 Описываем класс для команд ships.

2 У sailors подкоманд нет, так что ее можно описать в виде функции.

3 Описываем класс, который будет играть роль группы верхнего уровня. Добавляем в качестве атрибутов этого класса функцию sailors и класс Ships.

4 Вызываем метод fire.Fire, передавая ему класс, который будет играть роль группы верхнего уровня.

В автоматически сгенерированной документации верхнего уровня класс Ships описан как группа, а команда sailors — как команда:

$ ./fire_example.py

NAME
    fire_example.py

SYNOPSIS
    fire_example.py GROUP | COMMAND

GROUPS
    GROUP is one of the following:

        ships

COMMANDS
    COMMAND is one of the following:

        sailors
(END)

В справке по группе ships показаны команды, соответствующие методам класса Ships:

$ ./fire_example.py ships --help
INFO: Showing help with the command 'fire_example.py ships -- --help'.

NAME
    fire_example.py ships

SYNOPSIS
    fire_example.py ships COMMAND

COMMANDS
    COMMAND is one of the following:

        list

        sail
(END)