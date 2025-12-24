---
source_image: page_101.png
page_number: 101
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.18
tokens: 6265
characters: 1739
timestamp: 2025-12-24T08:10:08.341694
finish_reason: stop
---

Ясно, что

\[
\bullet \quad a_{is} b_{sj} = \frac{\div (x_j + y_k)_{k \neq s} \div (x_k + y_s)_{k \neq i}}{\div (x_j - x_k)_{k \neq j} \div (y_s - y_k)_{k \neq s}}.
\]

Рассмотрим многочлен

\[
P(x) = \frac{\div (x_j + y_k - x)_{k \neq s} \div (x_k + y_s)_{k \neq i}}{\div (x_j - x_k)_{k \neq j} \div (y_s - y_k)_{k \neq s}}.
\]

Нужно доказать, что \( P(0) = \delta_{ij} \). Рассмотрим для этого второй многочлен

\[
Q(x) = \frac{\div (x_j - x_k - x)_{k \neq i}}{\div (x_j - x_k)_{k \neq j}}.
\]

Степени обоих рассматриваемых многочленов не превосходят \( n - 1 \). Легко также проверить, что \( P(x_j + y_t) = Q(x_j + y_t) \) при \( t = 1, \ldots, n \). Следовательно, \( P(x) = Q(x) \). В частности,

\[
P(0) = Q(0) = \frac{\div (x_j - x_k)_{k \neq i}}{\div (x_j - x_k)_{k \neq j}} = \delta_{ij}.
\]

2.19. Ответ:

\[
\begin{pmatrix}
0 & \ldots & 0 & 1 \\
\cdots & \cdots & \cdots & \cdots \\
0 & \ldots & 0 & 1
\end{pmatrix}.
\]

При вычёркивании последней строки и последнего столбца матрицы \( A \) получается единичная матрица, имеющая определитель 1. Ясно также, что ненулевой минор мы можем получить только при вычёркивании последней строки. Поэтому все столбцы матрицы \( \operatorname{adj} A \), кроме последнего, нулевые; в последнем столбце стоят числа \( x_1, x_2, \ldots, x_{n-1}, 1 \). Теперь из равенства \( A(\operatorname{adj} A) = 0 \) получаем \( x_1 = 1, x_2 = 1, \ldots, x_{n-1} = 1 \).

2.20. Пусть \( n \) — порядок матрицы \( A \), а \( A_{n-1} \) — матрица, образованная первыми \( n - 1 \) столбцами матрицы \( A \). Условие, что сумма элементов каждой строки матрицы \( A \) равна 0, влечёт, что

\[
A = (A_{n-1} \ 0) \begin{pmatrix}
1 & -1 \\
\vdots & \vdots \\
1 & -1 \\
0 & \ldots & 0 & 0
\end{pmatrix}.
\]