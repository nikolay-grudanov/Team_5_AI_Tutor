---
source_image: page_079.png
page_number: 79
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.62
tokens: 5489
characters: 1884
timestamp: 2025-12-24T07:07:12.121429
finish_reason: stop
---

* **497.** С помощью умножения определителей доказать тождество

\[
(a^3 + b^3 + c^3 - 3abc)(a'^3 + b'^3 + c'^3 - 3a'b'c') = A^3 + B^3 + C^3 - 3ABC,
\]

где \( A = aa' + bc' + cb', \ B = ac' + bb' + ca', \ C = ab' + ba' + cc' \).
Какое свойство целых чисел отсюда вытекает?

* **498.** При обозначениях предыдущей задачи доказать тождество:

\[
(a^2 + b^2 + c^2 - ab - ac - bc)(a'^2 + b'^2 + c'^2 - a'b' - a'c' - b'c') =
= A^2 + B^2 + C^2 - AB - AC - BC.
\]

* **499.** Доказать следующее обобщение теоремы об умножении определителей. Пусть даны две матрицы

\[
A = \begin{pmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\ldots & \ldots & \ldots & \ldots \\
a_{m1} & a_{m2} & \ldots & a_{mn}
\end{pmatrix}
\]
и
\[
B = \begin{pmatrix}
b_{11} & b_{12} & \ldots & b_{1n} \\
b_{21} & b_{22} & \ldots & b_{2n} \\
\ldots & \ldots & \ldots & \ldots \\
b_{m1} & b_{m2} & \ldots & b_{mn}
\end{pmatrix},
\]

каждая из \( m \) строк и \( n \) столбцов.

Комбинируя строки одной матрицы со строками другой, полагая \( c_{ij} = \sum_{k=1}^n a_{ik} b_{jk} \), составим определитель \( m \)-го порядка

\[
D = \begin{vmatrix}
c_{11} & c_{12} & \ldots & c_{1m} \\
c_{21} & c_{22} & \ldots & c_{2m} \\
\ldots & \ldots & \ldots & \ldots \\
c_{m1} & c_{m2} & \ldots & c_{mm}
\end{vmatrix}.
\]

Далее обозначим через \( A_{i_1, i_2, \ldots, i_m} \) и \( B_{i_1, i_2, \ldots, i_m} \) соответственно миноры \( m \)-го порядка матриц \( A \) и \( B \), составленные из столбцов этих матриц с номерами \( i_1, i_2, \ldots, i_m \) в том же порядке.
Тогда

\[
D = \sum_{1 \leq i_1 < i_2 < \cdots < i_m \leq n} A_{i_1, i_2, \ldots, i_m} B_{i_1, i_2, \ldots, i_m}
\]

при \( m \leq n \) (формула Бинэ–Коши), т. е. определитель \( D \) равен сумме произведений всех миноров порядка \( m \) матрицы \( A \) на соответствующие миноры матрицы \( B \). При \( m > n \)

\[
D = 0.
\]