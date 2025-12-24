---
source_image: page_087.png
page_number: 87
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.68
tokens: 5571
characters: 1820
timestamp: 2025-12-24T07:28:09.314557
finish_reason: stop
---

§ 31 СОВМЕСТНЫЕ РАСПРЕДЕЛЕНИЯ

ный вектор. Функцию от переменных \( x_1, x_2, \ldots, x_n \):
\[
F_{\xi_1 \ldots \xi_n}(x_1, x_2, \ldots, x_n) = P(\xi_1 < x_1, \xi_2 < x_2, \ldots, \xi_n < x_n),
\]
назовем многомерной функцией распределения случайного вектора \( (\xi_1, \xi_2, \ldots, \xi_n) \).

Так же, как в одномерном случае, проверяется, что \( F_{\xi_1 \ldots \xi_n}(x_1, x_2, \ldots, x_n) \) монотонна по каждому аргументу,
\[
\lim_{x_1 \to +\infty} F_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) = 1,
\]
\[
\ldots \ldots
\]
\[
\lim_{x_n \to +\infty} F_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) = 0,
\]
\[
\lim_{x_k \to -\infty} F_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) = F_{\xi_1 \ldots \xi_{n-1}}(x_1, \ldots, x_{n-1}).
\]
(3.1)

Аналогичное свойство выполняется при переходе к пределу по любому аргументу.

Случайный вектор \( (\xi_1, \ldots, \xi_n) \) назовем вектором дискретного типа, если существует конечное или счетное множество точек \( (x_{k1}, x_{k2}, \ldots, x_{kn}), k = 1, 2, \ldots \) (без предельных точек), таких, что
\[
P(\xi_1 = x_{k1}, \xi_2 = x_{k2}, \ldots, \xi_n = x_{kn}) = p_{x_{k1} x_{k2} \ldots x_{kn}}
\]
и
\[
\sum_{(x_{k1}, \ldots, x_{kn})} p_{x_{k1}, \ldots, x_{kn}} = 1.
\]
(3.2)

Случайный вектор дискретного типа можно определить на дискретном вероятностном пространстве \( (\Omega, \mathcal{F}, P) \), в котором \( \Omega \) является множеством значений данного вектора.

Случайный вектор \( (\xi_1, \ldots, \xi_n) \) назовем вектором абсолютно непрерывного типа, если существует функция \( p_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) \) такая, что при любых \( x_1, x_2, \ldots, x_n \)
\[
F_{\xi_1 \xi_2 \ldots \xi_n}(x_1, x_2, \ldots, x_n) =
\]
\[
= \int_{-\infty}^{x_1} \int_{-\infty}^{x_2} \ldots \int_{-\infty}^{x_n} p_{\xi_1 \xi_2 \ldots \xi_n}(u_1, \ldots, u_n) du_1 \ldots du_n.
\]