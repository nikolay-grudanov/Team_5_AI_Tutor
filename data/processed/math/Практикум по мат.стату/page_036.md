---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.79
tokens: 5460
characters: 1301
timestamp: 2025-12-24T07:38:46.360397
finish_reason: stop
---

6. Статистические распределения в Excel, MatCalc, R и Python

Ниже перечисляются функции Excel, MatCalc, R и Python, позволяющие вычислять процентные точки, а также значения функций распределения и плотности распределения для некоторых законов распределения.

Если есть намерение использовать статистические функции языка Python, то предварительно должна быть импортирована библиотека scipy.stats. Всюду в дальнейшем предполагается, что выполнена команда импортирования этой библиотеки под именем sts:
import scipy.stats as sts

Нормальный закон распределения

1. Процентная точка.
100\( \alpha \)-процентная точка \( z_{\alpha} \) стандартной нормально распределенной случайной величины находится с использованием следующих функций.
Excel:      НОРМ.СТ.ОБР(1 - \( \alpha \))
MatCalk:    nlaw(0,1).q(1 - \( \alpha \))
R:          norm(p = \( \alpha \), mean=0, s = 1, lower.tail=FALSE)
или кратко: qnorm(\( \alpha \), lower.tail=FALSE)
Python:     sts.norm.isf(\( \alpha \))

Пример. Значение 5%-й точки стандартного нормального распределения \( z_{0.05} = 1,6449 \) находится с использованием следующих функций.
Excel:      НОРМ.СТ.ОБР(0,95)
MatCalk:    nlaw(0,1).q(0.95)
R:          qnorm(0.05, lower.tail=FALSE) (qnorm(0.95, lower.tail=TRUE), или короче, qnorm(0.95))
Python:     sts.norm.isf(0.05)