---
source_image: page_490.png
page_number: 490
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.38
tokens: 6622
characters: 2551
timestamp: 2025-12-24T08:20:58.647937
finish_reason: stop
---

дает с кольцом всех многочленов, а значит, \( P \in (f_1, \ldots, f_n) \), что противоречит пункту а) теоремы. Следовательно, данная система уравнений разрешима. Пусть \( \xi = (\xi_1, \ldots, \xi_n) \) — решение этой системы. Тогда \( \xi_i^{m_i} = -P_i(\xi_1, \ldots, \xi_n) \), где \( \deg P_i < m_i \), поэтому любой многочлен \( Q(\xi_1, \ldots, \xi_n) \) представим в виде \( Q(\xi_1, \ldots, \xi_n) = \cdot a_{i_1 \ldots i_n} \xi_1^{i_1} \ldots \xi_n^{i_n} \), где \( i_k < m_k \). Следовательно, \( \dim K[\xi_1, \ldots, \xi_n] \leq m_1 \ldots m_n = m \), а значит, \( m + 1 \) элементов \( 1, \xi_i, \ldots, \xi_i^m \) линейно зависимы, т. е. любой элемент \( \xi_i \) удовлетворяет полиномиальному соотношению \( \cdot b_k \xi_i^k = 0 \). Ясно, что число решений уравнения \( \cdot b_k x^k = 0 \) конечно, а это уравнение едино для всех решений системы и зависит лишь от номера \( i \).

**Теорема 55.2.2.** Пусть в комплексной матрице \( A \) заданы все внедиагональные элементы. Тогда диагональные элементы \( x_1, \ldots, x_n \) можно подобрать так, что собственные значения матрицы \( A \) совпадут с данными комплексными числами; при этом количество таких наборов \( x_1, \ldots, x_n \) конечно.

**Доказательство [Fr3].** Ясно, что

\[
\det(A + \lambda I) = (x_1 + \lambda) \ldots (x_n + \lambda) + \sum_{k \leq n-2} \cdot a_{i_1 \ldots i_k} (x_{i_1} + \lambda) \ldots (x_{i_k} + \lambda) =
= \cdot \lambda^{n-k} \sigma_k(x_1, \ldots, x_n) + \sum_{k \leq n-2} \cdot \lambda^{n-k} p_k(x_1, \ldots, x_k),
\]

где \( p_k \) — многочлен, \( \deg p_k \leq k - 2 \). Уравнение \( \det(A + \lambda I) = 0 \) имеет корни \( \lambda_1, \ldots, \lambda_n \) тогда и только тогда, когда

\[
\sigma_k(\lambda_1, \ldots, \lambda_n) = \sigma_k(x_1, \ldots, x_n) + p_k(x_1, \ldots, x_n).
\]

Таким образом, наша задача сводится к решению системы уравнений \( \sigma_k(\lambda_1, \ldots, \lambda_n) = q_k(x_1, \ldots, x_n) \), где \( k = 1, \ldots, n \) и степень многочлена \( q_k \) не превосходит \( k - 1 \) (и даже \( k - 2 \) при \( k \geq 2 \)).

Пусть \( x = x_i, \sigma_k = \sigma_k(x_1, \ldots, x_n) \) и \( \sigma'_k = \sigma_k(x_1, \ldots, \hat{x}_i, \ldots, x_n) \). Тогда \( \sigma_k = x \sigma'_{k-1} + \sigma'_k \). Поэтому

\[
x_i^n - \sigma_1 x_i^{n-1} + \sigma_2 x_i^{n-2} - \ldots + (-1)^n \sigma_n =
= x^n - (x + \sigma'_1)x^{n-1} + (x \sigma'_1 + \sigma_2)x^{n-2} - \ldots = 0.
\]

Рассмотрим многочлены

\[
f_i(x_1, \ldots, x_n) = x_i^n + q_1 x_i^{n-1} - q_2 x_i^{n-2} + \ldots + (-1)^n q_n =
= x_i^n + r_i(x_1, \ldots, x_n),
\]