---
source_image: page_037.png
page_number: 37
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.40
tokens: 5524
characters: 1242
timestamp: 2025-12-24T07:38:50.317926
finish_reason: stop
---

2. Квантиль.
Квантиль \( x_{\alpha} \) порядка \( \alpha \) стандартного нормального закона распределения находится с помощью следующих функций.

Excel: НОРМ.СТ.ОБР (\( \alpha \))
MatCalk: nlaw(0,1).q(\( \alpha \))
R: qnorm(\( p = \alpha \), mean=0, s = 1, lower.tail=FALSE)
или кратко: qnorm(\( \alpha \))
Python: sts.norm.ppf(\( \alpha \))

Пример. Значение квантили порядка 0,9 стандартного нормального закона распределения \( x_{0,9} = 1,2816 \) находится с использованием следующих функций.
Excel: НОРМ.СТ.ОБР (0,9)
MatCalk: nlaw(0,1).q(0.9)
R: qnorm(0.9)
Python: sts.norm.ppf(0.9)

3. Функция распределения стандартного нормального распределения \( F_{0,1}(x) \)
Значение функции распределения стандартного нормального закона \( F_{0;1}(x) = \Phi(x) + 0,5 \) в точке \( x \) находится с использованием следующих функций.
Excel: НОРМ.СТ.ПАСП (x; ИСТИНА)
MatCalk: nlaw(0,1).pl(x)
R: pnorm(x, mean =0, sd = 1)
или кратко: pnorm(x)
Python: sts.norm.cdf(x, loc=0, scale=1)
или кратко: sts.norm.cdf(x)

Пример. Пусть \( X \sim N(0; 1) \). Значение функции распределения \( F_{0;1}(1) = 0,8413 \) в точке \( x = 1 \) находится с помощью следующих функций.
Excel: НОРМ.СТ.ПАСП (1; 1)
MatCalk: nlaw(0,1).pl(1)
R: pnorm(1)
Python: sts.norm.cdf(1)