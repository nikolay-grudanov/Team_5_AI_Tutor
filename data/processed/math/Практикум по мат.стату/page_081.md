---
source_image: page_081.png
page_number: 81
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.85
tokens: 5479
characters: 1273
timestamp: 2025-12-24T07:39:41.329928
finish_reason: stop
---

7. Примеры

chisq, p = sts.chisquare(f_obs = observed_frequencies_new,
f_exp = expected_frequencies_new, ddof=1)
print('chi2 = ', chisq)
print('p-value =', p)

Результат:
chi2 = 0.733098191813
p-value = 0.693122106189

P-значение равно 0,6931. Нулевая гипотеза на уровне значимости \( \alpha = 0,05 \) принимается.

Решение на языке R.
Для решения в R понадобится модуль "vcd". Если он отсутствует, нужно его загрузить командой install.packages.
install.packages("vcd")
library("vcd")
n <- 200
observed_frequencies <- c(70, 78, 34, 13, 4, 1) # наблюдаемые частоты
X <- c(0, 1, 2, 3, 4, 5) # значения случайной величины
# Используемая далее функция goodfit в качестве первого параметра
# принимает матрицу, состоящую из двух столбцов.
# В первом столбце располагаются наблюдаемые частоты,
# а во втором — соответствующие им значения случайной величины.
M <- cbind(observed_frequencies, X) # функция cbind формирует
    # матрицу из двух векторов-столбцов
gf <- goodfit(M, type = "poisson", method = "MinChisq")
    # Функция goodfit реализует проверку гипотезы.
    # Параметр type задает гипотетический закон распределения
    # (Пуассона), при задании параметра method = «MinChisq» будет производится расчет по критерию \( \chi^2 \)
summary(gf) # вывод результатов расчета