---
source_image: page_359.png
page_number: 359
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.63
tokens: 6517
characters: 2283
timestamp: 2025-12-24T08:17:21.886687
finish_reason: stop
---

36.7. Докажите, что если \( A > 0 \), то \( |A|^{1/n} = \min \operatorname{tr}(AB)/n \), где \( n \) — порядок матрицы \( A \) и минимум берётся по всем положительно определённым матрицам \( B \) с определителем 1.

36.8. Пусть \( A \) — вещественная положительно определённая матрица с собственными значениями \( \lambda_1 \geq \lambda_2 \geq \ldots \geq \lambda_n \). Докажите, что для любого вектора \( x \) единичной длины выполняется неравенство Канторовича

\[
(Ax, x)(A^{-1}x, x) \leq \frac{(\lambda_1 + \lambda_n)^2}{4\lambda_1 \lambda_n}.
\]

§ 37. Неравенства для собственных значений

37.1. Неравенство Шура

Теорема 37.1.1 (неравенство Шура). Пусть \( \lambda_1, \ldots, \lambda_n \) — собственные значения матрицы \( A = \|a_{ij}\|_1^n \). Тогда \( \sum_{i=1}^n |\lambda_i|^2 \leq \sum_{i,j=1}^n |a_{ij}|^2 \), причём равенство достигается тогда и только тогда, когда \( A \) — нормальная матрица.

Доказательство. Существует такая унитарная матрица \( U \), что матрица \( T = U^*AU \) верхняя треугольная, причём матрица \( T \) диагональна тогда и только тогда, когда матрица \( A \) нормальна (теорема 19.1.1). Так как \( T^* = U^*A^*U \), то \( TT^* = U^*AA^*U \), а значит, \( \operatorname{tr}(TT^*) = \operatorname{tr}(AA^*) \). Остаётся заметить, что

\[
\operatorname{tr}(AA^*) = \sum_{i,j=1}^n |a_{ij}|^2 \quad \text{и} \quad \operatorname{tr}(TT^*) = \sum_{i=1}^n |\lambda_i|^2 + \sum_{i<j} |\tau_{ij}|^2.
\]

Теорема 37.1.2. Пусть \( \lambda_1, \ldots, \lambda_n \) — собственные значения матрицы \( A = B + iC \), где матрицы \( B \) и \( C \) эрмитовы. Тогда

\[
\sum_{i=1}^n |\operatorname{Re} \lambda_i|^2 \leq \sum_{i,j=1}^n |b_{ij}|^2 \quad \text{и} \quad \sum_{i=1}^n |\operatorname{Im} \lambda_i|^2 \leq \sum_{i,j=1}^n |c_{ij}|^2.
\]

Доказательство. Пусть, как и в доказательстве теоремы 37.1.1, \( T = U^*AU \). Так как \( B = (A + A^*)/2 \) и \( iC = (A - A^*)/2 \), то \( U^*BU = (T + T^*)/2 \) и \( U^*(iC)U = (T - T^*)/2 \). Поэтому

\[
\sum_{i,j=1}^n |b_{ij}|^2 = \operatorname{tr}(BB^*) = \frac{1}{4} \operatorname{tr}(T + T^*)^2 = \sum_{i=1}^n |\operatorname{Re} \lambda_i|^2 + \frac{1}{2} \sum_{i<j} |\tau_{ij}|^2
\]

И

\[
\sum_{i,j=1}^n |c_{ij}|^2 = \sum_{i=1}^n |\operatorname{Im} \lambda_i|^2 + \frac{1}{2} \sum_{i<j} |\tau_{ij}|^2.
\]