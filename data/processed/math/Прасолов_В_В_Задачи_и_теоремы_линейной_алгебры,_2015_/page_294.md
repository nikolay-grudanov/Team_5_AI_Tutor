---
source_image: page_294.png
page_number: 294
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.70
tokens: 6577
characters: 2331
timestamp: 2025-12-24T08:15:31.865621
finish_reason: stop
---

Ясно, что \(2 \sum_{i<j} x_i x_j \leq \sum_i x_i^2\). Поэтому если \(-1 < \lambda < 1\) и \(\sum_i x_i^2 \neq 0\), то
\[
\left| 2\lambda \sum_{i<j} x_i x_j \right| < \sum_i x_i^2.
\]
Следовательно, \(f(x, x) = \sum_i x_i^2 + 2\lambda \sum_{i<j} x_i x_j > 0\).

21.8. Легко проверить, что
\[
\begin{pmatrix}
A & A \\
A & A
\end{pmatrix}
\begin{pmatrix}
x \\
y
\end{pmatrix}
= (A(x+y), (x+y)) \geq 0.
\]

21.9. Рассмотрим в пространстве многочленов степени не выше \(n-1\) скалярное произведение \((f, g) = \int_0^1 f(x)g(x)\, dx\). Данная матрица является матрицей Грама системы линейно независимых векторов \(1, x, x^2, \ldots, x^{n-1}\), поэтому согласно теореме 21.1.2 эта матрица положительно определена.

21.10. Пусть \(U\) — такая ортогональная матрица, что \(U^{-1}AU = \Lambda\) и \(|U| = 1\). Сделаем замену \(x = Uy\). Тогда \((x, Ax) = (y, \Lambda y)\) и \(dx_1 \ldots dx_n = dy_1 \ldots dy_n\), так как якобиан замены переменных равен \(|U|\). Поэтому
\[
\int_{-\infty}^{+\infty} e^{-(x, Ax)}\, dx = \int_{-\infty}^{+\infty} \ldots \int_{-\infty}^{+\infty} e^{-\lambda_1 y_1^2 - \ldots - \lambda_n y_n^2}\, dy =
\]
\[
= \prod_{i=1}^n \int_{-\infty}^{+\infty} e^{-\lambda_i y_i^2}\, dy_i = \prod_{i=1}^n \sqrt{\frac{\pi}{\lambda_i}} = (\sqrt{\pi})^n |A|^{-1/2}.
\]

21.11. Ясно, что \((Be_i, e_j) = (AA^{-1}Be_i, e_j) = \lambda_i (Ae_i, e_j)\). Аналогично \((Be_j, e_i) = \lambda_j (Ae_j, e_i)\). Остаётся заметить, что \((Be_i, e_j) = (Be_j, e_i)\) и \((Ae_i, e_j) = (Ae_j, e_i)\), так как матрицы \(A\) и \(B\) симметричны.

21.12. Скалярное произведение \(i\)-й строки \(S\) на \(j\)-й столбец \(S^{-1}\) равно нулю при \(i \neq j\). Поэтому в каждом столбце \(S^{-1}\) есть положительный и отрицательный элемент, а значит, число её ненулевых элементов не менее \(2n\), а число нулевых элементов не более \(n^2 - 2n\).

Пример матрицы \(S^{-1}\), имеющей \(2n\) ненулевых элементов, выглядит следующим образом:
\[
S^{-1} = \begin{pmatrix}
1 & 1 & 1 & 1 & 1 & \ldots \\
1 & 2 & 2 & 2 & 2 & \ldots \\
1 & 2 & 1 & 1 & 1 & \ldots \\
1 & 2 & 1 & 2 & 2 & \ldots \\
1 & 2 & 1 & 2 & 1 & \ldots \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots
\end{pmatrix}^{-1} =
\begin{pmatrix}
2 & -1 \\
-1 & 0 & 1 \\
1 & 0 & -1 & 0 & \ldots \\
-1 & 0 & \ldots & 0 & -s \\
0 & \ldots & 0 & -s & s
\end{pmatrix},
\]
где \(s = (-1)^n\).