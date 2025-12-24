---
source_image: page_510.png
page_number: 510
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.04
tokens: 6620
characters: 2373
timestamp: 2025-12-24T08:21:31.390152
finish_reason: stop
---

Поэтому если все собственные значения матрицы \( A \) нулевые, то все собственные значения матрицы \( e^A - I \) тоже нулевые.

Попутно мы доказали, что матрица \( e^A \) унипотентна тогда и только тогда, когда \( e^{\lambda_1} = 1, \ldots, e^{\lambda_n} = 1 \), т. е. \( \lambda_1 = 2k_1 \pi i, \ldots, \lambda_n = 2k_n \pi i \), где \( k_1, \ldots, k_n \) — целые числа. Если хотя бы одно из чисел \( k_1, \ldots, k_n \) отлично от нуля, то матрица \( A \) не нильпотентна.

53.8. Легко проверить тождество

\[
\left( \bigotimes_{i < j} X_i \right)^2 + \bigotimes_{i < j} [X_i, X_j] = \bigotimes_{i < j} X_i^2 + 2 \bigotimes_{i < j} X_i X_j.
\]

Таким образом,

\[
e^{tX_1} e^{tX_2} \ldots e^{tX_n} = I + t \bigotimes_{i < j} X_i + \frac{t^2}{2} \left( \bigotimes_{i < j} X_i \right)^2 + \frac{t^2}{2} \bigotimes_{i < j} [X_i, X_j] + O(t^3).
\]

С другой стороны,

\[
\exp \left\{ t \bigotimes_{i < j} X_i + \frac{t^2}{2} \bigotimes_{i < j} [X_i, X_j] \right\} = I + t \bigotimes_{i < j} X_i + \frac{t^2}{2} \bigotimes_{i < j} [X_i, X_j] + \frac{t^2}{2} \left( \bigotimes_{i < j} X_i \right)^2 + O(t^3).
\]

53.9. Рассматриваемые определители имеют вид

\[
\bigotimes_{i < j} \pm \partial_1^{r_1} \partial_2^{r_2} \ldots \partial_n^{r_n} \quad \text{и} \quad \bigotimes_{i < j} \pm x_1^{r_1} x_2^{r_2} \ldots x_n^{r_n},
\]

где \( (r_1, r_2, \ldots, r_n) \) — перестановка чисел \( (0, 1, \ldots, n-1) \). Произведение этих сумм содержит ровно \( n! \) ненулевых членов, а именно, оно равно

\[
\bigotimes_{i < j} \partial_1^{r_1} \partial_2^{r_2} \ldots \partial_n^{r_n} x_1^{r_1} x_2^{r_2} \ldots x_n^{r_n}.
\]

Каждый из этих членов равен \( 0! \ 1! \ 2! \ldots (n-1)! \).

53.10. Предположим сначала, что \( m > 0 \). Тогда

\[
(X^m)_{ij} = \bigotimes_{a, b, \ldots, p, q} x_{ia} x_{ab} \ldots x_{pq} x_{qj},
\]
\[
\operatorname{tr} X^m = \bigotimes_{a, b, \ldots, p, q, r} x_{ra} x_{ab} \ldots x_{pq} x_{qr}.
\]

Поэтому

\[
\frac{\partial}{\partial x_{ji}} (\operatorname{tr} X^m) =
\]
\[
= \bigotimes_{a, b, \ldots, p, q, r} \frac{\partial x_{ra}}{\partial x_{ji}} x_{ab} \ldots x_{pq} x_{qr} + \ldots + \bigotimes_{a, b, \ldots, p, q, r} x_{ra} x_{ab} \ldots x_{pq} \frac{\partial x_{qr}}{\partial x_{ji}} =
\]
\[
= \bigotimes_{b, \ldots, p, q} x_{ib} \ldots x_{pq} x_{qj} + \ldots + \bigotimes_{a, b, \ldots, p} x_{ia} x_{ab} \ldots x_{pj} = m (X^{m-1})_{ij}.
\]