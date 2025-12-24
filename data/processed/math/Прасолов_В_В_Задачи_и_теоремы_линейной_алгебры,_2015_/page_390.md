---
source_image: page_390.png
page_number: 390
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.25
tokens: 6898
characters: 3213
timestamp: 2025-12-24T08:18:26.713958
finish_reason: stop
---

матриц \( B_k \) стремятся к нулю. Поэтому все собственные значения матрицы \( (A^*)^m A^m \) по модулю меньше 1 при некотором \( m \). Рассмотрим матрицу

\[
H = I + A^*A + \ldots + (A^*)^{m-1}A^{m-1}.
\]

Легко проверить, что \( H - A^*HA = I - (A^*)^m A^m \). Собственные значения последней матрицы равны \( 1 - \alpha_i \), где \( \alpha_i \) — собственные значения матрицы \( (A^*)^m A^m \). Так как \( \alpha_i < 1 \), то \( 1 - \alpha_i > 0 \).

37.4. Ясно, что

\[
\operatorname{Re} \operatorname{tr} AB = \operatorname{Re} \sum_{i,j=1}^n a_{ij} b_{ji} = \frac{1}{2} \sum_{i,j=1}^n (a_{ij} b_{ji} + \overline{a_{ij}} \overline{b_{ji}}),
\]
\[
\frac{1}{2} (\operatorname{tr} AA^* + \operatorname{tr} BB^*) = \frac{1}{2} \sum_{i,j=1}^n (a_{ij} \overline{a_{ij}} + b_{ij} \overline{b_{ij}}) = \frac{1}{2} \sum_{i,j=1}^n (a_{ij} \overline{a_{ij}} + b_{ji} \overline{b_{ji}}) =
\]
\[
= \frac{1}{2} \sum_{i,j=1}^n (|a_{ij}|^2 + |b_{ji}|^2).
\]

Остаётся заметить, что для произвольных комплексных чисел \( z \) и \( w \) выполняется неравенство \( z \overline{w} + \overline{z} w \leq |z|^2 + |w|^2 \). Действительно, если \( z = a + ib \) и \( w = c + id \), то \( z \overline{w} + \overline{z} w = 2ac - 2bd \leq a^2 + c^2 + b^2 + d^2 \).

37.5. Матрица \( C = AB - BA \) косоэрмитова, поэтому её собственные значения чисто мнимые, а значит, \( \operatorname{tr}(C^2) \leq 0 \). Из неравенства \( \operatorname{tr}(AB - BA) \leq 0 \) получаем \( \operatorname{tr}(AB)^2 + \operatorname{tr}(BA)^2 \leq \operatorname{tr}(ABBA) + \operatorname{tr}(BAAB) \). Легко проверить, что \( \operatorname{tr}(AB)^2 = \operatorname{tr}(BA)^2 \) и \( \operatorname{tr}(ABBA) = \operatorname{tr}(BAAB) = \operatorname{tr}(A^2 B^2) \).

37.6. Согласно теореме 21.6.1 собственные значения матрицы \( AB \) положительны. Согласно задаче 21.4 матрицы \( A^{-1} \) и \( B^{-1} \) положительно определённые, поэтому собственные значения матрицы \( (AB)^{-1} = B^{-1} A^{-1} \) тоже положительны.

Согласно задаче 37.4

\[
\operatorname{tr} AB \leq \frac{1}{2} (\operatorname{tr} AA^* + \operatorname{tr} BB^*) = \frac{1}{2} (\operatorname{tr} A^2 + \operatorname{tr} B^2) = \frac{1}{2} \sum_{i=1}^n (\alpha_i^2 + \beta_i^2),
\]
\[
\operatorname{tr} B^{-1} A^{-1} \leq \frac{1}{2} (\operatorname{tr} B^{-1} B^{*-1} + \operatorname{tr} A^{-1} A^{*-1}) = \frac{1}{2} \sum_{i=1}^n \left( \frac{1}{\alpha_i^2} + \frac{1}{\beta_i^2} \right).
\]

Все собственные значения матриц \( AB \) и \( B^{-1} A^{-1} \) положительны, поэтому \( \lambda \leq \operatorname{tr} AB \leq \frac{n}{2} (\alpha_1^2 + \beta_1^2) \) и \( \lambda^{-1} \leq \operatorname{tr} B^{-1} A^{-1} \leq \frac{n}{2} \left( \frac{1}{\alpha_n^2} + \frac{1}{\beta_n^2} \right) = \frac{n}{2} \cdot \frac{\alpha_n^2 + \beta_n^2}{\alpha_n^2 \beta_n^2} \).

37.7. Для матрицы \( A \) можно выбрать унитарную матрицу \( U \) так, что

\[
U^* A U = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) = \Lambda.
\]

Тогда \( \operatorname{tr}(AB) = \operatorname{tr}(U^* A U U^* B U) = \operatorname{tr}(\Lambda C) \), где \( C = U^* B U \) — положительно определённая матрица. У матрицы \( \Lambda C \) на диагонали стоят числа \( \lambda_1 c_{11}, \ldots, \lambda_n c_{nn} \).