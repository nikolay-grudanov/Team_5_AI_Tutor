---
source_image: page_181.png
page_number: 181
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.30
tokens: 5401
characters: 1875
timestamp: 2025-12-24T07:09:29.616704
finish_reason: stop
---

1136. Доказать, что для подобия двух матриц необходимо (но не достаточно), чтобы они имели одинаковые характеристический и минимальный многочлены. Привести пример двух неподобных матриц, у которых характеристический многочлен \( \varphi(\lambda) \) и минимальный многочлен \( \psi(\lambda) \) одни и те же.

1137. Найти \( k \)-ю степень \( A^k \) жордановой клетки

\[
A = \begin{pmatrix}
\alpha & 1 & 0 & 0 & \ldots & 0 & 0 \\
0 & \alpha & 1 & 0 & \ldots & 0 & 0 \\
0 & 0 & \alpha & 1 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & \alpha & 1 \\
0 & 0 & 0 & 0 & \ldots & 0 & \alpha
\end{pmatrix}
\]

порядка \( n \).

1138. Доказать, что значение многочлена \( f(x) \) от клетки Жордана \( A \) порядка \( n \) с числом \( \alpha \) на главной диагонали определяется формулой

\[
A = \begin{pmatrix}
\alpha & 1 & 0 & \ldots & 0 \\
0 & \alpha & 1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & \alpha
\end{pmatrix}
\]

\[
f(A) = \begin{pmatrix}
f(\alpha) & \frac{f'(\alpha)}{1!} & \frac{f''(\alpha)}{2!} & \frac{f'''(\alpha)}{3!} & \ldots & \frac{f^{(n-1)}(\alpha)}{(n-1)!} \\
0 & f(\alpha) & \frac{f'(\alpha)}{1!} & \frac{f''(\alpha)}{2!} & \ldots & \frac{f^{(n-2)}(\alpha)}{(n-2)!} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & f(\alpha)
\end{pmatrix}.
\]

1139. Решить задачу 1080, пользуясь жордановой формой матрицы \( A \).

1140. Найти жорданову форму квадрата жордановой клетки, на диагонали которой стоит число \( \alpha \neq 0 \).

*1141. Найти жорданову форму квадрата жордановой клетки с нулем на главной диагонали (нильпотентная клетка Жордана).

1142. Пусть \( X_j \) — жорданова форма матрицы \( X \). Доказать равенство \( (A + \alpha E)_j = A_j + \alpha E \), где \( A \) — любая квадратная матрица и \( \alpha \) — число.