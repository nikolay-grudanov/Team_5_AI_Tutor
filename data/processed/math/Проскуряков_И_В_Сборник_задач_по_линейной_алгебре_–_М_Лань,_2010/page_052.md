---
source_image: page_052.png
page_number: 52
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.95
tokens: 5680
characters: 1943
timestamp: 2025-12-24T07:06:40.855028
finish_reason: stop
---

335.
\[
\begin{vmatrix}
1 & 1 & \ldots & 1 \\
f_1(\cos \varphi_1) & f_1(\cos \varphi_2) & \ldots & f_1(\cos \varphi_n) \\
f_2(\cos \varphi_1) & f_2(\cos \varphi_2) & \ldots & f_2(\cos \varphi_n) \\
\vdots & \vdots & & \vdots \\
f_{n-1}(\cos \varphi_1) & f_{n-1}(\cos \varphi_2) & \ldots & f_{n-1}(\cos \varphi_n)
\end{vmatrix},
\]
где \( f_k(x) = a_{k0} x^k + a_{k1} x^{k-1} + a_{k2} x^{k-2} + \cdots + a_{kk} \).

336.
\[
\begin{vmatrix}
1 & C^1_{x_1} & C^2_{x_1} & \ldots & C^{n-1}_{x_1} \\
1 & C^1_{x_2} & C^2_{x_2} & \ldots & C^{n-1}_{x_2} \\
\vdots & \vdots & \vdots & & \vdots \\
1 & C^1_{x_n} & C^2_{x_n} & \ldots & C^{n-1}_{x_n}
\end{vmatrix},
\]
где \( C^k_x = \frac{x(x-1)(x-2)\ldots(x-k+1)}{k!} \).

337.
\[
\begin{vmatrix}
(2n-1)^n & (2n-2)^n & \ldots & n^n & (2n)^n \\
(2n-1)^{n-1} & (2n-2)^{n-1} & \ldots & n^{n-1} & (2n)^{n-1} \\
2n-1 & 2n-2 & \ldots & n & 2n \\
1 & 1 & \ldots & 1 & 1
\end{vmatrix}.
\]

338.
\[
\begin{vmatrix}
\frac{x_1}{x_1-1} & \frac{x_2}{x_2-1} & \ldots & \frac{x_n}{x_n-1} \\
x_1 & x_2 & \ldots & x_n \\
x_1^2 & x_2^2 & \ldots & x_n^2 \\
x_1^{n-1} & x_2^{n-1} & \ldots & x_n^{n-1}
\end{vmatrix}.
\]

339.
\[
\begin{vmatrix}
1 & 2 & 3 & \ldots & n \\
1 & 2^3 & 3^3 & \ldots & n^3 \\
\vdots & \vdots & \vdots & & \vdots \\
1 & 2^{2n-1} & 3^{2n-1} & \ldots & n^{2n-1}
\end{vmatrix}.
\]

340.
\[
\begin{vmatrix}
a_1^n & a_1^{n-1} b_1 & a_1^{n-2} b_1^2 & \ldots & b_1^n \\
a_2^n & a_2^{n-1} b_2 & a_2^{n-2} b_2^2 & \ldots & b_2^n \\
\vdots & \vdots & \vdots & & \vdots \\
a_{n+1}^n & a_{n+1}^{n-1} b_{n+1} & a_{n+1}^{n-2} b_{n+1}^2 & \ldots & b_{n+1}^n
\end{vmatrix}.
\]

341.
\[
\begin{vmatrix}
\sin^{n-1} \alpha_1 & \sin^{n-2} \alpha_1 \cos \alpha_1 & \ldots & \cos^{n-1} \alpha_1 \\
\sin^{n-1} \alpha_2 & \sin^{n-2} \alpha_2 \cos \alpha_2 & \ldots & \cos^{n-1} \alpha_n \\
\vdots & \vdots & & \vdots \\
\sin^{n-1} \alpha_n & \sin^{n-2} \alpha_n \cos \alpha_n & \ldots & \cos^{n-1} \alpha_n
\end{vmatrix}.
\]