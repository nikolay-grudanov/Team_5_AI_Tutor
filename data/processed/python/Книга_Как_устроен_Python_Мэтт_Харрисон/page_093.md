---
source_image: page_093.png
page_number: 93
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.92
tokens: 7276
characters: 1249
timestamp: 2025-12-24T02:36:26.197773
finish_reason: stop
---

...
    count.setdefault(name, 0)
    count[name] += 1

Без метода .setdefault потребовалось бы немного больше кода:

>>> names = ['Ringo', 'Paul', 'John',
...           'Ringo']
>>> count = {}
>>> for name in names:
...     if name not in count:
...         count[name] = 1
...     else:
...         count[name] += 1

>>> count['Ringo']
2

СОВЕТ

Подобные операции подсчета встречаются настолько часто, что позднее в стандартную библиотеку Python был добавлен класс collections.Counter. Этот класс позволяет выполнять такие операции в более компактном виде:

    >>> import collections
    >>> count = collections.Counter(['Ringo', 'Paul',
...           'John', 'Ringo'])
    >>> count
    Counter({'Ringo': 2, 'Paul': 1, 'John': 1})
    >>> count['Ringo']
    2
    >>> count['Fred']
    0

Ниже приведен несколько искусственный пример, демонстрирующий изменение результата .setdefault. Предположим, имеется словарь, связывающий имя музыканта с названием группы, в которой он играл. Если человек по имени Paul участвует в двух группах, результат должен связывать имя Paul со списком, содержащим обе группы:

>>> band1_names = ['John', 'George',
...   'Paul', 'Ringo']
>>> band2_names = ['Paul']
>>> names_to_bands = {}
>>> for name in band1_names: