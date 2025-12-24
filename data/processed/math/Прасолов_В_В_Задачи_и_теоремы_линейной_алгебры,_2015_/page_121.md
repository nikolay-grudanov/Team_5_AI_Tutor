---
source_image: page_121.png
page_number: 121
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.25
tokens: 6315
characters: 1990
timestamp: 2025-12-24T08:10:41.199392
finish_reason: stop
---

поэтому \( \overrightarrow{A_0 X} = \sum_{i=1}^n \lambda_i e_i \), где числа \( \lambda_1, \ldots, \lambda_n \) определены однозначно.
Точка \( X \) является центром масс точек \( A_0, \ldots, A_n \) с массами 1 — \( \lambda_i, \lambda_1, \ldots, \lambda_n \) (или с массами, пропорциональными им). Барицентрические координаты, сумма которых равны 1, называют абсолютными. Для абсолютных барицентрических координат мы будем использовать обозначение \( (x_0, \ldots, x_n) \).

**Теорема 5.10.1.** *Точки \( B_0, \ldots, B_n \) лежат в одной гиперплоскости тогда и только тогда, когда матрица*

\[
\begin{pmatrix}
x_0^0 & x_1^0 & \ldots & x_n^0 \\
\ldots & \ldots & \ldots & \ldots \\
x_0^n & x_1^n & \ldots & x_n^n
\end{pmatrix},
\]

*составленная из их барицентрических координат, вырожденная.*

**Доказательство.** Можно считать, что барицентрические координаты абсолютные. Определитель матрицы не изменится, если к первому столбцу прибавить сумму всех остальных. В результате мы получим матрицу

\[
\begin{pmatrix}
1 & x_1^0 & \ldots & x_n^0 \\
\ldots & \ldots & \ldots & \ldots \\
1 & x_1^n & \ldots & x_n^n
\end{pmatrix}.
\]

Вычтем теперь первую строку из всех остальных. Определитель при этом не изменится, а матрица примет вид

\[
\begin{pmatrix}
1 & x_1^0 & \ldots & x_n^0 \\
0 & x_1^1 - x_1^0 & \ldots & x_n^1 - x_n^0 \\
\ldots & \ldots & \ldots & \ldots \\
0 & x_1^n - x_1^0 & \ldots & x_n^n - x_n^0
\end{pmatrix}.
\]

Её определитель равен определителю матрицы

\[
\begin{pmatrix}
x_1^1 - x_1^0 & \ldots & x_n^1 - x_n^0 \\
\ldots & \ldots & \ldots \\
x_1^n - x_1^0 & \ldots & x_n^n - x_n^0
\end{pmatrix}.
\]

Эта матрица состоит из координат векторов \( \overrightarrow{B_0 B_1}, \ldots, \overrightarrow{B_0 B_n} \) относительно базиса \( \overrightarrow{A_0 A_1}, \ldots, \overrightarrow{A_0 A_n} \). Её невырожденность эквивалентна линейной независимости этих векторов, что, в свою очередь, эквивалентно тому, что точки \( B_0, \ldots, B_n \) не лежат в одной гиперплоскости. □