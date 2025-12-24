---
source_image: page_038.png
page_number: 38
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 14.09
tokens: 5445
characters: 1099
timestamp: 2025-12-24T07:38:50.250657
finish_reason: stop
---

4. Плотность стандартного нормального распределения \( \varphi(x) \)

Значение плотности распределения

\[
\varphi(x) = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}
\]

стандартной normally распределенной случайной величины в точке \( x \) вычисляется с использованием следующих функций.

Excel: НОРМ.СТ.ПАСП (x; ЛОЖЬ)
MatCalk: nlaw(0,1).den(x)
R: dnorm(x)
Python: sts.norm.pdf(x)

Пример. Пусть \( X \sim N(0; 1) \). Значение плотности распределения \( \varphi(0) = 0,3989 \) в точке \( x = 0 \) находится с помощью следующих функций.

Excel: НОРМ.СТ.ПАСП (0; 0)
MatCalc: nlaw(0,1).den(0)
R: dnorm(0)
Python: sts.norm.pdf(0)

5. Функция распределения \( F_{\mu;\sigma}(x) \).

Значение функции распределения normally распределенной случайной величины \( X \sim N(m; \sigma) \) с параметрами \( m \) и \( \sigma \), т.е. значение

\[
F_{\mu;\sigma}(x) = \Phi\left(\frac{x - m}{\sigma}\right) + 0,5
\]

находится с использованием следующих функций.

Excel: НОРМ.ПАСП (x; m; \sigma; ИСТИНА)
MatCalc: nlaw(m,\sigma).pl(x)
R: pnorm (x, m, \sigma)
Python: gaus = sts.norm(loc = m, scale = \sigma)
gaus.cdf(x)