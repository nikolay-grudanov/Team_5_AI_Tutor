---
source_image: page_396.png
page_number: 396
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.74
tokens: 7348
characters: 1165
timestamp: 2025-12-24T02:50:57.457993
finish_reason: stop
---

In [279]: corr = returns.rolling(125, min_periods=100).corr(spx_rets)

In [280]: corr.plot()

![Корреляция доходности нескольких акций с индексом S&P 500, рассчитанная за шесть месяцев](../images/11_9.png)

Рис. 11.9. Корреляция доходности нескольких акций с индексом S&P 500, рассчитанная за шесть месяцев

Скользящие оконные функции, определенные пользователем

Метод apply скользящего окна rolling и других подобных объектов позволяет применить произвольную функцию, принимающую массив, к скользящему окну. Единственное требование заключается в том, что функция должна порождать только одно скалярное значение (производить редукцию) для каждого фрагмента массива. Например, при вычислении выборочных квантилей с помощью rolling(...).quantile(q) нам может быть интересен процентильный ранг некоторого значения относительно выборки. Это можно сделать с помощью функции scipy.stats.percentileofscore (график показан на рис. 11.10):

In [282]: from scipy.stats import percentileofscore

In [283]: def score_at_2percent(x):
    .....: return percentileofscore(x, 0.02)

In [284]: result = returns["AAPL"].rolling(250).apply(score_at_2percent)

In [285]: result.plot()