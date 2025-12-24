---
source_image: page_289.png
page_number: 289
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.67
tokens: 6511
characters: 2265
timestamp: 2025-12-24T08:15:23.823155
finish_reason: stop
---

то \( W = V_1 + \ldots + V_k \) — прямая сумма. Для нормального оператора \( \mathrm{Ker}\, N_i = (\mathrm{Im}\, N_i)^\perp \), поэтому \( \mathrm{Ker}\, N_i \subset W^\perp \), а значит, \( \mathrm{Ker}\, N \subset W^\perp \). Ясно также, что \( \dim\, \mathrm{Ker}\, N = \dim\, W^\perp \). Поэтому без потери общности можно ограничиться пространством \( W \) и считать, что \( r_1 + \ldots + r_k = \dim\, V \), т. е. \( \det\, N \neq 0 \).

Пусть \( M_i = N_i|_{V_i} \) и \( P_i : V \to V_i \) — ортогональный проектор. Возьмём в качестве базиса пространства \( V \) объединение базисов пространств \( V_i \). Так как \( N = \bullet\ N_i = \bullet\ N_i P_i = \bullet\ M_i P_i \), в этом базисе матрица оператора \( N \) имеет вид

\[
\begin{pmatrix}
M_1 P_{11} & \ldots & M_1 P_{k1} \\
\ldots & \ldots & \ldots \\
M_k P_{1k} & \ldots & M_k P_{kk}
\end{pmatrix}
=
\begin{pmatrix}
M_1 & 0 & \ldots \\
0 & \ddots & \\
\ldots & & M_k
\end{pmatrix}
\begin{pmatrix}
P_{11} & \ldots & P_{k1} \\
\ldots & \ldots & \ldots \\
P_{1k} & \ldots & P_{kk}
\end{pmatrix}.
\]

Условие на собственные значения операторов \( N_i \) и \( N \) влечёт равенство
\[
|N - \lambda I| = \prod_{i=1}^k |M_i - \lambda I|.
\]
В частности, при \( \lambda = 0 \) получаем \( |N| = \prod_{i=1}^k |M_i| \). Следовательно,
\[
\left| \begin{array}{ccc}
P_{11} & \ldots & P_{k1} \\
\ldots & \ldots & \ldots \\
P_{1k} & \ldots & P_{kk}
\end{array} \right| = 1,
\]
т. е. \( |P_1 + \ldots + P_k| = 1 \). Применяя теорему 27.4.1, получаем, что
\[
V = V_1 \oplus \ldots \oplus V_k
\]
— прямая сумма ортогональных подпространств. Следовательно, оператор \( N \) нормален (см. п. 19.1) и \( N_i N_j = 0 \), так как \( \mathrm{Im}\, N_j \subset (\mathrm{Im}\, N_i)^\perp = \mathrm{Ker}\, N_i \).

Задачи

27.1. Пусть \( P_1 \) и \( P_2 \) — проекторы. Докажите, что:
а) \( P_1 + P_2 \) — проектор тогда и только тогда, когда \( P_1 P_2 = P_2 P_1 = 0 \);
б) \( P_1 - P_2 \) — проектор тогда и только тогда, когда \( P_1 P_2 = P_2 P_1 = P_2 \).

27.2. Найдите все матрицы порядка 2, являющиеся проекторами.

27.3. Пусть \( A \) — унитарный оператор. Тогда
\[
\lim_{n \to \infty} \frac{1}{n} \sum_{i=0}^{n-1} A^i x = P x,
\]
где \( P \) — эрмитов проектор на \( \mathrm{Ker}\,(A - I) \) (эргодическая теорема).