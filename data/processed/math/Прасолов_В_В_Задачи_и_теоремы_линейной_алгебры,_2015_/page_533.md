---
source_image: page_533.png
page_number: 533
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.79
tokens: 6608
characters: 2711
timestamp: 2025-12-24T08:22:09.693373
finish_reason: stop
---

Чтобы доказать это тождество, рассмотрим (следуя [Fu]) вспомогательные операторы

\[
\Delta_{i_1 j_1} \ldots \Delta_{i_m j_m} F = \bigotimes_{k_1, \ldots, k_m=1}^n x_{k_1 i_1} \ldots x_{k_m i_m} \frac{\partial^m F}{\partial x_{k_1 j_1} \ldots \partial x_{k_m j_m}}.
\]

Обратите внимание, что так обозначается оператор в целом, а не композиция операторов \( \Delta_{ij} = D_{ij} \). Но при этом, как легко видеть, порядок членов в выражении \( \Delta_{i_1 j_1} \ldots \Delta_{i_m j_m} \) несуществен. Поэтому можно формально рассмотреть матрицу \( \| \Delta_{ij} \|_1^n \) с некоммутирующими элементами и формально записать её определитель:

\[
| \Delta_{ij} |_1^n = \bigotimes_{\sigma} (-1)^{\sigma} \Delta_{1 \sigma(1)} \ldots \Delta_{n \sigma(n)}.
\]

Матрицу \( \| \Delta_{ij} \|_1^n \) можно представить в виде произведения матриц \( \| x_{ij} \|_1^n \cdot \| \partial / \partial x_{ij} \|_1^n \). Поэтому

\[
| \Delta_{ij} |_1^n = | x_{ij} |_1^n \cdot \left| \frac{\partial}{\partial x_{ij}} \right|_1^n.
\]

Таким образом, нужно доказать тождество

\[
\begin{vmatrix}
D_{11} + n - 1 & D_{12} & \ldots & D_{1n} \\
D_{21} & D_{22} + n - 2 & \ldots & D_{2n} \\
\cdots & \cdots & \cdots & \cdots \\
D_{n1} & D_{n2} & \ldots & D_{nn}
\end{vmatrix}
=
\begin{vmatrix}
\Delta_{11} & \Delta_{12} & \ldots & \Delta_{1n} \\
\Delta_{21} & \Delta_{22} & \ldots & \Delta_{2n} \\
\cdots & \cdots & \cdots & \cdots \\
\Delta_{n1} & \Delta_{n2} & \ldots & \Delta_{nn}
\end{vmatrix}.
\]

Его можно рассматривать как формальное тождество для определителей двух матриц (у одной из которых элементы некоммутирующие); для доказательства этого тождества достаточно знать, что элементы данных матриц связаны следующими соотношениями:

\[
D_{ij} D_{kl} = \begin{cases}
D_{ij} \Delta_{kl} = \Delta_{ij} \Delta_{kl} & \text{при } j \neq k; \\
\Delta_{ij} \Delta_{kl} + D_{il} & \text{при } j = k;
\end{cases}
\]

и вообще, если \( j \) отлично от \( a_1, \ldots, a_r \), то

\[
D_{ij} \Delta_{a_1 b_1} \ldots \Delta_{a_r b_r} = \Delta_{ij} \Delta_{a_1 b_1} \ldots \Delta_{a_r b_r},
\] (2)

а если \( j \) совпадает ровно с одним из чисел \( a_1, \ldots, a_r \) (а именно, с \( a_k \)), то

\[
D_{ij} \Delta_{a_1 b_1} \ldots \Delta_{a_r b_r} = \Delta_{ij} \Delta_{a_1 b_1} \ldots \Delta_{a_r b_r} + \Delta_{a_1 b_1} \ldots \Delta_{ib_k} \ldots \Delta_{a_r b_r},
\] (3)

где \( \Delta_{ib_k} \) стоит на месте члена \( \Delta_{a_k b_k} \). (Кроме того, \( D_{ij} = \Delta_{ij} \), но следует помнить, что \( \Delta_{i_1 j_1} \ldots \Delta_{i_r j_r} \) — это не произведение отдельных множителей, а обозначение для некоторого оператора, и мы не можем заменить сразу несколько членов \( \Delta_{ij} \) на соответствующие \( D_{ij} \).)