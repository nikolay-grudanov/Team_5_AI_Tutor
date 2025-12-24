---
source_image: page_406.png
page_number: 406
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.18
tokens: 7481
characters: 1189
timestamp: 2025-12-24T02:51:20.684702
finish_reason: stop
---

Числовые столбцы можно интерпретировать как категориальные с помощью функции C:

In [56]: y, X = patsy.dmatrices('v2 ~ C(key2)', data)

In [57]: X
Out[57]:
DesignMatrix with shape (8, 2)
    Intercept   C(key2)[T.1]
    1           0
    1           1
    1           0
    1           1
    1           0
    1           1
    1           0
    1           0
Terms:
    'Intercept' (column 0)
    'C(key2)' (column 1)

Если в модели несколько категориальных термов, то ситуация осложняется, поскольку можно включать термы взаимодействия вида key1:key2, например в моделях дисперсионного анализа (ANOVA):

In [58]: data['key2'] = data['key2'].map({0: 'zero', 1: 'one'})

In [59]: data
Out[59]:
   key1  key2   v1   v2
0   0     a zero  1 -1.0
1   1     a one   2  0.0
2   2     b zero  3  2.5
3   3     b one   4 -0.5
4   4     a zero  5  4.0
5   5     b one   6 -1.2
6   6     a zero  7  0.2
7   7     b zero  8 -1.7

In [60]: y, X = patsy.dmatrices('v2 ~ key1 + key2', data)

In [61]: X
Out[61]:
DesignMatrix with shape (8, 3)
    Intercept   key1[T.b]   key2[T.zero]
    1           0           1
    1           0           0
    1           1           1
    1           1           0