---
source_image: page_102.png
page_number: 102
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.50
tokens: 6548
characters: 2263
timestamp: 2025-12-24T08:10:20.121896
finish_reason: stop
---

Согласно задаче 2.19

\[
\operatorname{adj} \begin{pmatrix}
1 & & -1 \\
& \ddots & \\
& & 1 & -1 \\
0 & \ldots & 0 & 0
\end{pmatrix} = \begin{pmatrix}
0 & \ldots & 0 & 1 \\
\cdots & & & \\
0 & \ldots & 0 & 1
\end{pmatrix},
\]

поэтому

\[
\operatorname{adj} A = \begin{pmatrix}
0 & \ldots & 0 & 1 \\
\cdots & & & \\
0 & \ldots & 0 & 1
\end{pmatrix} \operatorname{adj}(A_{n-1}0).
\]

Для матрицы \((A_{n-1}0)\) ненулевой минор может получиться только при вычёркивании последнего столбца, поэтому

\[
\operatorname{adj} A = \begin{pmatrix}
0 & 0 & \ldots & 0 & 1 \\
0 & 0 & \ldots & 0 & 1 \\
\cdots & & & & \\
0 & 0 & \ldots & 0 & 1
\end{pmatrix} \begin{pmatrix}
0 & 0 & \ldots & 0 \\
0 & 0 & \ldots & 0 \\
\cdots & & & \\
a_1 & a_2 & \ldots & a_n
\end{pmatrix} = \begin{pmatrix}
a_1 & a_2 & \ldots & a_n \\
a_1 & a_2 & \ldots & a_n \\
\cdots & & & \\
a_1 & a_2 & \ldots & a_n
\end{pmatrix}.
\]

§ 3. Дополнение по Шуру

3.1. Согласно теореме 3.1.3

\[
\left| \begin{array}{cc}
I & A \\
A^T & I
\end{array} \right| = |I - A^T A| = (-1)^n |A^T A - I|.
\]

Остаётся воспользоваться результатом задачи 2.1 при \(\lambda = -1\), а затем результатом задачи 2.4.

3.2. Рассмотрим матрицу \(X = \begin{pmatrix} I_n & A \\ B & I_m \end{pmatrix}\). Согласно теореме 3.1.1

\[
|X| = |I_n| \cdot |I_m - BI_n^{-1}A| = |I_m - BA|,
\]

а согласно теореме 3.1.2 \(|X| = |I_n - AB|\).

3.3. Ясно, что

\[
\begin{pmatrix}
A_{11} & A_{12} \\
A_{21} & A_{22}
\end{pmatrix}
\begin{pmatrix}
I_m & A'_{12} \\
0 & A'_{22}
\end{pmatrix} =
\begin{pmatrix}
A_{11} & 0 \\
A_{21} & I_n
\end{pmatrix},
\]

поэтому \(\det A \det A'_{22} = \det A_{11}\).

3.4. Поменяем местами первый и последний столбец матрицы \(A_n\), затем второй и предпоследний и т. д. В результате получим матрицу \(A'_n\), причём \(|A_n| = \varepsilon |A'_n|\), где \(\varepsilon = (-1)^{n(n-1)/2}\). Преобразуем матрицу \(A'_n\) следующим образом. Вычтем первый столбец из второго, ..., \((n-1)\)-й из \(n\)-го; затем вычтем первую строку из второй, ..., \((n-1)\)-ю из \(n\)-й. В результате получим матрицу вида \(\begin{pmatrix} a & -u \\ v & B \end{pmatrix}\), где \(a = (n^2 - n + 2)/2\), \(u\) — строка \((n-1, n-2, \ldots, 3, 2, 1)\); \(v\) — столбец \((n, n-1, \ldots, 4, 3, 2)\); \(B\) — кососимметричная матрица