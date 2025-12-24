---
source_image: page_139.png
page_number: 139
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.88
tokens: 6462
characters: 2524
timestamp: 2025-12-24T08:11:14.143491
finish_reason: stop
---

§ 8. Ранг матрицы

8.1. Неравенства для ранга матрицы

Столбцы матрицы \( AB \) являются линейными комбинациями столбцов матрицы \( A \), поэтому \( \operatorname{rk} AB \leq \operatorname{rk} A \); строки матрицы \( AB \) являются линейными комбинациями строк матрицы \( B \), поэтому \( \operatorname{rk} AB \leq \operatorname{rk} B \). Если матрица \( B \) обратима, то \( \operatorname{rk} A = \operatorname{rk}(AB)B^{-1} \leq \operatorname{rk} A \), поэтому \( \operatorname{rk} A = \operatorname{rk} AB \).

Приведём еще два неравенства для рангов произведений матриц.

Теорема 8.1.1 (неравенство Фробениуса). Для рангов произведений матриц выполняется неравенство \( \operatorname{rk} BC + \operatorname{rk} AB \leq \operatorname{rk} ABC + \operatorname{rk} B \).

Доказательство. Если \( U \subset V \) и \( X : V \to W \), то
\[
\dim (\operatorname{Ker} X|_U) \leq \dim \operatorname{Ker} X = \dim V - \dim \operatorname{Im} X.
\]
Запишем это неравенство для \( U = \operatorname{Im} BC, V = \operatorname{Im} B \) и \( X = A \):
\[
\dim (\operatorname{Ker} A|_{\operatorname{Im} BC}) \leq \dim \operatorname{Im} B - \dim \operatorname{Im} AB.
\]
Ясно также, что \( \dim (\operatorname{Ker} A|_{\operatorname{Im} BC}) = \dim \operatorname{Im} BC - \dim \operatorname{Im} ABC \).

Теорема 8.1.2 (неравенство Сильвестра). Для ранга произведения матриц выполняется неравенство \( \operatorname{rk} A + \operatorname{rk} B \leq \operatorname{rk} AB + n \), где \( n \) — число столбцов матрицы \( A \) и число строк матрицы \( B \).

Доказательство. Запишем неравенство Фробениуса для матриц \( A_1 = A, B_1 = I \) и \( C_1 = B \). В итоге получим
\[
\operatorname{rk} B_1 C_1 + \operatorname{rk} A_1 B_1 \leq \operatorname{rk} A_1 B_1 C_1 + \operatorname{rk} B_1,
\]
т. е. \( \operatorname{rk} B + \operatorname{rk} A \leq \operatorname{rk} AB + n \).

8.2. Другое определение ранга

Для ранга матрицы можно дать другое определение: ранг матрицы \( A \) равен наименьшему из размеров матриц \( B \) и \( C \), произведение которых равно \( A \).

Докажем, что это определение эквивалентно обычному. Если \( A = BC \) и наименьший из размеров матриц \( B \) и \( C \) равен \( k \), то \( \operatorname{rk} A \leq \min(\operatorname{rk} B, \operatorname{rk} C) \leq k \). Остаётся доказать, что если \( A \) — матрица размера \( m \times n \) и \( \operatorname{rk} A = k \), то матрицу \( A \) можно представить в виде произведения матриц размеров \( m \times k \) и \( k \times n \). Выделим в матрице \( A \) линейно