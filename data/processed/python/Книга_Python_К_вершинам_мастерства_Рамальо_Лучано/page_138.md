---
source_image: page_138.png
page_number: 138
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.91
tokens: 11717
characters: 1719
timestamp: 2025-12-24T01:40:56.956427
finish_reason: stop
---

sys.getfilesystemencoding()
"""
my_file = open('dummy', 'w')
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

Этот скрипт выводит одно и то же в GNU/Linux (Ubuntu 14.04) и OS X (Mavericks 10.9), показывая, что в обоих случаях всюду используется кодировка UTF-8:

$ python3 default_encodings.py
locale.getpreferredencoding() -> 'UTF-8'
    type(my_file) -> <class '_io.TextIOWrapper'>
    my_file.encoding -> 'UTF-8'
    sys.stdout.isatty() -> True
    sys.stdout.encoding -> 'UTF-8'
    sys.stdin.isatty() -> True
    sys.stdin.encoding -> 'UTF-8'
    sys.stderr.isatty() -> True
    sys.stderr.encoding -> 'UTF-8'
    sys.getdefaultencoding() -> 'utf-8'
    sys.getfilesystemencoding() -> 'utf-8'

Однако в Windows выводится нечто совершенно иное (см. пример 4.12).

Пример 4.12. Кодировки по умолчанию в оболочке Windows 7 (SP 1) cmd.exe, локализованной для Бразилии; PowerShell дает такой же результат

Z:\>chcp ①
Pagina de codigo ativa: 850
Z:\>python default_encodings.py ②
locale.getpreferredencoding() -> 'cp1252' ③
    type(my_file) -> <class '_io.TextIOWrapper'>
    my_file.encoding -> 'cp1252' ④
    sys.stdout.isatty() -> True ⑤
    sys.stdout.encoding -> 'cp850' ⑥
    sys.stdin.isatty() -> True
    sys.stdin.encoding -> 'cp850'
    sys.stderr.isatty() -> True
    sys.stderr.encoding -> 'cp850'
    sys.getdefaultencoding() -> 'utf-8'
    sys.getfilesystemencoding() -> 'mbcs'

① chcp показывает активную кодовую страницу для консоли: 850.
② При запуске default_encodings.py с выводом на консоль.
③ locale.getpreferredencoding() — самый важный параметр.
④ Для текстовых файлов по умолчанию используется locale.getpreferredencoding().