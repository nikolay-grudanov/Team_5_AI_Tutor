---
source_image: page_080.png
page_number: 80
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.81
tokens: 7548
characters: 1646
timestamp: 2025-12-24T02:41:58.148885
finish_reason: stop
---

enumerate
При обходе последовательности часто бывает необходимо следить за индексом текущего элемента. «Ручками» это можно сделать так:

index = 0
for value in collection:
    # что-то сделать с value
    index += 1

Но поскольку эта задача встречается очень часто, в Python имеется встроенная функция enumerate, которая возвращает последовательность кортежей (i, value):

for index, value in enumerate(collection):
    # что-то сделать с value

sorted
Функция sorted возвращает новый отсортированный список, построенный из элементов произвольной последовательности:

In [145]: sorted([7, 1, 2, 6, 0, 3, 2])
Out[145]: [0, 1, 2, 2, 3, 6, 7]

In [146]: sorted("horse race")
Out[146]: [' ', 'a', 'c', 'e', 'e', 'h', 'o', 'r', 'r', 's']

Функция sorted принимает те же аргументы, что метод списков sort.

zip
Функция zip «сшивает» элементы нескольких списков, кортежей или других последовательностей в пары, создавая список кортежей:

In [147]: seq1 = ["foo", "bar", "baz"]
In [148]: seq2 = ["one", "two", "three"]
In [149]: zipped = zip(seq1, seq2)
In [150]: list(zipped)
Out[150]: [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]

Функция zip принимает любое число аргументов, а количество порождаемых ей кортежей определяется длиной самой короткой последовательности:

In [151]: seq3 = [False, True]
In [152]: list(zip(seq1, seq2, seq3))
Out[152]: [('foo', 'one', False), ('bar', 'two', True)]

Очень распространенное применение zip — одновременный обход нескольких последовательностей, возможно, в сочетании с enumerate:

In [153]: for index, (a, b) in enumerate(zip(seq1, seq2)):
    ....:     print(f"{index}: {a}, {b}")
    ....:
0: foo, one