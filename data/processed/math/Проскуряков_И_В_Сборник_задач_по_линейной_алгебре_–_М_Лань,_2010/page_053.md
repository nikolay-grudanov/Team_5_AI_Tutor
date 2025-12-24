---
source_image: page_053.png
page_number: 53
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.65
tokens: 5932
characters: 2459
timestamp: 2025-12-24T07:06:49.903912
finish_reason: stop
---

342.
\[
\begin{vmatrix}
f_n(x_1, y_1) & y_1 f_{n-1}(x_1, y_1) & \ldots & y_1^{n-1} f_1(x_1, y_1) & y_1^n \\
f_n(x_2, y_2) & y_2 f_{n-1}(x_2, y_2) & \ldots & y_2^{n-1} f_1(x_2, y_2) & y_2^n \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
f_n(x_{n+1}, y_{n+1}) & y_{n+1} f_{n-1}(x_{n+1}, y_{n+1}) & \ldots & y_{n+1}^{n-1} f_1(x_{n+1}, y_{n+1}) & y_{n+1}^n
\end{vmatrix},
\]
где \( f_i(x, y) \) — однородный многочлен \( x, y \) степени \( i \).

343.
\[
\begin{vmatrix}
a_1 & x_1 & x_1^2 & \ldots & x_1^{n-1} \\
a_2 & x_2 & x_2^2 & \ldots & x_2^{n-1} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_n & x_n & x_n^2 & \ldots & x_n^{n-1}
\end{vmatrix}.
\]

*344.
\[
\begin{vmatrix}
1 & x_1 & x_1^2 & \ldots & x_1^{n-2} & x_1^n \\
1 & x_2 & x_2^2 & \ldots & x_2^{n-2} & x_2^n \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
1 & x_n & x_n^2 & \ldots & x_n^{n-2} & x_n^n
\end{vmatrix}.
\]

345.
\[
\begin{vmatrix}
1 & x_1^2 & x_1^3 & \ldots & x_1^n \\
1 & x_2^2 & x_2^3 & \ldots & x_2^n \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n^2 & x_n^3 & \ldots & x_n^n
\end{vmatrix}.
\]

346.
\[
\begin{vmatrix}
1 & x_1 & x_1^2 & \ldots & x_1^{s-1} & x_1^{s+1} & \ldots & x_1^n \\
1 & x_2 & x_2^2 & \ldots & x_2^{s-1} & x_2^{s+1} & \ldots & x_2^n \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n & x_n^2 & \ldots & x_n^{s-1} & x_n^{s+1} & \ldots & x_n^n
\end{vmatrix}.
\]

*347.
\[
\begin{vmatrix}
1 & x_1(x_1-1) & x_1^2(x_1-1) & \ldots & x_1^{n-1}(x_1-1) \\
1 & x_2(x_2-1) & x_2^2(x_2-1) & \ldots & x_2^{n-1}(x_2-1) \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_n(x_n-1) & x_n^2(x_n-1) & \ldots & x_n^{n-1}(x_n-1)
\end{vmatrix}.
\]

*348.
\[
\begin{vmatrix}
1 + x_1 & 1 + x_1^2 & \ldots & 1 + x_1^n \\
1 + x_2 & 1 + x_2^2 & \ldots & 1 + x_2^n \\
\vdots & \vdots & \ddots & \vdots \\
1 + x_n & 1 + x_n^2 & \ldots & 1 + x_n^n
\end{vmatrix}.
\]

*349.
\[
\begin{vmatrix}
1 & \cos \varphi_1 & \cos 2\varphi_1 & \ldots & \cos(n-1)\varphi_1 \\
1 & \cos \varphi_2 & \cos 2\varphi_2 & \ldots & \cos(n-1)\varphi_2 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & \cos \varphi_n & \cos 2\varphi_n & \ldots & \cos(n-1)\varphi_n
\end{vmatrix}.
\]

*350.
\[
\begin{vmatrix}
\sin \varphi_1 & \sin 2\varphi_1 & \ldots & \sin n\varphi_1 \\
\sin \varphi_2 & \sin 2\varphi_2 & \ldots & \sin n\varphi_2 \\
\vdots & \vdots & \ddots & \vdots \\
\sin \varphi_n & \sin 2\varphi_n & \ldots & \sin n\varphi_n
\end{vmatrix}.
\]