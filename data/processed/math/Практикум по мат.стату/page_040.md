---
source_image: page_040.png
page_number: 40
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.31
tokens: 5614
characters: 1436
timestamp: 2025-12-24T07:39:00.947253
finish_reason: stop
---

6. Статистические распределения в Excel, MatCalc, R и Python

\( \chi^2 \)-распределение
1. Процентная точка
100\( \alpha \)-процентная точка \( \chi^2_{k;\alpha} \) случайной величины, распределенной по закону \( \chi^2 \) с \( k \) степенями свободы, находится с использованием следующих функций.
Excel:      ХИ2.ОБР.ПХ (\( \alpha; k \))
MatCalc:    x2law(k).q(1-\( \alpha \))
R:          qchisq(\( \alpha, k \), lower.tail=FALSE)
Python:     chi = sts.chi2(k)
            chi.isf(\( \alpha \))

Пример. Пусть \( X \sim \chi^2_{20} \) (\( \chi^2 \) распределение с 20 степенями свободы). 5%-ная точка \( \chi^2_{20;0.05} = 31,41 \) находится с помощью следующих функций.
Excel:      ХИ2.ОБР.ПХ (0,05; 20)
MatCalc:    x2law(20).q(0.95)
R:          qchisq(0.05, 20, lower.tail=FALSE)
Python:     chi = sts.chi2(20)
            chi.isf(0.05)

2. Квантиль
Квантиль \( x_\alpha \) порядка \( \alpha \) случайной величины, распределенной по закону \( \chi^2 \) с \( k \) степенями свободы, находится с использованием следующих функций.
Excel:      ХИ2.ОБР(\( \alpha; k \))
MatCalc:    x2law(k).q(\( \alpha \))
R:          qchisq(\( \alpha, k \))
Python:     chi = sts.chi2(k)

Пример. Пусть \( X \sim \chi^2_{20} \). Квантиль \( x_{0.9} = 28,41 \) порядка 0,9 находится с помощью следующих функций.
Excel:      ХИ2.ОБР(0,9; 20)
MatCalc:    x2law(20).q(0.9)
R:          qchisq(0.9, 20)
Python:     chi = sts.chi2(20)
            chi.ppf(0.9)