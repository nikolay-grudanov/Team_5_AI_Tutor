---
source_image: page_348.png
page_number: 348
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.27
tokens: 5623
characters: 2248
timestamp: 2025-12-24T07:13:34.113657
finish_reason: stop
---

Все члены одного и того же или двух разных произведений \( \varepsilon M_1 M_2 \ldots M_p \) отличаются друг от друга по составу элементов и потому будут различными членами определителя \( D \). Остается доказать, что общее число членов всех таких произведений равно \( n! \). Число миноров \( M_1 \) равно \( C_n^k \). Если \( M_1 \) уже выбран, то миноры \( M_2 \) могут лежать лишь в оставшихся \( n - k \) строках и их число (для каждого выбора \( M_1 \)) равно \( C_{n-k}^l \). При выбранных \( M_1 \) и \( M_2 \) число миноров \( M_3 \) равно \( C_{n-k-l}^m \) и т. д.; наконец, при выбранных \( M_1, M_2, \ldots, M_{p-1} \) число миноров \( M_p \) равно \( C_s^s = 1 \). Поэтому всех произведений вида \( \varepsilon M_1 M_2 \ldots M_p \) будет

\[
C_n^k \cdot C_{n-k}^l C_{n-k-l}^m \cdots C_s^s =
\]
\[
= \frac{n!}{k!(n-k)!} \cdot \frac{(n-k)!}{l!(n-k-l)!} \cdot \frac{(n-k-l)!}{m!(n-k-l-m)!} \cdots \frac{s!}{s!} = \frac{n!}{k! l! m! \ldots s!}.
\]

Но число определителя \( D \) в каждом произведении \( \varepsilon M_1 M_2 \ldots M_p \) равно \( k! l! m! \ldots s! \). Значит, число членов во всех произведениях \( \varepsilon M_1 M_2 \ldots M_p \) равно \( \frac{n!}{k! l! m! \ldots s!} k! l! m! \ldots s! = n! \).

467. Получим при умножении

строки на строки:
\[
\begin{vmatrix}
-1 & 2 & -3 \\
-4 & -7 & -13 \\
-3 & -4 & -13
\end{vmatrix},
\]
\[
\begin{vmatrix}
7 & -26 & 13 \\
12 & -35 & 19 \\
17 & -52 & 27
\end{vmatrix},
\]
\[
\begin{vmatrix}
-3 & 1 & -6 \\
-3 & 1 & -8 \\
4 & 7 & 1
\end{vmatrix},
\]
\[
\begin{vmatrix}
9 & -35 & 18 \\
13 & -47 & 24 \\
12 & -37 & 17
\end{vmatrix}.
\]

Значения данных определителей —5 и 10, а значения всех полученных определителей равны —50.

468. \((a^2 + b^2 + c^2 + d^2)^2\).
469. \((a^2 + b^2 + c^2 + d^2 + e^2 + f^2 + g^2 + h^2)^4\).
470. 0 при \( n > 2 \); \((x_2 - x_1)(y_2 - y_1)\) при \( n = 2 \).
Указание. Представить в виде произведения определителей:

\[
\begin{vmatrix}
1 & x_1 & 0 & \ldots & 0 \\
1 & x_2 & 0 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & x_n & 0 & \ldots & 0
\end{vmatrix}
\text{ и }
\begin{vmatrix}
1 & y_1 & 0 & \ldots & 0 \\
1 & y_2 & 0 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & y_n & 0 & \ldots & 0
\end{vmatrix}.
\]