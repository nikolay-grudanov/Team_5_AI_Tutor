---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.66
tokens: 7671
characters: 2010
timestamp: 2025-12-24T02:42:09.059105
finish_reason: stop
---

строк. Допустим, что требуется построить множество, содержащее длины входящих в коллекцию строк; это легко сделать с помощью множественного включения:

In [157]: unique_lengths = {len(x) for x in strings}

In [158]: unique_lengths
Out[158]: {1, 2, 3, 4, 6}

То же самое можно записать в духе функционального программирования, воспользовавшись функцией map, с которой мы познакомимся ниже:

In [159]: set(map(len, strings))
Out[159]: {1, 2, 3, 4, 6}

В качестве простого примера словарного включения создадим словарь, сопоставляющий каждой строке ее позицию в списке:

In [160]: loc_mapping = {value: index for index, value in enumerate(strings)}

In [161]: loc_mapping
Out[161]: {'a': 0, 'as': 1, 'bat': 2, 'car': 3, 'dove': 4, 'python': 5}

Вложенное списковое включение
Пусть имеется список списков, содержащий английские и испанские имена:

In [162]: all_data = [["John", "Emily", "Michael", "Mary", "Steven"],
...:     ["Maria", "Juan", "Javier", "Natalia", "Pilar"]]

Допустим, что требуется получить один список, содержащий все имена, в которых встречается не менее двух букв а. Конечно, это можно было бы сделать в таком простом цикле for:

In [163]: names_of_interest = []

In [164]: for names in all_data:
...:     enough_as = [name for name in names if name.count("a") >= 2]
...:     names_of_interest.extend(enough_as)
...:
In [165]: names_of_interest
Out[165]: ['Maria', 'Natalia']

Но можно обернуть всю операцию одним вложенным списковым включением:

In [166]: result = [name for names in all_data for name in names
...:         if name.count("a") >= 2]

In [167]: result
Out[167]: ['Maria', 'Natalia']

Поначалу вложенное списковое включение с трудом укладывается в мозгу. Части for соответствуют порядку вложенности, а все фильтры располагаются в конце, как и раньше. Вот еще один пример, в котором мы линеаризуем список кортежей целых чисел, создавая один плоский список:

In [168]: some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

In [169]: flattened = [x for tup in some_tuples for x in tup]