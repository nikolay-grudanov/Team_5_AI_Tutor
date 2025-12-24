---
source_image: page_072.png
page_number: 72
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.99
tokens: 5479
characters: 1230
timestamp: 2025-12-24T07:39:34.832323
finish_reason: stop
---

Решение примера на языке Python.

Импортируем библиотеки: scipy.stats — для вызова программы расчета по критерию \( \chi^2 \) (sts.chisquare) и расчета вероятностей биномиального распределения (sts.binom); numpy — для работы с массивами.

import scipy.stats as sts
import numpy as np
N = 300
n = 10
X = np.arange(0, 11) # значения случайной величины от 0 до 10
observed_frequencies = np.array([13, 17, 15, 35, 10, 9, 40, 51, 45, 33, 32])    # наблюдаемые частоты значений
x_v = np.sum(observed_frequencies*X)/N # выборочное среднее
p_v = x_v/n
P = np.zeros(11)
binomial_rv = sts.binom(n, p_v) # функция для работы
# с биномиальным распределением
for i in range (11): # вычисление вероятностей pi
    P[i] = binomial_rv.pmf(i) # функция binomial_rv.pmf вычисляет
        # веротности pi биномиального распределения
expected_frequencies = N*P # ожидаемые частоты N*pi
chisq, p = st.chisquare(f_obs = observed_frequencies,
    f_exp = expected_frequencies, ddof=1)
# программа расчета по критерию хи-квадрат. Параметр ddof задает
    # число параметров распределения, оцениваемых по выборке
    # (оценивалась вероятность p)
print('chi2 = ', chisq)
print('p-value =', p)
Результат работы программы:
chi2 = 7164.53938864
p-value = 0.0