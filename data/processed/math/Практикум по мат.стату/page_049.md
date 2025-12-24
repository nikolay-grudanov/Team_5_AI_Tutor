---
source_image: page_049.png
page_number: 49
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.61
tokens: 5462
characters: 1090
timestamp: 2025-12-24T07:39:09.961700
finish_reason: stop
---

7. Примеры

Почему минимальное значение мощности достигается при \( \lambda = 0,1 \), а чем дальше от этого значения, тем ближе мощность к 1?

Сложно различать гипотезы \( H_0 : \lambda = \lambda_0 \) и \( H_1 : \lambda = \lambda_1 \), когда параметры \( \lambda_0 \) и \( \lambda_1 \) близки друг к другу.

И не сложно, если они далеки друг от друга.

На языке R. Строим график функции
\[
w(x) = 1 - (F(1296x) - F(742x))
\]
на интервале [0; 0,3].
x <- seq(0, 0.3, 0.001) # Значения независимой переменной
# с шагом 0,001.
plot(x, 1-(pchisq(1296*x, 100) – pchisq(742*x, 100)), type="l",
    col="blue", lty=1, pch=2, lwd=2,
    main="Функция мощности критерия", xlab="x", ylab="w(x)")

![График функции мощности критерия](../images/chapter7_1.png)

На языке Python.
import scipy.stats as sts
%matplotlib inline
import matplotlib.pyplot as plt # импорт графической библиотеки
import numpy as np # импорт библиотеки numpy
    # для работы с массивами
chi = sts.chi2(100)
chi.isf(0.975)
x = np.linspace(0, 0.3, 1000)  # Формирование 1000 значений
# независимой переменной на интервале (0; 0,3)