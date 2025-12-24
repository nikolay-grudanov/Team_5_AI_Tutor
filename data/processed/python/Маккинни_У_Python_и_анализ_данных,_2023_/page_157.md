---
source_image: page_157.png
page_number: 157
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.90
tokens: 7450
characters: 1011
timestamp: 2025-12-24T02:44:05.307361
finish_reason: stop
---

c    2.0
d    3.0
dtype: float64

In [126]: obj["b"]
Out[126]: 1.0

In [127]: obj[1]
Out[127]: 1.0

In [128]: obj[2:4]
Out[128]:
c    2.0
d    3.0
dtype: float64

In [129]: obj[["b", "a", "d"]]
Out[129]:
b    1.0
a    0.0
d    3.0
dtype: float64

In [130]: obj[[1, 3]]
Out[130]:
b    1.0
d    3.0
dtype: float64

In [131]: obj[obj < 2]
Out[131]:
a    0.0
b    1.0
dtype: float64

Хотя выбирать данные по метке можно и так, предпочтительнее выбирать значения из индекса с помощью специального оператора loc:

In [132]: obj.loc[["b", "a", "d"]]
Out[132]:
b    1.0
a    0.0
d    3.0
dtype: float64

Использовать loc лучше, потому что целые числа обрабатываются при этом не так, как при индексировании с помощью []. В последнем случае целые числа трактуются как метки, если индекс содержит целые числа, поэтому поведение зависит от типа данных в индексе. Например:

In [133]: obj1 = pd.Series([1, 2, 3], index=[2, 0, 1])

In [134]: obj2 = pd.Series([1, 2, 3], index=["a", "b", "c"])

In [135]: obj1
Out[135]:
2    1