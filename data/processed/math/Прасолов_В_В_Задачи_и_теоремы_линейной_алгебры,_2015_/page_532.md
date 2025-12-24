---
source_image: page_532.png
page_number: 532
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.12
tokens: 6511
characters: 2362
timestamp: 2025-12-24T08:22:05.560364
finish_reason: stop
---

В тождестве Капелли участвуют композиции умножений на переменные \( x_{ij} \), где \( i \) и \( j \) изменяются от 1 до \( n \), и дифференцирований \( \frac{\partial}{\partial x_{ij}} \). Для начала рассмотрим простейший нетривиальный случай \( n = 2 \). Чтобы упростить формулы, положим \( x_{k1} = x_k \) и \( x_{k2} = y_k \). Пусть \( F = x_1^{a_1} x_2^{a_2} y_1^{b_1} y_2^{b_2} \). Рассмотрим оператор

\[
D_{ij}(F) = \sum_{k=1}^n x_{ki} \frac{\partial F}{\partial x_{kj}}.
\]

Ясно, что

\[
D_{12} D_{21}(F) = \sum_k x_k \frac{\partial}{\partial y_k} \left( \sum_l y_l \frac{\partial F}{\partial x_l} \right) =
\]
\[
= \sum_k x_k \frac{\partial F}{\partial x_k} + \sum_{k,l} x_k y_l \frac{\partial^2 F}{\partial x_l \partial y_k} = bF + \sum_{k,l} x_k y_l \frac{\partial^2 F}{\partial x_l \partial y_k},
\]
где \( b = b_1 + b_2 \). Положим \( a = a_1 + a_2 \) и рассмотрим выражение

\[
abF = a \left( \sum_l y_l \frac{\partial F}{\partial y_l} \right) = \sum_k x_k y_l \frac{\partial^2 F}{\partial x_k \partial y_l}.
\]

Сравнивая это равенство с предыдущим, получаем

\[
(a + 1)bF = D_{12} D_{21}(F) + (x_1 y_2 - x_2 y_1) \left( \frac{\partial^2 F}{\partial x_1 \partial y_2} - \frac{\partial^2 F}{\partial x_2 \partial y_1} \right).
\]

Воспользовавшись тем, что \( (D_{11} + 1)D_{22}(F) = (a + 1)bF \), полученное тождество можно записать в виде

\[
\begin{vmatrix}
D_{11} + 1 & D_{12} \\
D_{21} & D_{22}
\end{vmatrix}(F) = \begin{vmatrix}
x_1 & y_1 \\
x_2 & y_2
\end{vmatrix} \cdot \begin{vmatrix}
\frac{\partial}{\partial x_1} & \frac{\partial}{\partial y_1} \\
\frac{\partial}{\partial x_2} & \frac{\partial}{\partial y_2}
\end{vmatrix}(F).
\]

В левой части стоит определитель матрицы с некоммутирующими элементами, и его нужно понимать именно так, как было указано выше.

В общем случае тождество Капелли имеет вид

\[
\begin{vmatrix}
D_{11} + n - 1 & D_{12} & \ldots & D_{1n} \\
D_{21} & D_{22} + n - 2 & \ldots & D_{2n} \\
\cdots & \cdots & \cdots & \cdots \\
D_{n1} & D_{n2} & \ldots & D_{nn}
\end{vmatrix} = \begin{vmatrix}
x_{11} & \ldots & x_{1n} \\
\cdots & \cdots & \cdots \\
x_{n1} & \ldots & x_{nn}
\end{vmatrix} \cdot \begin{vmatrix}
\frac{\partial}{\partial x_{11}} & \ldots & \frac{\partial}{\partial x_{1n}} \\
\cdots & \cdots & \cdots \\
\frac{\partial}{\partial x_{n1}} & \ldots & \frac{\partial}{\partial x_{nn}}
\end{vmatrix}.
\]