---
source_image: page_689.png
page_number: 689
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.08
tokens: 11502
characters: 1585
timestamp: 2025-12-24T06:52:45.318788
finish_reason: stop
---

Глава 31 Матрицы и действия с ними

если левая часть близка к правой, уже хорошо. Как поступать с такой системой?

Пусть \( A \) — матрица значений базисных функций в заданных точках:

\[
A = \begin{pmatrix}
f_1(x_1) & f_2(x_1) & \ldots & f_n(x_1) \\
f_1(x_2) & f_2(x_2) & \ldots & f_n(x_2) \\
\vdots & \vdots & \ddots & \vdots \\
f_1(x_m) & f_2(x_m) & \ldots & f_n(x_m)
\end{pmatrix},
\]

а \( c \) — вектор из \( n \) искомых коэффициентов: \( c = (c_k) \). Тогда

\[
Ac = \begin{pmatrix}
f_1(x_1) & f_2(x_1) & \ldots & f_n(x_1) \\
f_1(x_2) & f_2(x_2) & \ldots & f_n(x_2) \\
\vdots & \vdots & \ddots & \vdots \\
f_1(x_m) & f_2(x_m) & \ldots & f_n(x_m)
\end{pmatrix} \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_n \end{pmatrix}
= \begin{pmatrix} F(x_1) \\ F(x_2) \\ \vdots \\ F(x_m) \end{pmatrix}
\]

будет вектором из \( m \) значений, через которые проходит кривая.

Мы хотим, чтобы вектор невязки (approximation error)

\[
\eta = Ac - y,
\]

(размера \( m \)) был как можно меньше. Здесь "меньше" мы понимаем как "короче", вычисляя длину по формуле

\[
\|\eta\| = \left( \sum_{i=1}^m \eta_i^2 \right)^{1/2}
\]

(евклидова норма). Другими словами, мы хотим, чтобы сумма квадратов невязок была минимальной, отсюда и название метод наименьших квадратов (least squares). Как учат в курсе анализа, для поиска минимума надо продифференцировать

\[
\|\eta\|^2 = \|Ac - y\|^2 = \sum_{i=1}^n \left( \sum_{j=1}^n a_{ij} c_j - y_i \right)^2
\]

по всем переменным \( c_k \)

\[
\frac{\partial \|\eta\|^2}{\partial c_k} = \sum_{i=1}^n 2 \left( \sum_{j=1}^n a_{ij} c_j - y_i \right) a_{ik} = 0.
\]