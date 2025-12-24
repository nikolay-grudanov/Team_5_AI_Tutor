---
source_image: page_082.png
page_number: 82
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.16
tokens: 5316
characters: 1499
timestamp: 2025-12-24T07:07:09.088286
finish_reason: stop
---

*513. Пусть

\[
s_k = x_1^k + x_2^k + \cdots + x_n^k \quad (k = 1, 2, 3, \ldots),
\]
\[
p = x_1 x_2 \ldots x_n.
\]

Показать, что

\[
\begin{vmatrix}
n+1 & s_1 & s_2 & \ldots & s_n \\
s_1 & s_2 & s_3 & \ldots & s_{n+1} \\
s_2 & s_3 & s_4 & \ldots & s_{n+2} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
s_n & s_{n+1} & s_{n+2} & \ldots & s_{2n}
\end{vmatrix} =
\]
\[
= p^2 \begin{vmatrix}
n & s_1 & s_2 & \ldots & s_{n-1} \\
s_1 & s_2 & s_3 & \ldots & s_n \\
s_2 & s_3 & s_4 & \ldots & s_{n+1} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
s_{n-1} & s_n & s_{n+1} & \ldots & s_{2n-2}
\end{vmatrix}.
\]

514. Показать, что если

\[
D(x) = \begin{vmatrix}
a_{11} - x & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} - x & \ldots & a_{2n} \\
\ldots & \ldots & \ldots & \ldots \\
a_{1n} & a_{2n} & \ldots & a_{nn} - x
\end{vmatrix},
\]

то произведение \( D(x) \cdot D(-x) \) можно представить в виде

\[
\begin{vmatrix}
A_{11} - x^2 & A_{12} & \ldots & A_{1n} \\
A_{21} & A_{22} - x^2 & \ldots & A_{2n} \\
\ldots & \ldots & \ldots & \ldots \\
A_{n1} & A_{n2} & \ldots & A_{nn} - x^2
\end{vmatrix},
\]

где все \( A_{ij} \) не зависят от \( x \). Найти выражение \( A_{ij} \) через \( a_{kl} \).

*515. С помощью умножения определителей доказать, что при перестановке двух строк (или столбцов) определитель меняет знак.

*516. С помощью умножения определителей доказать, что определитель не изменяется, если к одной его строке (столбцу) прибавить другую строку (столбец), умноженную на число \( c \).