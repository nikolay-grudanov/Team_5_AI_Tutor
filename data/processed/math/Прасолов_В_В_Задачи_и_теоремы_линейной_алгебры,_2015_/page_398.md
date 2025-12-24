---
source_image: page_398.png
page_number: 398
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.53
tokens: 6360
characters: 2100
timestamp: 2025-12-24T08:18:17.928603
finish_reason: stop
---

элементы равны нулю. Рассмотрим уравнение

\[(\lambda I_m + N_m)X = X(\mu I_n + N_n),\]

т. е.

\[N_m X - XN_n = (\mu - \lambda)X.\]

Легко проверить, что

\[
N_m X = \begin{pmatrix}
x_{21} & \ldots & x_{2n} \\
\cdots & \cdots & \cdots \\
x_{m1} & \ldots & x_{mn} \\
0 & \ldots & 0
\end{pmatrix}
\quad \text{и} \quad
XN_n = \begin{pmatrix}
0 & x_{11} & \ldots & x_{1,n-1} \\
\cdots & \cdots & \cdots & \cdots \\
0 & x_{m1} & \ldots & x_{m,n-1}
\end{pmatrix}.
\]

Если \( \lambda \neq \mu \), то, рассмотрев первый столбец обеих частей уравнения, последовательно получим \( x_{m1} = 0, x_{m-1,1} = 0, \ldots, x_{11} = 0 \). Продолжив далее такие же рассуждения для следующих столбцов, получим \( X = 0 \). Предположим теперь, что \( \lambda = \mu \), т. е. \( N_m X = XN_n \). Легко проверить, что в этом случае решение \( X \) имеет вид \( (0, Y) \) при \( n > m \), \( \begin{pmatrix} Y \\ 0 \end{pmatrix} \) при \( n < m \) и \( Y \) при \( n = m \), где

\[
Y = \begin{pmatrix}
y_1 & y_2 & \ldots & y_k \\
0 & y_1 & \ldots & y_{k-1} \\
\cdots & \cdots & \cdots & \cdots \\
0 & 0 & \ldots & y_1
\end{pmatrix}
\quad \text{и} \quad k = \min(m, n).
\]

Размерность пространства решений равна \( \min(m, n) \). В результате доказано следующее утверждение.

**Теорема 42.1.1.** Пусть \( \lambda \) — собственное значение матрицы \( A \) или матрицы \( B \), причём этому собственному значению соответствуют жордановы клетки порядков \( a_1(\lambda), \ldots, a_r(\lambda) \) и \( b_1(\lambda), \ldots, b_s(\lambda) \); если \( \lambda \) — собственное значение лишь одной матрицы, то порядки жордановых клеток второй матрицы считаются нулевыми. Тогда размерность пространства решений уравнения \( AX = XB \) равна

\[\min_{\lambda, i, j} (a_i(\lambda), b_j(\lambda)).\]

**Следствие.** Размерность пространства решений уравнения \( AX = XA \) равна

\[\min_{\lambda, i, j} (a_i(\lambda), a_j(\lambda)).\]

**Теорема 42.1.2.** Пусть \( m \) — размерность пространства решений уравнения \( AX = XA \), где \( A \) — квадратная матрица порядка \( n \). Тогда следующие условия эквивалентны:

а) \( m = n; \)