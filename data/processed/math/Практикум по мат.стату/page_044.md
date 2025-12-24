---
source_image: page_044.png
page_number: 44
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.83
tokens: 5422
characters: 916
timestamp: 2025-12-24T07:39:05.933110
finish_reason: stop
---

6. Статистические распределения в Excel, MatCalc, R и Python

MatCalc:    Flaw(5,15).q(0.9)
R:          qf(0.9, 5, 15)
Python:     \( F = \text{sts.f}(5,15) \)
            \( F.\text{ppf}(0.9) \)

3. Функция распределения.
Значение функции распределения \( F(x) \) случайной величины \( F_{k_1;k_2} \) находится с использованием следующих функций.

Excel:      F.ПАСП(x; k_1; k_2; ИСТИНА)
MatCalc:    Flaw(k_1,k_2).pl(x)
R:          pf(x, k_1, k_2)
Python:     \( F = \text{sts.f}(x, k_1, k_2) \)
            \( F.\text{cdf}(x) \)

Пример. Пусть \( X \) имеет \( F \)-распределение с 5 и 15 степенями свободы. Значение функции распределения \( F(2,9013) = 0,95 \) в точке \( x = 2,9013 \) находится с использованием следующих функций.

Excel:      F.ПАСП(2,9013; 5; 15; 1)
MatCalc:    Flaw(5,15).pl(2.9013)
R:          pf(2.9013, 5, 15)
Python:     \( F = \text{sts.f}(5,15) \)
            \( F.\text{cdf}(2.9013) \)