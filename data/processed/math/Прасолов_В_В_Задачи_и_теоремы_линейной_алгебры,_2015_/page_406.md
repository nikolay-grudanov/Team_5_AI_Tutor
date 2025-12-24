---
source_image: page_406.png
page_number: 406
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.01
tokens: 6782
characters: 3029
timestamp: 2025-12-24T08:18:44.939178
finish_reason: stop
---

Доказательство [Gi]. Существует такая матрица \( P \), что все диагональные элементы матрицы \( PAP^{-1} = B = \| b_{ij} \|_1^n \) нулевые (см. п. 17.1). Пусть \( D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \) и \( c_{ij} = b_{ij}/(\lambda_i - \lambda_j) \) при \( i \neq j \). Диагональные элементы \( c_{ii} \) матрицы \( C \) можно подобрать так, чтобы она имела собственные значения \( \mu_1, \ldots, \mu_n \) (теорема 55.2.2). Тогда \( DC - CD = = \| (\lambda_i - \lambda_j)c_{ij} \|_1^n = B \). Остаётся положить \( X = P^{-1}DP \) и \( Y = P^{-1}CP \).

43.3. Равенство \( \operatorname{ad}_A^s X = 0 \) влечёт равенство \( \operatorname{ad}_X^s B = 0 \)

Теорема 43.3.1. Пусть матрицы \( A \) и \( B \) таковы, что для некоторого \( s > 0 \) равенство \( \operatorname{ad}_A^s X = 0 \) влечёт равенство \( \operatorname{ad}_X^s B = 0 \). Тогда матрица \( B \) полиномиально выражается через \( A \).

Доказательство [Sm]. Случай \( s = 1 \) разобран в п. 42.3; поэтому в дальнейшем будем считать, что \( s \geq 2 \). Отметим, что при \( s \geq 2 \) из равенства \( \operatorname{ad}_A^s X = 0 \) не обязательно следует равенство \( \operatorname{ad}_X^s A = 0 \).

Можно считать, что \( A = \operatorname{diag}(J_1, \ldots, J_t) \), где \( J_i \) — жорданова клетка. Пусть \( X = \operatorname{diag}(1, \ldots, n) \). Легко проверить, что \( \operatorname{ad}_A^2 X = 0 \) (см. задачу 43.1), а значит, \( \operatorname{ad}_A^s X = 0 \) и \( \operatorname{ad}_X^s B = 0 \). Матрица \( X \) диагонализируема, поэтому \( \operatorname{ad}_X B = 0 \) (см. задачу 43.8). Следовательно, \( B \) — диагональная матрица (см. задачу 42.1 а)). В соответствии с блочной записью \( A = \operatorname{diag}(J_1, \ldots, J_t) \) запишем матрицы \( B \) и \( X \) в виде \( B = \operatorname{diag}(B_1, \ldots, B_t) \) и \( X = \operatorname{diag}(X_1, \ldots, X_t) \). Пусть

\[
Y = \operatorname{diag}((J_1 - \lambda_1 I)X_1, \ldots, (J_t - \lambda_t I)X_t),
\]

где \( \lambda_i \) — собственное значение жордановой клетки \( J_i \). Тогда \( \operatorname{ad}_A^2 Y = 0 \) (см. задачу 43.1). Следовательно, \( \operatorname{ad}_A^2 (X + Y) = 0 \), а значит, \( \operatorname{ad}_{X+Y}^2 B = 0 \). Матрица \( X + Y \) диагонализируема, так как её собственные значения равны \( 1, \ldots, n \). Поэтому \( \operatorname{ad}_{X+Y} B = 0 \), а значит, \( \operatorname{ad}_Y B = 0 \).

Из равенств \([X, B] = 0\) и \([Y, B] = 0\) следует, что \( B_i = b_i I \) (см. задачу 42.1). Докажем, что если собственные значения матриц \( J_i \) и \( J_{i+1} \) равны, то \( b_i = b_{i+1} \). Рассмотрим матрицу

\[
U = \begin{pmatrix}
0 & \ldots & 0 & 1 \\
0 & \ldots & 0 & 0 \\
\cdots & \cdots & \cdots & \cdots \\
0 & \ldots & 0 & 0
\end{pmatrix},
\]

порядок которой равен сумме порядков матриц \( J_i \) и \( J_{i+1} \), и в соответствии с блочной записью \( A = \operatorname{diag}(J_1, \ldots, J_t) \) введём матрицу \( Z = \operatorname{diag}(0, U, 0) \). Легко проверить, что \( ZA = AZ = \lambda Z \), где \( \lambda \) — соб-