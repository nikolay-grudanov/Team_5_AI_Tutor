---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.70
tokens: 6467
characters: 2061
timestamp: 2025-12-24T08:09:53.005636
finish_reason: stop
---

1.17. Добавим к матрице \( V \) сначала \((n + 1)\)-й столбец, состоящий из \( n \)-х степеней, а потом добавим первую строку \((1, -x, x^2, \ldots, (-x)^n)\). Полученная матрица \( W \) снова является матрицей Вандермонда, поэтому

\[
\det W = (x + x_1) \ldots (x + x_n) \det V = (\sigma_n + \sigma_{n-1} x + \ldots + \sigma_1 x^{n-1} + x^n) \det V.
\]

С другой стороны, разложив определитель матрицы \( W \) по первой строке, получим

\[
\det W = \det V_0 + x \det V_1 + \ldots + x^{n-1} \det V_{n-1} + x^n \det V.
\]

При фиксированных \( x_1, \ldots, x_n \) получаем равенство двух многочленов от \( x \). Их коэффициенты должны быть равны, поэтому \( \det V_k = \sigma_{n-k}(x_1, \ldots, x_n) \det V \).

1.18. Точно такие же рассуждения, как и при втором доказательстве теоремы 1.5.1, показывают, что искомый определитель равен \( a_1 \ldots a_n \frac{1}{(x_i - x_j)} \).

1.19. а) Ясно, что

\[
f'(x_i) = (x_i - x_1) \ldots (x_i - x_{i-1})(x_i - x_{i+1}) \ldots (x_i - x_n) =
\]
\[
= (-1)^{n-i} (x_i - x_1) \ldots (x_i - x_{i-1})(x_{i+1} - x_i) \ldots (x_n - x_i) =
\]
\[
= (-1)^{n-i} \frac{\prod_{j > k} (x_j - x_k)}{\prod_{j > k, j \neq i} (x_j - x_k)} = (-1)^{n-i} \frac{V(x_1, \ldots, x_n)}{V(x_1, \ldots, \hat{x}_i, \ldots, x_n)}.
\]

б) Согласно а) получаем

\[
\bullet \sum_{i=1}^n \frac{x_i^k}{f'(x_i)} = \bullet \sum_{i=1}^n (-1)^{n-i} x_i^k \left[ \frac{V(x_1, \ldots, x_n)}{V(x_1, \ldots, \hat{x}_i, \ldots, x_n)} \right]^{-1} =
\]
\[
= \frac{(-1)^{n-1}}{V(x_1, \ldots, x_n)} \bullet \sum_{i=1}^n (-1)^{i-1} x_i^k V(x_1, \ldots, \hat{x}_i, \ldots, x_n) =
\]
\[
= \frac{(-1)^{n-1}}{V(x_1, \ldots, x_n)} (-1)^{n-1} \begin{vmatrix}
1 & x_1 & \ldots & x_1^{n-2} & x_1^k \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
1 & x_n & \ldots & x_n^{n-2} & x_n^k
\end{vmatrix}.
\]

При записи последнего равенства мы воспользовались разложением определителя по последнему столбцу.

в) Воспользуемся формулой б). Если \( 0 \leq k \leq n-2 \), то мы получаем определитель с двумя одинаковыми столбцами. При \( k = n-1 \) получаем определитель Вандермонда.