---
source_image: page_366.png
page_number: 366
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.36
tokens: 6430
characters: 2139
timestamp: 2025-12-24T08:17:32.734168
finish_reason: stop
---

Доказательство. Рассмотрим матрицу, обратную матрице (3) из доказательства теоремы 37.5.3 для \( \rho = t \):

\[
\begin{pmatrix}
-\frac{a_1}{a_0} & -\frac{ta_2}{a_0} & \ldots & -\frac{t^{n-2}a_{n-1}}{a_0} & -\frac{t^{n-1}}{a_0} \\
1/t & 0 & \ldots & 0 & 0 \\
0 & 1/t & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & \ldots & 1/t & 0
\end{pmatrix}.
\]

Каждое собственное значение \( \lambda \) этой матрицы удовлетворяет неравенству

\[
|\lambda| \leq \max \left\{ \frac{|a_0| + |a_i| t^i}{|a_0| t} \right\} \leq \frac{|a_0| + M}{|a_0| t}.
\]

Ясно также, что корнями многочлена (1) являются числа \( 1/\lambda \).

Задачи

37.1. Докажите, что если \( U \) — унитарная матрица, а \( S \geq 0 \), то \( |\operatorname{tr}(US)| \leq \leq \operatorname{tr} S \).

37.2. Докажите, что если \( A \) и \( B \) — неотрицательно определённые матрицы, то \( |\operatorname{tr}(AB)| \leq \operatorname{tr} A \operatorname{tr} B \).

37.3 [Cu]. Докажите, что \( \lim_{k \to \infty} A^k = 0 \) тогда и только тогда, когда выполнено одно из следующих условий:
а) все собственные значения матрицы \( A \) по модулю меньше 1;
б) существует положительно определённая матрица \( H \), для которой \( H - A^* H A > 0 \).

37.4. Пусть \( A = \|a_{ij}\|_1^n \) и \( B = \|b_{ij}\|_1^n \), где \( a_{ij}, b_{ij} \in \mathbb{C} \). Докажите, что

\[
\operatorname{Re} \operatorname{tr}(AB) \leq \frac{1}{2} (\operatorname{tr} AA^* + \operatorname{tr} BB^*).
\]

37.5. Матрицы \( A \) и \( B \) эрмитовы. Докажите, что \( \operatorname{tr}(AB)^2 \leq \operatorname{tr}(A^2 B^2) \).

37.6 [Hu]. Пусть \( \alpha_1 \geq \ldots \geq \alpha_n \) и \( \beta_1 \geq \ldots \geq \beta_n \) — собственные значения положительно определённых матриц \( A \) и \( B \), а \( \lambda \) — любое собственное значение матрицы \( AB \). Докажите, что

\[
\frac{2}{n} \cdot \frac{\alpha_n^2 \beta_n^2}{\alpha_n^2 + \beta_n^2} \leq \lambda \leq \frac{n}{2} (\alpha_1^2 + \beta_1^2).
\]

37.7 [Y1]. Матрицы \( A \) и \( B \) положительно определены. Докажите, что \( \sqrt{\operatorname{tr}(AB)} \leq \frac{\operatorname{tr} A + \operatorname{tr} B}{2} \).