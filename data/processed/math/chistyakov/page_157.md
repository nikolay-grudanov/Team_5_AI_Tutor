---
source_image: page_157.png
page_number: 157
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.23
tokens: 5217
characters: 1687
timestamp: 2025-12-24T07:29:49.845953
finish_reason: stop
---

Если случайные величины \( \xi_1, \xi_2, \ldots, \xi_n, \ldots \) независимы, \( P(\xi_n = 1) = 1 - P(\xi_n = 0) = p \), то при \( n \to \infty, 0 < p < 1 \)

\[
P \left( \frac{\xi_1 + \xi_2 + \ldots + \xi_n - nM_{\xi_1}}{\sqrt{nD_{\xi_1}}} < x \right) \to \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{u^2}{2}} du \tag{2.1}
\]

равномерно по \( x \in (-\infty, \infty) \).

Утверждение (2.1) сохраняется при достаточно общих предположениях о законе распределения слагаемых \( \xi_k \).

Докажем следующую теорему.

Теорема 2.1. Если случайные величины \( \xi_1, \xi_2, \ldots, \xi_n, \ldots \) независимы, одинаково распределены и имеют конечную дисперсию, то при \( n \to \infty \) равномерно по \( x \in (-\infty, \infty) \)

\[
P \left( \frac{\xi_1 + \xi_2 + \ldots + \xi_n - na}{\sigma \sqrt{n}} < x \right) \to \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{x} e^{-\frac{u^2}{2}} du,
\]

где \( a = M_{\xi_n}, \sigma^2 = D_{\xi_n} \).

Доказательство. Положим

\[
\eta_n = \frac{\xi_1 + \xi_2 + \ldots + \xi_n - na}{\sigma \sqrt{n}} = \sum_{k=1}^{n} \frac{\xi_k - a}{\sigma \sqrt{n}}.
\]

Разложим характеристическую функцию величин \( \xi_k - a \) по формуле (7.2.10):

\[
f_{\xi_k - a}(t) = 1 + itM(\xi_k - a) - \frac{t^2}{2} M(\xi_k - a)^2 + t^2 \varepsilon(t),
\]

где \( \varepsilon(t) \to 0 \) при \( t \to 0 \). Так как \( M(\xi_k - a) = 0 \) и \( M(\xi_k - a)^2 = \sigma^2 \), то

\[
f_{\xi_k - a}(t) = 1 - \frac{t^2 \sigma^2}{2} + t^2 \varepsilon(t). \tag{2.2}
\]

Отметим, что в этом равенстве функция \( \varepsilon(t) \) не зависит от \( k \). По теореме 2.3 гл. 7

\[
f_{\sum_{k=1}^{n} (\xi_k - a)}(t) = \left( 1 - \frac{t^2 \sigma^2}{2} + t^2 \varepsilon(t) \right)^n.
\]