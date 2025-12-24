---
source_image: page_068.png
page_number: 68
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.28
tokens: 6318
characters: 1774
timestamp: 2025-12-24T08:09:19.554063
finish_reason: stop
---

Иногда используются мономиальные симметрические многочлены

\[
m_{i_1 \ldots i_n}(x_1, \ldots, x_n) = \sum_{\sigma \in S_n} x_{\sigma(1)}^{i_1} \cdots x_{\sigma(n)}^{i_n}.
\]

Производящие функции \( \sigma(t) \) и \( p(t) \) связаны соотношением

\[
\sigma(t)p(-t) = 1.
\]

Приравнивая коэффициенты при \( t^n, n \geqslant 1 \), в левой и правой части, получаем

\[
\sum_{r=0}^n (-1)^r \sigma_r p_{n-r} = 0.
\] (1)

Производящая функция \( s(t) \) выражается через \( p(t) \) и \( \sigma(t) \) следующим образом:

\[
s(t) = \frac{d}{dt} \ln p(t) = \frac{p'(t)}{p(t)}, \quad \text{т. е. } s(t)p(t) = p'(t);
\]
\[
s(-t) = -\frac{d}{dt} \ln \sigma(t) = -\frac{\sigma'(t)}{\sigma(t)}, \quad \text{т. е. } s(-t)\sigma(t) = -\sigma'(t).
\]

Приравнивая коэффициенты при \( t^{n+1} \), получаем

\[
np_n = \sum_{r=1}^n S_r p_{n-r},
\] (2)
\[
n\sigma_n = \sum_{r=1}^n (-1)^{r-1} S_r \sigma_{n-r}.
\] (3)

Соотношения (3) называют формулами Ньютона.

Запишем соотношения (1) для \( n = 1, \ldots, k \). При фиксированных \( \sigma_1, \ldots, \sigma_k \) эти соотношения можно рассматривать как систему линейных уравнений для \( p_1, \ldots, p_k \), а при фиксированных \( p_1, \ldots, p_k \) — как систему уравнений для \( \sigma_1, \ldots, \sigma_k \). Решая эти системы, находим

\[
\sigma_k = \begin{vmatrix}
p_1 & 1 & 0 & \ldots & 0 \\
p_2 & p_1 & 1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
p_{k-1} & p_{k-2} & \ldots & \ldots & 1 \\
p_k & p_{k-1} & \ldots & \ldots & p_1
\end{vmatrix}, \quad p_k = \begin{vmatrix}
\sigma_1 & 1 & 0 & \ldots & 0 \\
\sigma_2 & \sigma_1 & 1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
\sigma_{k-1} & \sigma_{k-2} & \ldots & \ldots & 1 \\
\sigma_k & \sigma_{k-1} & \ldots & \ldots & \sigma_1
\end{vmatrix}.
\]