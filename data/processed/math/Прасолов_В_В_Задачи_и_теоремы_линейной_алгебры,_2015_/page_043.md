---
source_image: page_043.png
page_number: 43
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.47
tokens: 6849
characters: 2713
timestamp: 2025-12-24T08:08:47.538215
finish_reason: stop
---

1.34. Докажите, что

\[
\begin{vmatrix}
\binom{n}{m_1} & \binom{n}{m_1-1} & \cdots & \binom{n}{m_1-k} \\
\cdots & \cdots & \cdots & \cdots \\
\binom{n}{m_k} & \binom{n}{m_k-1} & \cdots & \binom{n}{m_k-k}
\end{vmatrix}
=
\begin{vmatrix}
\binom{n}{m_1} & \binom{n+1}{m_1} & \cdots & \binom{n+k}{m_1} \\
\cdots & \cdots & \cdots & \cdots \\
\binom{n}{m_k} & \binom{n+1}{m_k} & \cdots & \binom{n+k}{m_k}
\end{vmatrix}.
\]

1.35. Пусть \( \Delta_n(k) = |a_{ij}|_0^n \), где \( a_{ij} = \binom{k+i}{2j} \). Докажите, что

\[
\Delta_n(k) = \frac{k(k+1)\ldots(k+n-1)}{1 \cdot 3 \cdot \ldots \cdot (2n-1)} \Delta_{n-1}(k-1).
\]

1.36. Пусть \( D_n = |a_{ij}|_0^n \), где \( a_{ij} = \binom{n+1}{2j-i} \). Докажите, что \( D_n = 2^{n(n+1)/2} \).

1.37. Даны числа \( a_0, a_1, \ldots, a_n \). Пусть \( b_k = \sum_{i=0}^k (-1)^i \binom{k}{i} a_i \) (\( k = 0, \ldots, 2n \)), \( a_{ij} = a_{i+j} \), \( b_{ij} = b_{i+j} \). Докажите, что \( |a_{ij}|_0^n = |b_{ij}|_0^n \).

1.38 [Fi1]. Пусть \( A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix} \) и \( B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix} \), где \( A_{11} \) и \( B_{11} \), а также \( A_{22} \) и \( B_{22} \) — квадратные матрицы одного порядка соответственно, причем \( \operatorname{rk} A_{11} = \operatorname{rk} A \) и \( \operatorname{rk} B_{22} = \operatorname{rk} B \). Докажите, что

\[
\begin{vmatrix}
A_{11} & B_{12} \\
A_{21} & B_{22}
\end{vmatrix}
\cdot
\begin{vmatrix}
A_{11} & A_{12} \\
B_{21} & B_{22}
\end{vmatrix}
= |A+B| \cdot |A_{11}| \cdot |B_{22}|.
\]

1.39. Пусть \( A \) и \( B \) — квадратные матрицы порядка \( n \). Докажите, что \( |A| \cdot |B| = \prod_{k=1}^n |A_k| \cdot |B_k| \), где матрицы \( A_k \) и \( B_k \) получены из \( A \) и \( B \) обменом столбцов с номерами 1 и \( k \) соответственно (первый столбец матрицы \( A \) и \( k \)-й столбец матрицы \( B \) меняются местами).

1.40. Даны столбцы \( A_1, \ldots, A_p, B_1, \ldots, B_{n-p}, C_1, \ldots, C_p \) длины \( n \). Пусть \( a_{ij} = |\hat{A}_i B C_j| \) — определитель матрицы \( (A_1 \ldots \hat{A}_i \ldots A_p B_1 \ldots B_{n-p} C_j) \). Докажите, что \( |a_{ij}|_1^p = |AB|^{p-1} |BC| \) (тождество Базена).

Числа Фибоначчи

Числами Фибоначчи называют последовательность чисел \( F_1 = 1, F_2 = 1, F_n = F_{n-1} + F_{n-2} \) при \( n \geq 3 \). Начало этой последовательности имеет вид 1, 1, 2, 3, 5, 8, 13, 21, ...

1.41. Докажите, что при \( n \geq 2 \)

\[
\begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}^n = \begin{pmatrix} F_{n+1} & F_n \\ F_n & F_{n-1} \end{pmatrix} \quad \text{и} \quad \begin{pmatrix} -1 & 1 \\ 1 & 0 \end{pmatrix}^n = (-1)^n \begin{pmatrix} F_{n+1} & -F_n \\ -F_n & F_{n-1} \end{pmatrix}.
\]