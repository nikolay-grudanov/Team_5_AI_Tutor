---
source_image: page_072.png
page_number: 72
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.67
tokens: 5508
characters: 1928
timestamp: 2025-12-24T07:07:05.489586
finish_reason: stop
---

* **464.** Пусть

\[
f(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 + a_4 x^4,
\]
\[
g(x) = b_0 + b_1 x + b_2 x^2 + b_3 x^3 + b_4 x^4,
\]
\[
h(x) = c_0 + c_1 x + c_2 x^2 + c_3 x^3 + c_4 x^4
\]

и
\[
(x - \alpha)(x - \beta)(x - \gamma) = x^3 + px^2 + qx + r.
\]

Показать, что

\[
\begin{vmatrix}
f(\alpha) & f(\beta) & f(\gamma) \\
g(\alpha) & g(\beta) & g(\gamma) \\
h(\alpha) & h(\beta) & h(\gamma)
\end{vmatrix}
=
\begin{vmatrix}
1 & \alpha & \alpha^2 \\
1 & \beta & \beta^2 \\
1 & \gamma & \gamma^2
\end{vmatrix}
\cdot
\begin{vmatrix}
a_0 & a_1 & a_2 & a_3 & a_4 \\
b_0 & b_1 & b_2 & b_3 & b_4 \\
c_0 & c_1 & c_2 & c_3 & c_4 \\
r & q & p & 1 & 0 \\
0 & r & q & p & 1
\end{vmatrix}.
\]

**465.** Говорят, что определитель

\[
D =
\begin{vmatrix}
a_{11} & \ldots & a_{1n} & x_{11} & \ldots & x_{1k} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
a_{n1} & \ldots & a_{nn} & x_{n1} & \ldots & x_{nk} \\
y_{11} & \ldots & y_{1n} & 0 & \ldots & 0 \\
y_{k1} & \ldots & y_{kn} & 0 & \ldots & 0
\end{vmatrix}
\]

получен окаймлением при помощи \( k \) строк и \( k \) столбцов из определителя:

\[
\Delta =
\begin{vmatrix}
a_{11} & \ldots & a_{1n} \\
\ldots & \ldots & \ldots \\
a_{n1} & \ldots & a_{nn}
\end{vmatrix}.
\]

Показать, что при \( k > n \) \( D = 0 \), а при \( k \leq n \) \( D \) является формой (т. е. однородным многочленом) степени \( n - k \) относительно элементов \( a_{ij} \) определителя \( \Delta \) и формой степени \( 2k \) относительно окаймляющих элементов \( x_{ij}, y_{ij} \), коэффициентами которой служат алгебраические дополнения миноров \( k \)-го порядка в определителе \( \Delta \). А именно, доказать, что

\[
D = (-1)^k \sum A_{i_1 i_2 \ldots i_k j_1 j_2 \ldots j_k} X_{i_1 i_2 \ldots i_k} Y_{j_1 j_2 \ldots j_k},
\]

где \( A_{i_1 i_2 \ldots i_k j_1 j_2 \ldots j_k} \) есть алгебраическое дополнение минора определителя \( \Delta \), стоящего в строках с номерами \( i_1, i_2, \ldots, i_k \)