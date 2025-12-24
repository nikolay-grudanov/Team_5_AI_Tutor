---
source_image: page_318.png
page_number: 318
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.57
tokens: 6836
characters: 2943
timestamp: 2025-12-24T08:16:25.058316
finish_reason: stop
---

то \( e_{i_1} \wedge \ldots \wedge e_{i_q} \leq e_{j_1} \wedge \ldots \wedge e_{j_q} \) и \( e_{i_1} \ldots e_{i_q} = e_1^{k_1} \ldots e_n^{k_n} \leq e_1^{l_1} \ldots e_n^{l_n} = e_{j_1} \ldots e_{j_q} \). Поэтому имеем \( \Lambda^q B(e_{i_1} \wedge \ldots \wedge e_{i_q}) \leq e_{i_1} \wedge \ldots \wedge e_{i_q} \) и

\[
S^q B(e_1^{k_1} \ldots e_n^{k_n}) \leq e_1^{k_1} \ldots e_n^{k_n}.
\]

Теорема 30.5.3. \( \det(\Lambda^q B) = (\det B)^p, \) где \( p = \binom{n-1}{q-1} \) и

\[
\det(S^q B) = (\det B)^r,
\]

где \( r = \frac{q}{n} \binom{n+q-1}{q} \).

Доказательство. Можно считать, что \( B \) — оператор над \( \mathbb{C} \). Пусть \( e_1, \ldots, e_n \) — жорданов базис для оператора \( B \). Согласно теореме 30.5.2 матрицы операторов \( \Lambda^q B \) и \( S^q B \) треугольны в базисах \( \{e_{i_1} \wedge \ldots \wedge e_{i_q}\} \) и \( \{e_1^{k_1} \ldots e_n^{k_n}\} \), упорядоченных лексикографически. Если вектору \( e_i \) соответствует диагональный элемент \( \lambda_i \), то векторам \( e_{i_1} \wedge \ldots \wedge e_{i_q} \) и \( e_1^{k_1} \ldots e_n^{k_n} \) соответствуют диагональные элементы \( \lambda_{i_1} \ldots \lambda_{i_q} \) и \( \lambda_1^{k_1} \ldots \lambda_n^{k_n} \), причём \( k_1 + \ldots + k_n = q \). Поэтому произведение всех диагональных элементов матриц \( \Lambda^q B \) и \( S^q B \) имеет по \( \lambda \) суммарную степень \( q \dim \Lambda^q(V) \) и \( q \dim S^q(V) \) соответственно. Следовательно, \( |\Lambda^q B| = |B|^p \) и \( |S^q B| = |B|^r \), где \( p = \frac{q}{n} \binom{n}{q} = \binom{n-1}{q-1} \) и \( r = \frac{q}{n} \binom{n+q-1}{q} \).

Матрице \( B \) порядка \( n \) можно сопоставить многочлен \( \Lambda_B(t) = 1 + \sum_{q=1}^n \cdot \operatorname{tr}(\Lambda^q B)t^q \) и ряд \( S_B(t) = 1 + \sum_{q=1}^\infty \cdot \operatorname{tr}(S^q B)t^q \).

Теорема 30.5.4. \( S_B(t) = (\Lambda_B(-t))^{-1} \).

Доказательство. Как и при доказательстве теоремы 30.5.3, получаем, что если матрица \( B \) треугольная с диагональю \( (\lambda_1, \ldots, \lambda_n) \), то матрицы \( \Lambda^q B \) и \( S^q B \) треугольные с диагональными элементами \( \lambda_{i_1}, \ldots, \lambda_{i_q} \) и \( \lambda_1^{k_1} \ldots \lambda_n^{k_n} \) (\( k_1 + \ldots + k_n = q \)). Поэтому \( \Lambda_B(-t) = (1 - t\lambda_1) \ldots (1 - t\lambda_n) \) и \( S_B(t) = (1 + t\lambda_1 + t^2 \lambda_1^2 + \ldots) \ldots (1 + t\lambda_n + t^2 \lambda_n^2 + \ldots) \). Остаётся заметить, что \( 1/(1 - t\lambda_i) = 1 + t\lambda_i + t^2 \lambda_i^2 + \ldots \)

30.6. Отображение Ходжа

Пусть \( V \) — вещественное векторное пространство размерности \( n \). Если фиксировать в \( V \) базис \( e_1, \ldots, e_n \), то можно рассмотреть отображение \( * : \Lambda^p V \to \Lambda^{n-p} V \), которое переводит вектор \( e_{i_1} \wedge \ldots \wedge e_{i_p} \) в вектор \( (-1)^\sigma e_{j_1} \wedge \ldots \wedge e_{j_{n-p}} \), где \( \{j_1, \ldots, j_{n-p}\} \) — дополнение множества