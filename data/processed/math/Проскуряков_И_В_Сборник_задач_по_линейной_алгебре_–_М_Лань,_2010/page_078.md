---
source_image: page_078.png
page_number: 78
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.12
tokens: 5558
characters: 1755
timestamp: 2025-12-24T07:07:13.843815
finish_reason: stop
---

*492. \[
\begin{vmatrix}
1^2 & 2^2 & 3^2 & \ldots & n^2 \\
n^2 & 1^2 & 2^2 & \ldots & (n-1)^2 \\
(n-1)^2 & n^2 & 1^2 & \ldots & (n-2)^2 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
2^2 & 3^2 & 4^2 & \ldots & 1^2
\end{vmatrix}.
\]

*493. Вычислить косой циркулянт (или косоциклический определитель)

\[
\begin{vmatrix}
a_1 & a_2 & a_3 & \ldots & a_n \\
-a_n & a_1 & a_2 & \ldots & a_{n-1} \\
-a_{n-1} & -a_n & a_1 & \ldots & a_{n-2} \\
-a_2 & -a_3 & -a_4 & \ldots & a_1
\end{vmatrix}.
\]

494. \[
\begin{vmatrix}
a_1 & a_2 & a_3 & \ldots & a_n \\
a_n z & a_1 & a_2 & \ldots & a_{n-1} \\
a_{n-1} z & a_n z & a_1 & \ldots & a_{n-2} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
a_2 z & a_3 z & a_4 z & \ldots & a_1
\end{vmatrix},
\]
где \(z\) — любое число.

*495. Доказать, что циркулянт порядка \(2n\) с первой строкой из элементов \(a_1, a_2, \ldots, a_{2n-1}, a_{2n}\) равен произведению циркулянта порядка \(n\) с первой строкой из элементов \(a_1 + a_{n+1}, a_2 + a_{n+2}, \ldots, a_n + a_{2n}\) и косого циркулянта порядка \(n\) с первой строкой из элементов \(a_1 - a_{n+1}, a_2 - a_{n+2}, a_n - a_{2n}\).

*496. Перемножая два определителя

\[
\begin{vmatrix}
x_1 & x_2 & x_3 & x_4 \\
x_2 & -x_1 & -x_4 & x_3 \\
x_3 & x_4 & -x_1 & -x_2 \\
x_4 & -x_3 & x_2 & -x_1
\end{vmatrix}
\cdot
\begin{vmatrix}
y_1 & y_2 & y_3 & y_4 \\
y_2 & -y_1 & -y_4 & y_3 \\
y_3 & y_4 & -y_1 & -y_2 \\
y_4 & -y_3 & y_2 & -y_1
\end{vmatrix},
\]

доказать тождество Эйлера

\[
(x_1^2 + x_2^2 + x_3^2 + x_4^2)(y_1^2 + y_2^2 + y_3^2 + y_4^2) =
= (x_1 y_1 + x_2 y_2 + x_3 y_3 + x_4 y_4)^2 + (x_1 y_2 - x_2 y_1 - x_3 y_4 + x_4 y_3)^2 +
+ (x_1 y_3 + x_2 y_4 - x_3 y_1 - x_4 y_2)^2 + (x_1 y_4 - x_2 y_4 + x_3 y_2 - x_4 y_1)^2.
\]

Какое свойство целых чисел отсюда вытекает?