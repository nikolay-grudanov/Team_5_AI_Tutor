---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.91
tokens: 7278
characters: 1091
timestamp: 2025-12-24T00:56:57.160160
finish_reason: stop
---

3    eric idle
4    terry jones
5    michael palin
dtype: object

Часть других возвращает числовые значения:

In[8]: monte.str.len()

Out[8]: 0    14
         1    11
         2    13
         3     9
         4    11
         5    13
dtype: int64

Или булевы значения:

In[9]: monte.str.startswith('T')

Out[9]: 0    False
         1    False
         2     True
         3    False
         4     True
         5    False
dtype: bool

Или списки и другие составные значения для каждого элемента:

In[10]: monte.str.split()

Out[10]: 0    [Graham, Chapman]
         1    [John, Cleese]
         2    [Terry, Gilliam]
         3    [Eric, Idle]
         4    [Terry, Jones]
         5    [Michael, Palin]
dtype: object

Мы увидим манипуляции над подобными объектами типа «ряды списков», когда продолжим обсуждение.

Методы, использующие регулярные выражения

Помимо этого, существует и несколько методов, принимающих на входе регулярные выражения для проверки содержимого каждого из строковых элементов и следующих некоторым соглашениям по API встроенного модуля re языка Python (табл. 3.4).