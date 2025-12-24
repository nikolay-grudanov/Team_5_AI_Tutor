---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.65
tokens: 6166
characters: 1224
timestamp: 2025-12-24T08:09:23.267842
finish_reason: stop
---

т. е.

\[
b_1 = -\frac{1}{2!},
\]
\[
\frac{b_1}{2!} + b_2 = -\frac{1}{3!},
\]
\[
\frac{b_1}{3!} + \frac{b_2}{2!} + b_3 = -\frac{1}{4!},
\]
\[
\ldots
\]

Решая эту систему линейных уравнений по правилу Крамера, получаем

\[
B_k = k! \; b_k = (-1)^k k! \left| \begin{array}{ccccc}
1/2! & 1 & 0 & \ldots & 0 \\
1/3! & 1/2! & 1 & \ldots & 0 \\
1/4! & 1/3! & 1/2! & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1/(k+1)! & 1/k! & 1/(k-1)! & \ldots & 1/2!
\end{array} \right|.
\]

Докажем теперь, что \( B_{2k+1} = 0 \) при \( k \geqslant 1 \). Пусть \( \frac{x}{e^x - 1} = -\frac{x}{2} + f(x) \).
Тогда

\[
f(x) - f(-x) = \frac{x}{e^x - 1} + \frac{x}{e^{-x} - 1} + x = 0,
\]

т. е. \( f \) — чётная функция. Пусть \( c_k = \frac{B_{2k}}{(2k)!} \). Тогда

\[
x = \left( x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots \right) \left( 1 - \frac{x}{2} + c_1 x^2 + c_2 x^4 + c_3 x^6 + \ldots \right).
\]

Приравнивая коэффициенты при \( x^3, x^5, x^7, \ldots \) и учитывая, что

\[
\frac{1}{2(2n)!} - \frac{1}{(2n+1)!} = \frac{2n-1}{2(2n+1)!},
\]

получаем

\[
c_1 = \frac{1}{2 \cdot 3!},
\]
\[
\frac{c_1}{3!} + c_2 = \frac{3}{2 \cdot 5!},
\]
\[
\frac{c_1}{5!} + \frac{c_2}{3!} + c_3 = \frac{5}{2 \cdot 7!},
\]
\[
\ldots
\]