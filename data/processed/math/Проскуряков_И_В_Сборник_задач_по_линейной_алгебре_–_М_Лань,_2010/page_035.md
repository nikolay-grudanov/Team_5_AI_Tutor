---
source_image: page_035.png
page_number: 35
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.27
tokens: 5165
characters: 1349
timestamp: 2025-12-24T07:06:11.229472
finish_reason: stop
---

5.1. Метод приведения к треугольному виду

Этот метод заключается в преобразовании определителя к такому виду, где все элементы, лежащие по одну сторону одной из диагоналей, равны нулю. Случай побочной диагонали путем изменения порядка строк (или столбцов) на обратный сводится на случай главной диагонали. Полученный определитель равен произведению элементов главной диагонали.

Пример 1: Вычислить определитель порядка n:

\[
D = \begin{vmatrix}
1 & 1 & 1 & \ldots & 1 \\
1 & 0 & 1 & \ldots & 1 \\
1 & 1 & 0 & \ldots & 1 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & 1 & 1 & \ldots & 0
\end{vmatrix}.
\]

Вычитаем первую строку из всех остальных:

\[
D = \begin{vmatrix}
1 & 1 & 1 & \ldots & 1 \\
0 & -1 & 0 & \ldots & 0 \\
0 & 0 & -1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & -1
\end{vmatrix} = (-1)^{n-1}.
\]

Пример 2: Вычислить определитель

\[
D = \begin{vmatrix}
a_1 & x & x & \ldots & x \\
x & a_2 & x & \ldots & x \\
x & x & a_3 & \ldots & x \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
x & x & x & \ldots & a_n
\end{vmatrix}.
\]

Вычитаем первую строку из всех остальных:

\[
D = \begin{vmatrix}
a_1 & x & x & \ldots & x \\
x-a_1 & a_2-x & 0 & \ldots & 0 \\
x-a_1 & 0 & a_3-x & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
x-a_1 & 0 & 0 & \ldots & a_n-x
\end{vmatrix}.
\]