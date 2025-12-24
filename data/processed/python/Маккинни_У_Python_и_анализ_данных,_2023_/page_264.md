---
source_image: page_264.png
page_number: 264
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.41
tokens: 7613
characters: 1599
timestamp: 2025-12-24T02:47:14.109375
finish_reason: stop
---

8.2. Комбинирование и слияние наборов данных

In [52]: df2
Out[52]:
   key  data2
0    a      0
1    b      1
2    a      2
3    b      3
4    d      4

In [53]: pd.merge(df1, df2, on="key", how="left")
Out[53]:
   key  data1  data2
0    b      0      1
1    b      0      3
2    b      1      1
3    b      1      3
4    a      2      0
5    a      2      2
6    c      3     <NA>
7    a      4      0
8    a      4      2
9    b      5      1
10   b      5      3

Поскольку в левом объекте DataFrame было три строки с ключом "b", а в правом — две, то в результирующем объекте таких строк получилось шесть. Метод соединения, переданный в аргументе how, оказывает влияние только на множество различных ключей в результате:

In [54]: pd.merge(df1, df2, how="inner")
Out[54]:
   key  data1  data2
0    b      0      1
1    b      0      3
2    b      1      1
3    b      1      3
4    b      5      1
5    b      5      3
6    a      2      0
7    a      2      2
8    a      4      0
9    a      4      2

Для соединения по нескольким ключам передаем список имен столбцов:

In [55]: left = pd.DataFrame({"key1": ["foo", "foo", "bar"],
    ....:                 "key2": ["one", "two", "one"],
    ....:                 "lval": pd.Series([1, 2, 3], dtype='Int64')})

In [56]: right = pd.DataFrame({"key1": ["foo", "foo", "bar", "bar"],
    ....:                 "key2": ["one", "one", "one", "two"],
    ....:                 "rval": pd.Series([4, 5, 6, 7], dtype='Int64')})

In [57]: pd.merge(left, right, on=["key1", "key2"], how="outer")
Out[57]:
   key1  key2  lval  rval
0  foo   one     1     4