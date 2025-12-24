---
source_image: page_386.png
page_number: 386
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.79
tokens: 6529
characters: 2340
timestamp: 2025-12-24T08:18:07.024155
finish_reason: stop
---

Теорема 41.4.1 (Гофман—Виландт [Ho]). Пусть \( A \) и \( B \) — нормальные матрицы, \( \alpha_1, \ldots, \alpha_n \) и \( \beta_1, \ldots, \beta_n \) — их собственные значения. Тогда

\[
\|A - B\|_e^2 \geq \min_{i=1}^n (\alpha_{\sigma(i)} - \beta_i)^2,
\]

где минимум берётся по всем перестановкам \( \sigma \).

Доказательство. Матрицы \( A \) и \( B \) можно представить в виде \( A = V \Lambda_a V^* \) и \( B = W \Lambda_b W^* \), где \( \Lambda_a = \operatorname{diag}(\alpha_1, \ldots, \alpha_n) \), \( \Lambda_b = \operatorname{diag}(\beta_1, \ldots, \beta_n) \), \( V \) и \( W \) — унитарные матрицы. Тогда

\[
\|A - B\|_e^2 = \|V \Lambda_a V^* - W \Lambda_b W^*\|_e^2 = \|U \Lambda_a U^* - \Lambda_b\|_e^2,
\]

где \( U = W^* V \). Кроме того,

\[
\|U \Lambda_a U^* - \Lambda_b\|_e^2 = \operatorname{tr}(U \Lambda_a U^* - \Lambda_b)(U \Lambda_a^* U^* - \Lambda_b^*) =
\]
\[
= \operatorname{tr}(\Lambda_a \Lambda_a^* + \Lambda_b \Lambda_b^*) - 2 \operatorname{Re} \operatorname{tr}(U \Lambda_a U^* \Lambda_b^*) =
\]
\[
= \sum_{i=1}^n (|\alpha_i|^2 + |\beta_i|^2) - 2 \sum_{i,j=1}^n |u_{ij}|^2 \operatorname{Re}(\overline{\beta}_i \alpha_j).
\]

А так как матрица \( \|c_{ij}\| \), где \( c_{ij} = |u_{ij}|^2 \), дважды стохастическая, то

\[
\|A - B\|_e^2 \geq \sum_{i=1}^n (|\alpha_i|^2 + |\beta_i|^2) - 2 \min_{i,j=1}^n c_{ij} \operatorname{Re}(\overline{\beta}_i \alpha_j),
\]

где минимум берётся по всем дважды стохастическим матрицам \( C \). При фиксированных наборах чисел \( \alpha_i, \beta_j \) нужно найти минимум линейной функции на выпуклом многограннике, вершины которого — матрицы перестановок. Этот минимум достигается в одной из вершин, т. е. для некоторой матрицы \( c_{ij} = \delta_{i, \sigma(i)} \). В этом случае

\[
2 \sum_{i,j=1}^n c_{ij} \operatorname{Re}(\overline{\beta}_i \alpha_j) = 2 \sum_{i,j=1}^n c_{ij} \operatorname{Re}(\overline{\beta}_i \alpha_{\sigma(i)}).
\]

Следовательно,

\[
\|A - B\|_e^2 \geq \sum_{i=1}^n (|\alpha_{\sigma(i)}|^2 + |\beta_i|^2 - 2 \operatorname{Re}(\overline{\beta}_i \alpha_{\sigma(i)})) = \sum_{i=1}^n (\alpha_{\sigma(i)} - \beta_i)^2.
\]

Задачи

41.1 [Mi4]. Пусть \( A = \|a_{ij}\|_1^n \) — дважды стохастическая матрица; \( x_1 \geq \ldots \geq x_n \geq 0 \) и \( y_1 \geq \ldots \geq y_n \geq 0 \). Докажите, что \( \sum_{r,s} a_{rs} x_r y_s \leq \sum_r x_r y_r \).