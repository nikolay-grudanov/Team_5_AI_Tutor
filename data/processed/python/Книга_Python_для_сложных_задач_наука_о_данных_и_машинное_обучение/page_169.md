---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.97
tokens: 7603
characters: 1752
timestamp: 2025-12-24T00:55:41.238209
finish_reason: stop
---

In[14]: pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])

Out[14]: MultiIndex(levels=[['a', 'b'], [1, 2]],
    labels=[[0, 0, 1, 1], [0, 1, 0, 1]])

Или из списка кортежей, задающих все значения индекса в каждой из точек:

In[15]: pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])

Out[15]: MultiIndex(levels=[['a', 'b'], [1, 2]],
    labels=[[0, 0, 1, 1], [0, 1, 0, 1]])

Или из декартова произведения обычных индексов:

In[16]: pd.MultiIndex.from_product([['a', 'b'], [1, 2]])

Out[16]: MultiIndex(levels=[['a', 'b'], [1, 2]],
    labels=[[0, 0, 1, 1], [0, 1, 0, 1]])

Можно сформировать объект MultiIndex непосредственно с помощью его внутреннего представления, передав в конструктор levels (список списков, содержащих имеющиеся значения индекса для каждого уровня) и labels (список списков меток):

In[17]: pd.MultiIndex(levels=[['a', 'b'], [1, 2]],
    labels=[[0, 0, 1, 1], [0, 1, 0, 1]])

Out[17]: MultiIndex(levels=[['a', 'b'], [1, 2]],
    labels=[[0, 0, 1, 1], [0, 1, 0, 1]])

Любой из этих объектов можно передать в качестве аргумента метода index при создании объектов Series или DataFrame или методу reindex уже существующих объектов Series или DataFrame.

Названия уровней мультииндексов

Иногда бывает удобно задать названия для уровней объекта MultiIndex. Сделать это можно, передав аргумент names любому из вышеперечисленных конструкторов класса MultiIndex или задав значения атрибута names постфактум:

In[18]: pop.index.names = ['state', 'year']
    pop

Out[18]: state      year
    California   2000    33871648
                 2010    37253956
    New York     2000    18976457
                 2010    19378102
    Texas        2000    20851820
                 2010    25145561
    dtype: int64