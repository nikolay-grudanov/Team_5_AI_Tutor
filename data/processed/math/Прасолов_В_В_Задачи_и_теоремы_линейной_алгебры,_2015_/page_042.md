---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.80
tokens: 6776
characters: 2335
timestamp: 2025-12-24T08:08:45.562775
finish_reason: stop
---

1.26. Пусть \( a_{ij} = (x_i + y_j)^n \). Докажите, что

\[
|a_{ij}|_0^n = \binom{n}{1} \cdots \binom{n}{n} \div_{i > k} (x_i - x_k)(y_k - y_i).
\]

1.27. Найдите над полем \( \mathbb{C} \) все решения системы уравнений \( \lambda_1^k + \ldots + \lambda_n^k = 0 \) (\( k = 1, \ldots, n \)).

1.28. Пусть \( \sigma_k(x_0, \ldots, x_n) \) — \( k \)-я элементарная симметрическая функция, \( \sigma_0 = 1; \sigma_k(\hat{x}_i) = \sigma_k(x_0, \ldots, x_{i-1}, x_{i+1}, \ldots, x_n) \). Докажите, что если \( a_{ij} = \sigma_i(\hat{x}_j) \), то \( |a_{ij}|_0^n = \div_{i < j} (x_i - x_j) \).

Соотношения между определителями

1.29. а) Пусть \( b_{ij} = (-1)^{i+j} a_{ij} \). Докажите, что \( |a_{ij}|_1^n = |b_{ij}|_1^n \).
   б) Пусть \( b_{ij} = (-1)^{m_i + n_j} a_{ij} \). Докажите, что \( |a_{ij}|_1^n = (-1)^{M+N} |b_{ij}|_1^n \), где \( M = \bullet m_i \) и \( N = \bullet n_j \).

1.30. Пусть \( b_{ij} = a_{n+1-i, n+1-j} \). Докажите, что \( |b_{ij}|_1^n = |a_{ij}|_1^n \).

1.31. Докажите, что

\[
\begin{vmatrix}
a_1 c_1 & a_2 d_1 & a_1 c_2 & a_2 d_2 \\
a_3 c_1 & a_4 d_1 & a_3 c_2 & a_4 d_2 \\
b_1 c_3 & b_2 d_3 & b_1 c_4 & b_2 d_4 \\
b_3 c_3 & b_4 d_3 & b_3 c_4 & b_4 d_4
\end{vmatrix}
= \begin{vmatrix}
a_1 & a_2 \\
a_3 & a_4
\end{vmatrix}
\cdot
\begin{vmatrix}
b_1 & b_2 \\
b_3 & b_4
\end{vmatrix}
\cdot
\begin{vmatrix}
c_1 & c_2 \\
c_3 & c_4
\end{vmatrix}
\cdot
\begin{vmatrix}
d_1 & d_2 \\
d_3 & d_4
\end{vmatrix}.
\]

1.32. Докажите, что

\[
\begin{vmatrix}
a_1 & 0 & 0 & b_1 & 0 & 0 \\
0 & a_2 & 0 & 0 & b_2 & 0 \\
0 & 0 & a_3 & 0 & 0 & b_3 \\
b_{11} & b_{12} & b_{13} & a_{11} & a_{12} & a_{13} \\
b_{21} & b_{22} & b_{23} & a_{21} & a_{22} & a_{23} \\
b_{31} & b_{32} & b_{33} & a_{31} & a_{32} & a_{33}
\end{vmatrix}
=
\begin{vmatrix}
a_1 a_{11} - b_1 b_{11} & a_2 a_{12} - b_2 b_{12} & a_3 a_{13} - b_3 b_{13} \\
a_1 a_{21} - b_1 b_{21} & a_2 a_{22} - b_2 b_{22} & a_3 a_{23} - b_3 b_{23} \\
a_1 a_{31} - b_1 b_{31} & a_2 a_{32} - b_2 b_{32} & a_3 a_{33} - b_3 b_{33}
\end{vmatrix}.
\]

1.33. Пусть \( s_k = \sum_{i=1}^n a_{ki} \). Докажите, что

\[
\begin{vmatrix}
s_1 - a_{11} & \ldots & s_1 - a_{1n} \\
\ldots & \ldots & \ldots \\
s_n - a_{n1} & \ldots & s_n - a_{nn}
\end{vmatrix}
= (-1)^{n-1}(n-1)
\begin{vmatrix}
a_{11} & \ldots & a_{1n} \\
\ldots & \ldots & \ldots \\
a_{n1} & \ldots & a_{nn}
\end{vmatrix}.
\]