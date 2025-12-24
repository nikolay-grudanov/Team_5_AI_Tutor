---
source_image: page_077.png
page_number: 77
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.18
tokens: 5686
characters: 2251
timestamp: 2025-12-24T07:07:17.631674
finish_reason: stop
---

*486. Доказать равенство:

\[
\begin{vmatrix}
s - a_1 & s - a_2 & \ldots & s - a_n \\
s - a_n & s - a_1 & \ldots & s - a_{n-1} \\
\ldots & \ldots & \ldots & \ldots \\
s - a_2 & s - a_3 & \ldots & s - a_1
\end{vmatrix}
=
(-1)^{n-1}(n-1)
\begin{vmatrix}
a_1 & a_2 & \ldots & a_n \\
a_n & a_1 & \ldots & a_{n-1} \\
\ldots & \ldots & \ldots & \ldots \\
a_2 & a_3 & \ldots & a_1
\end{vmatrix},
\]

где \( s = a_1 + a_2 + \cdots + a_n \).

Вычислить определители:

*487.

\[
\begin{vmatrix}
-1 & -1 & -1 & \ldots & -1 \\
1 & -1 & -1 & \ldots & -1 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
-1 & -1 & -1 & \ldots & 1
\end{vmatrix}
\]

\( p \) столбцов

\[
\begin{vmatrix}
1 & 1 & \ldots & 1 & 1 \\
-1 & 1 & \ldots & 1 & 1 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & 1 & \ldots & 1 & -1
\end{vmatrix}
\]

\( n - p \) столбцов

*488.

\[
\begin{vmatrix}
a & a & a & \ldots & a \\
b & a & a & \ldots & a \\
b & b & a & \ldots & a \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
a & a & a & \ldots & b
\end{vmatrix}
\]

\( p \) столбцов

\[
\begin{vmatrix}
b & b & \ldots & b & b \\
a & b & \ldots & b & b \\
a & a & \ldots & b & b \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
b & b & \ldots & b & a
\end{vmatrix}
\]

\( n - p \) столбцов

*489.

\[
\begin{vmatrix}
\cos \frac{\pi}{n} & \cos \frac{2\pi}{n} & \cos \frac{3\pi}{n} & \ldots & -1 \\
-1 & \cos \frac{\pi}{n} & \cos \frac{2\pi}{n} & \ldots & \cos \frac{(n-1)\pi}{n} \\
\cos \frac{(n-1)\pi}{n} & -1 & \cos \frac{\pi}{n} & \ldots & \cos \frac{(n-2)\pi}{n} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
\cos \frac{2\pi}{n} & \cos \frac{3\pi}{n} & \cos \frac{4\pi}{n} & \ldots & \cos \frac{\pi}{n}
\end{vmatrix}
\]

*490.

\[
\begin{vmatrix}
\cos \theta & \cos 2\theta & \cos 3\theta & \ldots & \cos n\theta \\
\cos n\theta & \cos \theta & \cos 2\theta & \ldots & \cos(n-1)\theta \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
\cos 2\theta & \cos 3\theta & \cos 4\theta & \ldots & \cos \theta
\end{vmatrix}
\]

*491.

\[
\begin{vmatrix}
\sin a & \sin(a+h) & \sin(a+2h) & \ldots & \sin[a+(n-1)h] \\
\sin[a+(n-1)h] & \sin a & \sin(a+h) & \ldots & \sin[a+(n-2)h] \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
\sin a + h & \sin(a+2h) & \sin(a+3h) & \ldots & \sin a
\end{vmatrix}
\]