---
source_image: page_166.png
page_number: 166
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.60
tokens: 6115
characters: 3523
timestamp: 2025-12-24T07:09:20.488180
finish_reason: stop
---

Найти инвариантные множители следующих \( \lambda \)-матриц:

1015.
\[
\begin{pmatrix}
3\lambda^2 + 2\lambda - 3 & 2\lambda - 1 & \lambda^2 + 2\lambda - 3 \\
4\lambda^2 + 3\lambda - 5 & 3\lambda - 2 & \lambda^2 + 3\lambda - 4 \\
\lambda^2 + \lambda - 4 & \lambda - 2 & \lambda - 1
\end{pmatrix}.
\]

1016.
\[
\begin{pmatrix}
3\lambda^3 - 2\lambda + 1 & 2\lambda^2 + \lambda - 1 & 3\lambda^3 + 2\lambda^2 - 2\lambda - 1 \\
2\lambda^3 - 2\lambda & \lambda^2 - 1 & 2\lambda^3 + \lambda^2 - 2\lambda - 1 \\
5\lambda^3 - 4\lambda + 1 & 3\lambda^2 + \lambda - 2 & 5\lambda^3 + 3\lambda^2 - 4\lambda - 2
\end{pmatrix}.
\]

1017.
\[
\begin{pmatrix}
2\lambda^3 - \lambda^2 + 2\lambda - 1 & 2\lambda^3 - 3\lambda^2 + 2\lambda - 3 & \lambda^3 - 2\lambda^2 + \lambda - 2 & 5\lambda^3 - 2\lambda^2 + 5\lambda - 2 \\
\lambda^3 + \lambda^2 + \lambda + 1 & \lambda^3 - 3\lambda^2 + \lambda - 3 & -\lambda^3 - \lambda^2 - \lambda - 1 & 7\lambda^3 - \lambda^2 + 7\lambda - 1 \\
\lambda^3 - 2\lambda^2 + \lambda - 2 & \lambda^3 + \lambda & 2\lambda^3 - \lambda^2 + 2\lambda - 1 & -2\lambda^3 - \lambda^2 - 2\lambda - 1 \\
3\lambda^3 - 2\lambda^2 + 3\lambda - 2 & 3\lambda^3 - 4\lambda^2 + 3\lambda - 4 & 2\lambda^3 - 3\lambda^2 - 2\lambda - 3 & 6\lambda^3 - 3\lambda^2 + 6\lambda - 3
\end{pmatrix}.
\]

1018.
\[
\begin{pmatrix}
\lambda^3 + \lambda^2 - \lambda + 3 & \lambda^3 - \lambda^2 + \lambda & 2\lambda^3 + \lambda^2 - \lambda + 4 & \lambda^3 + \lambda^2 - \lambda + 2 \\
\lambda^3 + 3\lambda^2 - 3\lambda + 6 & \lambda^3 - 3\lambda^2 + 3\lambda - 2 & 2\lambda^3 + 3\lambda^2 - 3\lambda + 7 & \lambda^3 + 3\lambda^2 - 3\lambda + 4 \\
\lambda^3 + 2\lambda^2 - 2\lambda + 4 & \lambda^3 - 2\lambda^2 + 2\lambda - 1 & 2\lambda^3 + 2\lambda^2 - 2\lambda + 5 & \lambda^3 + 2\lambda^2 - 2\lambda + 3 \\
2\lambda^3 + \lambda^2 - \lambda + 5 & 2\lambda^3 - \lambda^2 + \lambda + 1 & 4\lambda^3 + \lambda^2 - \lambda + 7 & 2\lambda^3 + \lambda^2 - \lambda + 3
\end{pmatrix}.
\]

1019.
\[
\begin{pmatrix}
\lambda & 1 & 2 & \ldots & n \\
0 & \lambda & 1 & 2 & \ldots & n-1 \\
0 & 0 & \lambda & 1 & \ldots & n-2 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & \lambda
\end{pmatrix}.
\]

1020.
\[
\begin{pmatrix}
\lambda - \alpha & \beta & \beta & \beta & \ldots & \beta \\
0 & \lambda - \alpha & \beta & \beta & \ldots & \beta \\
0 & 0 & \lambda - \alpha & \beta & \ldots & \beta \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & \lambda - \alpha
\end{pmatrix}
\]
(порядок матрицы равен \( n \)).

Элементарными делителями \( \lambda \)-матрицы \( A \) называются многочлены \( e_1(\lambda), e_2(\lambda), \ldots, e_s(\lambda) \) со старшими коэффициентами, равными единице, совпадающие с наивысшими степенями неприводимых множителей, входящими в разложения инвариантных множителей \( E_1(\lambda), E_2(\lambda), \ldots, E_n(\lambda) \) матрицы \( A \) на неприводимые множители. При этом совокупность элементарных делителей матрицы \( A \) содержит каждый многочлен \( E_i(\lambda) \) столько раз, сколько инвариантных множителей \( E_k(\lambda) \) содержит его в своем разложении. Разложение на неприводимые множители берется над тем полем, над которым рассматриваются многочлены, являющиеся элементами матрицы \( A \). В дальнейшем, если не оговорено противное, рассматриваются элементарные делители над полем комплексных чисел, т. е. наивысшие степени многочленов вида \( \lambda - \alpha \), входящие в разложения инвариантных множителей матрицы \( A \) на линейные множители.