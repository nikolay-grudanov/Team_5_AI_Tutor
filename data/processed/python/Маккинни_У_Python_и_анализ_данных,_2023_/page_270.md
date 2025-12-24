---
source_image: page_270.png
page_number: 270
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.22
tokens: 7787
characters: 1951
timestamp: 2025-12-24T02:47:39.819224
finish_reason: stop
---

8.2. Комбинирование и слияние наборов данных

In [80]: another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
    ....:                        index=["a", "c", "e", "f"],
    ....:                        columns=["New York", "Oregon"])

In [81]: another
Out[81]:
   New York  Oregon
a      7.0     8.0
c      9.0    10.0
e     11.0    12.0
f     16.0    17.0

In [82]: left2.join([right2, another])
Out[82]:
   Ohio  Nevada  Missouri  Alabama  New York  Oregon
a     1       2        <NA>      <NA>      7.0      8.0
c     3       4        9         10        9.0     10.0
e     5       6       13        14       11.0     12.0

In [83]: left2.join([right2, another], how="outer")
Out[83]:
   Ohio  Nevada  Missouri  Alabama  New York  Oregon
a     1       2        <NA>      <NA>      7.0      8.0
c     3       4        9         10        9.0     10.0
e     5       6       13        14       11.0     12.0
b    <NA>    <NA>        7         8        NaN      NaN
d    <NA>    <NA>       11        12        NaN      NaN
f    <NA>    <NA>      <NA>      <NA>     16.0     17.0

Конкатенация вдоль оси
Еще одну операцию комбинирования данных разные авторы называют по-разному: конкатенация или составление. В библиотеке NumPy имеется функция concatenate для выполнения этой операции над массивами:

In [84]: arr = np.arange(12).reshape((3, 4))

In [85]: arr
Out[85]:
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

In [86]: np.concatenate([arr, arr], axis=1)
Out[86]:
array([[ 0,  1,  2,  3,  0,  1,  2,  3],
       [ 4,  5,  6,  7,  4,  5,  6,  7],
       [ 8,  9, 10, 11,  8,  9, 10, 11]])

В контексте объектов pandas, Series и DataFrame наличие помеченных осей позволяет обобщить конкатенацию массивов. В частности, нужно решить следующие вопросы.

О Если объекты по-разному проиндексированы по другим осям, следует ли объединять различные элементы на этих осях или использовать только общие значения?