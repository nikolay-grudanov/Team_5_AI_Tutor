---
source_image: page_093.png
page_number: 93
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.47
tokens: 6858
characters: 2698
timestamp: 2025-12-24T08:10:11.694857
finish_reason: stop
---

1.31. Легко проверить, что оба выражения равны произведению определителей

\[
\begin{vmatrix}
a_1 & a_2 & 0 & 0 \\
a_3 & a_4 & 0 & 0 \\
0 & 0 & b_1 & b_2 \\
0 & 0 & b_3 & b_4
\end{vmatrix} \cdot 
\begin{vmatrix}
c_1 & 0 & c_2 & 0 \\
0 & d_1 & 0 & d_2 \\
c_3 & 0 & c_4 & 0 \\
0 & d_3 & 0 & d_4
\end{vmatrix}.
\]

1.32. Оба определителя равны

\[
a_1 a_2 a_3 \begin{vmatrix}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{23}
\end{vmatrix} + a_1 b_2 b_3 \begin{vmatrix}
a_{11} & b_{12} & b_{13} \\
a_{21} & b_{22} & b_{23} \\
a_{31} & b_{32} & b_{23}
\end{vmatrix} + b_1 a_2 b_3 \begin{vmatrix}
b_{11} & a_{12} & b_{13} \\
b_{21} & a_{22} & b_{23} \\
b_{31} & a_{32} & b_{23}
\end{vmatrix} -
\]
\[
- a_1 a_2 b_3 \begin{vmatrix}
a_{11} & a_{12} & b_{13} \\
a_{21} & a_{22} & b_{23} \\
a_{31} & a_{32} & b_{23}
\end{vmatrix} - b_1 a_2 a_3 \begin{vmatrix}
b_{11} & a_{12} & a_{13} \\
b_{21} & a_{22} & a_{23} \\
b_{31} & a_{32} & a_{23}
\end{vmatrix} - b_1 b_2 b_3 \begin{vmatrix}
b_{11} & b_{12} & b_{13} \\
b_{21} & b_{22} & b_{23} \\
b_{31} & b_{32} & b_{23}
\end{vmatrix}.
\]

1.33. Для определителей матриц порядка \( n + 1 \) легко проверить следующие равенства:

\[
\begin{vmatrix}
s_1 - a_{11} & \ldots & s_1 - a_{1n} & 0 \\
\ldots & \ldots & \ldots & \ldots \\
s_n - a_{n1} & \ldots & s_n - a_{nn} & 0 \\
-1 & \ldots & -1 & 1
\end{vmatrix} =
\begin{vmatrix}
s_1 - a_{11} & \ldots & s_1 - a_{1n} & (n-1)s_1 \\
\ldots & \ldots & \ldots & \ldots \\
s_n - a_{n1} & \ldots & s_n - a_{nn} & (n-1)s_n \\
-1 & \ldots & -1 & 1-n
\end{vmatrix} =
\]
\[
= (n-1)
\begin{vmatrix}
s_1 - a_{11} & \ldots & s_1 - a_{1n} & s_1 \\
\ldots & \ldots & \ldots & \ldots \\
s_n - a_{n1} & \ldots & s_n - a_{nn} & s_n \\
-1 & \ldots & -1 & -1
\end{vmatrix} = (n-1)
\begin{vmatrix}
-a_{11} & \ldots & -a_{1n} & s_1 \\
\ldots & \ldots & \ldots & \ldots \\
-a_{n1} & \ldots & -a_{nn} & s_n \\
0 & \ldots & 0 & -1
\end{vmatrix}.
\]

Чтобы получить первое равенство, нужно к последнему столбцу прибавить сумму всех остальных, а чтобы получить последнее равенство, нужно последний столбец вычесть из всех остальных.

1.34. Воспользуемся тождеством \( \binom{p}{q} + \binom{p}{q-1} = \binom{p+1}{q} \). Складывая соответствующим образом столбцы, от матрицы со строками вида
\[
\left( \binom{n}{m}, \binom{n}{m-1}, \ldots, \binom{n}{m-k} \right)
\]
можно перейти к матрице со строками
\[
\left( \binom{n}{m}, \binom{n+1}{m}, \binom{n+1}{m-1}, \ldots, \binom{n+1}{m-k+1} \right).
\]
Проделывая аналогичную операцию для столбцов с номерами 2, 3, ..., \( n \), получим матрицу со строками
\[
\left( \binom{n}{m}, \binom{n+1}{m}, \binom{n+2}{m}, \binom{n+2}{m-1}, \ldots, \binom{n+2}{m-k+2} \right).
\]