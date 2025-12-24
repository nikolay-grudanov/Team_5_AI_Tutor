---
source_image: page_269.png
page_number: 269
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.84
tokens: 7622
characters: 1775
timestamp: 2025-12-24T02:47:26.108174
finish_reason: stop
---

Ohio    Nevada
a      1      2
c      3      4
e      5      6

In [76]: right2
Out[76]:
    Missouri   Alabama
b        7        8
c        9       10
d       11       12
e       13       14

In [77]: pd.merge(left2, right2, how="outer", left_index=True, right_index=True)
Out[77]:
    Ohio   Nevada   Missouri   Alabama
a     1      2      <NA>      <NA>
b   <NA>   <NA>        7        8
c     3      4        9       10
d   <NA>   <NA>       11       12
e     5      6       13       14

В классе DataFrame есть и более удобный метод экземпляра join для слияния по индексу. Его также можно использовать для комбинирования нескольких объектов DataFrame, обладающих одинаковыми или похожими индексами, но непересекающимися столбцами. В предыдущем примере можно было бы написать:

In [78]: left2.join(right2, how="outer")
Out[78]:
    Ohio   Nevada   Missouri   Alabama
a     1      2      <NA>      <NA>
b   <NA>   <NA>        7        8
c     3      4        9       10
d   <NA>   <NA>       11       12
e     5      6       13       14

По сравнению с pandas.merge, метод join объекта DataFrame по умолчанию выполняет левое внешнее соединение по ключам соединения. Он также поддерживает соединение с индексом переданного DataFrame по одному из столбцов вызывающего:

In [79]: left1.join(right1, on="key")
Out[79]:
  key  value  group_val
0   a      0      3.5
1   b      1      7.0
2   a      2      3.5
3   a      3      3.5
4   b      4      7.0
5   c      5      NaN

Этот метод можно представлять себе как присоединение данных к объекту, чей метод join был вызван.
Наконец, в случае простых операций слияния индекса с индексом можно передать список объектов DataFrame методу join в качестве альтернативы использованию более общей функции concat, которая описана ниже: