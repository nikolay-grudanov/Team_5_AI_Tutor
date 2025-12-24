---
source_image: page_109.png
page_number: 109
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.94
tokens: 5401
characters: 1609
timestamp: 2025-12-24T07:28:36.976877
finish_reason: stop
---

и, следовательно,

\[
p_{\xi_1}(x) = \frac{2}{9} x, \quad x \in [0, 3]; \quad p_{\xi_1}(x) = 0, \quad x \notin [0, 3].
\]

Так как \(\{\xi_2 = k\} = \{(u, v): k-1 \leq \sqrt{u^2 + v^2} < k\},\) \(k = 1, 2, 3,\) то

\[
P(\xi_2 = 1) = 1/9, \quad P(\xi_2 = 2) = 1/3, \quad P(\xi_2 = 3) = 5/9.
\]

Нетрудно проверить, что

\[
F_{\xi_3}(x) = \begin{cases}
0, & x < 0, \\
x^2/9, & 0 \leq x \leq 1, \\
1, & x > 1.
\end{cases}
\]

Если уже известна плотность распределения случайной величины или вероятности значений дискретной величины, то может оказаться, что математическое ожидание удобнее вычислять не по определению, а по формулам, которые мы получим в качестве частного случая следующих двух теорем.

Теорема 1.1. Пусть \((\xi_1, \xi_2, \ldots, \xi_n)\) — дискретный случайный вектор, для которого

\[
P(\xi_1 = x_{k1}, \xi_2 = x_{k2}, \ldots, \xi_n = x_{kn}) = p_{x_{k1} x_{k2} \ldots x_{kn}} \geq 0,
\]
\[
\sum_{x_{k1} \ldots x_{kn}} p_{x_{k1} x_{k2} \ldots x_{kn}} = 1.
\]

Если ряд
\[
\sum_{x_{k1} \ldots x_{kn}} |g(x_{k1}, \ldots, x_{kn})| p_{x_{k1} \ldots x_{kn}}
\]
сходится, то случайная величина \(\eta = g(\xi_1, \xi_2, \ldots, \xi_n)\) имеет математическое ожидание

\[
M\eta = \sum_{x_{k1} \ldots x_{kn}} g(x_{k1}, \ldots, x_{kn}) p_{x_{k1} \ldots x_{kn}}. \tag{1.6}
\]

Теорема 1.2. Пусть \((\xi_1, \xi_2, \ldots, \xi_n)\) — абсолютно непрерывный случайный вектор с плотностью распределения \(p_{\xi_1 \ldots \xi_n}(x_1, x_2, \ldots, x_n)\). Если интеграл

\[
\int_{-\infty}^{\infty} \ldots \int_{-\infty}^{\infty} |g(x_1, \ldots, x_n)| p_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) dx_1 \ldots dx_n
\]