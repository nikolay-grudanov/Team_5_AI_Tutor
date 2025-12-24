---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.82
tokens: 5680
characters: 2011
timestamp: 2025-12-24T07:07:16.326744
finish_reason: stop
---

474.
\[
\begin{vmatrix}
\frac{1-a_1^n b_1^n}{1-a_1 b_1} & \frac{1-a_1^n b_2^n}{1-a_1 b_2} & \cdots & \frac{1-a_1^n b_n^n}{1-a_1 b_n} \\
\frac{1-a_2^n b_1^n}{1-a_2 b_1} & \frac{1-a_2^n b_2^n}{1-a_2 b_2} & \cdots & \frac{1-a_2^n b_n^n}{1-a_2 b_n} \\
\cdots & \cdots & \cdots & \cdots \\
\frac{1-a_n^n b_1^n}{1-a_n b_1} & \frac{1-a_n^n b_2^n}{1-a_n b_2} & \cdots & \frac{1-a_n^n b_n^n}{1-a_n b_n}
\end{vmatrix}.
\]

475.
\[
\begin{vmatrix}
(a_0 + b_0)^n & (a_0 + b_1)^n & \cdots & (a_0 + b_n)^n \\
(a_1 + b_0)^n & (a_1 + b_1)^n & \cdots & (a_1 + b_1)^n \\
\cdots & \cdots & \cdots & \cdots \\
(a_n + b_0)^n & (a_n + b_1)^n & \cdots & (a_n + b_n)^n
\end{vmatrix}.
\]

*476.
\[
\begin{vmatrix}
1^{n-1} & 2^{n-1} & \cdots & n^{n-1} \\
2^{n-1} & 3^{n-1} & \cdots & (n+1)^{n-1} \\
\cdots & \cdots & \cdots & \cdots \\
n^{n-1} & (n+1)^{n-1} & \cdots & (2n-1)^{n-1}
\end{vmatrix}.
\]

477.
\[
\begin{vmatrix}
s_0 & s_1 & s_2 & \cdots & s_{n-1} \\
s_1 & s_2 & s_3 & \cdots & s_n \\
s_2 & s_3 & s_4 & \cdots & s_{n+1} \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
s_{n-1} & s_n & s_{n+1} & \cdots & s_{2n-2}
\end{vmatrix},
\]
где \( s_k = x_1^k + x_2^k + \cdots + x_n^k \).

*478.
\[
\begin{vmatrix}
s_0 & s_1 & s_2 & \cdots & s_{n-1} & 1 \\
s_1 & s_2 & s_3 & \cdots & s_n & x \\
s_2 & s_3 & s_4 & \cdots & s_{n+1} & x^2 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
s_n & s_{n+1} & s_{n+2} & \cdots & s_{2n-1} & x^n
\end{vmatrix},
\]
где \( s_k = x_1^k + x_2^k + \cdots + x_n^k \).

*479. Доказать, что значение циркулянта определяется равенством
\[
\begin{vmatrix}
a_1 & a_2 & a_3 & \cdots & a_n \\
a_n & a_1 & a_2 & \cdots & a_{n-1} \\
a_{n-1} & a_n & a_1 & \cdots & a_{n-2} \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
a_2 & a_3 & a_4 & \cdots & a_1
\end{vmatrix} = f(\varepsilon_1) f(\varepsilon_2) \cdots f(\varepsilon_n),
\]
где \( f(x) = a_1 + a_2 x + a_3 x^2 + \cdots + a_n x^{n-1} \) и \( \varepsilon_1, \varepsilon_2, \ldots, \varepsilon_n \) — все значения корня \( n \)-й степени из единицы.