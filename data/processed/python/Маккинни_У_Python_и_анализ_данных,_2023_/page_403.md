---
source_image: page_403.png
page_number: 403
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.29
tokens: 7604
characters: 1593
timestamp: 2025-12-24T02:51:22.807928
finish_reason: stop
---

Объекты Patsy можно передать напрямую в алгоритмы типа numpy.linalg.lstsq, который выполняет регрессию методом обыкновенных наименьших квадратов:

In [38]: coef, resid, _, _ = np.linalg.lstsq(X, y)

Метаданные модели сохраняются в атрибуте design_info, так что имена столбцов модели можно связать с найденными коэффициентами для получения объекта Series, например:

In [39]: coef
Out[39]:
array([[ 0.3129],
       [-0.0791],
       [-0.2655]])

In [40]: coef = pd.Series(coef.squeeze(), index=X.design_info.column_names)

In [41]: coef
Out[41]:
Intercept    0.312910
x0           -0.079106
x1           -0.265464
dtype: float64

Преобразование данных в формулах Patsy
В формулы Patsy можно включить код на Python; при вычислении формулы библиотека будет искать использованные функции в объемлющей области видимости:

In [42]: y, X = patsy.dmatrices('y ~ x0 + np.log(np.abs(x1) + 1)', data)

In [43]: X
Out[43]:
DesignMatrix with shape (5, 3)
   Intercept   x0   np.log(np.abs(x1) + 1)
      1        1     0.00995
      1        2     0.00995
      1        3     0.22314
      1        4     1.62924
      1        5     0.00000
Terms:
  'Intercept' (column 0)
  'x0' (column 1)
  'np.log(np.abs(x1) + 1)' (column 2)

Из часто используемых преобразований отметим стандартизацию (приведение к распределению со средним 0 и дисперсией 1) и центрирование (вычитание среднего). Для этих целей в Patsy имеются встроенные функции:

In [44]: y, X = patsy.dmatrices('y ~ standardize(x0) + center(x1)', data)

In [45]: X
Out[45]:
DesignMatrix with shape (5, 3)
   Intercept  standardize(x0)  center(x1)