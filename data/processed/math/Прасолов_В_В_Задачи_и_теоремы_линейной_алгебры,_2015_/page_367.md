---
source_image: page_367.png
page_number: 367
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.92
tokens: 6417
characters: 2161
timestamp: 2025-12-24T08:17:35.182366
finish_reason: stop
---

§ 37. Неравенства для собственных значений

Сингулярные значения

37.8. Докажите, что для любой квадратной матрицы \( A \) собственные значения матриц \( A^*A \) и \( AA^* \) одинаковые.

37.9. Докажите, что если все сингулярные значения матрицы \( A \) равны, то \( A = \lambda U \), где \( U \) — унитарная матрица.

37.10. Докажите, что если сингулярные значения матрицы \( A \) равны \( \sigma_1, \ldots, \sigma_n \), то сингулярные значения матрицы \( \operatorname{adj} A \) равны

\[
\frac{\sigma_i}{i \neq 1}, \ldots, \frac{\sigma_i}{i \neq n}.
\]

37.11. Пусть \( \sigma_1, \ldots, \sigma_n \) — сингулярные значения матрицы \( A \). Докажите, что собственными значениями матрицы

\[
\begin{pmatrix}
0 & A \\
A^* & 0
\end{pmatrix}
\]

являются числа \( \sigma_1, \ldots, \sigma_n, -\sigma_1, \ldots, -\sigma_n \).

37.12. Пусть \( A \) — сопровождающая матрица многочлена

\[
p(\lambda) = \lambda^n - a_{n-1}\lambda^{n-1} - \ldots - a_0,
\]

\( \sigma_1 \geqslant \ldots \geqslant \sigma_n \) — её сингулярные значения. Докажите, что \( \sigma_2 = \ldots = \sigma_{n-1} = 1 \), а \( \sigma_1 \) и \( \sigma_n \) являются корнями квадратного уравнения

\[
z^2 - (|a_0|^2 + \ldots + |a_{n-1}|^2 + 1)z + |a_0|^2 = 0.
\]

37.13 [Da]. Пусть \( A \) — квадратная матрица порядка \( n \), а \( B \) — матрица размером \( n \times m \), где \( n > m \). Пусть, далее, \( \alpha_1 \geqslant \ldots \geqslant \alpha_n \) — сингулярные значения матрицы \( A \), \( \beta_1 \geqslant \ldots \geqslant \beta_m \) — сингулярные значения матрицы \( B \), \( \gamma_1 \geqslant \ldots \geqslant \gamma_m \) — сингулярные значения матрицы \( C = AB \). Докажите, что

\[
\alpha_{n-m+1} \ldots \alpha_n \beta_1 \ldots \beta_m \leqslant \gamma_1 \ldots \gamma_m \leqslant \alpha_1 \ldots \alpha_m \beta_1 \ldots \beta_m.
\]

37.14 [Da]. Пусть \( H \) — положительно определённая эрмитова матрица порядка \( n \) с собственными значениями \( \lambda_1, \ldots, \lambda_n \), \( M \) — матрица размером \( n \times m \), где \( m < n \). Докажите, что

\[
\lambda_{n-m+1} \ldots \lambda_n \det(M^*M) \leqslant \det(M^*HM) \leqslant \lambda_1 \ldots \lambda_m \det(M^*M).
\]