---
source_image: page_400.png
page_number: 400
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.14
tokens: 7685
characters: 1705
timestamp: 2025-12-24T02:51:22.865962
finish_reason: stop
---

Out[20]:
    x0   x1   y  strings
0   1  0.01 -1.5      a
1   2 -0.01  0.0      b
2   3  0.25  3.6      c
3   4 -4.10  1.3      d
4   5  0.00 -2.0      e

In [21]: df3.to_numpy()
Out[21]:
array([[1, 0.01, -1.5, 'a'],
       [2, -0.01, 0.0, 'b'],
       [3, 0.25, 3.6, 'c'],
       [4, -4.1, 1.3, 'd'],
       [5, 0.0, -2.0, 'e']], dtype=object)

Для некоторых моделей нужно использовать лишь подмножество столбцов. Я рекомендую loc-индексирование в сочетании с to_numpy:

In [22]: model_cols = ['x0', 'x1']

In [23]: data.loc[:, model_cols].to_numpy()
Out[23]:
array([[1., 0.01],
       [2., -0.01],
       [3., 0.25],
       [4., -4.1],
       [5., 0.]])]

В некоторые библиотеки уже встроена поддержка pandas, и часть работы они делают автоматически: выполняют преобразование в NumPy из DataFrame и при-соединяют имена параметров модели к столбцам выходных таблиц или объектов Series. Если это не так, то такое «управление метаданными» ложится на вас.

В разделе 7.5 мы рассматривали тип pandas Categorical и функцию pandas.get_dummies. Пусть в нашем наборе данных имеется нечисловой столбец:

In [24]: data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'], categories=['a', 'b'])

In [25]: data
Out[25]:
    x0   x1   y  category
0   1  0.01 -1.5      a
1   2 -0.01  0.0      b
2   3  0.25  3.6      a
3   4 -4.10  1.3      a
4   5  0.00 -2.0      b

Если бы мы хотели заменить столбец 'category' индикаторными переменными, то создали бы индикаторные переменные, удалили столбец 'category' и выполнили бы операцию соединения:

In [26]: dummies = pd.get_dummies(data.category, prefix='category')

In [27]: data_with_dummies = data.drop('category', axis=1).join(dummies)

In [28]: data_with_dummies