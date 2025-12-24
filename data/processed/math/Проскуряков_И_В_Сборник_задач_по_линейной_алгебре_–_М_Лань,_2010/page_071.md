---
source_image: page_071.png
page_number: 71
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.38
tokens: 5585
characters: 1982
timestamp: 2025-12-24T07:07:05.807096
finish_reason: stop
---

460. Написать разложение континуанты (ср. с задачей 420) порядка \( n \):

\[
(a_1, a_2, \ldots, a_n) = \begin{vmatrix}
a_1 & 1 & 0 & 0 & \ldots & 0 & 0 \\
-1 & a_2 & 1 & 0 & \ldots & 0 & 0 \\
0 & -1 & a_3 & 1 & \ldots & 0 & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & 0 & \ldots & -1 & a_n
\end{vmatrix}
\]

по первым \( k \) строкам. Какое свойство чисел Фибоначчи (задача 365) получается отсюда при \( n = 2k \)?

461. Не раскрывая скобок, доказать, что равенство

\[
(ab' - a'b)(cd' - c'd) - (ac' - a'c)(bd' - b'd) + 
+(ad' - a'd)(bc' - b'c) = 0
\]

справедливо при любых значениях \( a, b, c, d, a', b', c', d' \).

*462. В матрице

\[
\left( \begin{array}{c|c}
a_{11} \ldots a_{1n} & a_{1,n+1} \ldots a_{1,2n} \\
\cdots & \cdots \\
a_{n1} \ldots a_{nn} & a_{n,n+1} \ldots a_{n,2n}
\end{array} \right),
\]

содержащей \( n \) строк и \( 2n \) столбцов, берем любой минор \( M \) порядка \( n \), содержащий по крайней мере половину столбцов левой половины матрицы.

Пусть \( \sigma \) — сумма номеров столбцов минора \( M \), и пусть \( M' \) — минор порядка \( n \), составленный из остальных столбцов матрицы. Доказать, что \( \sum (-1)^{\sigma} MM' = 0 \), где сумма берется по всем минорам \( M \) указанного типа.

*463. Показать, что три определителя

\[
D = \begin{vmatrix}
a_1 x_1 & b_1 x_1 & a_1 x_2 & b_1 x_2 & a_1 x_3 & b_1 x_3 \\
a_2 x_1 & b_2 x_1 & a_2 x_2 & b_2 x_2 & a_2 x_3 & b_2 x_3 \\
a_1 y_1 & b_1 y_1 & a_1 y_2 & b_1 y_2 & a_1 y_3 & b_1 y_3 \\
a_2 y_1 & b_2 y_1 & a_2 y_2 & b_2 y_2 & a_2 y_3 & b_2 y_3 \\
a_1 z_1 & b_1 z_1 & a_1 z_2 & b_1 z_2 & a_1 z_3 & b_1 z_3 \\
a_2 z_1 & b_2 z_1 & a_2 z_2 & b_2 z_2 & a_2 z_3 & b_2 z_3
\end{vmatrix},
\]
\[
\delta = \begin{vmatrix}
a_1 & b_1 \\
a_2 & b_2
\end{vmatrix} \quad \text{и} \quad \Delta = \begin{vmatrix}
x_1 & x_2 & x_3 \\
y_1 & y_2 & y_3 \\
z_1 & z_2 & z_3
\end{vmatrix},
\]

связаны равенством \( D = \delta^3 \Delta^2 \).6

6Обобщение этого свойства дано в задаче 540.