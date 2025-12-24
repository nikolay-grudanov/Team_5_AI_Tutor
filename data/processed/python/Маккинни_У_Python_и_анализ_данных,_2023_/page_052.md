---
source_image: page_052.png
page_number: 52
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.38
tokens: 7416
characters: 1231
timestamp: 2025-12-24T02:41:13.033218
finish_reason: stop
---

Эта функция возвращает True для строк, а также для большинства типов коллекций в Python:

In [34]: isiterable("a string")
Out[34]: True

In [35]: isiterable([1, 2, 3])
Out[35]: True

In [36]: isiterable(5)
Out[36]: False

Импорт
В Python модуль – это просто файл с расширением .py, который содержит функции и различные определения, в том числе импортированные из других py-файлов. Пусть имеется следующий модуль:

# some_module.py
PI = 3.14159

def f(x):
    return x + 2

def g(a, b):
    return a + b

Если бы мы захотели обратиться к переменным или функциям, определенным в some_module.py, из другого файла в том же каталоге, то должны были бы написать:

import some_module
result = some_module.f(5)
pi = some_module.PI

Или эквивалентно:

from some_module import g, PI
result = g(5, PI)

Ключевое слово as позволяет переименовать импортированные сущности:

import some_module as sm
from some_module import PI as pi, g as gf

r1 = sm.f(pi)
r2 = gf(6, pi)

Бинарные операторы и операции сравнения
В большинстве бинарных математических операций и операций сравнения используется такой же синтаксис, как в других языках программирования:

In [37]: 5 - 7
Out[37]: -2

In [38]: 12 + 21.5
Out[38]: 33.5

In [39]: 5 <= 2
Out[39]: False