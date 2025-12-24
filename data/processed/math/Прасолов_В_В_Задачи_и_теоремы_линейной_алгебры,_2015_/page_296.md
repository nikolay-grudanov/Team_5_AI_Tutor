---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.41
tokens: 6839
characters: 3125
timestamp: 2025-12-24T08:15:42.453778
finish_reason: stop
---

и числа \( \lambda_1, \ldots, \lambda_n \) положительны. Тогда \( \operatorname{adj}(tA + B) = \operatorname{adj} T \operatorname{adj}(tI + D) \operatorname{adj} T^* \), причём \( \operatorname{adj} T^* = (\operatorname{adj} T)^* \). Матрица \( \operatorname{adj}(tI + D) \) диагональна, причём на диагонали на \( i \)-м месте стоит элемент \( \frac{1}{(t + \lambda_j)} \). Таким образом, эта матрица имеет вид \( t^{n-1} I + t^{n-2} \hat{A}_1 + \ldots + \hat{A}_{n-1} \), где матрицы \( \hat{A}_1, \ldots, \hat{A}_{n-1} \) диагональные и на \( i \)-м месте матрицы \( \hat{A}_k \) стоит число \( \sigma_k(\lambda_1, \ldots, \hat{\lambda}_i, \ldots, \lambda_n) \). Это число положительно, поэтому матрицы \( \hat{A}_0 = I, \hat{A}_1, \ldots, \hat{A}_{n-1} \) положительно определённые. Остаётся заметить, что если \( X \) — положительно определённая матрица, а \( S \) — невырожденная матрица, то матрица \( S^*XS \) положительно определённая.

22.3. Нет, не обязательно. Пусть \( A_1 = B_1 = \operatorname{diag}(0, 1, -1) \),

\[
A_2 = \begin{pmatrix}
0 & \sqrt{2} & 2 \\
\sqrt{2} & 0 & 0 \\
2 & 0 & 0
\end{pmatrix}
\quad \text{и} \quad
B_2 = \begin{pmatrix}
0 & 0 & \sqrt{2} \\
0 & 0 & 2 \\
\sqrt{2} & 2 & 0
\end{pmatrix}.
\]

Легко проверить, что

\[
|xA_1 + yA_2 + \lambda I| = \lambda^3 - \lambda(x^2 + 6y^2) - 2y^2x = |xB_1 + yB_2 + \lambda I|.
\]

Предположим теперь, что существует такая ортогональная матрица \( U \), что \( UA_1 U^T = B_1 = A_1 \) и \( UA_2 U^T = B_2 \). Тогда \( UA_1 = A_1 U \), а так как матрица \( A_1 \) диагональная и на диагонали стоят попарно различные числа, то \( U \) — диагональная ортогональная матрица (см. задачу 42.1 а), т. е. \( U = \operatorname{diag}(\lambda, \mu, \nu) \), где \( \lambda, \mu, \nu = \pm 1 \). Следовательно,

\[
\begin{pmatrix}
0 & 0 & \sqrt{2} \\
0 & 0 & 2 \\
\sqrt{2} & 2 & 0
\end{pmatrix} = B_2 = UA_2 U^T = \begin{pmatrix}
0 & \sqrt{2}\lambda\mu & 2\lambda\nu \\
\sqrt{2}\lambda\mu & 0 & 0 \\
2\lambda\nu & 0 & 0
\end{pmatrix}.
\]

Получено противоречие.

§ 23. Кососимметрические матрицы

23.1. Ненулевые собственные значения матрицы \( A \) чисто мнимые, поэтому \( -1 \) не может быть её собственным значением.

23.2. Так как \( (-A)^{-1} = -A^{-1} \), то \( (A^{-1})^T = (A^T)^{-1} = (-A)^{-1} = -A^{-1} \).

23.3. Размерности этих пространств дополнительные, поэтому нужно лишь проверить, что если \( X^* = X \) и \( Y^* = -Y \), то \( \operatorname{Re} \operatorname{tr}(XY) = 0 \), т. е. \( \operatorname{tr}(XY + \overline{XY}) = 0 \). Но \( \operatorname{tr}(XY) = \operatorname{tr}(XY)^T = \operatorname{tr}(-\overline{Y} \cdot \overline{X}) = -\operatorname{tr}(\overline{YX}) = -\operatorname{tr}(\overline{XY}) \).

23.4. Ясно, что \( |I + \lambda A| = |(I + \lambda A)^T| = |I - \lambda A| \). Поэтому \( f(\lambda) = f(-\lambda) \), т. е. \( f \) — чётная функция.

23.5. Доказательство проведём индукцией по \( n \). При \( n = 1 \) имеем

\[
\begin{pmatrix}
0 & x \\
-x & 0
\end{pmatrix} = \begin{pmatrix}
0 & x \\
-1 & 0
\end{pmatrix} \begin{pmatrix}
-x & 0 \\
0 & 1
\end{pmatrix}.
\]

Для доказательства шага индукции разберём два случая.