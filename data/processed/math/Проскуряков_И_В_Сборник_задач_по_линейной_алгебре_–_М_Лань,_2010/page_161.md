---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.37
tokens: 5492
characters: 2049
timestamp: 2025-12-24T07:08:58.084925
finish_reason: stop
---

981. \[
\begin{pmatrix}
\lambda - 2 & -1 & 0 \\
0 & \lambda - 2 & -1 \\
0 & 0 & \lambda - 2
\end{pmatrix}.
\]

982. \[
\begin{pmatrix}
\lambda(\lambda + 1) & 0 & 0 \\
0 & \lambda & 0 \\
0 & 0 & (\lambda + 1)^2
\end{pmatrix}.
\]

983. \[
\begin{pmatrix}
1 - \lambda & \lambda^2 & \lambda \\
\lambda & \lambda & -\lambda \\
1 + \lambda^2 & \lambda^2 & -\lambda^2
\end{pmatrix}.
\]

* 984. Инвариантными множителями \( \lambda \)-матрицы \( A \) порядка \( n \) называются многочлены \( E_1(\lambda), E_2(\lambda), \ldots, E_n(\lambda) \), стоящие на главной диагонали в нормальной диагональной форме матрицы \( A \). Делителями миноров матрицы \( A \) называются многочлены \( D_1(\lambda), D_2(\lambda), \ldots, D_n(\lambda) \), где \( D_k(\lambda) \) — наибольший общий делитель (взятый со старшим коэффициентом, равным единице) миноров \( k \)-го порядка матрицы \( A \), если не все эти миноры равны нулю, и \( D_k(\lambda) = 0 \) в противном случае. Доказать, что \( E_k(\lambda) \neq 0 \) и \( D_k(\lambda) \neq 0 \) для \( k = 1, 2, \ldots, r \), где \( r \) — ранг матрицы \( A \), тогда как \( E_k(\lambda) = D_k(\lambda) = 0 \) для \( k = r + 1, \ldots, n \). Далее показать, что \( E_k(\lambda) = \frac{D_k(\lambda)}{D_{k-1}(\lambda)} \) (\( k = 1, 2, \ldots, r; D_0 = 1 \)).

Следующие \( \lambda \)-матрицы привести к нормальной диагональной форме при помощи делителей миноров, определенных в задаче 984.

985. \[
\begin{pmatrix}
\lambda(\lambda - 1) & 0 & 0 \\
0 & \lambda(\lambda - 2) & 0 \\
0 & 0 & (\lambda - 1)(\lambda - 2)
\end{pmatrix}.
\]

986. \[
\begin{pmatrix}
\lambda(\lambda - 1) & 0 & 0 \\
0 & \lambda(\lambda - 2) & 0 \\
0 & 0 & \lambda(\lambda - 3)
\end{pmatrix}.
\]

987. \[
\begin{pmatrix}
a_{11} & 0 & 0 & 0 \\
0 & a_{22} & 0 & 0 \\
0 & 0 & a_{33} & 0 \\
0 & 0 & 0 & a_{44}
\end{pmatrix},
\]
где \( a_{11} = (\lambda - 1)(\lambda - 2)(\lambda - 3) \), \( a_{22} = (\lambda - 1)(\lambda - 2)(\lambda - 4) \), \( a_{33} = (\lambda - 1)(\lambda - 3)(\lambda - 4) \), \( a_{44} = (\lambda - 2)(\lambda - 3)(\lambda - 4) \).