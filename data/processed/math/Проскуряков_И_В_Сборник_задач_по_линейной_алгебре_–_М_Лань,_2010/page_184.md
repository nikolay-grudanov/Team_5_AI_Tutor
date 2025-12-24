---
source_image: page_184.png
page_number: 184
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.20
tokens: 5211
characters: 1410
timestamp: 2025-12-24T07:09:26.717180
finish_reason: stop
---

определенная на спектре этой матрицы. Написать выражение для матрицы \( f(A) \), пользуясь предыдущей задачей.

**1153.** Доказать, что если матрицы \( A \) и \( B \) подобны, причем \( B = T^{-1}AT \) и для функции \( f(\lambda) \) матрица \( f(A) \) существует, то и матрица \( f(B) \) существует и подобна \( f(A) \), причем \( f(B) = T^{-1}f(A)T \) с той же матрицей \( T \).

* **1154.** Доказать, что если матрица \( A \) клеточно-диагональная

\[
A = \begin{pmatrix}
A_1 & & & \\
& A_2 & & \\
& & \ddots & \\
0 & & & A_s
\end{pmatrix}
\]

и функция \( f(\lambda) \) определена на спектре матрицы \( A \), то

\[
f(A) = \begin{pmatrix}
f(A_1) & & & \\
& f(A_2) & & \\
& & \ddots & \\
0 & & & f(A_s)
\end{pmatrix}.
\]

**1155.** Найти интерполяционный многочлен Лагранжа — Сильвестера \( r(\lambda) \) и значение \( f(A) \) функции \( f(\lambda) \) для матрицы

\[
A = \begin{pmatrix}
0 & 1 & 0 & \ldots & 0 \\
0 & 0 & 1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & 1 \\
0 & 0 & 0 & \ldots & 0
\end{pmatrix}.
\]

Для каких функций \( f(\lambda) \) значение \( f(A) \) имеет смысл?

**1156.** Решить задачу, аналогичную предыдущей, для матрицы

\[
A = \begin{pmatrix}
\alpha & 1 & 0 & \ldots & 0 & 0 \\
0 & \alpha & 1 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & \alpha & 1 \\
0 & 0 & 0 & \ldots & 0 & \alpha
\end{pmatrix}.
\]