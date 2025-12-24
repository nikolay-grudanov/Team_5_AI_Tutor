---
source_image: page_403.png
page_number: 403
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.57
tokens: 5623
characters: 2276
timestamp: 2025-12-24T07:14:57.579923
finish_reason: stop
---

1137.
\[
\begin{pmatrix}
\alpha^k & C_k^1 \alpha^{k-1} & C_k^2 \alpha^{k-2} & C_k^3 \alpha^{k-3} & \ldots & C_k^{n-1} \alpha^{k-n+1} \\
0 & \alpha^k & C_k^1 \alpha^{k-1} & C_k^2 \alpha^{k-2} & \ldots & C_k^{n-2} \alpha^{k-n+2} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & \alpha^k
\end{pmatrix},
\]
при \( k \leq n - 1 \) здесь следует положить \( C_k^0 = 1 \) и \( C_k^s \) для \( k < s \).

1138. Указание. Положить \( A = \alpha E + H \) и в равенстве
\[
f(x) = f(\alpha) + \frac{f'(\alpha)}{1!}(x-\alpha) + \frac{f''(\alpha)}{2!}(x-\alpha)^2 + \cdots + \frac{f^{(s)}(\alpha)}{s!}(x-\alpha)^s
\]
\((s — степень многочлена \( f(x) \)) положить \( x = A \).

1140. Одна клетка Жордана с числом \( \alpha^2 \) на диагонали.

1141. Если \( n > 1 \) порядок клетки Жордана \( A \) с нулем на диагонали, то жорданова форма матрицы \( A^2 \) состоит из двух клеток с нулем на диагонали, имеющих порядки \( n/2 \) при четном \( n \) и \( (n-1)/2, (n+1)/2 \) при нечетном \( n \).
Указание. Пользуясь задачей 1130, найти минимальные многочлены матриц \( A \) и \( A^2 \) и показать, что клетки жордановой формы матрицы \( A^2 \) имеют порядки не выше \( n/2 \) для четного \( n \) и \( (n+1)/2 \) для нечетного \( n \). Проверить, что делитель миноров \( D_{n-2}(\lambda) \) матрицы \( A^2 - \lambda E \) равен единице, и далее показать, что жорданова форма матрицы \( A^2 \) содержит не более двух клеток.

1143. Искомая матрица содержит две клетки Жордана с числом \( \alpha \) на диагонали, имеющих порядки \( n/2 \) при четном \( n \) или \( (n-1)/2 \) и \( (n+1)/2 \) при нечетном \( n \).
Указание. Применить две предыдущие задачи.

1144. Решение. Пусть \( A = T B T^{-1} \), где \( A \) — данная матрица и
\[
B = \begin{pmatrix}
B_1 & & & 0 \\
& B_2 & & \\
& & \ddots & \\
0 & & & B_k
\end{pmatrix}
\]
— ее жорданова форма с клетками Жордана
\[
B_i = \begin{pmatrix}
\lambda_i & 1 & 0 & \ldots & 0 \\
0 & \lambda_i & 1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & \lambda_i
\end{pmatrix} \quad (i = 1, 2, \ldots, k).
\]
Тогда \( A' = T'^{-1} B' T' \). Пусть
\[
H_i = \begin{pmatrix}
0 & \ldots & 0 & 1 \\
0 & \ldots & 1 & 0 \\
\ldots & \ldots & \ldots & \ldots \\
1 & \ldots & 0 & 0
\end{pmatrix}
\]