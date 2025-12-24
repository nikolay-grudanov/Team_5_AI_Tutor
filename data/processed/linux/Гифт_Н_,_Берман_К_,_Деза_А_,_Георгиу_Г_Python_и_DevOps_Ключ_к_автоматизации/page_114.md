---
source_image: page_114.png
page_number: 114
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.43
tokens: 7349
characters: 1610
timestamp: 2025-12-24T03:03:52.196341
finish_reason: stop
---

Параметры функции sailors превратились в позиционно зависимые аргументы:

$ ./fire_example.py sailors --help
INFO: Showing help with the command 'fire_example.py sailors -- --help'.

NAME
    fire_example.py sailors

SYNOPSIS
    fire_example.py sailors GREETING NAME

POSITIONAL ARGUMENTS
    GREETING
    NAME

NOTES
    You can also use flags syntax for POSITIONAL ARGUMENTS (END)

Как и ожидалось, теперь можно вызывать команды и подкоманды:

$ ./fire_example.py ships sail
Your ship is setting sail
$ ./fire_example.py ships list
Ships: John B,Yankee Clipper,Pequod
$ ./fire_example.py sailors Hiya Karl
Hiya Karl

Замечательная возможность fire — легкий переход в интерактивный режим. Если использован флаг --interactive, fire открывает командную оболочку IPython, в которой доступны объект и функции из вашего сценария:

$ ./fire_example.py sailors Hiya Karl -- --interactive
Hiya Karl
Fire is starting a Python REPL with the following objects:
Modules: fire
Objects: Cli, Ships, component, fire_example.py, result, sailors, self, trace

Python 3.7.0 (default, Sep 23 2018, 09:47:03)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.5.0 -- An enhanced Interactive Python. Type '?' for help.
------------------------------------------------------------
In [1]: sailors
Out[1]: <function __main__.sailors(greeting, name)>

In [2]: sailors('hello', 'fred')
hello fred

Здесь мы запускаем команду sailors нашей программы для судоходства в интерактивном режиме. Открывается командная оболочка IPython, в которой у вас есть доступ к функции sailors. Этот интерактивный режим в сочетании