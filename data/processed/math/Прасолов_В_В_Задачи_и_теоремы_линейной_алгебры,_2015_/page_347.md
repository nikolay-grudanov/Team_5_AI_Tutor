---
source_image: page_347.png
page_number: 347
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.61
tokens: 6672
characters: 2670
timestamp: 2025-12-24T08:17:09.497702
finish_reason: stop
---

30.2. Продолжим отображение \( f \) до билинейного отображения \( \mathbb{C}^m \times \mathbb{C}^m \to \mathbb{C}^n \). Рассмотрим уравнение \( f(z, z) = 0 \), т. е. систему квадратных уравнений

\[
f_1(z, z) = 0, \quad \ldots, \quad f_n(z, z) = 0.
\]

Предположим, что \( n < m \). Тогда эта система имеет ненулевое решение \( z = x + iy \). Из второго условия следует, что \( y \neq 0 \). Ясно также, что \( 0 = f(z, z) = f(x + iy, x + iy) = f(x, x) - f(y, y) + 2if(x, y) \), поэтому \( f(x, x) = f(y, y) \neq 0 \) и \( f(x, y) = 0 \). Это противоречит первому условию.

30.3. Элементы \( \alpha_i = e_{2i-1} \wedge e_{2i} \) лежат в \( \Lambda^2(V) \), поэтому \( \alpha_i \wedge \alpha_j = \alpha_j \wedge \alpha_i \) и \( \alpha_i \wedge \alpha_i = 0 \). Следовательно,

\[
\bigwedge^n \omega = \sum_{i_1, \ldots, i_n} \alpha_{i_1} \wedge \ldots \wedge \alpha_{i_n} = n! \alpha_1 \wedge \ldots \wedge \alpha_n = n! e_1 \wedge \ldots \wedge e_{2n}.
\]

30.4. Пусть на диагонали жордановой нормальной формы матрицы \( A \) стоят числа \( \lambda_1, \ldots, \lambda_n \). Тогда

\[
|A - \lambda I| = (\lambda_1 - \lambda) \ldots (\lambda_n - \lambda) = \sum_{k=0}^n (-1)^k \sigma_{n-k}(\lambda_1, \ldots, \lambda_n) \lambda^k.
\]

Если \( e_1, \ldots, e_n \) — жорданов базис, то матрица \( \Lambda^{n-k} A \) в базисе, состоящем из элементов вида \( e_{i_1} \wedge \ldots \wedge e_{i_{n-k}} \), упорядоченных лексикографически, треугольная (теорема 30.5.2); на диагонали этой матрицы стоят числа \( \lambda_{i_1} \ldots \lambda_{i_{n-k}} \), поэтому

\[
\operatorname{tr}(\Lambda^{n-k} A) = \sum_{i_1 < \ldots < i_{n-k}} \lambda_{i_1} \ldots \lambda_{i_{n-k}} = \sigma_{n-k}(\lambda_1, \ldots, \lambda_n).
\]

30.5. На всё пространство это скалярное произведение распространяется по линейности; его симметричность очевидна. Поэтому нужно лишь проверить, что если \( x \wedge y \neq 0 \), то

\[
\begin{pmatrix}
(x, z) & (x, t) \\
(y, z) & (y, t)
\end{pmatrix} = (x, x)(y, y) - (x, y)^2 > 0.
\]

Это неравенство очевидно.

На \( \Lambda^k V \) скалярное произведение задаётся формулой

\[
(x_1 \wedge \ldots \wedge x_k, y_1 \wedge \ldots \wedge y_k) = \det \begin{pmatrix}
(x_1, y_1) & \ldots & (x_1, y_k) \\
\vdots & \ddots & \vdots \\
(x_k, y_1) & \ldots & (x_k, y_k)
\end{pmatrix}.
\]

При \( x_1 = y_1, \ldots, x_k = y_k \) этот определитель является определителем Грама, поэтому если \( x_1 \wedge \ldots \wedge x_k \neq 0 \), то он положителен.

30.6. Если \( A = \|a_{ij}\|_1^n \), то матрица рассматриваемой системы уравнений равна \( S^2(A) \). Кроме того, \( \det S^2(A) = (\det A)^r \), где \( r = \frac{2}{n} \binom{n+2-1}{2} = n+1 \) (см. теорему 30.5.3).