---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.98
tokens: 5570
characters: 1326
timestamp: 2025-12-24T07:39:08.266435
finish_reason: stop
---

6. Статистические распределения в Excel, MatCalc, R и Python

Python:
    student = sts.t(30)
    \( t_{30;0.1} = \) student.isf(0.1) = 1,3104

2. Квантиль
Квантиль \( x_\alpha \) случайной величины, распределенной по закону Стьюдента с \( k \) степенями свободы, находится с использованием следующих функций.
Excel:    СТЫЮДЕНТ.ОБР(\( \alpha; k \))
MatCalc:  tlaw(k).q(\( \alpha \))
R:        \( t_{k;\alpha} = qt(\alpha, k) \)
Python:   student = sts.t(k)
           student.ppf(\( \alpha \))

Пример. Пусть \( X \sim T_{30} \). Квантиль \( x_{0.95} = 1,6973 \) порядка 0,95 определяется с помощью следующих функций
Excel:    СТЫЮДЕНТ.ОБР(0,95; 30)
MatCalc:  tlaw(30).q(0.95)
R:        qt(0.95, 30).
Python:   student = sts.t(30)
           student.ppf(0.95).

3. Функция распределения.
Значение функции распределения \( F(x) \) случайной величины \( T_k \) в точке \( x \) находится с использованием следующих функций.
Excel:    СТЫЮДЕНТ.ПАСП(x; k; ИСТИНА)
MatCalc:  tlaw(k).pl(x)
R:        pt(x,k)
Python:   student = sts.t(k)
           student.cdf(x)

Пример. Пусть \( X \) имеет распределение Стьюдента с 30 степенями свободы. Значение функции распределения \( F(1,3104) = 0,9 \) в точке \( x = 1,3104 \) находится с использованием следующих функций.
Excel:    СТЫЮДЕНТ.ПАСП(1,3104; 30; 1)
MatCalc:  tlaw(30).pl(1.3104)