---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.04
tokens: 6619
characters: 2709
timestamp: 2025-12-24T08:14:31.591030
finish_reason: stop
---

нулевым собственным значением. Тогда

\[(N + \lambda I)^{-1} N = \lambda^{-1}(I - \lambda^{-1} N + \lambda^{-2} N^2 - ...) N = \lambda^{-1} N - \lambda^{-2} N^2 + ...\]

предел при \( \lambda \to 0 \) существует, только если \( N = 0 \).

Итак, чтобы указанный предел существовал, матрица \( A \) не должна иметь ненулевых жордановых клеток с нулевым собственным значением. Это условие эквивалентно тому, что \( \operatorname{rk} A = \operatorname{rk} A^2 \).

§ 15. Минимальный многочлен и характеристический многочлен

15.1. Пусть \( (\lambda_1, \ldots, \lambda_n) \) — диагональ жордановой нормальной формы матрицы \( A \), \( \sigma_k = \sigma_k(\lambda_1, \ldots, \lambda_n) \). Тогда \( |\lambda I - A| = \sum_{k=0}^n (-1)^k \lambda^{n-k} \sigma_k \). Поэтому достаточно доказать, что \( f_m(A) = \sum_{k=0}^m (-1)^k A^{m-k} \sigma_k \) для всех \( m \). При \( m = 1 \) это равенство совпадает с определением \( f_1 \). Предположим, что утверждение доказано для \( m \) и докажем его для \( m + 1 \). Ясно, что

\[
f_{m+1}(A) = \sum_{k=0}^m (-1)^k A^{m-k+1} \sigma_k - \frac{1}{m+1} \operatorname{tr} \left( \sum_{k=0}^m (-1)^k A^{m-k+1} \sigma_k \right) I.
\]

Так как

\[
\operatorname{tr} \left( \sum_{k=0}^m (-1)^k A^{m-k+1} \sigma_k \right) = \sum_{k=0}^m (-1)^k s_{m-k+1} \sigma_k,
\]

где \( s_p = \lambda_1^p + \ldots + \lambda_n^p \), то остаётся заметить, что

\[
\sum_{k=0}^m (-1)^k s_{m-k+1} \sigma_k + (m+1)(-1)^{m+1} \sigma_{m+1} = 0
\]

(см. п. 4.1).

15.2. Согласно решению задачи 15.1 коэффициенты характеристического многочлена матрицы \( X \) являются функциями от \( \operatorname{tr} X, \ldots, \operatorname{tr}(X^n) \), поэтому характеристические многочлены матриц \( A \) и \( B \) совпадают.

15.3. Если \( \lambda_1, \ldots, \lambda_k \) — различные собственные значения матрицы \( A \), то \( p_A(t) = (t - \lambda_1)^{n_1} \ldots (t - \lambda_k)^{n_k} \) для некоторых натуральных \( n_1, \ldots, n_k \). Поэтому

\[
|p_A(B)| = |B - \lambda_1 I|^{n_1} \ldots |B - \lambda_k I|^{n_k} \neq 0.
\]

Действительно, \( |B - \lambda_i I| \neq 0 \), поскольку \( \lambda_i \) не является собственным значением матрицы \( B \).

15.4. Пусть \( f(\lambda) \) — произвольный многочлен, \( g(\lambda) = \lambda^n f(\lambda^{-1}) \) и \( B = A^{-1} \). Если \( 0 = g(B) = B^n f(A) \), то \( f(A) = 0 \). Поэтому минимальный многочлен матрицы \( B \) пропорционален \( \lambda^n p(\lambda^{-1}) \). Остаётся заметить, что старший коэффициент многочлена \( \lambda^n p(\lambda^{-1}) \) равен \( \lim_{\lambda \to \infty} (\lambda^n p(\lambda^{-1}))/\lambda^n = p(0) \).

15.5. Ясно, что

\[
B_k = \{ A \in M_n \mid \text{матрицы } I, A, A^2, \ldots, A^{k-1} \text{ линейно зависимы} \}.
\]