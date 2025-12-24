---
source_image: page_357.png
page_number: 357
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.61
tokens: 6507
characters: 2217
timestamp: 2025-12-24T08:17:18.407990
finish_reason: stop
---

§ 36. Неравенства для симметрических и эрмитовых матриц

следует, что \( M \begin{pmatrix} i_1 & \cdots & i_p \\ i_1 & \cdots & i_p \end{pmatrix} \geqslant 0 \) и \( d_j \geqslant 0 \). Поэтому

\[
|\det(A_1 + \lambda A_2)| \leqslant \prod_{p=0}^n |\lambda|^p M \begin{pmatrix} i_1 & \cdots & i_p \\ i_1 & \cdots & i_p \end{pmatrix} d_{j_1} \ldots d_{j_{n-p}} =
= \det(D + |\lambda| M) = \det(A_1 + |\lambda| A_2).
\]

Проведём теперь доказательство индуктивного шага. Снова будем считать, что \( \lambda_1 = 1 \). Пусть \( A = A_1 \) и \( A' = \lambda_2 A_2 + \ldots + \lambda_{k+1} A_{k+1} \). Существует такая унитарная матрица \( U \), что матрица \( UAU^{-1} = D \) диагональна; матрицы \( M_j = UA_j U^{-1} \) и \( M = UA' U^{-1} \) неотрицательно определены. Поэтому

\[
|\det(A + A')| = |\det(D + M)| \leqslant \prod_{p=0}^n \prod_{i_1 < \ldots < i_p} M \begin{pmatrix} i_1 & \cdots & i_p \\ i_1 & \cdots & i_p \end{pmatrix} d_{j_1} \ldots d_{j_{n-p}}.
\]

Так как \( M = \lambda_2 M_2 + \ldots + \lambda_{k+1} M_{k+1} \), то согласно предположению индукции

\[
M \begin{pmatrix} i_1 & \cdots & i_p \\ i_1 & \cdots & i_p \end{pmatrix} \leqslant \det \left( \prod_{j=2}^{k+1} |\lambda_j| M_j \begin{pmatrix} i_1 & \cdots & i_p \\ i_1 & \cdots & i_p \end{pmatrix} \right).
\]

Остаётся заметить, что

\[
\prod_{p=0}^n \prod_{i_1 < \ldots < i_p} d_{j_1} \ldots d_{j_{n-p}} \det \left( \prod_{j=2}^{k+1} |\lambda_j| M_j \begin{pmatrix} i_1 & \cdots & i_p \\ i_1 & \cdots & i_p \end{pmatrix} \right) =
= \det(D + |\lambda_2| M_2 + \ldots + |\lambda_{k+1}| M_{k+1}) = \det(\bullet |\lambda_i| A_i).
\]

36.4. Отношение миноров

Теорема 36.4.1. Пусть вещественные матрицы \( A \) и \( B \) положительно определены, а матрицы \( A_1 \) и \( B_1 \) получаются из \( A \) и \( B \) вычёркиванием первой строки и первого столбца. Тогда

\[
\frac{|A + B|}{|A_1 + B_1|} \geqslant \frac{|A|}{|A_1|} + \frac{|B|}{|B_1|}.
\]

Доказательство [Be2]. Если \( A > 0 \), то

\[
(x, Ax)(y, A^{-1} y) \geqslant (x, y)^2.
\]

В самом деле, существует такая унитарная матрица \( U \), что \( U^* A U = \Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \), причём \( \lambda_i > 0 \). После замены \( x = Ua \) и \( y = Ub \)