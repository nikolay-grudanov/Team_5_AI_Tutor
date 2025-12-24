---
source_image: page_016.png
page_number: 16
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.93
tokens: 6235
characters: 1695
timestamp: 2025-12-24T08:07:54.031068
finish_reason: stop
---

\[
A^* = (\bar{A})^T.
\]
\[
\sigma = \begin{pmatrix} 1 & \ldots & n \\ k_1 & \ldots & k_n \end{pmatrix}
\] перестановка (подстановка); \( \sigma(i) = k_i \); для краткости иногда обозначается \( (k_1, \ldots, k_n) \).
\[
(-1)^{\sigma} =
\begin{cases}
1, & \text{если перестановка } \sigma \text{ чётная;} \\
-1, & \text{если перестановка } \sigma \text{ нечётная.}
\end{cases}
\]
\[
\langle e_1, \ldots, e_n \rangle
\] линейное пространство, порождённое векторами \( e_1, \ldots, e_n \).

Если в пространствах \( V^n \) и \( W^m \) заданы базисы \( e_1, \ldots, e_n \) и \( \varepsilon_1, \ldots, \varepsilon_m \), то матрице \( A \) соответствует линейное отображение \( A : V^n \to W^m \), переводящее вектор
\[
\begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}
\] в вектор
\[
\begin{pmatrix} y_1 \\ \vdots \\ y_m \end{pmatrix} = \begin{pmatrix} a_{11} & \ldots & a_{1n} \\ \vdots & \ddots & \vdots \\ a_{m1} & \ldots & a_{mn} \end{pmatrix} \begin{pmatrix} x_1 \\ \vdots \\ x_n \end{pmatrix}.
\]

Так как \( y_i = \sum_{j=1}^n a_{ij} x_j \), то \( A \left( \sum_{j=1}^n x_j e_j \right) = \sum_{i=1}^m \sum_{j=1}^n a_{ij} x_j \varepsilon_i \); в частности,
\[
Ae_j = \sum_{i} a_{ij} \varepsilon_i.
\]

rk \( A \) ранг матрицы \( A \).
tr \( A \) след матрицы \( A \).
\[
\delta_{ij} =
\begin{cases}
0 & \text{при } i \neq j, \\
1 & \text{при } i = j.
\end{cases}
\]
Hom\((V, W)\) линейное пространство, состоящее из линейных отображений пространства \( V \) в пространство \( W \) (сложение двух линейных отображений и умножение линейного отображения на число определяются естественным образом).
\[
(x_1, \ldots, \hat{x}_i, \ldots, x_n)
\] \( = (x_1, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n) \).