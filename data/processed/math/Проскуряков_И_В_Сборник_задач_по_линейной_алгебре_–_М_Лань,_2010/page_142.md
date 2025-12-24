---
source_image: page_142.png
page_number: 142
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.27
tokens: 5588
characters: 2065
timestamp: 2025-12-24T07:08:38.857285
finish_reason: stop
---

856. Показать, что вычисление матрицы, обратной к данной матрице порядка \( n \), можно свести к решению \( n \) систем линейных уравнений, каждая из которых содержит \( n \) уравнений с \( n \) неизвестными и имеет матрицей коэффициентов при неизвестных матрицу \( A \).

Пользуясь методом задачи 856, найти обратные матрицы для следующих матриц:

857.
\[
\begin{pmatrix}
3 & 3 & -4 & -3 \\
0 & 6 & 1 & 1 \\
5 & 4 & 2 & 1 \\
2 & 3 & 3 & 2
\end{pmatrix}.
\]

*858.
\[
\begin{pmatrix}
1 & 2 & 3 & \ldots & n-1 & n \\
n & 1 & 2 & \ldots & n-2 & n-1 \\
n-1 & n & 1 & \ldots & n-3 & n-2 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
2 & 3 & 4 & \ldots & n & 1
\end{pmatrix}.
\]

859.
\[
\begin{pmatrix}
a & a+h & a+2h & \ldots & a+(n-2)h & a+(n-1)h \\
a+(n-1)h & a & a+h & \ldots & a+(n-3)h & a+(n-2)h \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
a+h & a+2h & a+3h & \ldots & a+(n-1)h & a
\end{pmatrix}.
\]

*860.
\[
\begin{pmatrix}
1 & 1 & 1 & 1 & \ldots & 1 \\
1 & \varepsilon & \varepsilon^2 & \varepsilon^3 & \ldots & \varepsilon^{n-1} \\
1 & \varepsilon^2 & \varepsilon^4 & \varepsilon^6 & \ldots & \varepsilon^{2(n-1)} \\
1 & \varepsilon^3 & \varepsilon^6 & \varepsilon^9 & \ldots & \varepsilon^{3(n-1)} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
1 & \varepsilon^{n-1} & \varepsilon^{2(n-1)} & \varepsilon^{3(n-1)} & \ldots & \varepsilon^{(n-1)^2}
\end{pmatrix},
\]
где \( \varepsilon = \cos \frac{2\pi}{n} + i \sin \frac{2\pi}{n} \).

Решить матричные уравнения:

861. \( \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \cdot X = \begin{pmatrix} 3 & 5 \\ 5 & 9 \end{pmatrix} \).

862. \( X \cdot \begin{pmatrix} 3 & -2 \\ 5 & -4 \end{pmatrix} = \begin{pmatrix} -1 & 2 \\ -5 & 6 \end{pmatrix} \).

863. \( \begin{pmatrix} 3 & -1 \\ 5 & -2 \end{pmatrix} \cdot X \cdot \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 14 & 16 \\ 9 & 10 \end{pmatrix} \).

864. \( \begin{pmatrix} 1 & 2 & -3 \\ 3 & 2 & -4 \\ 2 & -1 & 0 \end{pmatrix} \cdot X = \begin{pmatrix} 1 & -3 & 0 \\ 10 & 2 & 7 \\ 10 & 7 & 8 \end{pmatrix} \).