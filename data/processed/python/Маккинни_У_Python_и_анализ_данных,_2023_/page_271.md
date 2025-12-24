---
source_image: page_271.png
page_number: 271
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.43
tokens: 7481
characters: 1256
timestamp: 2025-12-24T02:47:23.066228
finish_reason: stop
---

О Нужно ли иметь возможность идентифицировать группы в результирующем объекте?
О Содержит ли «ось конкатенации» данные, которые необходимо сохранить? Во многих случаях подразумеваемые по умолчанию целочисленные метки в объекте DataFrame в процессе конкатенации лучше отбросить.

Функция concat в pandas дает согласованные ответы на эти вопросы. Я покажу, как она работает, на примерах. Допустим, имеются три объекта Series с непересекающимися индексами:

In [87]: s1 = pd.Series([0, 1], index=["a", "b"], dtype="Int64")
In [88]: s2 = pd.Series([2, 3, 4], index=["c", "d", "e"], dtype="Int64")
In [89]: s3 = pd.Series([5, 6], index=["f", "g"], dtype="Int64")

Если передать их функции pandas.concat списком, то она «склеит» данные и индексы:

In [90]: s1
Out[90]:
   a    0
   b    1
dtype: Int64

In [91]: s2
Out[91]:
   c    2
   d    3
   e    4
dtype: Int64

In [92]: s3
Out[92]:
   f    5
   g    6
dtype: Int64

In [93]: pd.concat([s1, s2, s3])
Out[93]:
   a  b  c  d  e  f  g
0   0  1  2  3  4  5  6
dtype: Int64

По умолчанию pandas.concat работает вдоль оси axis="index", порождая новый объект Series. Но если передать параметр axis="columns", то результатом будет DataFrame:

In [94]: pd.concat([s1, s2, s3], axis="columns")
Out[94]:
      0  1  2