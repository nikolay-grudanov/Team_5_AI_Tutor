---
source_image: page_258.png
page_number: 258
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.75
tokens: 7516
characters: 1638
timestamp: 2025-12-24T02:46:59.549058
finish_reason: stop
---

Обратите внимание, что имена индексов "state" и "color" не являются частями меток строк (значений frame.index).

Количество уровней индекса показывает атрибут nlevels:

In [25]: frame.index.nlevels
Out[25]: 2

Доступ по частичному индексу позволяет также выбирать группы столбцов:

In [26]: frame["Ohio"]
Out[26]:
color    Green   Red
key1 key2
a      1     0     1
       2     3     4
b      1     6     7
       2     9    10

Мультииндекс можно создать отдельно, а затем использовать повторно; в показанном выше объекте DataFrame столбцы с именами уровней можно было бы создать так:

pd.MultiIndex.from_arrays([["Ohio", "Ohio", "Colorado"],
                           ["Green", "Red", "Green"]],
                          names=["state", "color"])

Переупорядочение и уровни сортировки
Иногда требуется изменить порядок уровней на оси или отсортировать данные по значениям на одном уровне. Метод swaplevel принимает номера или имена двух уровней и возвращает новый объект, в котором эти уровни переставлены (но во всех остальных отношениях данные не изменяются):

In [27]: frame.swaplevel("key1", "key2")
Out[27]:
state    Ohio    Colorado
color    Green   Red   Green
key2 key1
1   a     0     1     2
2   a     3     4     5
1   b     6     7     8
2   b     9    10    11

Метод sort_index по умолчанию сортирует данные лексикографически, используя все уровни индексов, но мы можем указать только один уровень или подмножество уровней, задав аргумент level. Например:

In [28]: frame.sort_index(level=1)
Out[28]:
state    Ohio    Colorado
color    Green   Red   Green
key1 key2
a      1     0     1     2
b      1     6     7     8