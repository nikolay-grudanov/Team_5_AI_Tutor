---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.54
tokens: 6160
characters: 1484
timestamp: 2025-12-24T08:08:58.707051
finish_reason: stop
---

2.15. Докажите, что площадь треугольника, образованного прямыми \(a_i x + b_i y = c_i,\ i = 1, 2, 3\), равна

\[
\pm \frac{1}{2} \left| \begin{array}{ccc}
a_1 & b_1 & c_1 \\
a_2 & b_2 & c_2 \\
a_3 & b_3 & c_3
\end{array} \right|^2
\]

\[
\pm \frac{1}{2} \left| \begin{array}{cc}
a_1 & b_1 \\
a_2 & b_2
\end{array} \right| \cdot \left| \begin{array}{cc}
a_2 & b_2 \\
a_3 & b_3
\end{array} \right| \cdot \left| \begin{array}{cc}
a_3 & b_3 \\
a_1 & b_1
\end{array} \right|.
\]

2.16. Пусть \( \varepsilon \) — первообразный корень \( n \)-й степени из 1; \( A = \| a_{ij} \|_1^n \), где \( a_{ij} = \varepsilon^{ij} \). Вычислите матрицу \( A^{-1} \).

2.17. Вычислите матрицу, обратную к матрице Вандермонда.

2.18. Вычислите матрицу, обратную матрице Коши \( \| a_{ij} \|_1^n \), где \( a_{ij} = (x_i + y_j)^{-1} \).

2.19. Вычислите матрицу, присоединённую к матрице

\[
A = \begin{pmatrix}
1 & -1 \\
\vdots & \vdots \\
1 & -1 \\
0 & \ldots & 0 & 0
\end{pmatrix}.
\]

2.20. Сумма элементов каждой строки квадратной матрицы \( A \) равна 0. Докажите, что каждый столбец матрицы \( \operatorname{adj} A \) состоит из равных чисел.

§ 3. Дополнение по Шуру

3.1. Определитель блочной матрицы

Квадратную матрицу \( X \) можно записать в блочном виде:

\[
X = \begin{pmatrix} A & B \\ C & D \end{pmatrix},
\]

где \( A \) и \( D \) — квадратные матрицы, сумма порядков которых равна порядку матрицы \( X \).

Теорема 3.1.1. Если \( |A| \neq 0 \), то

\[
|X| = |A| \cdot |D - CA^{-1}B|.
\]