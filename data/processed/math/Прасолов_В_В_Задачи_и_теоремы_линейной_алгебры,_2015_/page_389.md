---
source_image: page_389.png
page_number: 389
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.41
tokens: 6850
characters: 3139
timestamp: 2025-12-24T08:18:20.690370
finish_reason: stop
---

При этом \( A - \lambda_n I \leq 0, \ A - \lambda_1 I \geq 0 \) и \( A^{-1} > 0 \), значит, \( (A - \lambda_n I)(A - \lambda_1 I)A^{-1} \leq 0 \).
Для любого вектора \( x \) получаем
\[
((A + \lambda_1 \lambda_n A^{-1})x, x) \leq (\lambda_1 + \lambda_n)(x, x).
\]
Для вектора \( x \) единичной длины получаем
\[
(Ax, x) + \lambda_1 \lambda_n (A^{-1}x, x) \leq \lambda_1 + \lambda_n.
\]
Пусть \( u = \lambda_1 \lambda_n (A^{-1}x, x) \). Домножив неравенство \( (Ax, x) \leq \lambda_1 + \lambda_n - u \) на \( u \), получим
\[
u(Ax, x) \leq (\lambda_1 + \lambda_n)u - u^2 \leq \frac{(\lambda_1 + \lambda_n)^2}{4\lambda_1 \lambda_n},
\]
т. е.
\[
(Ax, x)(A^{-1}x, x) \leq \frac{(\lambda_1 + \lambda_n)^2}{4\lambda_1 \lambda_n}.
\]

§ 37. Неравенства для собственных значений

37.1. Пусть \( S = V^*DV \), где \( D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \), \( V \) — унитарная матрица. Тогда \( \operatorname{tr}(US) = \operatorname{tr}(UV^*DV) = \operatorname{tr}(VUV^*D) \). Пусть \( VUV^* = W = \|w_{ij}\|_1^n \). Тогда \( \operatorname{tr}(US) = \bullet w_{ii} \lambda_i \). Так как \( W \) — унитарная матрица, то \( |w_{ii}| \leq 1 \), а значит, \( |\bullet w_{ii} \lambda_i| \leq |\lambda_i| = \bullet \lambda_i = \operatorname{tr} S \).
Если \( S > 0 \), т. е. \( \lambda_i \neq 0 \), то \( \operatorname{tr} S = \operatorname{tr}(US) \) тогда и только тогда, когда \( w_{ii} = 1 \), т. е. \( W = I \), а значит, \( U = I \). Равенство \( \operatorname{tr} S = |\operatorname{tr}(US)| \) для положительно определённой матрицы \( S \) может выполняться, только если \( w_{ii} = e^{i\varphi} \), т. е. \( U = e^{i\varphi}I \).

37.2. Пусть \( \alpha_1 \geq \ldots \geq \alpha_n \geq 0 \) и \( \beta_1 \geq \ldots \geq \beta_n \geq 0 \) — собственные значения матриц \( A \) и \( B \). Для неотрицательно определённых матриц собственные значения совпадают с сингулярными значениями, поэтому
\[
|\operatorname{tr}(AB)| \leq \bullet \alpha_i \beta_i \leq (\bullet \alpha_i)(\bullet \beta_i) = \operatorname{tr} A \operatorname{tr} B
\]
(см. теорему 37.4.3).

37.3. а) Если \( \lim_{k \to \infty} A^k = 0 \) и \( Ax = \lambda x \), то \( \lim_{k \to \infty} \lambda^k x = 0 \). Докажем теперь, что если \( |\lambda_i| < 1 \) для всех собственных значений матрицы \( A \), то \( \lim_{k \to \infty} A^k = 0 \). Это утверждение достаточно доказать для жордановой клетки \( A = \hat{\lambda} I + N \). Ясно, что \( (\hat{\lambda} I + N)^k = \bullet \binom{k}{i} \hat{\lambda}^{k-i} N^i \) и \( N^i = 0 \) при \( i \geq n \), где \( n \) — порядок матрицы \( A \).
Остаётся заметить, что \( \binom{k}{i} < \frac{k^i}{i!} \) и \( \lim_{k \to \infty} k^i \lambda^k = 0 \).
б) Если \( Ax = \lambda x \) и матрица обладает указанными свойствами, то
\[
0 < (Hx - A^* H A x, x) = (Hx, x) - (H \lambda x, \lambda x) = (Hx, x)(1 - |\lambda|^2).
\]
Поэтому \( |\lambda| < 1 \), так как \( (Hx, x) > 0 \).
Предположим теперь, что \( \lim_{k \to \infty} A^k = 0 \). Тогда \( \lim_{k \to \infty} (A^*)^k = 0 \) и \( \lim_{k \to \infty} (A^*)^k A^k = 0 \). Легко проверить, что если \( \lim_{k \to \infty} B_k = 0 \), то все собственные значения