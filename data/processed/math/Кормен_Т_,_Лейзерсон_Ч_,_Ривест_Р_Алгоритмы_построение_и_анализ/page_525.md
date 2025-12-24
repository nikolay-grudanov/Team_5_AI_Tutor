---
source_image: page_525.png
page_number: 525
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.62
tokens: 11484
characters: 1644
timestamp: 2025-12-24T06:45:02.706317
finish_reason: stop
---

Чтобы увидеть аналогию этой процедуры с процессом умножения матриц, запишем процедуру умножения матриц \( A \) и \( B \) размером \( n \times n \) по формуле

\[
c_{ij} = \sum_{k=1}^{n} a_{ik} \cdot b_{kj}
\]

{\sc Matrix-Multiply}$(A,B)$\\
\verb|1 |$n \leftarrow rows[A]|\\
\verb|2 |пусть $C=(c_{ij})$ --- $n\times n$-матрица
\verb|3 |for $i \leftarrow 1$ to $n$\\
\verb|4 |do for $j \leftarrow 1$ to $n$\\
\verb|5 |do $c_{ij} \leftarrow 0$\\
\verb|6 |for $k \leftarrow 1$ to $n$\\
\verb|7 |do $c_{ij} \leftarrow c_{ij}+a_{ik}\cdot b_{kj}$\\
\verb|8 |return $C$

Видно, что эта процедура получается из предыдущей заменами

\[
\begin{array}{ll}
d^{(m-1)} & \rightarrow a, \\
w & \rightarrow b, \\
d^{(m)} & \rightarrow c, \\
\min & \rightarrow +, \\
+ & \rightarrow .
\end{array}
\]

При этом символу \( \infty \), являющемуся нейтральным элементом для операции \( \min \) (в том смысле, что \( \min(\infty, a) = a \), соответствует число 0, являющееся нейтральным элементов для операции \( + \) (\( 0 + a = a \)).

С точки зрения этой аналогии, мы как бы вычисляем "произведение" \( n-1 \) экземпляров матрицы \( W \) с помощью последовательных умножений:

\[
\begin{align*}
D^{(1)} &= D^{(0)} \cdot W = W, \\
D^{(2)} &= D^{(1)} \cdot W = W^2, \\
D^{(3)} &= D^{(2)} \cdot W = W^3, \\
&\vdots \\
D^{(n-1)} &= D^{(n-2)} \cdot W = W^{n-1}.
\end{align*}
\]

Результат этих "умножений", матрица \( D^{(n-1)} = W^{n-1} \) содержит веса кратчайших путей. Оформим описанное вычисление в виде процедуры (с временем работы \( \Theta(n^4) \)):

{\sc Slow-All-Paths-Shortest-Paths}$(W)$\\
\verb|1 |$n \leftarrow rows[W]|\\
\verb|2 |$D^{(1)} \leftarrow W|$