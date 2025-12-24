---
source_image: page_265.png
page_number: 265
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.17
tokens: 7710
characters: 2048
timestamp: 2025-12-24T02:47:19.739475
finish_reason: stop
---

1 foo one    1   5
2 foo two    2   <NA>
3 bar one    3   6
4 bar two    <NA>   7

Чтобы определить, какие комбинации ключей появятся в результате при данном выборе метода слияния, полезно представить несколько ключей как массив кортежей, используемый в качестве единственного ключа соединения.

При соединении столбцов по столбцам индексы над переданными объектами DataFrame отбрасываются. Если нужно сохранить значения индексов, то следует использовать reset_index для добавления индекса к столбцам.

Последний момент, касающийся операций слияния, — обработка столбцов с одинаковыми именами. Например:

In [58]: pd.merge(left, right, on="key1")
Out[58]:
  key1  key2_x  lval  key2_y  rval
0  foo    one     1   one     4
1  foo    one     1   one     5
2  foo    two     2   one     4
3  foo    two     2   one     5
4  bar    one     3   one     6
5  bar    one     3   two     7

Хотя эту проблему можно решить вручную (см. раздел о переименовании меток на осиах ниже), у функции pandas.merge имеется параметр suffixes, позволяющий задать строки, которые должны дописываться в конец одинаковых имен в левом и правом объектах DataFrame:

In [59]: pd.merge(left, right, on="key1", suffixes=("_left", "_right"))
Out[59]:
  key1  key2_left  lval  key2_right  rval
0  foo    one      1   one           4
1  foo    one      1   one           5
2  foo    two      2   one           4
3  foo    two      2   one           5
4  bar    one      3   one           6
5  bar    one      3   two           7

В табл. 8.2 приведена справка по аргументам функции pandas.merge. Соединение с использованием индекса строк DataFrame — тема следующего раздела.

Таблица 8.2. Аргументы функции merge

<table>
  <tr>
    <th>Аргумент</th>
    <th>Описание</th>
  </tr>
  <tr>
    <td>left</td>
    <td>Объект DataFrame в левой части операции слияния</td>
  </tr>
  <tr>
    <td>right</td>
    <td>Объект DataFrame в правой части операции слияния</td>
  </tr>
  <tr>
    <td>how</td>
    <td>Допустимые значения: 'inner', 'outer', 'left', 'right'</td>
  </tr>
</table>