---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.17
tokens: 6454
characters: 1946
timestamp: 2025-12-24T08:10:14.909792
finish_reason: stop
---

Из формулы \( A \operatorname{adj} A = |A| \cdot I \) следует, что \( |\operatorname{adj} A| = |A|^{n-1} \), где \( n \) — порядок матрицы \( A \). Поэтому

\[
\begin{vmatrix}
a_1 & b_1 & c_1 \\
a_2 & b_2 & c_2 \\
a_3 & b_3 & c_3
\end{vmatrix}^2 = - \begin{vmatrix}
b_1 & c_1 \\
b_3 & c_3
\end{vmatrix} \begin{vmatrix}
a_1 & c_1 \\
a_3 & c_3
\end{vmatrix} - \begin{vmatrix}
a_1 & b_1 \\
a_3 & b_3
\end{vmatrix} \begin{vmatrix}
b_1 & c_1 \\
b_2 & c_2
\end{vmatrix} + \begin{vmatrix}
a_1 & c_1 \\
a_2 & c_2
\end{vmatrix} \begin{vmatrix}
a_1 & b_1 \\
a_2 & b_2
\end{vmatrix}.
\]

В последнем определителе знаки можно убрать, воспользовавшись задачей 1.29.

**2.16.** Докажем, что \( A^{-1} = \| b_{ij} \|_1^n \), где \( b_{ij} = \varepsilon^{-ij}/n \). В самом деле,

\[
\bullet \sum_{k=1}^n a_{ik} b_{kj} = \frac{1}{n} \sum_{k=1}^n \varepsilon^{ik} \varepsilon^{-kj} = \frac{1}{n} \sum_{k=1}^n \varepsilon^{k(i-j)} = \delta_{ij}.
\]

**2.17. Первое решение [Kl2].** Пусть \( \sigma_{n-k}^i = \sigma_{n-k}(x_1, \ldots, \hat{x}_i, \ldots, x_n) \). Используя результат задачи 1.17, легко проверить, что \( (\operatorname{adj} V)^T = \| b_{ij} \|_1^n \), где

\[
b_{ij} = (-1)^{i+j} \sigma_{n-j}^i V(x_1, \ldots, \hat{x}_i, \ldots, x_n).
\]

**Второе решение.** Пусть \( a_{ij} = x_i^{j-1} \). Пусть также

\[
\frac{(x_1 - x) \ldots (x_n - x)}{x_j - x} = c_{1j} + c_{2j} x + \ldots + c_{nj} x^{n-1},
\]

т. е.

\[
c_{pj} = (-1)^{p+1} \sum_{1 \leq k_1 < k_2 < \ldots < k_{n-p} \leq n} x_{k_1} \ldots x_{k_{n-p}}.
\]

Положим \( b_{kj} = \frac{c_{kj}}{\div (x_p - x_j)} \). Тогда

\[
\bullet \sum_{k=1}^n a_{ik} b_{kj} = \bullet \sum_{k=1}^n b_{kj} x_i^{k-1} = \frac{(x_1 - x_i) \ldots (x_n - x_i)}{x_j - x_i} \cdot \frac{1}{\div (x_p - x_j)} = \delta_{ij}.
\]

**2.18.** Покажем, что матрица \( \| b_{ij} \|_1^n \), где

\[
b_{ij} = \frac{\div (x_j + y_k)(x_k + y_i)}{(x_j + y_i) \div (x_j - x_k) \div (y_i - y_k)},
\]

является обратной к матрице Коши.