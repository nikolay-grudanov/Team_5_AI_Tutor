---
source_image: page_181.png
page_number: 181
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.39
tokens: 5350
characters: 1701
timestamp: 2025-12-24T07:30:20.922488
finish_reason: stop
---

\[
\ldots, x_n \text{ и при любых значениях } \theta
\]
\[
P(\underline{\theta}(x_1, \ldots, x_n) < \theta < \overline{\theta}(x_1, \ldots, x_n)) = 1 - 2\alpha,
\]
т. е. вероятность того, что случайный интервал \((\underline{\theta}, \overline{\theta})\) накроет неизвестный параметр \(\theta\), не зависит от параметра \(\theta\). В этом случае интервал \((\underline{\theta}, \overline{\theta})\) называют доверительным интервалом для неизвестного параметра \(\theta\), соответствующим доверительной вероятности \(1 - 2\alpha\).
В ряде случаев функции \(\underline{\theta}\) и \(\overline{\theta}\), обладающие указанными свойствами, можно найти.
Пусть имеется выборка \(x_1, \ldots, x_n\), величины \(x_k\) нормально распределены с параметрами \((a, \sigma)\), параметр \(\sigma\) известен. Найдем доверительный интервал для \(a\). Случайная величина \(\bar{x} = (x_1 + \ldots + x_n)/n\) имеет нормальное распределение и
\[
M_{\bar{x}} = a, \quad D_{\bar{x}} = \frac{\sigma^2}{n}.
\]
Тогда величина
\[
\frac{\bar{x} - a}{\sigma/\sqrt{n}}
\]
распределена нормально с параметрами \((0, 1)\), и, следовательно, ее распределение не зависит от \(a\). Определяя \(u_\alpha\) как решение уравнения
\[
\frac{1}{\sqrt{2\pi}} \int_{u_\alpha}^\infty e^{-\frac{x^2}{2}} dx = \alpha,
\]
(2.6)
получим
\[
P\left( \left| \frac{\bar{x} - a}{\sigma/\sqrt{n}} \right| < u_\alpha \right) = 1 - 2\alpha
\]
или
\[
P\left( \bar{x} - u_\alpha \frac{\sigma}{\sqrt{n}} < a < \bar{x} + u_\alpha \frac{\sigma}{\sqrt{n}} \right) = 1 - 2\alpha.
\]
(2.7)
Таким образом, мы нашли доверительный интервал \(\left( \bar{x} - u_\alpha \frac{\sigma}{\sqrt{n}}, \bar{x} + u_\alpha \frac{\sigma}{\sqrt{n}} \right)\) для параметра \(a\).