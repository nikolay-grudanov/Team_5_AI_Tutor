---
source_image: page_358.png
page_number: 358
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.46
tokens: 6357
characters: 1888
timestamp: 2025-12-24T08:17:14.575669
finish_reason: stop
---

перейдём к неравенству Коши—Шварца

\[
\left( \bullet \; \lambda_i a_i^2 \right) \left( \bullet \; \frac{b_i^2}{\lambda_i} \right) \geqslant \left( \bullet \; a_i b_i \right)^2.
\]

Неравенство (2) обращается в равенство при \( a_i = b_i / \lambda_i \), поэтому

\[
f(A) = \frac{1}{(y, A^{-1} y)} = \min_x \frac{(x, A x)}{(x, y)^2}.
\]

Докажем теперь, что если \( y = (1, 0, 0, \ldots, 0) = e_1 \), то \( f(A) = |A|/|A_1| \). В самом деле,

\[
(e_1, A^{-1} e_1) = e_1 A^{-1} e_1^T = \frac{(e_1 \operatorname{adj} A \, e_1^T)}{|A|} = \frac{(\operatorname{adj} A)_{11}}{|A|} = \frac{|A_1|}{|A|}.
\]

Остаётся заметить, что \( \min_x g(x) + \min_x h(x) \leqslant \min_x (g(x) + h(x)) \) для любых функций \( g \) и \( h \), и положить \( g(x) = (x, A x)/(x, e_1) \) и \( h(x) = (x, B x)/(x, e_1) \).

Задачи

36.1. Пусть \( A \) и \( B \) — матрицы порядка \( n \) (\( n > 1 \)), причём \( A > 0 \) и \( B \geqslant 0 \). Докажите, что \( |A + B| \geqslant |A| + |B| \), причём равенство достигается только при \( B = 0 \).

36.2. Матрицы \( A \) и \( B \) эрмитовы, причём \( A > 0 \). Докажите, что

\[
|\det (A + iB)| \geqslant \det A,
\]

причём равенство достигается только при \( B = 0 \).

36.3. Пусть \( A_k \) и \( B_k \) — угловые подматрицы порядка \( k \) положительно определённых матриц \( A \) и \( B \), причём \( A > B \). Докажите, что \( |A_k| > |B_k| \).

36.4. Пусть \( A \geqslant B \geqslant 0 \). Верно ли, что \( A^2 \geqslant B^2 \)?

36.5. Матрицы \( A \) и \( B \) вещественные симметрические, причём \( A \geqslant 0 \). Докажите, что если матрица \( C = A + iB \) вырожденная, то \( C x = 0 \) для некоторого ненулевого вещественного вектора \( x \).

36.6. Вещественная симметричная матрица \( A \) положительно определена. Докажите, что

\[
\det \begin{pmatrix}
0 & x_1 & \cdots & x_n \\
x_1 & & & \\
\vdots & & A & \\
x_n & & &
\end{pmatrix} \leqslant 0.
\]