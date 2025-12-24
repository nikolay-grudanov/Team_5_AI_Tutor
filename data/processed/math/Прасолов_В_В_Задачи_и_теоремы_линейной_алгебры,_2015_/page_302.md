---
source_image: page_302.png
page_number: 302
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.05
tokens: 6978
characters: 3428
timestamp: 2025-12-24T08:15:56.655516
finish_reason: stop
---

27.2. Если \( P \) — матрица порядка 2 и \( \operatorname{rk} P = 1 \), то \( \operatorname{tr} P = 1 \) и \( \det P = 0 \) (если \( \operatorname{rk} P \neq 1 \), то \( P = I \) или \( P = 0 \)). Поэтому

\[
P = \frac{1}{2} \begin{pmatrix} 1 + a & b \\ c & 1 - a \end{pmatrix},
\]

где \( a^2 + bc = 1 \). Ясно также, что если \( \operatorname{tr} P = 1 \) и \( \det P = 0 \), то согласно теореме Гамильтона—Кэли \( P^2 - P = P^2 - (\operatorname{tr} P)P + \det P = 0 \).

27.3. Так как \( \operatorname{Im}(I - A) = (\operatorname{Ker}(I - A)^*)^\perp \), то любой вектор \( x \) можно представить в виде \( x = x_1 + x_2 \), где \( x_1 \in \operatorname{Im}(I - A) \) и \( x_2 \in \operatorname{Ker}(I - A^*) \). Достаточно отдельно рассмотреть \( x_1 \) и \( x_2 \). Вектор \( x_1 \) имеет вид \( y - Ay \), поэтому

\[
\left| \frac{1}{n} \sum_{i=0}^{n-1} A^i x_1 \right| = \left| \frac{1}{n} (y - A^n y) \right| \leq \frac{2|y|}{n} \to 0.
\]

Так как \( x_2 \in \operatorname{Ker}(I - A^*) \), то \( x_2 = A^* x_2 = A^{-1} x_2 \), т. е. \( Ax_2 = x_2 \). Поэтому

\[
\lim_{n \to \infty} \frac{1}{n} \sum_{i=0}^{n-1} A^i x_2 = \lim_{n \to \infty} \frac{1}{n} \sum_{i=0}^{n-1} x_2 = x_2.
\]

Остаётся заметить, что \( \operatorname{Ker}(I - A^*) = \operatorname{Ker}(A - I) \).

27.4. (б) \( \Rightarrow \) (а). Достаточно домножить равенство \( A_1 + \ldots + A_k = I \) на \( A_i \).
(а) \( \Rightarrow \) (в). \( A_i \) — проектор, поэтому \( \operatorname{rk} A_i = \operatorname{tr} A_i \). Следовательно, \( \bullet \operatorname{rk} A_i = \bullet \operatorname{tr} A_i = \operatorname{tr}(\bullet A_i) = n \).
(в) \( \Rightarrow \) (б). Так как \( \bullet A_i = I \), то \( \operatorname{Im} A_1 + \ldots + \operatorname{Im} A_k = V \). Но \( \operatorname{rk} A_1 + \ldots + \operatorname{rk} A_k = \dim V \), поэтому \( V = \operatorname{Im} A_1 \oplus \ldots \oplus \operatorname{Im} A_k \). Для любого \( x \in V \) справедливо равенство \( A_j x = (A_1 + \ldots + A_k)A_j x = A_1 A_j x + \ldots + A_k A_j x \), причём \( A_i A_j x \in \operatorname{Im} A_i \) и \( A_j x \in \operatorname{Im} A_j \). Следовательно, \( A_i A_j = 0 \) при \( i \neq j \) и \( A_j^2 = A_j \).

27.5. Матрица \( A(I - A) \) неотрицательно определена, поэтому согласно теореме 21.4.1 существует единственная неотрицательно определённая матрица \( S \), для которой \( S^2 = A(I - A) \). Конструкция матрицы \( S \) показывает, что \( AS = SA \).

Используя это свойство, легко проверить, что эрмитова матрица \( \begin{pmatrix} A & S \\ S & I - A \end{pmatrix} \) является проектором.

§ 28. Инволюции

28.1. Если инволюция \( A \) в двумерном пространстве не равна \( \pm I \), то её матрица в некотором базисе имеет вид \( \operatorname{diag}(1, -1) \). Поэтому \( \operatorname{tr} A = 0 \) и \( \det A = -1 \), т. е. \( A = \begin{pmatrix} x & y \\ z & -x \end{pmatrix} \), где \( x^2 + yz = 1 \). Согласно теореме Гамильтона—Кэли такая матрица \( A \) удовлетворяет уравнению \( A^2 - (\operatorname{tr} A)A + (\det A)I = 0 \), т. е. \( A^2 = I \).

28.2. Требуется доказать, что \( H^2 + \overline{S}S = I \) и \( SH = \overline{HS} \). Для доказательства этих равенств достаточно воспользоваться перестановочностью матриц \( \overline{AA} + I \) и \( \overline{AA} - I \), а также равенствами

\[
A(\overline{AA} \pm I) = (A\overline{A} \pm I)A \quad \text{и} \quad A(\overline{AA} \pm I)^{-1} = (A\overline{A} \pm I)^{-1}A.
\]