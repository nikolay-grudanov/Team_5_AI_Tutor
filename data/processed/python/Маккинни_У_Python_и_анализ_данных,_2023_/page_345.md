---
source_image: page_345.png
page_number: 345
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.03
tokens: 7458
characters: 1179
timestamp: 2025-12-24T02:49:24.652428
finish_reason: stop
---

О функция может возвращать скалярное значение, которое будет уложено на группу;
О функция может возвращать объект такой же формы, как входная группа;
О функция не должна модифицировать свой вход.
Рассмотрим в качестве иллюстрации простой пример:

In [144]: df = pd.DataFrame({'key': ['a', 'b', 'c'] * 4,
    ....:                 'value': np.arange(12.)})

In [145]: df
Out[145]:
   key  value
0    a    0.0
1    b    1.0
2    c    2.0
3    a    3.0
4    b    4.0
5    c    5.0
6    a    6.0
7    b    7.0
8    c    8.0
9    a    9.0
10   b   10.0
11   c   11.0

Вычислим групповые средние для каждого ключа:

In [146]: g = df.groupby('key')['value']

In [147]: g.mean()
Out[147]:
key
a    4.5
b    5.5
c    6.5
Name: value, dtype: float64

Но предположим, что вместо этого мы хотим получить объект Series такой же формы, как df['value'], в котором значения заменены средним, сгруппированным по 'key'. Мы можем передать методу transform функцию, которая вычисляет среднее для одной группы:

In [148]: def get_mean(group):
    ....:     return group.mean()

In [149]: g.transform(get_mean)
Out[149]:
0    4.5
1    5.5
2    6.5
3    4.5
4    5.5
5    6.5
6    4.5
7    5.5
8    6.5