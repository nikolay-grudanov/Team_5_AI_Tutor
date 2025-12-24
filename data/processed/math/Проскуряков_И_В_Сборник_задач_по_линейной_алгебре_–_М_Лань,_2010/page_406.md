---
source_image: page_406.png
page_number: 406
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.58
tokens: 5742
characters: 2527
timestamp: 2025-12-24T07:15:09.410666
finish_reason: stop
---

полагая \( \lambda = \lambda_k \) в равенстве \( r(\lambda) = \sum_{k=1}^s \varphi_k(\lambda)\psi_k(\lambda) \) и равенствах, полученных из него \( j \)-кратным дифференцированием (\( j < r_k \)), мы получим

\[
r^{(j)}(\lambda_k) = f^{(j)}(\lambda_k) \quad (j = 0, 1, \ldots, r_k - 1; \quad k = 1, 2, \ldots, s),
\]

т. е. значения \( r(\lambda) \) и \( f(\lambda) \) на спектре матрицы совпадают.

**1152.** \( f(A) = [aE + b(A - \lambda_1 E)](A - \lambda_2 E)^3 + [cE + d(A - \lambda_2 E) + e(A - \lambda_2 E)^2](A - \lambda_1 E)^2 \), где

\[
\begin{align*}
a &= \frac{f(\lambda_1)}{(\lambda_1 - \lambda_2)^3}, \\
b &= -\frac{3}{(\lambda_1 - \lambda_2)^4} f(\lambda_1) + \frac{1}{(\lambda_1 - \lambda_2)^3} f'(\lambda_1), \\
c &= \frac{f(\lambda_2)}{(\lambda_2 - \lambda_1)^2}, \\
d &= -\frac{2}{(\lambda_2 - \lambda_1)^3} f(\lambda_2) + \frac{1}{(\lambda_2 - \lambda_1)^2} f'(\lambda_2), \\
e &= \frac{3}{(\lambda_2 - \lambda_1)^4} f(\lambda_2) - \frac{2}{(\lambda_2 - \lambda_1)^3} f'(\lambda_2) + \frac{1}{2! 2! (\lambda_2 - \lambda_1)^2} f''(\lambda_2).
\end{align*}
\]

**1154. Указание.** Показать, что значения интерполяционного многочлена Лагранжа–Сильвестра \( r(\lambda) \) для \( f(\lambda) \) на спектре матрицы \( A \) совпадают со значениями \( f(\lambda) \) на спектре каждой клетки \( A_k \), и применить задачу 1147.

**1155.** \( r(\lambda) = f(0) + f'(0)\lambda + \frac{f''(0)}{2!}\lambda^2 + \cdots + \frac{f^{(n-1)}(0)}{(n-1)!}\lambda^{n-1} \).

\[
f(A) = \begin{pmatrix}
f(0) & f'(0) & \frac{f''(0)}{2!} & \cdots & \frac{f^{(n-1)}(0)}{(n-1)!} \\
0 & f(0) & f'(0) & \cdots & \frac{f^{(n-2)}(0)}{(n-2)!} \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \cdots & f(0)
\end{pmatrix}.
\]

\( f(A) \) имеет смысл для любой функции \( f(\lambda) \), для которой определены значения \( f(0), f'(0), \ldots, f^{(n-1)}(0) \).

**1156.** \( r(\lambda) = f(\alpha) + f'(\alpha)(\lambda - \alpha) + \frac{f''(\alpha)}{2!}(\lambda - \alpha)^2 + \cdots + \frac{f^{(n-1)}(\alpha)}{(n-1)!}(\lambda - \alpha)^{n-1} \).

\[
f(A) = \begin{pmatrix}
f(\alpha) & f'(\alpha) & \frac{f''(\alpha)}{2!} & \cdots & \frac{f^{(n-1)}(\alpha)}{(n-1)!} \\
0 & f(\alpha) & f'(\alpha) & \cdots & \frac{f^{(n-2)}(\alpha)}{(n-2)!} \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \cdots & f(\alpha)
\end{pmatrix}.
\]

\( f(A) \) имеет смысл для любой функции \( f(\lambda) \), для которой существуют значения \( f(\alpha), f'(\alpha), \ldots, f^{(n-1)}(\alpha) \).

**1160. Указание.** Применить предыдущую задачу.