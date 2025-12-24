---
source_image: page_392.png
page_number: 392
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.94
tokens: 5494
characters: 1956
timestamp: 2025-12-24T07:14:40.988364
finish_reason: stop
---

997. \[
\begin{pmatrix}
1 & 0 & 0 \\
0 & \lambda - 3 & 0 \\
0 & 0 & (\lambda - 3)^2
\end{pmatrix}
\]
998. \[
\begin{pmatrix}
\lambda - 1 & 0 & 0 \\
0 & \lambda - 1 & 0 \\
0 & 0 & (\lambda - 1)^2
\end{pmatrix}
\]
999. \[
\begin{pmatrix}
1 & 0 \\
1 & 1 \\
\vdots & \vdots \\
0 & \lambda^n
\end{pmatrix}
\]
, где \( n \) — порядок данной матрицы.

1000. Эквивалентны.
1001. Не эквивалентны.
1002. Матрицы \( A \) и \( C \) эквивалентны между собой и не эквивалентны матрице \( B \).
1003. Единичная матрица.
1005. Указание. Воспользоваться тем, что элементарное преобразование строк матрицы \( A \) сводится к умножению \( A \) слева (а столбцов справа) на специальную унимодулярную \( \lambda \)-матрицу. Далее, если \( B = P_s P_{s-1} \ldots P_1 A Q_1 Q_2 \ldots Q_t \), где \( P_i, Q_j \) — специальные унимодулярные \( \lambda \)-матрицы, то положить \( P = P_s P_{s-1} \ldots P_1 E_m \) и \( Q = E_n Q_1 Q_2 \ldots Q_t \). При доказательстве достаточности использовать ответ задачи 1003.
1006.
\[
B = \begin{pmatrix}
1 & 0 \\
0 & \lambda^2 - 1
\end{pmatrix}; \quad
P = \begin{pmatrix}
0 & 1/2 \\
-2 & \lambda + 3
\end{pmatrix};
\]
\[
Q = \begin{pmatrix}
\lambda & -\frac{1}{2}\lambda^2 + \frac{1}{2}\lambda - 1 \\
1 - \lambda & \frac{1}{2}\lambda^2 - \lambda + \frac{3}{2}
\end{pmatrix}.
\]
1007.
\[
B = \begin{pmatrix}
\lambda + 2 & 0 \\
0 & \lambda^2 + 4\lambda + 4
\end{pmatrix}; \quad
P = \begin{pmatrix}
1 & 0 \\
-1 & 1
\end{pmatrix};
\]
\[
Q = \begin{pmatrix}
1 & -\lambda^2 - 2\lambda \\
-\lambda & \lambda^3 + 2\lambda^2 + 1
\end{pmatrix}.
\]
1008.
\[
B = \begin{pmatrix}
1 & 0 & 0 \\
0 & \lambda - 1 & 0 \\
0 & 0 & \lambda^3 - \lambda^2
\end{pmatrix}; \quad
P = \begin{pmatrix}
-2\lambda - 3 & 0 & 2\lambda + 4 \\
-3 & -1 & 4 \\
3 & 0 & -1
\end{pmatrix};
\]
\[
Q = \begin{pmatrix}
1 & -\lambda^3 + \lambda^2 - \lambda + 1 & 0 \\
\lambda & -\lambda^4 + \lambda^3 - \lambda^2 + \lambda + 1 & 0 \\
-\lambda - 1 & \lambda^4 - 2 & 1
\end{pmatrix}.
\]