---
source_image: page_172.png
page_number: 172
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.96
tokens: 5502
characters: 1997
timestamp: 2025-12-24T07:09:12.704284
finish_reason: stop
---

1059. Матрицу

\[
A = \begin{pmatrix}
-\lambda^3 + \lambda^2 + 3\lambda + 6 & \lambda^2 + 2\lambda & \lambda^2 + 2\lambda + 6 \\
-2\lambda^3 + 2\lambda^2 + 9\lambda + 8 & \lambda^2 + 6\lambda + 1 & 2\lambda^2 + 7\lambda + 8 \\
-\lambda^3 + \lambda^2 + 3\lambda + 5 & \lambda^2 + 2\lambda - 9 & \lambda^2 + 5\lambda - 2
\end{pmatrix}
\]

разделить справа на \( B - \lambda E \), где \( B = \begin{pmatrix} 1 & 2 & 1 \\ 3 & 2 & 3 \\ 1 & 2 & 3 \end{pmatrix} \).

*1060. Доказать, что если две матрицы \( A \) и \( B \) с числовыми элементами (или с элементами из некоторого поля \( P \)) подобны, то их характеристические матрицы \( A - \lambda E \) и \( B - \lambda E \) эквивалентны.

*1061. Доказать, что если характеристические матрицы \( A - \lambda E \) и \( B - \lambda E \) двух матриц \( A \) и \( B \) эквивалентны, то сами эти матрицы подобны. При этом показать, что если \( B - \lambda E = P(A - \lambda E)Q \), где \( P \) и \( Q \) — унимодулярные \( \lambda \)-матрицы и \( P_0, Q_0 \) — остатки при делении \( P \) слева, а \( Q \) справа на \( B - \lambda E \), то \( B = P_0 AQ_0 \) и \( P_0 Q_0 = E \), т. е. матрица \( Q_0 \) осуществляет подобное преобразование матрицы \( A \) в матрицу \( B \).

1062. Доказать, что любая квадратная матрица \( A \) подобна своей транспонированной матрице \( A' \).

Выяснить, являются ли подобными между собой следующие матрицы:

1063. \( A = \begin{pmatrix} 3 & 2 & -5 \\ 2 & 6 & -10 \\ 1 & 2 & -3 \end{pmatrix}; \quad B = \begin{pmatrix} 6 & 20 & -34 \\ 6 & 32 & -51 \\ 4 & 20 & -32 \end{pmatrix} \).

1064. \( A = \begin{pmatrix} 6 & 6 & -15 \\ 1 & 5 & -5 \\ 1 & 2 & -2 \end{pmatrix}; \quad B = \begin{pmatrix} 37 & -20 & -4 \\ 34 & -17 & -4 \\ 119 & -70 & -11 \end{pmatrix} \).

1065. \( A = \begin{pmatrix} 4 & 6 & -15 \\ 1 & 3 & -5 \\ 1 & 2 & -4 \end{pmatrix}; \quad B = \begin{pmatrix} 1 & -3 & 3 \\ -2 & -6 & 13 \\ -1 & -4 & 8 \end{pmatrix} \);
\[
C = \begin{pmatrix} -13 & -70 & 119 \\ -4 & -19 & 34 \\ -4 & -20 & 35 \end{pmatrix}.
\]