---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.74
tokens: 12075
characters: 1900
timestamp: 2025-12-24T07:36:44.242180
finish_reason: stop
---

Пример 70 (стандартное нормальное распределение \( N_{0,1} \)). Математическое ожидание этого распределения существует, поскольку \( E| | < \infty \):

\[
E| | = \frac{2}{\sqrt{2\pi}} \int_0^{\infty} x e^{-x^2/2} dx = \frac{2}{\sqrt{2\pi}} \int_0^{\infty} e^{-x^2/2} d(x^2/2) = \frac{2}{\sqrt{2\pi}} < \infty.
\]

Математическое ожидание равно

\[
E = \int_{-\infty}^{\infty} x f(x) dx = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x e^{-x^2/2} dx = 0,
\]

т. к. интеграл сходится, а подынтегральная функция нечётна. Далее,

\[
E^2 = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} x^2 e^{-x^2/2} dx = \frac{2}{\sqrt{2\pi}} \int_0^{\infty} x^2 e^{-x^2/2} dx = -\frac{2}{\sqrt{2\pi}} \int_0^{\infty} x de^{-x^2/2} =
\]
\[
= -\frac{2x}{\sqrt{2\pi}} e^{-x^2/2}\Bigg|_0^{\infty} + 2 \int_0^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 0 + \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 1.
\]

Поэтому \( D = E^2 - (E)^2 = 1 - 0 = 1 \).

Пример 71 (нормальное распределение \( N_{a,2} \)). Мы знаем, что если \( \sim N_{a,2} \), то \( = \frac{-a}{2} \) имеет стандартное нормальное распределение. Мы только что вычислили \( E = 0, D = 1 \). Тогда (на \( \textit{каждым равенством подписать, каким свойствам оно обязано!} \))

\[
E = E(\cdot + a) = E + a = a; \quad D = D(\cdot + a) = ^2D = ^2.
\]

Итак, параметры \( a \) и \( ^2 \) нормального распределения суть его математическое ожидание и дисперсия.

Пример 72 (показательное распределение \( E \)). Найдём для произвольного натурального числа \( k \) момент порядка \( k \):

\[
E^k = \int_{-\infty}^{\infty} x^k f(x) dx = \int_0^{\infty} x^k e^{-x} dx = \frac{1}{k} \int_0^{\infty} (\cdot x)^k e^{-x} d(\cdot x) = \frac{k!}{k}.
\]

В последнем равенстве мы воспользовались гамма-функцией Эйлера:

\[
\Gamma(k+1) = \int_0^{\infty} u^k e^{-u} du = k!
\]

Тогда \( E = \frac{1}{1}, E^2 = \frac{2}{2}, D = E^2 - (E)^2 = \frac{1}{2} \).