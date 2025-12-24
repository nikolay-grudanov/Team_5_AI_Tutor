---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.06
tokens: 6585
characters: 2353
timestamp: 2025-12-24T08:10:01.540554
finish_reason: stop
---

После нескольких таких операций в итоге получим матрицу со строками \(\left( \binom{n}{m}, \binom{n+1}{m}, \ldots, \binom{n+k}{m} \right)\).

**1.35.** Вычтем в определителе \( \Delta_n(k) \) из строки с номером \( i + 1 \) строку с номером \( i \) для \( i = n - 1, \ldots, 0 \). В результате получим \( \Delta_n(k) = \Delta'_{n-1}(k) \), где \( \Delta'_m(k) = |a'_{ij}|_0^m \), \( a'_{ij} = \binom{k+i}{2j+1} \). А так как \( \binom{k+i}{2j+1} = \frac{k+i}{2j+1} \binom{k-1+i}{2j} \), то

\[
\Delta'_{n-1}(k) = \frac{k(k+1) \ldots (k+n-1)}{1 \cdot 3 \cdot \ldots \cdot (2n-1)} \Delta_{n-1}(k-1).
\]

**1.36** [Ca2]. Согласно задаче 1.34 \( D_n = D'_n = |a'_{ij}|_0^n \), где \( a'_{ij} = \binom{n+1+i}{2j} \), т. е. в обозначениях задачи 1.35 получаем

\[
D_n = \Delta_n(n+1) = \frac{(n+1)(n+2) \ldots 2n}{1 \cdot 3 \cdot \ldots \cdot (2n-1)} \Delta_{n-1}(n) = 2^n D_{n-1},
\]

так как \( (n+1)(n+2) \ldots 2n = (2n)!/n! \), \( 1 \cdot 3 \cdot \ldots \cdot (2n-1) = (2n)!/2 \cdot 4 \cdot \ldots \cdot 2n \) и \( \Delta_{n-1}(n) = D_{n-1} \). А так как \( D_0 = 1 \), то \( D_n = 2^k \), где \( k = n + (n-1) + \ldots + 1 = n(n+1)/2 \).

**1.37.** Доказательство проведём при \( n = 2 \). Согласно задаче 1.29 а) \( |a_{ij}|_0^2 = |a'_{ij}|_0^2 \), где \( a'_{ij} = (-1)^{i+j} a_{ij} \). Прибавим к последнему столбцу матрицы \( ||a'_{ij}||_0^2 \) её предпоследний столбец, а затем к последней строке полученной матрицы прибавим её предпоследнюю строку. В результате получим матрицу

\[
\begin{pmatrix}
a_0 & -a_1 & -\Delta^1 a_1 \\
-a_1 & a_2 & \Delta^1 a_2 \\
-\Delta^1 a_1 & \Delta^1 a_2 & \Delta^2 a_2
\end{pmatrix},
\]

где \( \Delta^1 a_k = a_k - a_{k+1} \), \( \Delta^{n+1} a_k = \Delta^1 (\Delta^n a_k) \). Затем прибавим ко второй строке первую, а к третьей прибавим вторую строку полученной матрицы; такую же операцию проделаем для столбцов. В результате получим матрицу

\[
\begin{pmatrix}
a_0 & \Delta^1 a_0 & \Delta^2 a_0 \\
\Delta^1 a_0 & \Delta^2 a_0 & \Delta^3 a_0 \\
\Delta^2 a_0 & \Delta^3 a_0 & \Delta^4 a_0
\end{pmatrix}.
\]

Индукцией по \( k \) легко проверить, что \( b_k = \Delta^k a_0 \). В общем случае доказательство аналогично.

**1.38.** Матрицы \( A \) и \( B \) можно представить в виде

\[
A = \begin{pmatrix} P & PX \\ YP & YPX \end{pmatrix} \quad \text{и} \quad B = \begin{pmatrix} WQV & WQ \\ QV & Q \end{pmatrix},
\]