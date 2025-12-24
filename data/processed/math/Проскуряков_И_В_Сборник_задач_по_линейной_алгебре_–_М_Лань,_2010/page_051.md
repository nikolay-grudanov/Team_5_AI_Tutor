---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.28
tokens: 5651
characters: 1983
timestamp: 2025-12-24T07:06:39.083669
finish_reason: stop
---

328.
\[
\begin{vmatrix}
1 & 1 & 1 & \ldots & 1 \\
1 & 2 & 2^2 & \ldots & 2^n \\
1 & 3 & 3^2 & \ldots & 3^n \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & n+1 & (n+1)^2 & \ldots & (n+1)^n
\end{vmatrix}.
\]

329.
\[
\begin{vmatrix}
a^n & (a-1)^n & \ldots & (a-n)^n \\
a^{n-1} & (a-1)^{n-1} & \ldots & (a-n)^{n-1} \\
\vdots & \vdots & \ddots & \vdots \\
a & a-1 & \ldots & a-n \\
1 & 1 & \ldots & 1
\end{vmatrix}.
\]

330.
\[
\begin{vmatrix}
1 & 1 & \ldots & 1 \\
x_1 + 1 & x_2 + 1 & \ldots & x_n + 1 \\
x_1^2 + x_1 & x_2^2 + x_2 & \ldots & x_n^2 + x_n \\
x_1^3 + x_1^2 & x_2^3 + x_2^2 & \ldots & x_n^3 + x_n^2 \\
\vdots & \vdots & \ddots & \vdots \\
x_1^{n-1} + x_1^{n-2} & x_2^{n-1} + x_2^{n-2} & \ldots & x_n^{n-1} + x_n^{n-2}
\end{vmatrix}.
\]

331.
\[
\begin{vmatrix}
(x+a_1)^n & (x+a_1)^{n-1} & \ldots & x+a_1 & 1 \\
(x+a_2)^n & (x+a_2)^{n-1} & \ldots & x+a_2 & 1 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
(x+a_{n+1})^n & (x+a_{n+1})^{n-1} & \ldots & x+a_{n+1} & 1
\end{vmatrix}.
\]

332.
\[
\begin{vmatrix}
1 & \sin \varphi_1 & \sin^2 \varphi_1 & \ldots & \sin^{n-1} \varphi_1 \\
1 & \sin \varphi_2 & \sin^2 \varphi_2 & \ldots & \sin^{n-1} \varphi_2 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \sin \varphi_n & \sin^2 \varphi_n & \ldots & \sin^{n-1} \varphi_n
\end{vmatrix}.
\]

333.
\[
\begin{vmatrix}
1 & \cos \varphi_1 & \cos^2 \varphi_1 & \ldots & \cos^{n-1} \varphi_1 \\
1 & \cos \varphi_2 & \cos^2 \varphi_2 & \ldots & \cos^{n-1} \varphi_2 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \cos \varphi_n & \cos^2 \varphi_n & \ldots & \cos^{n-1} \varphi_n
\end{vmatrix}.
\]

334.
\[
\begin{vmatrix}
1 & \varphi_1(x_1) & \varphi_2(x_1) & \ldots & \varphi_{n-1}(x_1) \\
1 & \varphi_1(x_2) & \varphi_2(x_2) & \ldots & \varphi_{n-1}(x_2) \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \varphi_1(x_n) & \varphi_2(x_n) & \ldots & \varphi_{n-1}(x_n)
\end{vmatrix},
\]
где \( \varphi_k(x) = x^k + a_{k1} x^{k-1} + a_{k2} x^{k-2} + \ldots + a_{kk} \).