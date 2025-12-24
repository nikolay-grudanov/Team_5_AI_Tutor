---
source_image: page_064.png
page_number: 64
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 13.83
tokens: 5376
characters: 841
timestamp: 2025-12-24T07:39:22.126580
finish_reason: stop
---

Z = exp_rv.rvs (n)
X1 = Y + Z
X = np.sort (X1)
FX = 1 – np.exp(–0.5*X)

In1 = np.arange(1, n+1)/n

In2 = np.arange(0,n)/n

Dn1 = np.max(In1–FX)

print(Dn1)
# Результат: 0.060237971290968861

Dn2 = np.max(FX-In2)
print(Dn2)
# Результат: 0.1836021368099004

Dn = max(Dn1, Dn2)*np.sqrt(n) # наблюдаемое значение статистики Dn
print(Dn)
Результат: 2.0357309060655249

В языке Python в модуле scipy.stats имеется функция kstest(), реализующая проверку гипотезы \( H_0 \) с помощью критерия Колмогорова-Смирнова.

Соответствующая команда имеет вид:
sts.kstest(X, 'expon', [0, 2])
# Первый аргумент — массив выборочных данных.
# Второй аргумент — строка, указывающая тип
    # гипотетического распределения.
# Третий аргумент — параметры гипотетического распределения;
# должны быть оформлены в виде списка (в языке Python —
# в квадратных скобках.