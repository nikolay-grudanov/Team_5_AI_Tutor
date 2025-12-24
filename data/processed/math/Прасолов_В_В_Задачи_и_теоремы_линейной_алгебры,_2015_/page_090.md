---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.57
tokens: 6465
characters: 2032
timestamp: 2025-12-24T08:09:53.065936
finish_reason: stop
---

1.20. Ясно, что \( \binom{x}{k} = \frac{x^k}{k!} + \sum_{i=0}^{k-1} c_i x^i \). Поэтому исходный определитель равен

\[
\begin{vmatrix}
1 & x_1 & x_1^2/2! & \ldots & x_1^{n-1}/(n-1)! \\
1 & x_2 & x_2^2/2! & \ldots & x_2^{n-1}/(n-1)! \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & x_n & x_n^2/2! & \ldots & x_n^{n-1}/(n-1)!
\end{vmatrix}
= \frac{1}{2! \ 3! \ldots (n-1)!} \prod_{1 \leq i < j \leq n} (x_j - x_i).
\]

Кроме того, \( 2! \ 3! \ldots (n-1)! = \prod_{1 \leq i < j \leq n} (j - i) \).

1.21. Пусть \( x_i = in \). Тогда

\[
a_{i1} = x_i, \quad a_{i2} = \frac{x_i(x_i-1)}{2}, \ldots, \quad a_{ir} = \frac{x_i(x_i-1)\ldots(x_i-r+1)}{r!},
\]

т. е. в \( k \)-м столбце стоят одинаковые многочлены \( k \)-й степени от \( x \). Так как определитель не изменяется при прибавлении к его столбцам линейных комбинаций других столбцов, то его можно привести к виду \( |b_{ik}|_1^r \), где \( b_{ik} = \frac{x_i^k}{k!} = \frac{n^k}{k!} i^k \). Поделив \( k \)-ю строку на \( k \frac{n^k}{k!} \) для всех \( k = 1, \ldots, r \), получим определитель Вандермонда. Следовательно,

\[
|a_{ik}|_1^r = |b_{ik}|_1^r = n \frac{n^2}{2!} \ldots \frac{n^r}{r!} r! \ V(1, 2, \ldots, r) = n^{r(r+1)/2},
\]

так как \( \prod_{1 \leq j < i \leq r} (i - j) = 2! \ 3! \ldots (r-1)! \).

Замечание. По поводу другого решения этой задачи см. следствие 1 теоремы 1.14.1.

1.22. Как видно из решения задачи 1.20, рассматриваемое произведение равно

\[
\begin{vmatrix}
1 & \binom{x_1}{1} & \ldots & \binom{x_1}{n-1} \\
1 & \binom{x_2}{1} & \ldots & \binom{x_2}{n-1} \\
\ldots & \ldots & \ldots & \ldots \\
1 & \binom{x_n}{1} & \ldots & \binom{x_n}{n-1}
\end{vmatrix},
\]

где \( \binom{x}{k} = \frac{x(x-1)\ldots(x-k+1)}{k!} \). Индукцией по \( k \) легко доказать, что число \( \binom{x}{k} \) целое для всех целых \( x \). Действительно, \( \binom{x}{1} = x \). Кроме того,

\[
\binom{x+1}{k+1} - \binom{x}{k+1} = \binom{x}{k}
\]

и \( \binom{0}{k+1} = 0 \). Ясно также, что определитель матрицы с целочисленными элементами является целым числом.