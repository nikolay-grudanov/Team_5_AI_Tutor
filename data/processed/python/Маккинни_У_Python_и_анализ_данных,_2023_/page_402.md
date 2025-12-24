---
source_image: page_402.png
page_number: 402
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.64
tokens: 7504
characters: 1138
timestamp: 2025-12-24T02:51:16.811471
finish_reason: stop
---

0.0
3.6
1.3
-2.0
Terms:
'y' (column 0)

In [34]: X
Out[34]:
DesignMatrix with shape (5, 3)
    Intercept   x0   x1
      1         1   0.01
      1         2  -0.01
      1         3   0.25
      1         4  -4.10
      1         5   0.00
Terms:
'Intercept' (column 0)
'x0' (column 1)
'x1' (column 2)

Эти объекты класса Patsy DesignMatrix являются массивами NumPy ndarray с дополнительными метаданными:

In [35]: np.asarray(y)
Out[35]:
array([[-1.5],
       [ 0. ],
       [ 3.6],
       [ 1.3],
       [-2. ]])

In [36]: np.asarray(X)
Out[36]:
array([[ 1.,  1.,  0.01],
       [ 1.,  2., -0.01],
       [ 1.,  3.,  0.25],
       [ 1.,  4., -4.1 ],
       [ 1.,  5.,  0. ]])

Вам, наверное, интересно, откуда взялся свободный член — терм Intercept. Это соглашение, принятое для таких линейных моделей, как регрессия методом обыкновенных наименьших квадратов. Свободный член можно подавить, добавив в модель терм + θ:

In [37]: patsy.dmatrices('y ~ x0 + x1 + θ', data)[1]
Out[37]:
DesignMatrix with shape (5, 2)
    x0   x1
      1   0.01
      2  -0.01
      3   0.25
      4  -4.10
      5   0.00
Terms:
'x0' (column 0)
'x1' (column 1)