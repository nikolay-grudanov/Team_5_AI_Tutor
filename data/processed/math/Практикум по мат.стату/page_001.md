---
source_image: page_001.png
page_number: 1
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.84
tokens: 5589
characters: 1194
timestamp: 2025-12-24T07:38:20.448112
finish_reason: stop
---

В. И. Глебов
С. Я. Криволапов

ПРАКТИКУМ ПО МАТЕМАТИЧЕСКОЙ СТАТИСТИКЕ
Проверка гипотез с использованием Excel, MatCalc, R и Python

χ²-распределение
1. Процентная точка
100α-процентная точка χ²_{k,α} случайной по закону χ² с k степенями свободы определяется следующими функциями.
Excel: ХИ2.ОБР.ПХ(α; k)
MatCalc: x2law(k).q(1-α)
R: qchisq(α, k, lower.tail=FALSE)
Python: chi = stats.chi2(k)
chi.isf(α)

Пример. Пусть X ~ χ²_{20} (χ² распределение с 20 степенями свободы). 5%-ная точка χ²_{20,0.05} = 31,41 находится с помощью следующих функций.
Excel: ХИ2.ОБР.ПХ(0,05; 20)
MatCalc: x2law(20).q(0.95)
R: qchisq(0.05, 20, lower.tail=FALSE)
Python: chi = stats.chi2(20)
chi.isf(0.05)

2. Квантиль
Квантиль x_α порядка α случайной величины, распределенной по закону χ² с k степенями свободы, находится с использованием следующих функций.
Excel: ХИ2.ОБР(α; k)
MatCalc: x2law(k).q(α)
R: qchisq(α, k)
Python: chi = stats.chi2(k)

Пример. Пусть X ~ χ²_{20}. Квантиль x_{0.9} = 28,41 порядка 0,9 находится с помощью следующих функций.
Excel: ХИ2.ОБР(0.9; 20)
MatCalc: x2law(20).q(0.9)
R: qchisq(0.9, 20)
Python: chi = stats.chi2(20)
chi.ppf(0.9)

Так как χ²_{набл} > χ²_{кр}, то гипотеза Н0 отклоняется.