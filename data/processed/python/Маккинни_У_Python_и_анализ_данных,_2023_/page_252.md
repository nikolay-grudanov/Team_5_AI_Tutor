---
source_image: page_252.png
page_number: 252
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.59
tokens: 7427
characters: 1149
timestamp: 2025-12-24T02:46:49.546122
finish_reason: stop
---

In [256]: actual_categories = ['a', 'b', 'c', 'd', 'e']

In [257]: cat_s2 = cat_s.cat.set_categories(actual_categories)

In [258]: cat_s2
Out[258]:
   0    a
   1    b
   2    c
   3    d
   4    a
   5    b
   6    c
   7    d
dtype: category
Categories (5, object): ['a', 'b', 'c', 'd', 'e']

Хотя, на первый взгляд, данные не изменились, новые категории найдут отражения в операциях. Например, метод value_counts учитывает все категории:

In [259]: cat_s.value_counts()
Out[259]:
a    2
b    2
c    2
d    2
dtype: int64

In [260]: cat_s2.value_counts()
Out[260]:
a    2
b    2
c    2
d    2
e    0
dtype: int64

В больших наборах категориальные данные часто используются для экономии памяти и повышения производительности. После фильтрации большого объекта DataFrame или Series многих категорий в данных может не оказаться. Метод remove_unused_categories убирает ненаблюдаемые категории:

In [261]: cat_s3 = cat_s[cat_s.isin(['a', 'b'])]

In [262]: cat_s3
Out[262]:
   0    a
   1    b
   4    a
   5    b
dtype: category
Categories (4, object): ['a', 'b', 'c', 'd']

In [263]: cat_s3.cat.remove_unused_categories()
Out[263]:
   0    a
   1    b