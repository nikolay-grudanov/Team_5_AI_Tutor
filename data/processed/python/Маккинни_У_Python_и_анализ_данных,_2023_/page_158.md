---
source_image: page_158.png
page_number: 158
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.33
tokens: 7436
characters: 1093
timestamp: 2025-12-24T02:44:02.722525
finish_reason: stop
---

0    2
1    3
dtype: int64

In [136]: obj2
Out[136]:
   a   1
   b   2
   c   3
dtype: int64

In [137]: obj1[[0, 1, 2]]
Out[137]:
   0    2
   1    3
   2    1
dtype: int64

In [138]: obj2[[0, 1, 2]]
Out[138]:
   a   1
   b   2
   c   3
dtype: int64

При использовании loc выражение obj.loc[[0, 1, 2]] приведет к ошибке, если индекс содержит не целые числа:

In [134]: obj2.loc[[0, 1]]
------------------------------------------------------------
KeyError                                 Traceback (most recent call last)
/tmp/ipykernel_804589/4185657903.py in <module>
----> 1 obj2.loc[[0, 1]]

^ LONG EXCEPTION ABBREVIATED ^

KeyError: "None of [Int64Index([0, 1], dtype="int64")] are in the [index]"

Поскольку оператор loc индексирует только метками, имеется также оператор iloc, который индексирует только целыми числами, чтобы обеспечить единообразную работу вне зависимости от того, содержит индекс целые числа или нет:

In [139]: obj1.iloc[[0, 1, 2]]
Out[139]:
   2    1
   0    2
   1    3
dtype: int64

In [140]: obj2.iloc[[0, 1, 2]]
Out[140]:
   a   1
   b   2
   c   3
dtype: int64