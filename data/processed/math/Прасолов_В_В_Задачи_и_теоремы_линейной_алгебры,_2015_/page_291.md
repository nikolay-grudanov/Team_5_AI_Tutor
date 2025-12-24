---
source_image: page_291.png
page_number: 291
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.16
tokens: 6836
characters: 3227
timestamp: 2025-12-24T08:15:36.516451
finish_reason: stop
---

Предположим теперь, что матрицы \( A \) и \( A^{-1} \) подобны. Жорданова нормальная форма матрицы \( A \) имеет вид \( \operatorname{diag}(J_1, \ldots, J_k) \), поэтому матрицы \( \operatorname{diag}(J_1, \ldots, J_k) \) и \( \operatorname{diag}(J_1^{-1}, \ldots, J_k^{-1}) \) подобны. Если \( J \) — жорданова клетка, то матрица \( J^{-1} \) подобна жордановой клетке. Следовательно, матрицы \( J_1, \ldots, J_k \) можно разбить на два класса: для матриц первого класса \( J_\alpha^{-1} \sim J_\alpha \), а для матриц второго класса \( J_\alpha^{-1} \sim J_\beta \) и \( J_\beta^{-1} \sim J_\alpha \). Достаточно доказать, что в виде произведения двух инволюций можно представить матрицу \( J_\alpha \) в первом случае и матрицу \( \operatorname{diag}(J_\alpha, J_\beta) \) во втором случае.

Характеристический многочлен жордановой клетки совпадает с минимальным многочленом, поэтому если \( p \) и \( q \) — минимальные многочлены матриц \( J_\alpha \) и \( J_\alpha^{-1} \), то \( q(\lambda) = p(0)^{-1} \lambda^n p(\lambda^{-1}) \), где \( n \) — порядок матрицы \( J_\alpha \) (см. задачу 15.4).

Пусть \( J_\alpha \sim J_\alpha^{-1} \). Тогда \( p(\lambda) = p(0)^{-1} \lambda^n p(\lambda^{-1}) \), т. е. \( p(\lambda) = \cdot \alpha_i \lambda^{n-i} \), где \( \alpha_0 = 1 \) и \( \alpha_n \alpha_{n-i} = \alpha_i \). Матрица \( J_\alpha \) подобна циклической клетке, поэтому существует такой базис \( e_1, \ldots, e_n \), что \( J_\alpha e_k = e_{k+1} \) при \( k \leq n-1 \) и \( J_\alpha e_n = -\alpha_n e_1 - \alpha_{n-1} e_2 - \ldots - \alpha_1 e_n \). Пусть \( Te_k = e_{n+1-k} \); очевидно, что \( T \) — инволюция. Если \( STe_k = J_\alpha e_k \), то \( Se_{n+1-k} = e_{k+1} \) при \( k \neq n \) и \( Se_1 = -\alpha_n e_1 - \ldots - \alpha_1 e_n \). Проверим, что \( S \) — инволюция:

\[
S^2 e_1 = \alpha_n (\alpha_n e_1 + \ldots + \alpha_1 e_n) - \alpha_{n-1} e_n - \ldots - \alpha_1 e_2 =
= e_1 + (\alpha_n \alpha_{n-1} - \alpha_1) e_2 + \ldots + (\alpha_n \alpha_1 - \alpha_{n-1}) e_n = e_1;
\]

при \( i \neq 1 \) равенство \( S^2 e_i = e_i \) очевидно.

Рассмотрим теперь случай \( J_\alpha^{-1} \sim J_\beta \); пусть \( \cdot \alpha_i \lambda^{n-i} \) и \( \cdot \beta_i \lambda^{n-i} \) — минимальные многочлены матриц \( J_\alpha \) и \( J_\beta \). Тогда

\[
\cdot \alpha_i \lambda^{n-i} = \beta_n^{-1} \lambda^n \cdot \beta_i \lambda^{i-n} = \beta_n^{-1} \cdot \beta_i \lambda^i.
\]

Поэтому \( \alpha_{n-i} \beta_n = \beta_i \) и \( \alpha_n \beta_n = \beta_0 = 1 \). Существуют такие базисы \( e_1, \ldots, e_n \) и \( \varepsilon_1, \ldots, \varepsilon_n \), что

\[
J_\alpha e_k = e_{k+1}, \quad J_\alpha e_n = -\alpha_n e_1 - \ldots - \alpha_1 e_n \\
J_\beta \varepsilon_{k+1} = \varepsilon_k, \quad J_\beta \varepsilon_1 = -\beta_1 \varepsilon_1 - \ldots - \beta_n \varepsilon_n.
\]

Пусть \( Te_k = \varepsilon_k \) и \( T \varepsilon_k = e_k \). Если \( \operatorname{diag}(J_\alpha, J_\beta) = ST \), то

\[
Se_{k+1} = ST \varepsilon_{k+1} = J_\beta \varepsilon_{k+1} = \varepsilon_k, \\
S \varepsilon_k = e_{k+1}, \\
Se_1 = ST \varepsilon_1 = J_\beta \varepsilon_1 = -\beta_1 \varepsilon_1 - \ldots - \beta_n \varepsilon_n, \\
S \varepsilon_n = -\alpha_n e_1 - \ldots - \alpha_1 e_n.
\]