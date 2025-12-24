---
source_image: page_160.png
page_number: 160
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.52
tokens: 7542
characters: 1678
timestamp: 2025-12-24T02:44:16.030846
finish_reason: stop
---

Colorado    6   4
Utah        10  8
New York   14  12

У доступа по индексу есть несколько частных случаев. Во-первых, выборка или вырезание данных с помощью булева массива:

In [148]: data[:2]
Out[148]:
      one  two  three  four
Ohio   0    1     2     3
Colorado 4    5     6     7

In [149]: data[data["three"] > 5]
Out[149]:
      one  two  three  four
Colorado 4    5     6     7
Utah     8    9     10    11
New York 12   13    14    15

Для удобства предоставляется специальный синтаксис выборки строк data[:2]. Если передать один элемент или список оператору [], то выбираются столбцы.

Еще одна возможность — доступ по индексу с помощью булева DataFrame, например порожденного в результате скалярного сравнения. Рассмотрим DataFrame, содержащий только булевые значения, порожденные сравнением со скаляром:

In [150]: data < 5
Out[150]:
      one  two  three  four
Ohio  True  True  True  True
Colorado  True False False False
Utah  False False False False
New York  False False False False

Мы можем использовать этот DataFrame, чтобы присвоить значение 0 всем элементам, которым соответствует значение True:

In [151]: data[data < 5] = 0

In [152]: data
Out[152]:
      one  two  three  four
Ohio  0    0     0     0
Colorado  0    5     6     7

Выборка из DataFrame с помощью loc и iloc

Как и Series, объект DataFrame имеет специальные атрибуты loc и iloc для индексирования метками и целыми числами соответственно. Поскольку объект DataFrame двумерный, мы можем выбрать подмножество строк и столбцов DataFrame с применением нотации NumPy, используя либо метки строк (loc), либо целые числа (iloc).

В качестве вступительного примера выберем одну строку по метке: