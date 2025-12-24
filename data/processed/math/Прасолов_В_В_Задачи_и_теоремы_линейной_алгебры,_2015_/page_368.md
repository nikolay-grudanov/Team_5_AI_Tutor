---
source_image: page_368.png
page_number: 368
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.59
tokens: 6404
characters: 2134
timestamp: 2025-12-24T08:17:38.478924
finish_reason: stop
---

§ 38. Неравенства для норм матриц

38.1. Операторная норма

Операторной (или спектральной) нормой матрицы \( A \) называют величину \( \|A\|_s = \sup_{x \neq 0} \frac{\|Ax\|}{\|x\|} \); число \( \rho(A) = \max |\lambda_i| \), где \( \lambda_1, \ldots, \lambda_n \) — собственные значения матрицы \( A \), называют спектральным радиусом матрицы \( A \). Так как существует такой ненулевой вектор \( x \), что \( Ax = \lambda_i x \), то \( \|A\|_s \geq \rho(A) \).

Легко проверить, что если \( U \) — унитарная матрица, то \( \|A\|_s = \|AU\|_s = \|UA\|_s \). Для этого достаточно заметить, что \( \|AUx\|/\|x\| = \|Ay\|/\|U^{-1}y\| = \|Ay\|/\|y\| \), где \( y = Ux \), и \( \|UAx\|/\|x\| = \|Ax\|/\|x\| \).

Теорема 38.1.1. \( \|A\|_s = \sqrt{\rho(A^*A)} \).

Доказательство. Если \( \Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \), то
\[
\left( \frac{|\Lambda x|}{|x|} \right)^2 = \frac{\cdot |\lambda_i x_i|^2}{\cdot |x_i|^2} \leq \max |\lambda_i|.
\]
Пусть \( |\lambda_j| = \max |\lambda_i| \) и \( \Lambda x = \lambda_j x \). Тогда \( |\Lambda x|/|x| = |\lambda_j| \). Поэтому \( \|\Lambda\|_s = \rho(\Lambda) \).

Любую матрицу \( A \) можно представить в виде \( A = U \Lambda V \), где \( U \) и \( V \) — унитарные матрицы, а матрица \( \Lambda \) диагональна, причём на её диагонали стоят сингулярные числа матрицы (см. п. 37.4). Поэтому \( \|A\|_s = \|\Lambda\|_s = \rho(\Lambda) = \sqrt{\rho(A^*A)} \).

Теорема 38.1.2. Если матрица \( A \) нормальна, то \( \|A\|_s = \rho(A) \).

Доказательство. Нормальную матрицу \( A \) можно представить в виде \( A = U^* \Lambda U \), где \( \Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \) и \( U \) — унитарная матрица. Поэтому \( A^*A = U^* \Lambda \overline{\Lambda} U \). Пусть \( Ae_i = \lambda_i e_i \) и \( x_i = U^{-1} e_i \). Тогда \( A^*A x_i = |\lambda_i|^2 x_i \), а значит, \( \rho(A^*A) = \rho(A)^2 \).

38.2. Евклидова норма

Евклидовой нормой матрицы \( A \) называют величину
\[
\|A\|_e = \sqrt{\sum_{i,j} |a_{ij}|^2} = \sqrt{\operatorname{tr}(A^*A)} = \sqrt{\sum_i \sigma_i^2},
\]
где \( \sigma_i \) — сингулярные числа матрицы \( A \).