---
source_image: page_263.png
page_number: 263
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.40
tokens: 7685
characters: 1702
timestamp: 2025-12-24T02:47:13.990194
finish_reason: stop
---

0   b   0   1
1   b   1   1
2   b   6   1
3   a   2   0
4   a   4   0
5   a   5   0
6   c   3   <NA>
7   d   <NA>   2

In [48]: pd.merge(df3, df4, left_on="lkey", right_on="rkey", how="outer")
Out[48]:
    lkey  data1  rkey  data2
0   b     0     b     1
1   b     1     b     1
2   b     6     b     1
3   a     2     a     0
4   a     4     a     0
5   a     5     a     0
6   c     3     NaN   <NA>
7   NaN   <NA>   d     2

При внешнем соединении строки из левого или правого объекта DataFrame, которым не нашлось равного ключа в другом объекте, представлены значениями NA в столбцах, происходящих из этого другого объекта.
В табл. 8.1 перечислены возможные значения аргумента how.

Таблица 8.1. Различные типы соединения, задаваемые аргументом how

<table>
  <tr>
    <th>Значение</th>
    <th>Поведение</th>
  </tr>
  <tr>
    <td>'inner'</td>
    <td>Брать только комбинации ключей, встречающиеся в обеих таблицах</td>
  </tr>
  <tr>
    <td>'left'</td>
    <td>Брать все ключи, встречающиеся в левой таблице</td>
  </tr>
  <tr>
    <td>'right'</td>
    <td>Брать все ключи, встречающиеся в правой таблице</td>
  </tr>
  <tr>
    <td>'outer'</td>
    <td>Брать все комбинации ключей</td>
  </tr>
</table>

При соединении типа многие ко многим строится декартово произведение соответственных ключей. Вот пример:

In [49]: df1 = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "b"],
    ....:                 "data1": pd.Series(range(6), dtype="Int64")})
In [50]: df2 = pd.DataFrame({"key": ["a", "b", "a", "b", "d"],
    ....:                 "data2": pd.Series(range(5), dtype="Int64")})

In [51]: df1
Out[51]:
   key  data1
0   b     0
1   b     1
2   a     2
3   c     3
4   a     4
5   b     5