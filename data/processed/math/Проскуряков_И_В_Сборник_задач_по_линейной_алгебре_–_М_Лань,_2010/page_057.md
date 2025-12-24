---
source_image: page_057.png
page_number: 57
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.82
tokens: 5609
characters: 2068
timestamp: 2025-12-24T07:06:48.685030
finish_reason: stop
---

Пользуясь этим равенством и результатом задачи 369, получить выражение \( \cos n\alpha \) через \( \cos \alpha \).

**372.** Доказать равенство

\[
\frac{\sin n\alpha}{\sin \alpha} = \begin{vmatrix}
2 \cos \alpha & 1 & 0 & 0 & \ldots & 0 & 0 \\
1 & 2 \cos \alpha & 1 & 0 & \ldots & 0 & 0 \\
0 & 1 & 2 \cos \alpha & 1 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & 1 & 2 \cos \alpha
\end{vmatrix},
\]

где определитель имеет порядок \( n - 1 \). Пользуясь этим равенством и результатом задачи 369, представить \( \sin n\alpha \) в виде произведения \( \sin \alpha \) на многочлен от \( \cos \alpha \).

* **373.** Доказать равенство, не вычисляя самих определителей:

\[
\begin{vmatrix}
a_1 & b_1 & 0 & 0 & \ldots & 0 & 0 \\
c_1 & a_2 & b_2 & 0 & \ldots & 0 & 0 \\
0 & c_2 & a_3 & b_3 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & c_{n-1} & a_n
\end{vmatrix} =
\begin{vmatrix}
a_1 & b_1 c_1 & 0 & 0 & \ldots & 0 & 0 \\
1 & a_2 & b_2 c_2 & 0 & \ldots & 0 & 0 \\
0 & 1 & a_3 & b_3 c_3 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & 1 & a_n
\end{vmatrix}.
\]

Вычислить определители:

**374.**

\[
\begin{vmatrix}
1 + x^2 & x & 0 & 0 & \ldots & 0 & 0 \\
x & 1 + x^2 & x & 0 & \ldots & 0 & 0 \\
0 & x & 1 + x^2 & x & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & x & 1 + x^2
\end{vmatrix}.
\]

**375.**

\[
\begin{vmatrix}
1 & 2 & 3 & \ldots & n-1 & n \\
2 & 3 & 4 & \ldots & n & 1 \\
3 & 4 & 5 & \ldots & 1 & 2 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
n & 1 & 2 & \ldots & n-2 & n-1
\end{vmatrix}.
\]

* **376.**

\[
\begin{vmatrix}
a & a+x & a+2x & \ldots & a+(n-2)x & a+(n-1)x \\
a+(n-1)x & a & a+x & \ldots & a+(n-3)x & a+(n-2)x \\
a+(n-2)x & a+(n-1)x & a & \ldots & a+(n-4)x & a+(n-3)x \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
a+x & a+2x & a+3x & \ldots & a+(n-1)x & a
\end{vmatrix}.
\]