---
source_image: page_409.png
page_number: 409
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.66
tokens: 7852
characters: 2666
timestamp: 2025-12-24T02:51:40.593886
finish_reason: stop
---

аггай([[1., -0.9005, -0.1894, -1.0279],
      [1., 0.7993, -1.546, -0.3274],
      [1., -0.5507, -0.1203, 0.3294],
      [1., -0.1639, 0.824, 0.2083],
      [1., -0.0477, -0.2131, -0.0482]])

Класс sm.OLS реализует линейную регрессию методом обыкновенных наименьших квадратов:

In [70]: model = sm.OLS(y, X)

Метод модели fit возвращает объект с результатами регрессии, содержащий оценки параметров модели и диагностическую информацию:

In [71]: results = model.fit()

In [72]: results.params
Out[72]: array([0.0668, 0.268 , 0.4505])

Метод summary объекта results печатает подробную диагностическую информацию о модели:

In [73]: print(results.summary())
OLS Regression Results
==============================================================================
Dep. Variable:                      y   R-squared (uncentered):      0.469
Model:                              OLS   Adj. R-squared (uncentered):  0.452
Method:                             Least Squares   F-statistic:           28.51
Date:     Fri, 12 Aug 2022   Prob (F-statistic):    2.66e-13
Time:         14:09:18   Log-Likelihood:             -25.611
No. Observations:                  100   AIC:                   57.22
Df Residuals:                       97   BIC:                   65.04
Df Model:                           3
Covariance Type:                nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
x1            0.0668    0.054      1.243      0.217     -0.040      0.174
x2            0.2680    0.042      6.313      0.000      0.184      0.352
x3            0.4505    0.068      6.605      0.000      0.315      0.586
==============================================================================
Omnibus:                        0.435   Durbin-Watson:               1.869
Prob(Omnibus):                    0.805   Jarque-Bera (JB):           0.301
Skew:                           0.134   Prob(JB):                     0.860
Kurtosis:                        2.995   Cond. No.                     1.64
==============================================================================
Notes:
[1] R^2 is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.

Параметрам присвоены обобщенные имена x1, x2 и т. д. Но пусть вместо этого все параметры модели хранятся в объекте DataFrame:

In [74]: data = pd.DataFrame(X, columns=['col0', 'col1', 'col2'])

In [75]: data['y'] = y