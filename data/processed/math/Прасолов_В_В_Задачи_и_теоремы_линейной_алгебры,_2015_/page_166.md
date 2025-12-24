---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.38
tokens: 6214
characters: 1473
timestamp: 2025-12-24T08:12:00.114770
finish_reason: stop
---

Задачи

10.1. а) Докажите, что многочлен Лежандра \( P_n(x) \) равен определителю матрицы

\[
\begin{pmatrix}
x & 1 & 0 & \ldots & 0 & 0 \\
\frac{1}{2} & \frac{3}{2}x & 1 & \ldots & 0 & 0 \\
0 & \frac{2}{3} & \frac{5}{3}x & \ldots & 0 & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \ldots & \frac{2n-3}{n-1}x & 1 \\
0 & 0 & 0 & \ldots & \frac{n-1}{n} & \frac{2n-1}{n}x
\end{pmatrix}.
\]

б) Докажите, что многочлен Эрмита \( H_n(x) \) равен определителю матрицы

\[
\begin{pmatrix}
2x & 1 & 0 & \ldots & 0 & 0 \\
2 & 2x & 2 & \ldots & 0 & 0 \\
0 & 2 & 2x & \ldots & 0 & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \ldots & 2x & n-1 \\
0 & 0 & 0 & \ldots & 2 & 2x
\end{pmatrix}.
\]

в) Докажите, что многочлен Чебышёва \( T_n(x) \) равен определителю матрицы порядка \( n \)

\[
\begin{pmatrix}
x & 1 & 0 & \ldots & 0 & 0 \\
1 & 2x & 1 & \ldots & 0 & 0 \\
0 & 1 & 2x & \ldots & 0 & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \ldots & 2x & 1 \\
0 & 0 & 0 & \ldots & 1 & 2x
\end{pmatrix}.
\]

§ 11. Комплексификация и овеществление. Эрмитовы пространства

11.1. Комплексификация

Комплексификацией линейного пространства \( V \) над \( \mathbb{R} \) называют множество пар \( (a, b) \), где \( a, b \in V \), на котором введена структура линейного пространства над \( \mathbb{C} \) следующим образом:

\[
(a, b) + (a_1, b_1) = (a + a_1, b + b_1),
\]
\[
(x + iy)(a, b) = (xa - yb, xb + ya).
\]