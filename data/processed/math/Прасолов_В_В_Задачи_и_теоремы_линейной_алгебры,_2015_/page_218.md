---
source_image: page_218.png
page_number: 218
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.12
tokens: 6689
characters: 2876
timestamp: 2025-12-24T08:13:36.939645
finish_reason: stop
---

Жордановой матрицей называют матрицу, состоящую из диагональных блоков \( J_{r_i}(\lambda_i) \) и нулей вне этих блоков.

Жордановым базисом для оператора \( A : V \to V \) называют базис пространства \( V \), в котором матрица \( A \) является жордановой.

Теорема 14.2.1. Для любого линейного оператора \( A : V \to V \) над алгебраически замкнутым полем существует жорданов базис, причём жорданова матрица оператора \( A \) определена однозначно с точностью до перестановки жордановых клеток.

Доказательство [Vä1]. Докажем сначала существование жорданова базиса. Доказательство проведем индукцией по \( n = \dim V \). При \( n = 1 \) утверждение очевидно. Пусть \( \lambda \) — собственное значение оператора \( A \). Рассмотрим вырожденный оператор \( B = A - \lambda I \). Жорданов базис для оператора \( B \) будет также жордановым базисом для оператора \( A = B + \lambda I \). Последовательность \( \operatorname{Im} B^0 \supset \operatorname{Im} B^1 \supset \operatorname{Im} B^2 \supset \ldots \) стабилизируется, поэтому можно выбрать натуральное число \( p \) так, что \( \operatorname{Im} B^{p+1} = \operatorname{Im} B^p \neq \operatorname{Im} B^{p-1} \). Тогда

\[
\operatorname{Im} B^p \cap \operatorname{Ker} B = 0 \quad \text{и} \quad \operatorname{Im} B^{p-1} \cap \operatorname{Ker} B \neq 0.
\]

Следовательно, \( B^p(\operatorname{Im} B^p) = \operatorname{Im} B^p \).

Пусть \( S_i = \operatorname{Im} B^{i-1} \cap \operatorname{Ker} B \). Тогда \( \operatorname{Ker} B = S_1 \supset S_2 \supset \ldots \supset S_p \neq 0 \) и \( S_{p+1} = 0 \). Следить за дальнейшим ходом доказательства поможет рис. 6. Выберем в пространстве \( S_p \) базис \( x_i^1 \ (i = 1, \ldots, n_p) \). Так как \( x_i^1 \in \operatorname{Im} B^{p-1} \), то \( x_i^1 = B^{p-1} x_i^p \) для некоторого вектора \( x_i^p \). Рассмотрим векторы \( x_i^k = B^{p-k} x_i^p \ (k = 1, \ldots, p) \). Векторы \( x_i^1 \) дополним до базиса пространства \( S_{p-1} \) векторами \( y_j^1 \), найдём вектор \( y_j^{p-1} \), для которого \( y_j^1 = B^{p-2} y_j^{p-1} \), и рассмотрим векторы \( y_j^l = B^{p-l-1} y_j^{p-1} \ (l = 1, \ldots, p-1) \). Затем дополним векторы \( x_i^1 \) и \( y_j^1 \) до базиса пространства \( S_{p-2} \) векторами \( z_k^1 \) и т. д. Если \( i \) изменяется от 1 до \( I, \ldots, t \) изменяется от 1 до \( T \), то количество всех выбранных векторов равно

\[
pI + (p-1)J + \ldots + 2S + T = I + (I + J) + \ldots + (I + J + \ldots + S + T) =
= \dim S_p + \dim S_{p-1} + \ldots + \dim S_1.
\]

А так как \( \dim (\operatorname{Im} B^{i-1} \cap \operatorname{Ker} B) = \dim \operatorname{Ker} B^i - \dim \operatorname{Ker} B^{i-1} \) (см. п. 6.1), то \( \prod_{i=1}^p \dim S_i = \dim \operatorname{Ker} B^p \).

Дополним выбранные векторы базисом пространства \( \operatorname{Im} B^p \) и докажем, что получится базис пространства \( V \). Количество этих век-