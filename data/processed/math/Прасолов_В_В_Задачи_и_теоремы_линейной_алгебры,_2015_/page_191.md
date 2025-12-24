---
source_image: page_191.png
page_number: 191
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.53
tokens: 6590
characters: 2623
timestamp: 2025-12-24T08:12:46.401116
finish_reason: stop
---

казать, что любая точка \( X \) прямой \( PA_0 \) имеет барицентрические координаты вида \( (\alpha : x_1 : \ldots : x_n) \). Для этого достаточно заметить, что

\[
\overrightarrow{A_0X} = \lambda \overrightarrow{A_0P} = \lambda x_1 \overrightarrow{A_0A_1} + \ldots + \lambda x_n \overrightarrow{A_0A_n}.
\]

5.7. Достаточно заметить, что если \( X \) — точка прямой \( AB \), а \( O \) — произвольная точка, то \( \overrightarrow{OX} = \lambda \overrightarrow{OA} + (1 - \lambda) \overrightarrow{OB} \) для некоторого \( \lambda \).

5.8. Воспользуемся результатом задачи 5.7. Бесконечно удалённая точка получается при \( \lambda \to \infty \). При этом мы получаем барицентрические координаты \( (a_0 - b_0 : \ldots : a_n - b_n) \). Остаётся заметить, что \( \bullet a_i = \bullet b_i = 1 \).

5.9. Центром масс точек \( B_0 = \bullet y_i^0 A_i, \ldots, B_n = \bullet y_i^n A_i \) с массами \( t_0, \ldots, t_n \) является точка

\[
t_0 \bullet y_i^0 A_i + \ldots + t_n \bullet y_i^n A_i = (t_0 y_0^0 + \ldots + t_n y_0^n) A_0 + \ldots + (t_0 y_n^0 + \ldots + t_n y_n^n) A_n.
\]

Поэтому \( (t_0 : \ldots : t_n) \) — барицентрические координаты точки \( X \) относительно точек \( B_0, \ldots, B_n \), если

\[
(t_0, \ldots, t_n) \begin{pmatrix}
y_0^0 & \ldots & y_n^0 \\
\cdots & \cdots & \cdots \\
y_0^n & \ldots & y_n^n
\end{pmatrix} = (x_0, \ldots, x_n),
\]

т. е.

\[
(t_0, \ldots, t_n) = (x_0, \ldots, x_n) \begin{pmatrix}
y_0^0 & \ldots & y_n^0 \\
\cdots & \cdots & \cdots \\
y_0^n & \ldots & y_n^n
\end{pmatrix}^{-1}.
\]

5.10. Отношение ориентированных объёмов симплексов \( P_0 \ldots P_n \) и \( A_0 \ldots A_n \) равно определителю матрицы, составленной из координат векторов \( \overrightarrow{P_0P_1}, \ldots, \overrightarrow{P_0P_n} \) относительно базиса \( \overrightarrow{A_0A_1}, \ldots, \overrightarrow{A_0A_n} \). При доказательстве теоремы 5.10.1 было доказано, что определитель этой матрицы равен указанному определителю.

5.11. Задачу а) можно получить из задачи б) при \( r = 0 \), поэтому решим сразу задачу б). Параллельные прямые проходят через бесконечно удалённую точку \( P \) с барицентрическими координатами \( (x_0 : x_1 : \ldots : x_n) \), сумма которых равна нулю (задача 5.8). Для бесконечно удалённой точки \( P \) результат задачи 5.6 остаётся в силе, поэтому точка \( B_i \) имеет барицентрические координаты \( (x_0 : \ldots : 0 : \ldots : x_n) \), где 0 стоит на \( i \)-м месте. Учитывая, что \( x_0 + \ldots + x_n = 0 \), получаем, что абсолютные барицентрические координаты точки \( B_i \) равны

\[
\left( -\frac{x_0}{x_i} : \ldots : 0 : \ldots : -\frac{x_n}{x_i} \right).
\]