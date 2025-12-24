---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.70
tokens: 5518
characters: 1890
timestamp: 2025-12-24T07:06:59.655369
finish_reason: stop
---

456. Пусть в определителе \( D \) порядка \( n \) выделены \( k \) строк и \( l \) столбцов, причем \( l \leq k \) и все элементы выделенных \( l \) столбцов, не лежащие в выделенных \( k \) строках, равны нулю. Показать, что в разложении Лапласа определителя \( D \) по выделенным \( k \) строкам нужно брать только те миноры порядка \( k \), которые содержат выделенные \( l \) столбцов; утверждение, полученное переменной роли строк и столбцов, также верно.

457. Пользуясь теоремой Лапласа, решить задачу 206.

458. Доказать, что

\[
\begin{vmatrix}
a_{11} & 0 & a_{12} & 0 & \ldots & a_{1n} & 0 \\
0 & b_{11} & 0 & b_{12} & \ldots & 0 & b_{1n} \\
a_{21} & 0 & a_{22} & 0 & \ldots & a_{2n} & 0 \\
0 & b_{21} & 0 & b_{22} & \ldots & 0 & b_{2n} \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
a_{n1} & 0 & a_{n2} & 0 & \ldots & a_{nn} & 0 \\
0 & b_{n1} & 0 & b_{n2} & \ldots & 0 & b_{nn}
\end{vmatrix}
\]

\[
= \begin{vmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
\cdots & \cdots & \cdots & \cdots \\
a_{n1} & a_{n2} & \ldots & a_{nn}
\end{vmatrix}
\cdot
\begin{vmatrix}
b_{11} & b_{12} & \ldots & b_{1n} \\
\cdots & \cdots & \cdots & \cdots \\
b_{n1} & b_{n2} & \ldots & b_{nn}
\end{vmatrix}
\]

*459. Вычислить определитель порядка \( k + l \):

\[
\begin{vmatrix}
3 & 2 & 0 & 0 & \ldots & 0 & 0 & 0 & 0 \\
1 & 3 & 2 & 0 & \ldots & 0 & 0 & 0 & 0 \\
0 & 1 & 3 & 2 & \ldots & 0 & 0 & 0 & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
0 & \ldots & 1 & 3 & 2 & 0 & \ldots & 0 \\
0 & \ldots & 0 & 2 & 5 & 3 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & 0 & \ldots & 2 & 5 & 3 & 0 \\
0 & 0 & 0 & 0 & \ldots & 0 & 2 & 5 & 3 \\
0 & 0 & 0 & 0 & \ldots & 0 & 0 & 2 & 5
\end{vmatrix}
\]

\[
\left\{
\begin{array}{l}
k \text{ строк} \\
l \text{ строк}
\end{array}
\right.
\]