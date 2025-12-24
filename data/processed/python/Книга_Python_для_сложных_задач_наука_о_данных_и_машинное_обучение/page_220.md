---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.67
tokens: 7379
characters: 1529
timestamp: 2025-12-24T00:57:01.170993
finish_reason: stop
---

In[2]: data = ['peter', 'Paul', 'MARY', 'gUIDO']
    [s.capitalize() for s in data]

Out[2]: ['Peter', 'Paul', 'Mary', 'Guido']

Вероятно, для работы с некоторыми данными этого достаточно, но при наличии отсутствующих значений все портится. Например:

In[3]: data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
    [s.capitalize() for s in data]

---------------------------------------------------------------------------
AttributeError                                 Traceback (most recent call last)
<ipython-input-3-fc1d891ab539> in <module>()
      1 data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
----> 2 [s.capitalize() for s in data]

<ipython-input-3-fc1d891ab539> in <listcomp>(.0)
      1 data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
----> 2 [s.capitalize() for s in data]

AttributeError: 'NoneType' object has no attribute 'capitalize'

Библиотека Pandas включает средства как для работы с векторизованными строковыми операциями, так и для корректной обработки отсутствующих значений посредством атрибута str объектов Series библиотеки Pandas и содержащих строки объектов Index. Так, допустим, мы создали объект Series библиотеки Pandas с теми же данными:

In[4]: import pandas as pd
    names = pd.Series(data)
    names

Out[4]: 0    peter
        1    Paul
        2    None
        3    MARY
        4    gUIDO
       dtype: object

Теперь можно вызвать один-единственный метод для преобразования строчных букв в заглавные, который будет игнорировать любые отсутствующие значения:

In[5]: names.str.capitalize()