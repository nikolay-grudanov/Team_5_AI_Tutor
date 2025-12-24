---
source_image: page_022.png
page_number: 22
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.27
tokens: 6664
characters: 2678
timestamp: 2025-12-24T08:08:11.747009
finish_reason: stop
---

(a) Определитель линейно зависит от каждого столбца, т. е.

\[
\begin{vmatrix}
a_{11} & \ldots & \lambda a_{1i} + \mu \beta_{1i} & \ldots & a_{1n} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
a_{n1} & \ldots & \lambda a_{ni} + \mu \beta_{ni} & \ldots & a_{nn}
\end{vmatrix} =
\]

\[
= \lambda \begin{vmatrix}
a_{11} & \ldots & a_{1i} & \ldots & a_{1n} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
a_{n1} & \ldots & a_{ni} & \ldots & a_{nn}
\end{vmatrix} + \mu \begin{vmatrix}
a_{11} & \ldots & \beta_{1i} & \ldots & a_{1n} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
a_{n1} & \ldots & \beta_{ni} & \ldots & a_{nn}
\end{vmatrix}.
\]

(b) Определитель матрицы с двумя одинаковыми столбцами равен 0.

(c) Определитель единичной матрицы \( I_n \) равен 1.

Нужно доказать, что такая функция det существует и единственна. Для этого нам понадобится ещё одно свойство определителя:

(b') При перестановке двух столбцов определитель меняет знак.

Чтобы доказать это свойство, фиксируем в матрице все столбцы, кроме двух столбцов с номерами \( i \) и \( j \), и будем рассматривать определитель матрицы как функцию \( f(u, v) \) этих двух столбцов. Тогда из свойств (a) и (b) следует, что \( 0 = f(u + v, u + v) = f(u, u) + f(v, u) + f(u, v) + f(v, v) = f(v, u) + f(u, v) \).

Замечание. Для матриц с элементами из поля характеристики 2 свойство (b) не следует из свойства (b').

Свойства (a), (b) и (c) позволяют вычислить определитель матрицы. Покажем это на примере матриц порядка 2. Запишем первый столбец \( \begin{pmatrix} a_{11} \\ a_{21} \end{pmatrix} \) в виде \( \begin{pmatrix} a_{11} \cdot 1 + 0 \\ 0 + a_{21} \cdot 1 \end{pmatrix} \) и воспользуемся свойством (a):

\[
\begin{vmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{vmatrix} = a_{11} \begin{vmatrix} 1 & a_{12} \\ 0 & a_{22} \end{vmatrix} + a_{21} \begin{vmatrix} 0 & a_{12} \\ 1 & a_{22} \end{vmatrix}.
\]

Затем в каждой из полученных матриц проделаем то же самое со вторым столбцом:

\[
\begin{vmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{vmatrix} = a_{11} a_{12} \begin{vmatrix} 1 & 1 \\ 0 & 0 \end{vmatrix} + a_{11} a_{22} \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} + a_{21} a_{12} \begin{vmatrix} 0 & 1 \\ 1 & 0 \end{vmatrix} + a_{21} a_{22} \begin{vmatrix} 0 & 0 \\ 1 & 1 \end{vmatrix}.
\]

Согласно свойству (b) определитель матрицы с одинаковыми столбцами равен 0, поэтому остается лишь вычислить определители \( \begin{vmatrix} 1 & 0 \\ 0 & 1 \end{vmatrix} \) и \( \begin{vmatrix} 0 & 1 \\ 1 & 0 \end{vmatrix} \). Для этого воспользуемся свойствами (b') и (c). В результате получим

\[
\begin{vmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{vmatrix} = a_{11} a_{22} - a_{21} a_{12}.
\]