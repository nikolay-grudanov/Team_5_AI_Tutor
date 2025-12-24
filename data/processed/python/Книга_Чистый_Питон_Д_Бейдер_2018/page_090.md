---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.37
tokens: 7292
characters: 1280
timestamp: 2025-12-24T02:29:24.517096
finish_reason: stop
---

Например, оригинальное имя функции, ее строка документации docstring и список параметров скрыты замыканием-оберткой:

def greet():
    """Вернуть дружеское приветствие."""
    return 'Привет!'

decorated_greet = uppercase(greet)

При попытке получить доступ к каким-либо из этих метаданных функции вместо них вы увидите метаданные замыкания-обертки:

>>> greet.__name__
'greet'
>>> greet.__doc__
'Вернуть дружеское приветствие.'

>>> decorated_greet.__name__
'wrapper'
>>> decorated_greet.__doc__
None

Это делает отладку и работу с интерпретатором Python неуклюжей и трудоемкой. К счастью, существует быстрое решение этой проблемы: декоратор functools.wraps, включенный в стандартную библиотеку Python¹.

Декоратор functools.wraps можно использовать в своих собственных декораторах для того, чтобы копировать потерянные метаданные из не-декорированной функции в замыкание декоратора. Вот пример:

import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper():
        return func().upper()
    return wrapper

Применение декоратора functools.wraps к замыканию-обертке, возвращаемому декоратором, переносит в него строку документации и другие метаданные входной функции:

¹ См. документацию Python «functools»: https://docs.python.org/3/library/functools.html