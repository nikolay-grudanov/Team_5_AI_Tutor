---
source_image: page_169.png
page_number: 169
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.87
tokens: 7609
characters: 1379
timestamp: 2025-12-24T02:44:36.235761
finish_reason: stop
---

Точно так же, выполняя переиндексацию объекта Series или DataFrame, можно указать восполняемое значение:

In [206]: df1.reindex(columns=df2.columns, fill_value=0)
Out[206]:
    a   b   c   d   e
0  0.0  1.0  2.0  3.0  0
1  4.0  5.0  6.0  7.0  0
2  8.0  9.0 10.0 11.0  0

Таблица 5.5. Гибкие арифметические методы

<table>
  <tr>
    <th>Метод</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>add, radd</td>
    <td>Сложение (+)</td>
  </tr>
  <tr>
    <td>sub, rsub</td>
    <td>Вычитание (-)</td>
  </tr>
  <tr>
    <td>div, rdiv</td>
    <td>Деление (/)</td>
  </tr>
  <tr>
    <td>floordiv, rfloordiv</td>
    <td>Деление с отсечением (//)</td>
  </tr>
  <tr>
    <td>mul, rmul</td>
    <td>Умножение (*)</td>
  </tr>
  <tr>
    <td>pow, rpow</td>
    <td>Возведение в степень (**)</td>
  </tr>
</table>

Операции между DataFrame и Series
Как и в случае массивов NumPy, арифметические операции между DataFrame и Series корректно определены. В качестве пояснительного примера рассмотрим вычисление разности между двумерным массивом и одной из его строк:

In [207]: arr = np.arange(12.).reshape((3, 4))

In [208]: arr
Out[208]:
array([[ 0.,  1.,  2.,  3.],
       [ 4.,  5.,  6.,  7.],
       [ 8.,  9., 10., 11.]])

In [209]: arr[0]
Out[209]: array([0., 1., 2., 3.])

In [210]: arr - arr[0]
Out[210]:
array([[0., 0., 0., 0.],
       [4., 4., 4., 4.],
       [8., 8., 8., 8.]])