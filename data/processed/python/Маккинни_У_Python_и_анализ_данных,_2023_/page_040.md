---
source_image: page_040.png
page_number: 40
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.49
tokens: 7631
characters: 1733
timestamp: 2025-12-24T02:41:03.661061
finish_reason: stop
---

$ ipython
Python 3.10.4 | packaged by conda-forge | (main, Mar 24 2022, 17:38:57)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.31.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: %run hello_world.py
Hello world

In [2]:

По умолчанию приглашение IPython содержит не стандартную строку >>>, а строку вида In [2]:, включающую порядковый номер предложения.

2.2. Основы IPython
В этом разделе мы научимся запускать оболочку IPython и Jupyter-блокнот, а также познакомимся с некоторыми важнейшими понятиями.

Запуск оболочки IPython
IPython можно запустить из командной строки, как и стандартный интерпретатор Python, только для этого служит команда ipython:

$ ipython
Python 3.10.4 | packaged by conda-forge | (main, Mar 24 2022, 17:38:57)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.31.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: a = 5

In [2]: a
Out[2]: 5

Чтобы выполнить произвольное предложение Python, нужно ввести его и нажать клавишу Enter. Если ввести только имя переменной, то IPython выведет строковое представление объекта:

In [5]: import numpy as np

In [6]: data = [np.random.standard_normal() for i in range(7)]

In [7]: data
Out[7]:
[-0.20470765948471295,
 0.47894333805754824,
 -0.5194387150567381,
 -0.55573030434749,
 1.9657805725027142,
 1.3934058329729904,
 0.09290787674371767]

Здесь первые две строки содержат код на Python; во второй строке создается переменная data, ссылающаяся на только что созданный словарь Python. В последней строке значение data выводится на консоль.
Многие объекты Python форматируются для удобства чтения; такая красивая печать отличается от обычного представления методом print. Тот же сло-