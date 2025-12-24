---
source_image: page_095.png
page_number: 95
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.28
tokens: 6857
characters: 2926
timestamp: 2025-12-24T08:10:11.757798
finish_reason: stop
---

где \( P = A_{11} \) и \( Q = B_{22} \) (см. п. 6.3). Используя теорему 1.13.1, получим

\[
\begin{vmatrix}
P + WQV & PX + WQ \\
YP + QV & YPX + Q
\end{vmatrix}
= \begin{vmatrix}
P & WQ \\
YP & Q
\end{vmatrix}
\cdot
\begin{vmatrix}
I & X \\
V & I
\end{vmatrix}
=
\frac{1}{|P| \cdot |Q|}
\begin{vmatrix}
P & WQ \\
YP & Q
\end{vmatrix}
\cdot
\begin{vmatrix}
P & PX \\
QV & Q
\end{vmatrix}.
\]

**1.39.** Раскладывая определитель матрицы

\[
C = \left(
\begin{array}{cccccc}
0 & a_{12} & \ldots & a_{1n} & b_{11} & \ldots & b_{1n} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & a_{n2} & \ldots & a_{nn} & b_{n1} & \ldots & b_{nn} \\
a_{11} & 0 & \ldots & 0 & b_{11} & \ldots & b_{1n} \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
a_{n1} & 0 & \ldots & 0 & b_{n1} & \ldots & b_{nn}
\end{array}
\right)
\]

по первым \( n \) строкам (теорема 2.4.1), получаем

\[
|C| = \prod_{k=1}^n (-1)^{\varepsilon_k}
\begin{vmatrix}
a_{12} & \ldots & a_{1n} & b_{1k} \\
\ldots & \ldots & \ldots & \ldots \\
a_{n2} & \ldots & a_{nn} & b_{nk}
\end{vmatrix}
\cdot
\begin{vmatrix}
a_{11} & b_{11} & \ldots & \hat{b}_{1k} & \ldots & b_{1n} \\
\ldots & \ldots & \ldots & \ldots \\
a_{n1} & b_{n1} & \ldots & \hat{b}_{nk} & \ldots & b_{nn}
\end{vmatrix}
=
\prod_{k=1}^n (-1)^{\varepsilon_k + \alpha_k + \beta_k}
\begin{vmatrix}
b_{1k} & a_{12} & \ldots & a_{1n} \\
\ldots & \ldots & \ldots & \ldots \\
b_{nk} & a_{n2} & \ldots & a_{nn}
\end{vmatrix}
\cdot
\begin{vmatrix}
b_{11} & \ldots & a_{11} & \ldots & b_{1n} \\
\ldots & \ldots & \ldots & \ldots \\
b_{n1} & \ldots & a_{n1} & \ldots & b_{nn}
\end{vmatrix},
\]

где \( \varepsilon_k = (1 + 2 + \ldots + n) + (2 + \ldots + n + (k + n)) \equiv k + n + 1 \pmod{2} \), \( \alpha_k = n - 1 \) и \( \beta_k = k - 1 \), т. е. \( \varepsilon_k + \alpha_k + \beta_k \equiv 1 \pmod{2} \). С другой стороны, вычитая из \( i \)-й строки матрицы \( C \) \((i + n)\)-ю строку для \( i = 1, \ldots, n \), получаем \( |C| = -|A| \cdot |B| \).

**1.40.** Доказательство проведём индукцией по \( p \). При \( p = 1 \) равенство очевидно. Тождество из задачи 1.39 можно в нашем случае записать в виде

\[
|AB| \cdot |BC| = \prod_{k=1}^p (-1)^{p+k+1} |\hat{A}_1 BC_k| \cdot |A_1 B \hat{C}_k|.
\] (1)

Разложим определитель \( \Delta = |\hat{A}_i BC_j|^p_1 \) по первой строке:

\[
\Delta = \prod_{k=1}^p (-1)^{k+1} |\hat{A}_1 BC_k| \cdot \Delta_k.
\] (2)

Все элементы определителя \( \Delta_k \) имеют вид \( |\hat{A}_i BC_k| \), где \( i > 1 \); присоединим в них столбец \( A_1 \) к матрице \( B \) (для этого нужно совершить \( p - 2 \) транспозиции). К полученному определителю можно применить предположение индукции; в результате получим

\[
\Delta_k = (-1)^p |AB|^{p-2} |A_1 B \hat{C}_k|
\]

(в определителе \( |AB| \) столбец \( A_1 \) снова переставлен на своё прежнее место). Подставляя это выражение для \( \Delta_k \) в (2) и учитывая (1), получаем требуемое.