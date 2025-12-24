---
source_image: page_392.png
page_number: 392
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.21
tokens: 6915
characters: 2895
timestamp: 2025-12-24T08:18:29.518286
finish_reason: stop
---

Сингулярные значения матриц \( \Lambda^m C \) и \( \Lambda^m B \) равны \( \gamma_1 \ldots \gamma_m \) и \( \beta_1 \ldots \beta_m \) (напомним, что для вектор-столбца сингулярное значение — это его длина). Сингулярные значения матрицы \( \Lambda^m A \) равны \( \alpha_{i_1} \ldots \alpha_{i_m} \), где числа \( i_1, \ldots, i_m \) попарно различны. Поэтому \( \sigma_{\max} = \alpha_1 \ldots \alpha_m \) и \( \sigma_{\min} = \alpha_{n-m+1} \ldots \alpha_n \).

37.14. Согласно теореме 21.4.1 существует положительно определённая матрица \( S \), для которой \( S^2 = H \). Применив результат задачи 37.13 к матрицам \( A = S \) и \( B = M \), получаем требуемое.

§ 38. Неравенства для норм матриц

38.1. Ясно, что
\[
\|A + B\|_s = \sup_{x \neq 0} \frac{\|Ax + Bx\|}{\|x\|} \leq \sup_{x \neq 0} \left( \frac{\|Ax\|}{\|x\|} + \frac{\|Bx\|}{\|x\|} \right) = \|A\|_s + \|B\|_s.
\]
Пусть \( a \) и \( b \) — векторы в \( n^2 \)-мерном пространстве с координатами \( a_{ij} \) и \( b_{ij} \). Тогда \( \|A + B\|_e = \|a + b\| \leq \|a\| + \|b\| = \|A\|_e + \|B\|_e \).

38.2. Предположим, что \( Ax = \lambda x \), причём \( \lambda x \neq 0 \). Тогда \( A^{-1} x = \lambda^{-1} x \). Поэтому
\[
\max_y \frac{\|Ay\|}{\|y\|} \geq \frac{\|Ax\|}{\|x\|} = \lambda \text{ и } \left( \max_y \frac{\|A^{-1} y\|}{\|y\|} \right)^{-1} = \min_y \frac{\|y\|}{\|A^{-1} y\|} \leq \frac{\|x\|}{\|A^{-1} x\|} = \lambda.
\]

38.3. Если \( \|AB\|_s \neq 0 \), то \( \|AB\|_s = \max_x \frac{\|ABx\|}{\|x\|} = \frac{\|ABx_0\|}{\|x_0\|} \), где \( Bx_0 \neq 0 \). Пусть \( y = Bx_0 \). Тогда
\[
\frac{\|ABx_0\|}{\|x_0\|} = \frac{\|Ay\|}{\|y\|} \cdot \frac{\|Bx_0\|}{\|x_0\|} \leq \|A\|_s \|B\|_s.
\]
Согласно задаче 37.2 \( \|AB\|_e^2 = \operatorname{tr}(B^* A^* AB) = \operatorname{tr}(BB^* A^* A) \leq \operatorname{tr}(BB^*) \operatorname{tr}(A^* A) = \|A\|_e^2 \|B\|_e^2 \).

38.4. Равенство \( (I \pm (P_1 - P_2))x = x \pm (P_1 - P_2)x \) показывает, что
\[
\|(I \pm (P_1 - P_2))x\| \geq \|x\| - \|(P_1 - P_2)x\| \geq (1 - \rho)\|x\|,
\]
где \( \rho = \|P_1 - P_2\|_s < 1 \). Поэтому операторы \( I \pm (P_1 - P_2) \) невырожденные, а значит,
\[
\operatorname{rk} P_1 = \operatorname{rk} P_1(I - P_1 + P_2) = \operatorname{rk} P_1 P_2,
\]
\[
\operatorname{rk} P_2 = \operatorname{rk} P_2(I - P_2 + P_1) = \operatorname{rk} P_2 P_1.
\]
Остаётся заметить, что
\[
\operatorname{rk} P_1 P_2 \leq \min\{\operatorname{rk} P_1, \operatorname{rk} P_2\} \quad \text{и} \quad \operatorname{rk} P_2 P_1 \leq \min\{\operatorname{rk} P_1, \operatorname{rk} P_2\}.
\]

38.5. Пусть \( \sigma_1, \ldots, \sigma_n \) — сингулярные значения матрицы \( A \). Тогда сингулярные значения матрицы \( \operatorname{adj} A \) равны \( \div \sigma_i, \ldots, \div \sigma_i \) (задача 37.10), поэтому \( \|A\|_e^2 = \sigma_1^2 + \ldots + \sigma_n^2 \) и \( \|\operatorname{adj} A\|_e^2 = \div \sigma_i + \ldots + \div \sigma_i \). Предполо-