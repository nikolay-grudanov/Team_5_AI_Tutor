---
source_image: page_492.png
page_number: 492
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.49
tokens: 6616
characters: 2588
timestamp: 2025-12-24T08:20:58.633874
finish_reason: stop
---

то существует такой номер \( j > 1 \), что \( \lambda_{j-1} \leq d_1 \leq \lambda_j \). Пусть \( P_1 \) — такая матрица перестановки, что \( P_1^T \Lambda P_1 = \operatorname{diag}(\lambda_1, \lambda_j, \lambda_2, \ldots, \hat{\lambda}_j, \ldots, \lambda_{n+1}) \). Легко проверить, что

\[
\lambda_1 \leq \min(d_1, \lambda_1 + \lambda_j - d_1) \leq \max(d_1, \lambda_1 + \lambda_j - d_1) \leq \lambda_j.
\]

Поэтому существует такая ортогональная матрица \( Q \) порядка 2, что на диагонали матрицы \( Q^T \operatorname{diag}(\lambda_1, \lambda_j) Q \) стоят числа \( d_1 \) и \( \lambda_1 + \lambda_j - d_1 \).

Рассмотрим матрицу \( P_2 = \begin{pmatrix} Q & 0 \\ 0 & I \end{pmatrix} \) порядка \( n + 1 \). Ясно, что

\[
P_2^T (P_1^T \Lambda P_1) P_2 = \begin{pmatrix} d_1 & b^T \\ b & \Lambda_1 \end{pmatrix},
\]

где \( \Lambda_1 = \operatorname{diag}(\lambda_1 + \lambda_j - d_1, \lambda_2, \ldots, \hat{\lambda}_j, \ldots, \lambda_{n+1}) \). Упорядоченные по возрастанию диагональные элементы матрицы \( \Lambda_1 \) и числа \( d_2, \ldots, d_{n+1} \) удовлетворяют условию теоремы. В самом деле,

\[
d_2 + \ldots + d_k \geq (k-1)d_1 \geq \lambda_2 + \ldots + \lambda_k
\]

при \( k = 2, \ldots, j-1 \) и

\[
\begin{align*}
d_2 + \ldots + d_k &= d_1 + \ldots + d_k - d_1 \geq \lambda_1 + \ldots + \lambda_k - d_1 = \\
&= (\lambda_1 + \lambda_j - d_1) + \lambda_2 + \ldots + \lambda_{j-1} + \lambda_{j+1} + \ldots + \lambda_k
\end{align*}
\]

при \( k = j, \ldots, n+1 \); в обоих случаях правые части неравенств не меньше суммы \( k-1 \) минимальных диагональных элементов матрицы \( \Lambda_1 \). Поэтому существует такая ортогональная матрица \( Q_1 \), что на диагонали матрицы \( Q_1^T \Lambda_1 Q_1 \) стоят числа \( d_2, \ldots, d_{n+1} \). Пусть \( P_3 = \begin{pmatrix} 1 & 0 \\ 0 & Q_1 \end{pmatrix} \). Тогда матрица \( P = P_1 P_2 P_3 \) искомая.

Замечание. Если \( \lambda_1 \leq \ldots \leq \lambda_n, d_1 \leq \ldots \leq d_n \) и на диагонали матрицы \( P^T \Lambda P \), где \( \Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \) и \( P \) — ортогональная матрица, стоят числа \( d_1, \ldots, d_n \), то \( d_1 + \ldots + d_k \geq \lambda_1 + \ldots + \lambda_k \) при \( k = 1, \ldots, n-1 \) и \( d_1 + \ldots + d_n = \lambda_1 + \ldots + \lambda_n \).

§ 56. Числовой образ оператора

56.1. Теорема Тёплица—Хаусдорфа

Пусть \( A \) — оператор в эрмитовом пространстве \( V \). Числовым образом оператора \( A \) называют множество \( W(A) \) всех комплексных чисел вида \( (Av, v) \), где \( v \) пробегает все векторы в \( V \) единичной длины. Это