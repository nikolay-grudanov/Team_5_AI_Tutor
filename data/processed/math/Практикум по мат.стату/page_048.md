---
source_image: page_048.png
page_number: 48
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.74
tokens: 5681
characters: 1404
timestamp: 2025-12-24T07:39:19.023959
finish_reason: stop
---

Когда справедлива гипотеза \( H_1 \), распределение случайной величины \( T \) нам неизвестно, но известно, что случайная величина \( 2\lambda n \overline{X} \) имеет распределение \( \chi^2_{2n} \).

Для вычисления вероятности \( P_{H_1}(T \in K) \), преобразуем статистику.

\[
P_{H_1}(T \in K) = 1 - P_{H_1}(74,2 < T < 129,6) =
= 1 - P_{H_1}(74,2 < 2\lambda_0 n \overline{X} < 129,6) =
= 1 - P_{H_1}(74,2 < 2 \cdot 0,1 \cdot n \overline{X} < 129,6).
\]

С целью получения выражения \( 2\lambda n \overline{X} \) (с известным законом распределения), умножим все составляющие неравенств на \( \lambda \):

\[
= 1 - P_{H_1}(74,2 \cdot \lambda < 2\lambda \cdot 0,1 \cdot n \overline{X} < 129,6 \cdot \lambda) =
= 1 - P_{H_1}\left(74,2 \cdot \frac{\lambda}{0,1} < 2\lambda n \overline{X} < 129,6 \cdot \frac{\lambda}{0,1}\right) =
= 1 - P(742\lambda < \chi^2_{2n} < 1296\lambda).
\]

Вероятность того, что случайная величина \( \chi^2_{2n} \) принадлежит заданному интервалу, вычисляем, используя ее функцию распределения.

В Excel — это функция: ХИ2.РАСП(x; v; 1).

\[
P_{H_1}(T \in K) = 1 - P(742\lambda < \chi^2_{2n} < 1296\lambda) = 1 - (F(1296\lambda) - F(742\lambda)) =
= 1 - (\text{ХИ2.РАСП}(1296\lambda; 100; 1) - \text{ХИ2.РАСП}(742\lambda; 100; 1)).
\]

График полученной функции:

![График w(\lambda)](https://i.imgur.com/3Q5z5QG.png)

Значение в точке \( \lambda = 0,15 \): \( w(0,15) = 0,8. \)