---
source_image: page_041.png
page_number: 41
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.44
tokens: 5577
characters: 1367
timestamp: 2025-12-24T07:38:58.886104
finish_reason: stop
---

6. Статистические распределения в Excel, MatCalc, R и Python

3. Функция распределения.
Значение функции распределения случайной величины \( \chi^2_k \) в точке \( x \) находится с использованием следующих функций.

Excel:    ХИ2.РАСП(x; k; ИСТИНА)
MatCalc:  x2law(k).pl(x)
R:        pchisq(x,k)
Python:   chi = sts.chi2(20)
           chi.cdf(x)

Пример. Пусть \( X \) имеет \( \chi^2 \)-распределение с 20 степенями свободы. Значение функции распределения \( F(31,41) = 0,95 \) в точке \( x = 31,41 \) находится с помощью следующих функций.

Excel:    ХИ2.РАСП(31,41;20; 1)
MatCalc:  x2law(20).pl(31.41)
R:        pchisq(31.41, 20)
Python:   chi = sts.chi2(20)
           chi.cdf(31.41)

Распределение Стьюдента
Процентная точка.
100\( \alpha \)-процентная точка \( t_{k;\alpha} \) случайной величины, распределенной по закону Стьюдента с \( k \) степенями свободы, находится с использованием следующих функций.

Excel:    СТЫЮДЕНТ.ОБР(1 - \( \alpha \); k)
MatCalk:  tlaw(k).q(1-\( \alpha \))
R:        qt(\( \alpha \),k,lower.tail=FALSE)
Python:   student = sts.t(k)
           student.isf(\( \alpha \))

Пример. Пусть \( X \sim T_{30} \). Распределение Стьюдента с 30 степенями свободы). 10%-процентная точка \( t_{30;0,1} \) находится с помощью следующих функций.

Excel:    СТЫЮДЕНТ.ОБР(0,9; 30)
MatCalc:  tlaw(30).q(0.9)
R:        qt(0.1, 30, lower.tail=FALSE)