---
source_image: page_058.png
page_number: 58
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.55
tokens: 5519
characters: 1770
timestamp: 2025-12-24T07:06:46.467193
finish_reason: stop
---

377.
\[
\begin{vmatrix}
1 & x & x^2 & \ldots & x^{n-2} & x^{n-1} \\
x^{n-1} & 1 & x & \ldots & x^{n-3} & x^{n-2} \\
x^{n-2} & x^{n-1} & 1 & \ldots & x^{n-4} & x^{n-3} \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
x & x^2 & x^3 & \ldots & x^{n-1} & 1
\end{vmatrix}.
\]

378. Не вычисляя определителей, установить, как связаны между собой два циркулянта:

\[
\begin{vmatrix}
a_1 & a_2 & a_3 & \ldots & a_{n-1} & a_n \\
a_n & a_1 & a_2 & \ldots & a_{n-2} & a_{n-1} \\
a_{n-1} & a_n & a_1 & \ldots & a_{n-3} & a_{n-2} \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
a_2 & a_3 & a_4 & \ldots & a_n & a_1
\end{vmatrix}
\]
И
\[
\begin{vmatrix}
a_1 & a_2 & a_3 & \ldots & a_{n-1} & a_n \\
a_2 & a_3 & a_4 & \ldots & a_n & a_1 \\
a_3 & a_4 & a_5 & \ldots & a_1 & a_2 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
a_n & a_1 & a_2 & \ldots & a_{n-2} & a_{n-1}
\end{vmatrix},
\]

построенные из одних и тех же чисел \(a_1, a_2, \ldots, a_n\) применением круговых перестановок в двух противоположных направлениях.

Вычислить определители:

* 379.
\[
\begin{vmatrix}
1 & 1 & 1 & \ldots & 1 \\
1 & \binom{2}{1} & \binom{3}{1} & \ldots & \binom{n}{1} \\
1 & \binom{3}{2} & \binom{4}{2} & \ldots & \binom{n+1}{2} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \binom{n}{n-1} & \binom{n+1}{n-1} & \ldots & \binom{2n-2}{n-1}
\end{vmatrix},
\]
где \(\binom{n}{k} = C_n^k = \frac{n!}{k!(n-k)!}\).

* 380.
\[
\begin{vmatrix}
1 & 1 & 1 & \ldots & 1 \\
\binom{m}{1} & \binom{m+1}{1} & \binom{m+2}{1} & \ldots & \binom{m+n}{1} \\
\binom{m+1}{2} & \binom{m+2}{2} & \binom{m+3}{2} & \ldots & \binom{m+n+1}{2} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
\binom{m+n-1}{n} & \binom{m+n}{n} & \binom{m+n+1}{n} & \ldots & \binom{m+2n-1}{n}
\end{vmatrix}.
\]