---
source_image: page_130.png
page_number: 130
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.96
tokens: 7262
characters: 1078
timestamp: 2025-12-24T02:37:19.630574
finish_reason: stop
---

File "<stdin>", line 1, in <module>
ImportError: No module named plot

Если вы запустите Python с присваиванием значения переменной PYTHONPATH, она укажет Python, где нужно искать библиотеки:

$ PYTHONPATH=/home/test/a python3
Python 3.6.0 (default, Dec 24 2016, 08:01:42)
>>> import plot
>>> plot.histogram()
...

СОВЕТ
Для установки пакетов Python могут использоваться менеджеры пакетов, исполняемые файлы Windows или специализированные средства Python, такие как pip¹.

25.5. sys.path

У модуля sys имеется атрибут path со списком каталогов, в которых Python ищет библиотеки. Просмотрев sys.path, вы увидите все просмотренные каталоги:

>>> import sys
>>> sys.path

['',
'/usr/lib/python35.zip',
'/usr/lib/python3.6',
'/usr/lib/python3.6/plat-darwin',
'/usr/lib/python3.6/lib-dynload',
'/usr/local/lib/python3.6/site-packages']

СОВЕТ
Если вы сталкиваетесь с ошибкой вида

    ImportError: No module named plot,

обратитесь к переменной sys.path и посмотрите, присутствует ли в ней каталог, в котором находится файл foo.py (если это модуль). Если plot

¹ https://pip.pypa.io/