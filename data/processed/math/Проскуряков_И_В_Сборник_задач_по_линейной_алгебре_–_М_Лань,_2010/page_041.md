---
source_image: page_041.png
page_number: 41
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.92
tokens: 5356
characters: 1540
timestamp: 2025-12-24T07:06:23.895675
finish_reason: stop
---

В первом определителе последний столбец вычтем из остальных, а второй определитель разложим по последнему столбцу:

\[
D_n = x(a_1 - x)(a_2 - x) \ldots (a_{n-1} - x) + (a_n - x)D_{n-1}.
\]

Это и есть рекуррентное соотношение. Вставляя в него аналогичное выражение для \( D_{n-1} \), найдем

\[
\begin{align*}
D_n &= x(a_1 - x)(a_2 - x) \ldots (a_{n-1} - x) + \\
&\quad + x(a_1 - x)(a_2 - x) \ldots (a_{n-2} - x)(a_n - x) + \\
&\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad + D_{n-2}(a_{n-1} - x)(a_n - x).
\end{align*}
\]

Повторяя то же рассуждение \( n-1 \) раз и замечая, что \( D_1 = a_1 = x + (a_1 - x) \), получим

\[
\begin{align*}
D &= x(a_1 - x)(a_2 - x) \ldots (a_{n-1} - x) + x(a_1 - x) \ldots (a_{n-2} - x)(a_n - x) + \ldots \\
&\quad \cdots + x(a_2 - x) \ldots (a_n - x) + (a_1 - x)(a_2 - x) \ldots (a_n - x) = \\
&= x(a_1 - x)(a_2 - x) \ldots (a_n - x) \left( \frac{1}{x} + \frac{1}{a_1 - x} + \cdots + \frac{1}{a_n - x} \right),
\end{align*}
\]

что совпадает с результатом примера 2.

Пример 6: Вычислить определитель порядка \( n \):

\[
D_n = \begin{vmatrix}
5 & 3 & 0 & 0 & \ldots & 0 & 0 \\
2 & 5 & 3 & 0 & \ldots & 0 & 0 \\
0 & 2 & 5 & 3 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & 0 & \ldots & 2 & 5
\end{vmatrix}.
\]

Разлагая по первой строке, найдем рекуррентное соотношение

\[
D_n = 5D_{n-1} - 6D_{n-2}.
\]

Уравнение \( x^2 - 5x + 6 = 0 \) имеет корни \( \alpha = 2, \beta = 3 \).
По формуле (4)

\[
D_n = C_1 \alpha^n + C_2 \beta^n = 3^{n+1} - 2^{n+1}.
\]