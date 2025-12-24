---
source_image: page_174.png
page_number: 174
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.81
tokens: 7456
characters: 1126
timestamp: 2025-12-24T02:44:30.638888
finish_reason: stop
---

one    4 5 6 7
three  0 1 2 3

In [240]: frame.sort_index(axis="columns")
Out[240]:
    a   b   c   d
three 1  2  3  0
one    5  6  7  4

По умолчанию данные сортируются в порядке возрастания, но можно отсортировать их и в порядке убывания:

In [241]: frame.sort_index(axis="columns", ascending=False)
Out[241]:
    d   c   b   a
three 0  3  2  1
one    4  7  6  5

Для сортировки Series по значениям служит метод sort_values:

In [242]: obj = pd.Series([4, 7, -3, 2])

In [243]: obj.sort_values()
Out[243]:
2   -3
3    2
0    4
1    7
dtype: int64

Значения NaN по умолчанию оказываются в конце Series:

In [244]: obj = pd.Series([4, np.nan, 7, np.nan, -3, 2])

In [245]: obj.sort_values()
Out[245]:
4   -3.0
5    2.0
0    4.0
2    7.0
1    NaN
3    NaN
dtype: float64

Значения NaN можно поместить в начало, а не в конец, добавив именованный параметр na_position:

In [246]: obj.sort_values(na_position="first")
Out[246]:
1    NaN
3    NaN
4   -3.0
5    2.0
0    4.0
2    7.0
dtype: float64

Объект DataFrame можно сортировать по значениям в одном или нескольких столбцах. Для этого передайте имя столбца методу sort_values: