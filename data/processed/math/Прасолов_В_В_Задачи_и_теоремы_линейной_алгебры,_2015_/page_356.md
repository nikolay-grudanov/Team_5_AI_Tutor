---
source_image: page_356.png
page_number: 356
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.52
tokens: 6725
characters: 2791
timestamp: 2025-12-24T08:17:22.024752
finish_reason: stop
---

Доказательство [Mi2]. Рассмотрим сначала случай \( k = 2 \). Пусть \( A, B > 0 \). Тогда существует такая матрица \( P \), что \( P^*AP = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) = \Lambda \) и \( P^*BP = I \). Поэтому \( P^*(\alpha A + (1 - \alpha)B)P = \alpha \Lambda + (1 - \alpha)I \), т. е.

\[
|\alpha A + (1 - \alpha)B| \cdot |P^*P| = |\alpha \Lambda + (1 - \alpha)I|;
\]

ясно также, что \( |P^*P| = |B|^{-1} \). Следовательно,

\[
|\alpha A + (1 - \alpha)B| = |B| \div \left( \sum_{i=1}^n (\alpha \lambda_i + 1 - \alpha) \right).
\]

Докажем теперь, что если \( 0 < \alpha < 1 \) и \( \lambda > 0 \), то \( \alpha \lambda + 1 - \alpha \geq \lambda^\alpha \). Функция \( f(t) = \lambda^t \) выпукла вниз, так как \( f''(t) = (\ln \lambda)^2 \lambda^t \geq 0 \). Поэтому \( f(\alpha x + (1 - \alpha)y) \leq \alpha f(x) + (1 - \alpha)f(y) \). Остаётся положить \( x = 1 \) и \( y = 0 \). В итоге получаем

\[
|\alpha A + (1 - \alpha)B| \geq |B| \cdot |\Lambda|^\alpha = |B| \cdot |A|^\alpha |B|^{-\alpha} = A^\alpha |B|^{1-\alpha}.
\]

Дальнейшее доказательство проведём индукцией по \( k \); будем считать, что \( k \geq 3 \). Так как \( \alpha_1 A_1 + \ldots + \alpha_k A_k = (1 - \alpha_k)B + \alpha_k A_k \), причём матрица \( B = \alpha_1 A_1/(1 - \alpha_k) + \ldots + \alpha_{k-1} A_{k-1}/(1 - \alpha_k) \) положительно определена, то

\[
|\alpha_1 A_1 + \ldots + \alpha_k A_k| \geq \left| \frac{\alpha_1}{1 - \alpha_k} A_1 + \ldots + \frac{\alpha_{k-1}}{1 - \alpha_k} A_{k-1} \right|^{1 - \alpha_k} |A_k|^{\alpha_k}.
\]

А так как \( \frac{\alpha_1}{1 - \alpha_k} + \ldots + \frac{\alpha_{k-1}}{1 - \alpha_k} = 1 \), то

\[
\left| \frac{\alpha_1}{1 - \alpha_k} A_1 + \ldots + \frac{\alpha_{k-1}}{1 - \alpha_k} A_{k-1} \right| \geq |A_1|^{\alpha_1/(1-\alpha_k)} \ldots |A_{k-1}|^{\alpha_{k-1}/(1-\alpha_k)}. \quad \Box
\]

Замечание. Можно проверить, что равенство достигается тогда и только тогда, когда \( A_1 = \ldots = A_k \).

Теорема 36.3.2. Пусть \( \lambda_i \) — произвольные комплексные числа и \( A_i \geq 0 \). Тогда

\[
|\det(\lambda_1 A_1 + \ldots + \lambda_k A_k)| \leq \det(|\lambda_1| A_1 + \ldots + |\lambda_k| A_k).
\]

Доказательство [Fr1]. Пусть \( k = 2 \); можно считать, что \( \lambda_1 = 1 \) и \( \lambda_2 = \lambda \). Существует такая унитарная матрица \( U \), что матрица \( UA_1 U^{-1} = D \) диагональна. Тогда \( M = UA_2 U^{-1} \geq 0 \) и

\[
\det(A_1 + \lambda A_2) = \det(D + \lambda M) = \sum_{p=0}^n \lambda^p \cdot \prod_{i_1 < \ldots < i_p} M\begin{pmatrix} i_1 & \ldots & i_p \\ i_1 & \ldots & i_p \end{pmatrix} d_{j_1} \ldots d_{j_{n-p}},
\]

где набор \( (j_1, \ldots, j_{n-p}) \) дополняет \( (i_1, \ldots, i_p) \) до \( (1, \ldots, n) \) (см. решение задачи 2.1). Из неотрицательной определённости матриц \( M \) и \( D \)