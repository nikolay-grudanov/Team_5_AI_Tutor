---
source_image: page_349.png
page_number: 349
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.84
tokens: 5817
characters: 2514
timestamp: 2025-12-24T07:13:38.974025
finish_reason: stop
---

471. 0, если \( n > 2 \), \( \sin(\alpha_1 - \alpha_2) \sin(\beta_1 - \beta_2) \), если \( n = 2 \).
472. 0, если \( n > 2 \), \( \sin^2(\alpha_1 - \alpha_2) \), если \( n = 2 \).
473. 0, если \( n > 2 \), \( -\sin^2(\alpha_1 - \alpha_2) \), если \( n = 2 \).
474. \( \prod_{n \geq i > k \geq 1} (a_i - a_k)(b_i - b_k) \).
475. \( C_n^1 C_n^2 \ldots C_n^n \prod_{n \geq i > k \geq 1} (a_k - a_i)(b_i - b_k) \).
476. \( (-1)^{\frac{n(n-1)}{2}} [(n-1)!]^n \).
Указание. Элемент в \( i \)-й строке и \( k \)-м столбце записать в виде \([i + (k-1)]^{n-1}\) и разложить по формуле степени бинома или прямо воспользоваться результатом предыдущей задачи.
477. \( \prod_{n \geq i > k \geq 1} (x_i - x_k)^2 \).
478. \( \prod_{i=1}^n (x - x_i) \prod_{n \geq i > k \geq 1} (x_i - x_k)^2 \).
Указание. Представить в виде произведения определителей:

\[
\begin{vmatrix}
1 & 1 & \ldots & 1 & 1 \\
x_1 & x_2 & \ldots & x_n & x \\
x_1^2 & x_2^2 & \ldots & x_n^2 & x^2 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
x_1^{n-1} & x_2^{n-1} & \ldots & x_n^{n-1} & x^{n-1} \\
x_1^n & x_2^n & \ldots & x_n^n & x^n
\end{vmatrix}
\]
и
\[
\begin{vmatrix}
1 & 1 & \ldots & 1 & 0 \\
x_1 & x_2 & \ldots & x_n & 0 \\
x_1^2 & x_2^2 & \ldots & x_n^2 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
x_1^{n-1} & x_2^{n-1} & \ldots & x_n^{n-1} & 0 \\
0 & 0 & \ldots & 0 & 1
\end{vmatrix},
\]
причем произведение составляется по строкам.
479. Указание. Данный определитель помножить на определитель Вандермонда
\[
v = \begin{vmatrix}
1 & \varepsilon_1 & \varepsilon_1^2 & \ldots & \varepsilon_1^{n-1} \\
1 & \varepsilon_2 & \varepsilon_2^2 & \ldots & \varepsilon_2^{n-1} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & \varepsilon_n & \varepsilon_n^2 & \ldots & \varepsilon_n^{n-1}
\end{vmatrix}.
\]
481. \( (1 - \alpha^n)^{n-1} \).
Указание. Использовать результат задачи 479 и равенство \( (1 - \alpha \varepsilon_1)(1 - \alpha \varepsilon_2) \ldots (1 - \alpha \varepsilon_n) = 1 - \alpha^n \), \( \varepsilon_1, \varepsilon_2, \ldots, \varepsilon_n \) — корни \( n \)-й степени из единицы. Проще, однако, вычислить этот определитель как частный случай определителя задачи 325.
483. \( (a + b + c + d)(a - b + c - d)(a + bi - c - di)(a - bi - c + di) = a^4 - b^4 + c^4 - d^4 - 2a^2c^2 + 2b^2d^2 - 4a^2bd + 4b^2ac - 4c^2bd + 4d^2ac. \)
484.
\[
[1 + (-1)^n]^n = \begin{cases}
0 & \text{при } n \text{ нечетном}, \\
2^n & \text{при } n \text{ четном}.
\end{cases}
\]
485. \( (-1)^n \frac{[(n+1)a^n - 1]^n - n^n a^{n(n+1)}}{(1-a^n)^2} \).