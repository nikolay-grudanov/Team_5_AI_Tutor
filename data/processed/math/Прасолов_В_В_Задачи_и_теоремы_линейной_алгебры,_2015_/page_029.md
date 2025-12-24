---
source_image: page_029.png
page_number: 29
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.03
tokens: 6192
characters: 1527
timestamp: 2025-12-24T08:08:15.479252
finish_reason: stop
---

Доказательство. Для наглядности доказательство проведём при \( n = 2 \) и укажем, какие изменения нужно сделать в общем случае. Разложение в ряд Тейлора позволяет записать матрицу \( \| c_{ij} \|_0^n \) в виде произведения двух матриц

\[
\begin{pmatrix}
f''(x)/2 & f'(x) & f(x) \\
f''(x+h)/2 & f'(x+h) & f(x+h) \\
f''(x+2h)/2 & f'(x+2h) & f(x+2h)
\end{pmatrix}
\begin{pmatrix}
0 & h^2 & (2h)^2 \\
0 & h & 2h \\
1 & 1 & 1
\end{pmatrix}.
\]

Первую из этих матриц тоже можно представить в виде произведения двух матриц

\[
\begin{pmatrix}
1 & x & x^2 \\
1 & x+h & (x+h)^2 \\
1 & x+2h & (x+2h)^2
\end{pmatrix}
\begin{pmatrix}
a_0 & a_1 & a_2 \\
0 & 2a_0 & a_1 \\
0 & 0 & a_0
\end{pmatrix}.
\]

В общем случае элементы второй матрицы имеют вид

\[
a_{ij} = a_{j-i} \binom{n+j-i}{i}.
\]

Для диагональных элементов (а нас интересуют только они) это следует из того, что \( \frac{1}{k!}(a_0 x^n)^{(k)} = \binom{n}{k} a_0 x^{n-k} \).

Таким образом,

\[
|c_{ij}|_0^n = a_0^{n-1} \left( \binom{n}{0} \binom{n}{1} \cdots \binom{n}{n} \right) V(nh, (n-1)h, \ldots, 0) \times
\]
\[
\times V(x, x+h, \ldots, x+nh) = \frac{a_0^{n+1} (n!)^{n+1}}{(n! (n-1)! \ldots 1!)^2} \div_{i>k} h^2 (k-i)(i-k).
\]

Остаётся заметить, что \( n! (n-1)! \ldots 1! = \div_{0 \leq k < i \leq n} (i-k) \). □

1.8. Определитель Коши

Определитель матрицы \( \| a_{ij} \|_1^n \), где \( a_{ij} = \frac{1}{x_i + y_j} \), называют определителем Коши.

Теорема 1.8.1. Определитель Коши равен

\[
\frac{\div_{i>j} (x_i - x_j)(y_i - y_j)}{\div_{i,j} (x_i + y_j)}.
\]