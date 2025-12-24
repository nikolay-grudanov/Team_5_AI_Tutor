---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.68
tokens: 5837
characters: 2419
timestamp: 2025-12-24T07:07:40.874909
finish_reason: stop
---

*540. Пусть даны два определителя:

\[
A = \begin{vmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\ldots & \ldots & \ldots & \ldots \\
a_{n1} & a_{n2} & \ldots & a_{nn}
\end{vmatrix}
\]
порядка \( n \)

И

\[
B = \begin{vmatrix}
b_{11} & b_{12} & \ldots & b_{1p} \\
b_{21} & b_{22} & \ldots & b_{2p} \\
\ldots & \ldots & \ldots & \ldots \\
b_{p1} & b_{p2} & \ldots & b_{pp}
\end{vmatrix}
\]
порядка \( p \).

Составим определитель порядка \( np \):

\[
D = \begin{vmatrix}
a_{11}b_{11} & \ldots & a_{1n}b_{11} & a_{11}b_{12} & \ldots & a_{1n}b_{12} & \ldots & a_{11}b_{1p} & \ldots & a_{1n}b_{1p} \\
a_{21}b_{11} & \ldots & a_{2n}b_{11} & a_{21}b_{12} & \ldots & a_{2n}b_{12} & \ldots & a_{21}b_{1p} & \ldots & a_{2n}b_{1p} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
a_{n1}b_{11} & \ldots & a_{nn}b_{11} & a_{n1}b_{12} & \ldots & a_{nn}b_{12} & \ldots & a_{n1}b_{1p} & \ldots & a_{nn}b_{1p} \\
a_{11}b_{21} & \ldots & a_{1n}b_{21} & a_{11}b_{22} & \ldots & a_{1n}b_{22} & \ldots & a_{11}b_{2p} & \ldots & a_{1n}b_{2p} \\
a_{21}b_{21} & \ldots & a_{2n}b_{21} & a_{21}b_{22} & \ldots & a_{2n}b_{22} & \ldots & a_{21}b_{2p} & \ldots & a_{2n}b_{2p} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
a_{n1}b_{21} & \ldots & a_{nn}b_{21} & a_{n1}b_{22} & \ldots & a_{nn}b_{22} & \ldots & a_{n1}b_{2p} & \ldots & a_{nn}b_{2p} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
a_{n1}b_{p1} & \ldots & a_{nn}b_{p1} & a_{n1}b_{p2} & \ldots & a_{nn}b_{p2} & \ldots & a_{n1}b_{pp} & \ldots & a_{nn}b_{pp}
\end{vmatrix}.
\]

Таким образом, матрица определителя \( D \) состоит из \( p^2 \) клеток по \( n \) строк и \( n \) столбцов в каждой. При этом клетка, стоящая в \( i \)-й клеточной строке и \( j \)-м клеточном столбце (\( i, j = 1, 2, \ldots, p \)), получается из матрицы определителя \( A \) умножением всех ее элементов на \( b_{ij} \). Доказать, что \( D = A^p B^n \). Определитель \( D \) называется кронекеровским произведением определителей \( A \) и \( B \) (см. задачи 963, 965).

541. Доказать следующее правило разложения окаймленного определителя: если

\[
D = \begin{vmatrix}
a_{11} & a_{12} & \ldots & a_{1n} \\
a_{21} & a_{22} & \ldots & a_{2n} \\
\ldots & \ldots & \ldots & \ldots \\
a_{n1} & a_{n2} & \ldots & a_{nn}
\end{vmatrix}
\]