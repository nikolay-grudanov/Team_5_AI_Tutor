---
source_image: page_460.png
page_number: 460
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.02
tokens: 6542
characters: 2102
timestamp: 2025-12-24T08:20:09.757955
finish_reason: stop
---

где матрицы \( A_i, B_i \) квадратные. Легко проверить, что

\[
A_1 B_1 = \begin{pmatrix}
c_0 & c_1 & \ldots & c_{n-1} & c_n \\
0 & c_0 & \ldots & c_{n-2} & c_{n-1} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & \ldots & c_0 & c_1 \\
0 & 0 & \ldots & 0 & c_0
\end{pmatrix} = B_1 A_1,
\]

где \( c_k = \sum_{i=0}^k a_i b_{k-i} \). Поэтому

\[
\begin{pmatrix}
I & 0 \\
-B_1 & A_1
\end{pmatrix}
\begin{pmatrix}
A_1 & A_2 \\
B_1 & B_2
\end{pmatrix}
=
\begin{pmatrix}
A_1 & A_2 \\
0 & A_1 B_2 - B_1 A_2
\end{pmatrix},
\]

а так как \( |A_1| = a_0^n \neq 0 \), то \( R(f, g) = |A_1 B_2 - B_1 A_2| \).

Пусть \( c_{pq} = a_p b_q - a_q b_p \). Легко проверить, что \( A_1 B_2 - B_1 A_2 = \| w_{ij} \|_1^n \), где \( w_{ij} = \sum c_{pq} \) и суммирование ведётся по таким парам \((p, q)\), что \( p + q = n + j - i, p \leq n - i \) и \( q \geq j \). А так как \( c_{\alpha \beta} + c_{\alpha+1, \beta-1} + \ldots + c_{\beta \alpha} = 0 \) при \( \alpha \leq \beta \), то можно ограничиться теми парами, для которых

\[
p \leq \min(n - i, j - 1).
\]

Например, при \( n = 4 \) получим матрицу

\[
\begin{pmatrix}
c_{04} & c_{14} & c_{24} & c_{34} \\
c_{03} & c_{04} + c_{13} & c_{14} + c_{23} & c_{24} \\
c_{02} & c_{03} + c_{12} & c_{04} + c_{13} & c_{14} \\
c_{01} & c_{02} & c_{03} & c_{04}
\end{pmatrix}.
\]

Если

\[
J = \begin{pmatrix}
0 & \ldots & 1 \\
1 & \ldots & 0
\end{pmatrix},
\]

то матрица \( Z = \| w_{ij} \|_1^n J \) симметрична; её называют безумианой (или матрицей Безу) многочленов \( f \) и \( g \). При этом \( z_{ij} = w_{i, n-j+1} = \sum c_{pq} \), где \( p + q = 2n + 1 - i - j \) и \( p \leq \min(n - i, n - j) \).

**Теорема 49.3.1.** *Пусть \( f \) и \( g \) — многочлены степени \( n \). Тогда*

\[
\frac{f(x)g(y) - f(y)g(x)}{x - y} = \sum_{p, q=0}^{n-1} z_{p+1, q+1} x^p y^q,
\]

*где \( Z = \| z_{ij} \|_1^n \) — матрица Безу многочленов \( f \) и \( g \).*

**Доказательство.** Если \( \alpha > \beta \), то

\[
\frac{x^\alpha y^\beta - x^\beta y^\alpha}{x - y} = x^\beta y^\beta \sum_{k+l=\beta-\alpha-1} x^k y^l = \sum_{k+l=\beta-\alpha-1} x^{k+\beta} y^{l+\beta}.
\]