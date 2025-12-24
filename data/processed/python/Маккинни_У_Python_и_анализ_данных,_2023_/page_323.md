---
source_image: page_323.png
page_number: 323
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.15
tokens: 7743
characters: 1763
timestamp: 2025-12-24T02:48:54.358541
finish_reason: stop
---

Обход групп
Объект, возвращенный groupby, поддерживает итерирование, в результате которого генерируется последовательность 2-кортежей, содержащих имя группы и блок данных. Взгляните на следующий код:

In [32]: for name, group in df.groupby("key1"):
    ....:     print(name)
    ....:     print(group)
    ....:
a
   key1  key2   data1   data2
0    a      1 -0.204708  0.281746
1    a      2  0.478943  0.769023
5    a    <NA>  1.393406  0.274992
b
   key1  key2   data1   data2
3    b      2 -0.555730  1.007189
4    b      1  1.965781 -1.296221

В случае нескольких ключей первым элементом кортежа будет кортеж, содержащий значения ключей:

In [33]: for (k1, k2), group in df.groupby(["key1", "key2"]):
    ....:     print((k1, k2))
    ....:     print(group)
    ....:
('a', 1)
   key1  key2   data1   data2
0    a      1 -0.204708  0.281746
('a', 2)
   key1  key2   data1   data2
1    a      2  0.478943  0.769023
('b', 1)
   key1  key2   data1   data2
4    b      1  1.965781 -1.296221
('b', 2)
   key1  key2   data1   data2
3    b      2 -0.555730  1.007189

Разумеется, только вам решать, что делать с блоками данных. Возможно, пригодится следующий односторочный код, который строит словарь блоков:

In [34]: pieces = {name: group for name, group in df.groupby("key1")}

In [35]: pieces["b"]
Out[35]:
   key1  key2   data1   data2
3    b      2 -0.555730  1.007189
4    b      1  1.965781 -1.296221

По умолчанию метод groupby группирует по оси axis="index", но можно задать любую другую ось. Например, в нашем примере столбцы объекта df можно было бы сгруппировать по тому, начинаются они с "key" или "data":

In [36]: grouped = df.groupby({"key1": "key", "key2": "key",
    ....:                         "data1": "data", "data2": "data"}, axis="columns")