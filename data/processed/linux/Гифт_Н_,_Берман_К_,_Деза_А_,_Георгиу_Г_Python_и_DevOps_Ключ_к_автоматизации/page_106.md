---
source_image: page_106.png
page_number: 106
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.95
tokens: 7427
characters: 1766
timestamp: 2025-12-24T03:03:45.063505
finish_reason: stop
---

click

Пакет click изначально предназначался для работы с веб-фреймворком flask. Для привязки интерфейса командной строки непосредственно к вашим функциям в нем применяются *функции-декораторы* (function decorators). В отличие от пакета argparse, click переплетает интерфейсные решения с остальными частями кода.

**ФУНКЦИИ-ДЕКОРАТОРЫ**

Функции языка Python являются объектами, так что любая из них может принимать в качестве аргументов другие функции. Синтаксис декоратора — простой и аккуратный способ сделать это. Простейший формат декоратора:

In [2]: def some_decorator(wrapped_function):
   ...:     def wrapper():
   ...:         print('Do something before calling wrapped function')
   ...:         wrapped_function()
   ...:         print('Do something after calling wrapped function')
   ...:     return wrapper
   ...:

Мы можем описать другую функцию и передать ее как аргумент этой функции:

In [3]: def foobat():
   ...:     print('foobat')
   ...:
In [4]: f = some_decorator(foobat)
In [5]: f()
Do something before calling wrapped function
foobat
Do something after calling wrapped function

Синтаксис декоратора упрощает эту задачу, позволяя указать обертываемую функцию посредством *декорирования* ее аннотацией @название_декоратора. Вот пример использования синтаксиса декоратора для функции some_decorator:

In [6]: @some_decorator
   ...: def batfoo():
   ...:     print('batfoo')
   ...:
In [7]: batfoo()
Do something before calling wrapped function
batfoo
Do something after calling wrapped function

Теперь можно вызывать обернутую функцию по ее имени, а не по имени декоратора. Готовые функции-декораторы включены в состав как стандартной библиотеки языка Python (staticMethod, classMethod), так и сторонних пакетов, таких как Flask и Click.