---
source_image: page_491.png
page_number: 491
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.40
tokens: 6784
characters: 2857
timestamp: 2025-12-24T08:21:07.006663
finish_reason: stop
---

где степень \( r_i \) меньше \( n \). Тогда

\[
f_i = f_i - (x_i^n - \sigma_1 x_i^{n-1} + \sigma_2 x_i^{n-2} - \ldots + (-1)^n \sigma_n) =
= x_i^{n-1} g_1 + \ldots + x_i^{n-2} g_2 + \ldots + g_n,
\]

где \( g_i = (-1)^{i-1} (\sigma_i + q_i) \), т. е. \( F = VG \), где \( F \) и \( G \) — столбцы \( (f_1, \ldots, f_n)^T \) и \( (g_n, \ldots, g_1)^T \), \( V = \| x_{i+1}^j \|_0^{n-1} \). Поэтому \( G = V^{-1} F \), а так как \( V^{-1} = W^{-1} V_1 \) где \( W = \det V = \frac{\prod_{i>j} (x_i - x_j)}{} \) и \( V_1 \) — матрица, элементы которой — многочлены от \( x_1, \ldots, x_n \), то \( W g_1, \ldots, W g_n \in (f_1, \ldots, f_n) \), где \( (f_1, \ldots, f_n) \) — идеал кольца многочленов над \( \mathbb{C} \), порождённый \( f_1, \ldots, f_n \).

Предположим, что многочлены \( g_1, \ldots, g_n \) не имеют общих корней. Тогда по теореме Гильберта о нулях \( 1 = \cdot v_i g_i \), поэтому \( W = \cdot v_i (W g_i) \in (f_1, \ldots, f_n) \). С другой стороны, \( W = \cdot a_{i_1 \ldots i_n} x_1^{i_1} \ldots x_n^{i_n} \), где \( i_k < n \). Поэтому \( W \notin (f_1, \ldots, f_n) \) (теорема 55.2.1 а)). Следовательно, многочлены \( g_1, \ldots, g_n \) имеют общий корень.

Докажем теперь, что количество общих корней многочленов \( g_1, \ldots, g_n \) конечно. Пусть \( \xi = (x_1, \ldots, x_n) \) — корень многочленов \( g_1, \ldots, g_n \). Тогда \( \xi \) — корень многочленов \( f_1, \ldots, f_n \), так как \( f_i = x_i^{n-1} g_1 + \ldots + g_n \). Поэтому \( x_i^n + r_i(x_1, \ldots, x_n) = f_i = 0 \), причём степень многочлена \( r_i \) меньше \( n \). Но такая система уравнений имеет конечное число решений (теорема 55.2.1 б)). Поэтому число различных наборов \( x_1, \ldots, x_n \) конечно.

\subsection*{55.3. Предписанная диагональ}

\textbf{Теорема 55.3.1.} \emph{Пусть \( \lambda_1 \leq \ldots \leq \lambda_n, d_1 \leq \ldots \leq d_n, d_1 + \ldots + d_k \geq \lambda_1 + \ldots + \lambda_k \) при \( k = 1, \ldots, n-1 \) и \( d_1 + \ldots + d_n = \lambda_1 + \ldots + \lambda_n \). Тогда существует такая ортогональная матрица \( P \), что на диагонали матрицы \( P^T \Lambda P \), где \( \Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \), стоят числа \( d_1, \ldots, d_n \).}

\textbf{Доказательство [Ch2].} Пусть сначала \( n = 2 \). Тогда \( \lambda_1 \leq d_1 \leq d_2 \leq \lambda_2 \) и \( d_2 = \lambda_1 + \lambda_2 - d_1 \). Если \( \lambda_1 = \lambda_2 \), то можно положить \( P = I \). Если же \( \lambda_1 < \lambda_2 \), то матрица

\[
P = \frac{1}{\sqrt{\lambda_2 - \lambda_1}} \begin{pmatrix}
\sqrt{\lambda_2 - d_1} & -\sqrt{d_1 - \lambda_1} \\
\sqrt{d_1 - \lambda_1} & \sqrt{\lambda_2 - d_1}
\end{pmatrix}
\]

искомая.

Предположим теперь, что утверждение верно для некоторого \( n \geq 2 \) и рассмотрим наборы из \( n+1 \) чисел. Так как \( \lambda_1 \leq d_1 \leq d_{n+1} \leq \lambda_{n+1} \),