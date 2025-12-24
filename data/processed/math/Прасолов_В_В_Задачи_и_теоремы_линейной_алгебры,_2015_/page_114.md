---
source_image: page_114.png
page_number: 114
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.91
tokens: 6247
characters: 1795
timestamp: 2025-12-24T08:10:29.938487
finish_reason: stop
---

Теорема 5.5.2. Если \( f_i(x) = \sum_{j=1}^n a_{ij} x_j \), где \( a_{ij} \in \mathbb{Q} \) и ковекторы \( f_1, \ldots, f_m \) образуют базис (в частности, \( m = n \)), то система (1) имеет решение \( x_i = \sum_{j=1}^n c_{ij} b_j \), где числа \( c_{ij} \) рациональны и не зависят от \( b_j \); это решение единственно.

Доказательство. Так как

\[
\begin{pmatrix}
a_{11} & \ldots & a_{1n} \\
\cdots & \cdots & \cdots \\
a_{n1} & \ldots & a_{nn}
\end{pmatrix}
\begin{pmatrix}
x_1 \\
\vdots \\
x_n
\end{pmatrix}
=
\begin{pmatrix}
b_1 \\
\vdots \\
b_n
\end{pmatrix},
\]

то

\[
\begin{pmatrix}
x_1 \\
\vdots \\
x_n
\end{pmatrix}
=
\left(
\begin{pmatrix}
a_{11} & \ldots & a_{1n} \\
\cdots & \cdots & \cdots \\
a_{n1} & \ldots & a_{nn}
\end{pmatrix}
\right)^{-1}
\begin{pmatrix}
b_1 \\
\vdots \\
b_n
\end{pmatrix}.
\]

Если элементы матрицы \( A \) рациональны, то элементы матрицы \( A^{-1} \) тоже рациональны.

5.6. Разрезание прямоугольника на квадраты

Полученные в п. 5.5 результаты имеют несколько неожиданное применение.

Теорема 5.6.1. Если прямоугольник со сторонами \( a \) и \( b \) произвольным образом разрезан на квадраты со сторонами \( x_1, \ldots, x_n \), то \( x_i / a \in \mathbb{Q} \) и \( x_i / b \in \mathbb{Q} \) для всех \( i \).

Доказательство. Например, для рис. 3 можно написать следующую систему уравнений:

\[
\begin{align*}
x_1 + x_2 &= a, & x_1 + x_3 + x_4 + x_7 &= b, \\
x_3 + x_2 &= a, & x_2 + x_5 + x_7 &= b, \\
x_4 + x_2 &= a, & x_2 + x_6 &= b. \\
x_4 + x_5 + x_6 &= a, \\
x_6 + x_7 &= a,
\end{align*}
\]

(1)

Аналогичную систему уравнений можно написать и для любого другого разбиения прямоугольника на квадраты. Заметим также, что если система, соответствующая некоторому рисунку, имеет еще одно положительное решение, то и этому решению можно сопоставить