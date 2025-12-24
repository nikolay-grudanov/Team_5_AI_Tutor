---
source_image: page_267.png
page_number: 267
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.53
tokens: 7689
characters: 1840
timestamp: 2025-12-24T02:47:19.539276
finish_reason: stop
---

In [63]: right1
Out[63]:
    group_val
a        3.5
b        7.0

In [64]: pd.merge(left1, right1, left_on="key", right_index=True)
Out[64]:
   key  value  group_val
0    a      0         3.5
2    a      2         3.5
3    a      3         3.5
1    b      1         7.0
4    b      4         7.0

Внимательно присмотревшись, вы заметите, что здесь значения индексов для left1 сохранены, тогда как в примерах выше индексы входных объектов DataFrame отброшены. Поскольку индекс right1 уникален, при таком слиянии типа «многие к одному» (подразумеваемым по умолчанию методом how="inner") можно сохранить значения индекса из left1, соответствующие строкам результата.

По умолчанию соединение производится по пересекающимся ключам, но можно вместо пересечения выполнить объединение, указав внешнее соединение:

In [65]: pd.merge(left1, right1, left_on="key", right_index=True, how="outer")
Out[65]:
   key  value  group_val
0    a      0         3.5
2    a      2         3.5
3    a      3         3.5
1    b      1         7.0
4    b      4         7.0
5    c      5         NaN

В случае иерархически индексированных данных ситуация усложняется, поскольку соединение по индексу эквивалентно слиянию по нескольким ключам:

In [66]: lefth = pd.DataFrame({"key1": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
.....:     "key2": [2000, 2001, 2002, 2001, 2002],
.....:     "data": pd.Series(range(5), dtype="Int64")})

In [67]: righth_index = pd.MultiIndex.from_arrays(
.....:     [
.....:         ["Nevada", "Nevada", "Ohio", "Ohio", "Ohio", "Ohio"],
.....:         [2001, 2000, 2000, 2000, 2001, 2002]
.....:     ]
.....: )

In [68]: righth = pd.DataFrame({"event1": pd.Series([0, 2, 4, 6, 8, 10], dtype="Int64",
.....:     index=righth_index),
.....:     "event2": pd.Series([1, 3, 5, 7, 9, 11], dtype="Int64",
.....:     index=righth_index)})