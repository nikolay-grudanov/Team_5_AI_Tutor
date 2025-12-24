---
source_image: page_043.png
page_number: 43
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.97
tokens: 5610
characters: 1268
timestamp: 2025-12-24T07:39:10.480555
finish_reason: stop
---

6. Статистические распределения в Excel, MatCalc, R и Python

R: pt(1.3104, 30)
Python: student = sts.t(30)
        student.cdf(1.3104)

F-распределение

1. Процентная точка.
100α-процентную точку \( f_{k_1; k_2; \alpha} \) F-распределения с \( k_1 \) и \( k_2 \) степенями свободы можно найти, вызывая следующие функции.

Excel: F.ОБР.П X(\alpha; k_1; k_2)
MatCalc: Flaw(k_1,k_2).q(1-\alpha)
R: qf(\alpha, k_1, k_2, lower.tail=FALSE)
Python: \( F = \text{sts.f}(k_1, k_2) \)
        F.isf(\alpha)

Пример. Пусть \( X \sim F_{5; 15} \). (F-распределение с 5 и 15 степенями свободы). 5%-процентная точка \( f_{5; 15; 0.05} = 2,9013 \) находится с использованием следующих функций.

Excel: F.ОБР.ПХ(0,05;5;15)
MatCalc: Flaw(5,15).q(0.95).
R: qf(0.05, 5, 15, lower.tail=FALSE)
Python: \( F = \text{sts.f}(5,15) \)
        F.isf(0.05)

2. Квантиль
Квантиль \( x_\alpha \) F-распределения с \( k_1 \) и \( k_2 \) степенями свободы можно найти, вызывая следующие функции.

Excel: F.ОБР.(\alpha; k_1; k_2)
MatCalc: Flaw(k_1,k_2).q(\alpha)
R: qf(\alpha, k_1, k_2).
Python: \( F = \text{sts.f}(k_1, k_2) \)
        F.ppf(\alpha)

Пример. Пусть \( X \sim F_{5; 15} \). Квантиль \( x_{0.9} = 2,2730 \) порядка 0,9 можно найти, используя следующие функции.
Excel: F.ОБР(0,9;5;15).