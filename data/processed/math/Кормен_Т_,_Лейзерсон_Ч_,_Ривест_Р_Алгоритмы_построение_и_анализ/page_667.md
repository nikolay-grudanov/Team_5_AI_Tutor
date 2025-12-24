---
source_image: page_667.png
page_number: 667
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 65.60
tokens: 11751
characters: 2109
timestamp: 2025-12-24T06:52:02.207979
finish_reason: stop
---

Часто встречаются квадратные матрицы (square matrices) — матрицы размера \( n \times n \). Некоторые их виды мы отметим особо.

1. У диагональной матрицы (diagonal matrix) все внедиагональные элементы равны нулю (\( a_{ij} = 0 \) при \( i \neq j \)), поэтому она может быть задана перечислением элементов, стоящих на диагонали.

\[
diag(a_{11}, a_{22}, \ldots, a_{nn}) = \begin{pmatrix}
a_{11} & 0 & \cdots & 0 \\
0 & a_{22} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & a_{nn}
\end{pmatrix}.
\]

2. Единичной матрицей (identity matrix) называется диагональная матрица, диагональ которой заполнена единицами:

\[
I_n = diag(1, 1, ..., 1) = \begin{pmatrix}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{pmatrix}.
\]

Иногда индекс \( n \) при букве \( I \) опускается; размер матрицы в этом случае определяется из контекста. Столбцами единичной матрицы служат векторы \( e_1, e_2, \ldots, e_n \).

3. У трёхдиагональной матрицы (tridiagonal matrix) ненулевые элементы могут появляться на главной диагонали (\( t_{i,i} \) при \( i = 1, 2, \ldots, n \)), прямо над ней (\( t_{i,i+1} \) при \( i = 1, 2, \ldots, n-1 \)), или прямо под ней (\( t_{i+1,i} \) при \( i = 1, 2, \ldots, n-1 \)). Все остальные элементы равны нулю (\( t_{ij} = 0 \) при \( |i - j| > 1 \)):

\[
T = \begin{pmatrix}
t_{11} & t_{12} & 0 & 0 & \cdots & 0 & 0 & 0 \\
t_{21} & t_{22} & t_{23} & 0 & \cdots & 0 & 0 & 0 \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots & \vdots & \vdots \\
0 & 0 & 0 & 0 & \cdots & t_{n-2,n-2} & t_{n-2,n-1} & 0 \\
0 & 0 & 0 & 0 & \cdots & t_{n-1,n-2} & t_{n-1,n-1} & t_{n-1,n} \\
0 & 0 & 0 & 0 & \cdots & 0 & t_{n,n-1} & t_{n,n}
\end{pmatrix}.
\]

4. У верхне-треугольной матрицы (upper-triangular matrix) все элементы под главной диагональю равны нулю (\( u_{ij} = 0 \) при \( i > j \)):

\[
U = \begin{pmatrix}
u_{11} & u_{12} & \cdots & u_{1n} \\
0 & u_{22} & \cdots & u_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & u_{nn}
\end{pmatrix}.
\]

5. У нижне-треугольной матрицы (lower-triangular matrix) все