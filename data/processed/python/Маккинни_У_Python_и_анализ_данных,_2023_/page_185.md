---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.42
tokens: 7531
characters: 1177
timestamp: 2025-12-24T02:44:56.119044
finish_reason: stop
---

In [304]: data
Out[304]:
   Qu1  Qu2  Qu3
0    1    2    1
1    3    3    5
2    4    1    2
3    3    2    4
4    4    3    4

Счетчики значений в одном столбце вычисляются следующим образом:

In [305]: data["Qu1"].value_counts().sort_index()
Out[305]:
1    1
3    2
4    2
Name: Qu1, dtype: int64

А для вычисления счетчиков по всем столбцам нужно передать pandas.value_counts методу apply объекта DataFrame:

In [306]: result = data.apply(pd.value_counts).fillna(0)

In [307]: result
Out[307]:
   Qu1  Qu2  Qu3
1  1.0  1.0  1.0
2  0.0  2.0  1.0
3  2.0  2.0  0.0
4  2.0  0.0  2.0
5  0.0  0.0  1.0

Здесь метками строк результирующего объекта являются неповторяющиеся значения, встречающиеся в столбцах. Значениями же являются счетчики значений в столбце.

Существует также метод DataFrame.value_counts, но он при вычислении счетчиков рассматривает каждую строку DataFrame как кортеж, чтобы определить количество вхождений различных строк:

In [308]: data = pd.DataFrame({"a": [1, 1, 1, 2, 2], "b": [0, 0, 1, 0, 0]})

In [309]: data
Out[309]:
   a  b
0  1  0
1  1  0
2  1  1
3  2  0
4  2  0

In [310]: data.value_counts()
Out[310]:
   a  b
1  0  2
2  0  2
1  1  1
dtype: int64