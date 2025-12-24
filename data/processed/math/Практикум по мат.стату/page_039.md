---
source_image: page_039.png
page_number: 39
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.77
tokens: 5493
characters: 1097
timestamp: 2025-12-24T07:38:55.359573
finish_reason: stop
---

6. Статистические распределения в Excel, MatCalc, R и Python

Пример. Пусть \( X \sim N(5; 2) \). Значение функции распределения \( F_{5;2}(4) = 0,3085 \) в точке \( x = 4 \) определяется ется с помощью следующих функций.
Excel: НОРМ.ПАСП(4; 5; 2; 1)
MatCalc: nlaw(5,2).pl(4)
R: pnorm(4, 5, 2)
Python: gaus = sts.norm(loc=5, scale=2)
gaus.cdf(4)

6. Плотность распределения \( \varphi_{m;\sigma}(x) \).
Значение плотности распределения

\[
\varphi_{m;\sigma}(x) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-m)^2}{2\sigma^2}}
\]

случайной величины \( X \sim N(m; \sigma) \) с параметрами \( m \) и \( \sigma \) определяется с помощью следующих функций.
Excel: НОРМ.ПАСП(x; m; \sigma; ЛОЖЬ)
MatCalc: nlaw(m,\sigma).den(x)
R: dnorm (x, m, \sigma)
Python: gaus = sts.norm(loc = m, scale = \sigma)
gaus.pdf(x)

Пример. Пусть \( X \sim N(5; 2) \). Значение плотности распределения \( \varphi_{5;2}(3) = 0,1210 \) в точке \( x = 3 \) в точке находится с помощью следующих функций.
Excel: НОРМ.ПАСП(3; 5; 2; 0)
MatCalc: nlaw(5,2).den(3)
R: dnorm(3, 5, 2)
Python: gaus = sts.norm(loc=5, scale=2)
gaus.pdf(3)