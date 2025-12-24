---
source_image: page_238.png
page_number: 238
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.97
tokens: 6774
characters: 2901
timestamp: 2025-12-24T08:14:10.199279
finish_reason: stop
---

\(\lambda = \mu\) не исключается. Следовательно, матрица \(A\) подобна матрице \(C = \begin{pmatrix} 0 & 1 & 0 \\ a & b & 0 \\ 0 & 0 & \lambda \end{pmatrix}\), причём характеристический многочлен матрицы \(\begin{pmatrix} 0 & 1 \\ a & b \end{pmatrix}\) делится на \(x - \lambda\), т. е. \(\lambda^2 - b\lambda - a = 0\). Если \(b = \lambda = 0\), то теорема верна. Пусть \(b = \lambda \neq 0\). Так как \(b^2 - b^2 - a = 0\), то \(a = 0\). В этом случае

\[
\begin{pmatrix} b & -1 & b \\ b & 0 & 0 \\ b & 0 & b \end{pmatrix}
\begin{pmatrix} 0 & 1 & 0 \\ 0 & b & 0 \\ 0 & 0 & b \end{pmatrix}
=
\begin{pmatrix} 0 & 0 & b^2 \\ 0 & b & 0 \\ 0 & b & b^2 \end{pmatrix}
=
\begin{pmatrix} 0 & -b & b \\ -b & 0 & b \\ -b & -b & 2b \end{pmatrix}
\begin{pmatrix} b & -1 & b \\ b & 0 & 0 \\ b & 0 & b \end{pmatrix},
\]

причём \(\det \begin{pmatrix} b & -1 & b \\ b & 0 & 0 \\ b & 0 & b \end{pmatrix} \neq 0\), поэтому \(A\) подобна матрице \(\begin{pmatrix} 0 & -b & b \\ -b & 0 & b \\ -b & -b & 2b \end{pmatrix}\).

Пусть, наконец, \(b \neq \lambda\). Тогда для матрицы \(D = \operatorname{diag}(b, \lambda)\) теорема верна, поэтому существует такая матрица \(P\), что \(PDP^{-1} = \begin{pmatrix} 0 & * \\ * & * \end{pmatrix}\).

Матрица

\[
\begin{pmatrix} 1 & 0 \\ 0 & P \end{pmatrix} C \begin{pmatrix} 1 & 0 \\ 0 & P^{-1} \end{pmatrix}
= \begin{pmatrix} 1 & 0 \\ 0 & P \end{pmatrix} \begin{pmatrix} 0 & * \\ * & D \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & P^{-1} \end{pmatrix}
= \begin{pmatrix} 0 & * \\ * & PDP^{-1} \end{pmatrix}
\]

имеет требуемый вид.

Предположим теперь, что теорема верна для матриц порядка \(m\), где \(m \geq 3\). Матрица \(A\) порядка \(m + 1\) имеет вид \(\begin{pmatrix} A_1 & * \\ * & * \end{pmatrix}\), где \(A_1\) — матрица порядка \(m\). Так как \(A \neq \lambda I\), можно считать, что \(A_1 \neq \lambda I\) (для доказательства можно воспользоваться результатом задачи 14.3). По предположению индукции существует такая матрица \(P\), что диагональ матрицы \(PA_1P^{-1}\) имеет вид \((0, 0, \ldots, 0, \alpha)\). Поэтому диагональ матрицы

\[
X = \begin{pmatrix} P & 0 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} A_1 & * \\ * & * \end{pmatrix} \begin{pmatrix} P^{-1} & 0 \\ 0 & 1 \end{pmatrix}
= \begin{pmatrix} PA_1P^{-1} & * \\ * & * \end{pmatrix}
\]

имеет вид \((0, \ldots, 0, \alpha, \beta)\). Если \(\alpha = 0\), то доказательство завершено. Пусть \(\alpha \neq 0\). Тогда \(X = \begin{pmatrix} 0 & * \\ * & C_1 \end{pmatrix}\), где диагональ матрицы \(C_1\) порядка \(m\) имеет вид \((0, 0, \ldots, \alpha, \beta)\), поэтому \(C_1 \neq \lambda I\). Следовательно, существует такая матрица \(Q\), что диагональ матрицы \(QC_1Q^{-1}\) имеет вид \((0, \ldots, 0, x)\). Поэтому диагональ матрицы \(\begin{pmatrix} 1 & 0 \\ 0 & Q \end{pmatrix} \begin{pmatrix} 0 & * \\ * & C_1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & Q^{-1} \end{pmatrix}\) имеет требуемый вид. \(\square\)