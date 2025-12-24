---
source_image: page_139.png
page_number: 139
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.26
tokens: 7384
characters: 1454
timestamp: 2025-12-24T00:54:57.663794
finish_reason: stop
---

In[30]: ind = pd.Index([2, 3, 5, 7, 11])
    ind

Out[30]: Int64Index([2, 3, 5, 7, 11], dtype='int64')

Объект Index как неизменяемый массив

Объект Index во многом ведет себя аналогично массиву. Например, для извлечения из него значений или срезов можно использовать стандартную нотацию индексации языка Python:

In[31]: ind[1]

Out[31]: 3

In[32]: ind[::2]

Out[32]: Int64Index([2, 5, 11], dtype='int64')

У объектов Index есть много атрибутов, знакомых нам по массивам NumPy:

In[33]: print(ind.size, ind.shape, ind.ndim, ind.dtype)

5 (5,) 1 int64

Одно из различий между объектами Index и массивами NumPy — неизменяемость индексов, то есть их нельзя модифицировать стандартными средствами:

In[34]: ind[1] = 0

---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-34-40e631c82e8a> in <module>()
----> 1 ind[1] = 0

/Users/jakevdp/anaconda/lib/python3.5/site-packages/pandas/indexes/base.py ...
   1243
   1244     def __setitem__(self, key, value):
-> 1245         raise TypeError("Index does not support mutable operations")
   1246
   1247     def __getitem__(self, key):

TypeError: Index does not support mutable operations

Неизменяемость делает безопаснее совместное использование индексов несколькими объектами DataFrame и массивами, исключая возможность побочных эффектов в виде случайной модификации индекса по неосторожности.