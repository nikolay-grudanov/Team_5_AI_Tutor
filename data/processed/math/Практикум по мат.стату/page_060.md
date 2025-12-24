---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.59
tokens: 5606
characters: 1448
timestamp: 2025-12-24T07:39:24.294256
finish_reason: stop
---

P-value = \( P(\chi_k^2 > \chi_{\text{набл}}^2) = P(\chi_9^2 > 9,36773) = \) ХИ2.РАСП.ПХ (514,94; 5) = 0,404.

Нулевая гипотеза будет приниматься на любом уровне значимости, не превосходящем 0,404, в частности при \( a = 0,05 \).

Решение задачи на языке Python.

Проверку гипотезы по критерию \( \chi^2 \) в языке Python осуществляет функция chisquare модуля scipy.stats.

Импортируем библиотеки: scipy.stats — для вызова программы расчета по критерию с \( \chi^2 \) (sts.chisquare); numpy — для работы с массивами.

import scipy.stats as sts
import numpy as np
n = 10002 # Объем выборки
observed_frequencies = np.array([968, 1026, 1021, 974, 1014, 1046, 1021, 970, 948, 1014]) # Формирование массива исходных данных (значения ni)
M = np.full(10, 0.1) # массив длиной 10 с теоретическими вероятностями pi = 0,1
expected_frequencies = M*n # ожидаемые частоты n*pi
chisq, p = sts.chisquare(f_obs = observed_frequencies,
                        f_exp = expected_frequencies)
# параметры: f_obs — наблюдаемые частоты, f_exp — теоретические частоты
# Выходные параметры функции:
# первый параметр, chisq — наблюдаемое значение статистики,
# второй параметр p — P-значение
print ('chi2 = ', chisq)
print ('p-value =', p)
Результат работы программы:
chi2 = 9.36772645471
p-value = 0.404045207515
Наблюдаемое значение статистики: 9.37, P-значение: 0.4. Так как P-значение больше 0.05, гипотеза \( H_0 \) принимается.
Ответ: Гипотеза \( H_0 \) принимается.