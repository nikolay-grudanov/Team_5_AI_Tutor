---
source_image: page_276.png
page_number: 276
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.13
tokens: 7569
characters: 1313
timestamp: 2025-12-24T02:47:36.066326
finish_reason: stop
---

a    0.0
b    NaN
c    2.0
d    NaN
e    NaN
f    5.0
dtype: float64

In [119]: np.where(pd.isna(a), b, a)
Out[119]: array([0., 2.5, 0., 3.5, 4.5, 5.])

Здесь выбирается значение из b, если значение в a отсутствует, в противном случае выбирается значение из a. Функция numpy.where не проверяет, совмещены метки индекса или нет (и даже не требует, чтобы все объекты имели одинаковую длину). Поэтому если вы хотите выровнять значения в соответствии с индексом, то пользуйтесь методом combine_first объекта Series:

In [120]: a.combine_first(b)
Out[120]:
a    0.0
b    4.5
c    3.5
d    0.0
e    2.5
f    5.0
dtype: float64

В случае DataFrame метод combine_first делает то же самое для каждого столбца, так что можно считать, что он «подставляет» вместо данных, отсутствующих в вызывающем объекте, данные из объекта, переданного в аргументе:

In [121]: df1 = pd.DataFrame({"a": [1., np.nan, 5., np.nan],
.....:     "b": [np.nan, 2., np.nan, 6.],
.....:     "c": range(2, 18, 4)})

In [122]: df2 = pd.DataFrame({"a": [5., 4., np.nan, 3., 7.],
.....:     "b": [np.nan, 3., 4., 6., 8.]})

In [123]: df1
Out[123]:
   a    b    c
0  1.0  NaN  2
1  NaN  2.0  6
2  5.0  NaN  10
3  NaN  6.0  14

In [124]: df2
Out[124]:
   a    b
0  5.0  NaN
1  4.0  3.0
2  NaN  4.0
3  3.0  6.0
4  7.0  8.0

In [125]: df1.combine_first(df2)