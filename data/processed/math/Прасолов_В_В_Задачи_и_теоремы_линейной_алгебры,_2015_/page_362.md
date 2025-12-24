---
source_image: page_362.png
page_number: 362
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.20
tokens: 6677
characters: 2663
timestamp: 2025-12-24T08:17:32.323860
finish_reason: stop
---

так как \( \sigma_1^2 \) — наибольшее собственное значение эрмитова оператора \( A^*A \). Поэтому \( |\lambda_1| \leq \sigma_1 \); при \( m = 1 \) неравенство доказано. Применим полученное неравенство к операторам \( \Lambda^m(A) \) и \( \Lambda^m(A^*A) \) (см. п. 30.5). Их собственные значения равны \( \lambda_{i_1} \ldots \lambda_{i_m} \) и \( \sigma_{i_1}^2 \ldots \sigma_{i_m}^2 \), поэтому

\[
|\lambda_1 \ldots \lambda_m| \leq \sigma_1 \ldots \sigma_m.
\]

Ясно также, что \( |\lambda_1 \ldots \lambda_n| = |\det A| = \sqrt{\det(A^*A)} = \sigma_1 \ldots \sigma_n. \)

**Теорема 37.4.3.** *Пусть \( \sigma_1 \geq \ldots \geq \sigma_n \) — сингулярные значения матрицы \( A \), \( \tau_i \geq \ldots \geq \tau_n \) — сингулярные значения матрицы \( B \). Тогда*

\[
|\operatorname{tr}(AB)| \leq \sum_{i=1}^n \sigma_i \tau_i.
\]

**Доказательство [Mi4].** Пусть \( A = U_1 SV_1 \) и \( B = U_2 TV_2 \), где \( U_i \) и \( V_i \) — унитарные матрицы, \( S = \operatorname{diag}(\sigma_1, \ldots, \sigma_n) \) и \( T = \operatorname{diag}(\tau_1, \ldots, \tau_n) \). Тогда \( \operatorname{tr}(AB) = \operatorname{tr}(U_1 SV_1 U_2 TV_2) = \operatorname{tr}(V_2 U_1 SV_1 V_2 T) = \operatorname{tr}(U^T S V T) \), где \( U = (V_2 U_1)^T \) и \( V = V_1 U_2 \). Поэтому

\[
|\operatorname{tr}(AB)| = \left| \sum_{ij} u_{ij} v_{ij} \sigma_i \tau_j \right| \leq \frac{1}{2} \left( \sum_{ij} |u_{ij}|^2 \sigma_i \tau_j + \sum_{ij} |v_{ij}|^2 \sigma_i \tau_j \right).
\]

Матрицы с элементами \( |u_{ij}|^2 \) и \( |v_{ij}|^2 \) дважды стохастические, поэтому \( \sum_{ij} |u_{ij}|^2 \sigma_i \tau_j \leq \sum_{i} \sigma_i \tau_i \) и \( \sum_{ij} |v_{ij}|^2 \sigma_i \tau_j \leq \sum_{i} \sigma_i \tau_i \) (см. задачу 41.1).

**37.5. Круги Гершгорина**

Следующее легко доказываемое утверждение даёт полезную оценку для собственных значений матрицы.

**Теорема 37.5.1 (Гершгорин [Г1]).** *Каждое собственное значение матрицы \( \|a_{ij}\|_1^n \) принадлежит одному из кругов \( |a_{kk} - z| \leq \rho_k \), где \( \rho_k = \sum_{j \neq k} |a_{kj}| \).*

**Доказательство.** Пусть \( \lambda \) — собственное значение данной матрицы. Тогда система \( a_{ij} x_j = \lambda x_i \) (\( i = 1, \ldots, n \)) имеет ненулевое решение \( (x_1, \ldots, x_n) \). Выберем среди чисел \( x_1, \ldots, x_n \) наибольшее по модулю; пусть это будет \( x_k \). Так как \( a_{kk} x_k - \lambda x_k = - \sum_{j \neq k} a_{kj} x_j \), то \( |a_{kk} x_k - \lambda x_k| \leq \sum_{j \neq k} |a_{kj} x_j| \leq \rho_k |x_k| \), т. е. \( |a_{kk} - \lambda| \leq \rho_k \).

**Следствие.** *Если \( |a_{kk}| > \sum_{j \neq k} |a_{kj}| \) для всех \( k \), то матрица \( A \) невырожденная.*