---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.12
tokens: 7519
characters: 1550
timestamp: 2025-12-24T02:42:12.855092
finish_reason: stop
---

In [216]: gen = (x ** 2 for x in range(100))

In [217]: gen
Out[217]: <generator object <genexpr> at 0x7fefe437d000>

Это в точности эквивалентно следующему более многословному определению генератора:

def _make_gen():
    for x in range(100):
        yield x ** 2
gen = _make_gen()

В некоторых случаях генераторные выражения можно передавать функциям вместо списковых включений:

In [218]: sum(x ** 2 for x in range(100))
Out[218]: 328350

In [219]: dict((i, i ** 2) for i in range(5))
Out[219]: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

В зависимости от того, сколько элементов порождает списковое включение, версия с генератором может оказаться заметно быстрее.

Модуль itertools
Стандартный библиотечный модуль itertools содержит набор генераторов для многих общеупотребительных алгоритмов. Так, генератор groupby принимает произвольную последовательность и функцию и группирует соседние элементы последовательности по значению, возвращенному функцией, например:

In [220]: import itertools

In [221]: def first_letter(x):
    return x[0]

In [222]: names = ["Alan", "Adam", "Wes", "Will", "Albert", "Steven"]

In [223]: for letter, names in itertools.groupby(names, first_letter):
    print(letter, list(names)) # names - это генератор
A ['Alan', 'Adam']
W ['Wes', 'Will']
A ['Albert']
S ['Steven']

В табл. 3.2 описаны некоторые функции из модуля itertools, которыми я часто пользуюсь. Дополнительную информацию об этом полезном стандартном модуле можно почерпнуть из официальной документации по адресу https://docs.python.org/3/library/itertools.html.