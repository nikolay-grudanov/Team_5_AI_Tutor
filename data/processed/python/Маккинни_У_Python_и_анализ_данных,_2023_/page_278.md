---
source_image: page_278.png
page_number: 278
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.92
tokens: 7463
characters: 1261
timestamp: 2025-12-24T02:47:30.193289
finish_reason: stop
---

Colorado    one   3
           two   4
           three  5
dtype: int64

Имея иерархически проиндексированный объект Series, мы можем восстановить DataFrame методом unstack:

In [130]: result.unstack()
Out[130]:
number   one  two  three
state
Ohio     0    1    2
Colorado 3    4    5

По умолчанию поворачивается самый внутренний уровень (как и в случае stack). Но можно повернуть и любой другой, если указать номер или имя уровня:

In [131]: result.unstack(level=0)
Out[131]:
state  Ohio  Colorado
number
one    0     3
two    1     4
three  2     5

In [132]: result.unstack(level="state")
Out[132]:
state  Ohio  Colorado
number
one    0     3
two    1     4
three  2     5

При обратном повороте могут появиться отсутствующие данные, если не каждое значение на указанном уровне присутствует в каждой подгруппе:

In [133]: s1 = pd.Series([0, 1, 2, 3], index=["a", "b", "c", "d"], dtype="Int64")

In [134]: s2 = pd.Series([4, 5, 6], index=["c", "d", "e"], dtype="Int64")

In [135]: data2 = pd.concat([s1, s2], keys=["one", "two"])

In [136]: data2
Out[136]:
one   a   0
      b   1
      c   2
      d   3
two   c   4
      d   5
      e   6
dtype: Int64

При выполнении поворота отсутствующие данные по умолчанию отфильтровываются, поэтому операция обратима: