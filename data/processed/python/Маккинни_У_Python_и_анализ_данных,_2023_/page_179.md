---
source_image: page_179.png
page_number: 179
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.57
tokens: 7545
characters: 1410
timestamp: 2025-12-24T02:44:50.097631
finish_reason: stop
---

In [271]: df.sum(axis="index", skipna=False)
Out[271]:
one    NaN
two    NaN
dtype: float64

In [272]: df.sum(axis="columns", skipna=False)
Out[272]:
a    NaN
b    2.60
c    NaN
d   -0.55
dtype: float64

Некоторым агрегатным функциям, например mean, для получения результата требуется, чтобы по крайней мере одно значение было отлично от NaN, поэтому в данном случае мы имеем:

In [273]: df.mean(axis="columns")
Out[273]:
a    1.400
b    1.300
c    NaN
d   -0.275
dtype: float64

Перечень часто употребляемых параметров методов редукции приведен в табл. 5.7.

Таблица 5.7. Параметры методов редукции

<table>
  <tr>
    <th>Метод</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>axis</td>
    <td>Ось, по которой производится редуцирование. В случае DataFrame "index" означает строки, "columns" – столбцы</td>
  </tr>
  <tr>
    <td>skipna</td>
    <td>Исключать отсутствующие значения. По умолчанию True</td>
  </tr>
  <tr>
    <td>level</td>
    <td>Редуцировать с группировкой по уровням, если индекс по оси иерархический (MultiIndex)</td>
  </tr>
</table>

Некоторые методы, например idxmin и idxmax, возвращают косвенные статистики, скажем индекс, при котором достигается минимум или максимум:

In [274]: df.idxmax()
Out[274]:
one    b
two    d
dtype: object

Существуют также аккумулирующие методы:

In [275]: df.cumsum()
Out[275]:
      one   two
a   1.40  NaN
b   8.50 -4.5
c   NaN   NaN
d   9.25 -5.8