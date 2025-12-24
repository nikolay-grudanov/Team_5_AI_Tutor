---
source_image: page_126.png
page_number: 126
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.91
tokens: 8559
characters: 1811
timestamp: 2025-12-24T07:29:13.488921
finish_reason: stop
---

Докажем формулу (5.4). Воспользовавшись определением (5.2), получим

\[
\sum_{j=1}^{\infty} P(\eta = y_j) M(\xi \mid \eta_j) = \sum_{j=1}^{\infty} P(\eta = y_j) \sum_{i=1}^{\infty} x_i \frac{P(\xi = x_i, \eta = y_j)}{P(\eta = y_j)} =
\]
\[
= \sum_{i,j=1}^{\infty} x_i P(\xi = x_i, \eta = y_j) = \sum_{i=1}^{\infty} x_i \left( \sum_{j=1}^{\infty} P(\xi = x_i, \eta = y_j) \right).
\]

Правая часть последнего равенства равна \( M_{\xi} \), так как
\[
\sum_{j=1}^{\infty} P(\xi = x_i, \eta = y_j) = P(\xi = x_i).
\]
Покажем, что из формул (5.3) и (5.4) следует формула полной вероятности. Пусть
\[
\xi = \begin{cases}
1, & \text{если } \omega \in A, \\
0, & \text{если } \omega \in \overline{A},
\end{cases}
\quad
\eta = \begin{cases}
y_j, & \text{если } \omega \in B_j, \\
j = 1, 2, \ldots,
\end{cases}
\]
где \( B_i B_j = \varnothing, \ i \neq j, \ \bigcup_{j=1}^{\infty} B_j = \Omega \). Тогда
\[
M_{\xi} = P(A), \quad P(\eta = y_j) = P(B_j), \quad M(\xi \mid \eta = y_j) = P(A \mid B_j).
\]
Подставляя эти выражения в (5.4), получим формулу полной вероятности со счетной системой событий \( B_1, B_2, \ldots \):
\[
P(A) = \sum_{k=1}^{\infty} P(B_k) P(A \mid B_k).
\]
(5.5)
Положим в (5.5)
\[
A = (\xi \in C), \quad B_k = (\eta = y_k),
\]
где \( C \subset (x_1, x_2, \ldots, x_n, \ldots) \), \( (x_i, y_j) \) — значения \( (\xi, \eta) \). Тогда при любом \( C \)
\[
P(\xi \in C) = \sum_{x_i \in C} P(\eta = y_k) P(\xi = x_i \mid \eta = y_k).
\]
(5.6)
Свойства условного математического ожидания:
1°.
\[
M[\varphi(\eta) \mid \eta] = \varphi(\eta).
\]
(5.7)
2°.
\[
M[\varphi(\eta) \xi \mid \eta] = \varphi(\eta) M(\xi \mid \eta).
\]
(5.8)
3°.
\[
M(\xi_1 + \xi_2 \mid \eta) = M(\xi_1 \mid \eta) + M(\xi_2 \mid \eta).
\]
(5.9)
4°. Если \( \xi \) и \( \eta \) независимы, то
\[
M(\xi \mid \eta) = M_{\xi}.
\]
(5.10)