---
source_image: page_190.png
page_number: 190
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.34
tokens: 7024
characters: 3573
timestamp: 2025-12-24T08:12:56.893448
finish_reason: stop
---

Решения

§ 5. Двойственное пространство. Ортогональное дополнение

5.1. Пусть \( V \) — пространство всех матриц порядка \( n \), \( W \subset V \) — подпространство матриц с нулевым следом. Тогда \( A^T \in W^\perp \). Кроме того, \( I \in W^\perp \) и \( \dim W^\perp = 1 \). Поэтому \( A^T = \lambda I \).

5.2. Пусть \( A_1, \ldots, A_m \) и \( B_1, \ldots, B_k \) — строки матриц \( A \) и \( B \). Из равенств \( A_1 X = \ldots = A_m X = 0 \) следует, что \( B_1 X = \ldots = B_k X = 0 \), т. е. если \( X \in \langle A_1, \ldots, A_m \rangle^\perp \), то \( X \in \langle B_1, \ldots, B_k \rangle^\perp \). Поэтому \( \langle A_1, \ldots, A_m \rangle^\perp \subset \langle B_1, \ldots, B_k \rangle^\perp \), и, следовательно, \( \langle B_1, \ldots, B_k \rangle \subset \langle A_1, \ldots, A_m \rangle \). Значит, строки матрицы \( B \) являются линейными комбинациями строк матрицы \( A \), т. е. \( b_{ij} = \bullet\ c_{ip} a_{pj} \).

5.3. Пусть \( v = (a_1, \ldots, a_n) \). Если \( w = (b_1, \ldots, b_n) \) — вектор из ортанта, не содержащего ни \( v \), ни \( -v \), то \( a_i b_i > 0 \) и \( a_j b_j < 0 \) для некоторых \( i \) и \( j \). К вектору \( w \) можно прибавить вектор \( w_1 = (x_1, \ldots, x_n) \), где \( a_i x_i > 0 \) и \( a_j x_j < 0 \), а все остальные координаты равны нулю. Числа \( x_i \) и \( x_j \) можно подобрать так, что \( a_i x_i + a_j x_j = -(v, w) \), т. е. \( (v, w + w_1) = 0 \).

5.4. Точка \( X \) принадлежит прямой \( a \) тогда и только тогда, когда \( a^\perp (\overrightarrow{AX}) = 0 \), т. е. \( a^\perp (\overrightarrow{OX}) = a^\perp (\overrightarrow{OA}) \). Пусть \( X \) — точка пересечения прямых \( a \) и \( b \). Тогда \( a^\perp (\overrightarrow{OX}) = a^\perp (\overrightarrow{OA}) \) и \( b^\perp (\overrightarrow{OX}) = b^\perp (\overrightarrow{OB}) \). Поэтому \( c^\perp (\overrightarrow{OX}) = -(a^\perp + b^\perp)(\overrightarrow{OX}) = -a^\perp (\overrightarrow{OA}) - b^\perp (\overrightarrow{OB}) \). Точка \( X \) принадлежит прямой \( c \) тогда и только тогда, когда \( c^\perp (\overrightarrow{OC}) = c^\perp (\overrightarrow{OX}) = -a^\perp (\overrightarrow{OA}) - b^\perp (\overrightarrow{OB}) \).

5.5. Пусть \( B(x, y) = x^*(y) \). Рассмотрим для фиксированного \( x \) две линейные функции \( f_1(y) = x^*(y) \) и \( f_2(y) = y^*(x) \). По условию равенства \( f_1(y) = 0 \) и \( f_2(y) = 0 \) эквивалентны. Поэтому \( \mathrm{Ker}\ f_1 = \mathrm{Ker}\ f_2 \), а значит, \( B(x, y) = k(x)B(y, x) \). Докажем, что \( k(x) \) — постоянное число. С одной стороны,

\[
B(x + x', y) = x^*(y) + x'^*(y) = k(x)y^*(x) + k(x')y^*(x').
\]

С другой стороны,

\[
B(x + x', y) = k(x + x')B(y, x + x') = k(x + x')y^*(x) + k(x + x')y^*(x').
\]

Поэтому \( (k(x + x') - k(x))y^*(x) = (k(x') - k(x + x'))y^*(x') \). Если \( x' = \lambda x \), то \( k(x') = k(x) \). Поэтому можно считать, что векторы \( x' \) и \( x \) неколлинеарны. Но тогда вектор \( y \) можно подобрать так, что \( y^*(x) \neq 0 \) и \( y^*(x') = 0 \). Следовательно, \( k(x + x') = k(x) \). Таким образом, \( B(x, y) = kB(y, x) = k^2 B(x, y) \). Можно подобрать такие векторы \( x \) и \( y \), что \( B(x, y) \neq 0 \). Поэтому \( k^2 = 1 \), т. е. \( k = \pm 1 \). При \( k = 1 \) получаем симметрическую функцию, при \( k = -1 \) — кососимметрическую.

5.6. Ответ: \( (0 : x_1 : \ldots : x_n) \). Если точка лежит в гиперплоскости \( A_1 \ldots A_n \), то она имеет барицентрические координаты вида \( (0 : y_1 : \ldots : y_n) \), поскольку является центром масс точек \( A_1, \ldots, A_n \) с некоторыми массами. Остаётся до-