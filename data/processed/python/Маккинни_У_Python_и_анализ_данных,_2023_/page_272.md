---
source_image: page_272.png
page_number: 272
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.12
tokens: 7488
characters: 1205
timestamp: 2025-12-24T02:47:23.226037
finish_reason: stop
---

a    0   <NA>   <NA>
b    1   <NA>   <NA>
c    <NA> 2   <NA>
d    <NA> 3   <NA>
e    <NA> 4   <NA>
f    <NA> <NA> 5
g    <NA> <NA> 6

В данном случае на другой оси нет перекрытия, и она, как видно, является отсортированным объединением (соединением в режиме "outer") индексов. Но можно образовать и пересечение индексов, если передать параметр join="inner":

In [95]: s4 = pd.concat([s1, s3])

In [96]: s4
Out[96]:
a    0
b    1
f    5
g    6
dtype: Int64

In [97]: pd.concat([s1, s4], axis="columns")
Out[97]:
      0   1
a    0   0
b    1   1
f    <NA> 5
g    <NA> 6

In [98]: pd.concat([s1, s4], axis="columns", join="inner")
Out[98]:
      0   1
a    0   0
b    1   1

В последнем примере метки 'f' и 'g' пропали, поскольку был задан аргумент join="inner".

Проблема может возникнуть из-за того, что в результирующем объекте не видно, конкатенацией каких объектов он получен. Допустим, что вы на самом деле хотите построить иерархический индекс на оси конкатенации. Для этого используется аргумент keys:

In [99]: result = pd.concat([s1, s1, s3], keys=["one", "two", "three"])

In [100]: result
Out[100]:
one    a    0
       b    1
two    a    0
       b    1
three  f    5
       g    6
dtype: Int64