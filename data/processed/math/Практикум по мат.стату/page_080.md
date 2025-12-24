---
source_image: page_080.png
page_number: 80
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.67
tokens: 5552
characters: 1459
timestamp: 2025-12-24T07:39:41.385372
finish_reason: stop
---

Решение на языке Python.
import scipy.stats as sts
import numpy as np # загрузка модулей
n = 200
observed_frequencies = np.array ([70, 78, 34, 13, 4, 1])
# наблюдаемые частоты
X = np.arange (0, 6) # значения случайной величины — от 0 до 5.
lambd = np.sum (observed_frequencies*X) /n # оценка параметра lambda
    # распределения Пуассона,
    # совпадающая с выборочным средним
P = np.zeros(6) # заготовка массива для теоретических вероятностей
poisson_rv = st.poisson(lambd) # функция для работы с распределением Пуассона с параметром lambd
for i in range (5): # вычисление теоретических вероятностей pi
    # функция poisson_rv.pmf(i) вычисляет вероятности
    # по формуле Пуассона
    P[i] = poisson_rv.pmf(i)
P[5] = 1-np.sum(P) # последнюю шестую вероятность вычисляем
    # как дополнение до 1 суммы предыдущих
expected_frequencies = n*P # вычисляем ожидаемые частоты npi
print(expected_frequencies)
    # 71.40139211, 73.54343388, 37.87486845, 13.00370483,
    # 3.34845399, 0.82814673
# Среди значений ожидаемых частот есть значения npi < 5;
    # объединяем последние три значения массивов
    # observed_frequencies и expected_frequencies
expected_frequencies_new = expected_frequencies[0:4]
expected_frequencies_new[3] = np.sum(expected_frequencies[3:6])
observed_frequencies_new = observed_frequencies[0:4]
observed_frequencies_new[3] = np.sum(observed_frequencies[3:6])
    # вызываем функцию, осуществляемую
    # расчет по критерию \( \chi^2 \)