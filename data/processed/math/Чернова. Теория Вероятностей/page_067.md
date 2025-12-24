---
source_image: page_067.png
page_number: 67
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.31
tokens: 11674
characters: 2060
timestamp: 2025-12-24T08:27:44.223647
finish_reason: stop
---

11.2 Свойства математического ожидания

Во всех свойствах предполагается, что рассматриваемые математические ожидания существуют.

Е0. Математическое ожидание случайной величины есть ЧИСЛО!

Е1. Для произвольной функции \( g : \mathbb{R} \to \mathbb{R} \)

\[
\mathbf{E} g(\xi) = \begin{cases}
\sum_k g(a_k) \mathbf{P}(\xi = a_k), & \text{если распределение } \xi \text{ дискретно;} \\
\int_{-\infty}^{\infty} g(x) f_{\xi}(x) \, dx, & \text{если распределение } \xi \text{ абсолютно непрерывно.}
\end{cases}
\]

Доказательство. Мы докажем это свойство (как и почти все дальнейшие) только для дискретного распределения. Пусть \( g(\xi) \) принимает значения \( c_1, c_2, \ldots \) с вероятностями \( \mathbf{P}(g(\xi) = c_m) = \sum_{k: g(a_k) = c_m} \mathbf{P}(\xi = a_k) \). Тогда

\[
\mathbf{E} g(\xi) = \sum_m c_m \mathbf{P}(g(\xi) = c_m) = \sum_m c_m \sum_{k: g(a_k) = c_m} \mathbf{P}(\xi = a_k) = \sum_m \sum_{k: g(a_k) = c_m} g(a_k) \mathbf{P}(\xi = a_k) = \sum_k g(a_k) \mathbf{P}(\xi = a_k).
\]

Е2. Математическое ожидание постоянной равно этой постоянной: \( \mathbf{E} c = c \).

Е3. Постоянную можно вынести за знак математического ожидания: \( \mathbf{E} (c \xi) = c \mathbf{E} \xi \).

Доказательство. Следует из свойства Е1 при \( g(x) = cx \).

Е4. Математическое ожидание суммы любых случайных величин \( \xi \) и \( \eta \) равно сумме их математических ожиданий:

\[
\mathbf{E} (\xi + \eta) = \mathbf{E} \xi + \mathbf{E} \eta.
\]

Доказательство. Для величин с дискретным распределением: пусть \( x_k \) и \( y_n \) — значения \( \xi \) и \( \eta \), соответственно. Для функции \( g : \mathbb{R}^2 \to \mathbb{R} \) можно доказать свойство, аналогичное Е1 (сделать это!). Пользуясь этим свойством для \( g(x, y) = x + y \), запишем:

\[
\mathbf{E} (\xi + \eta) = \sum_{k,n} (x_k + y_n) \mathbf{P}(\xi = x_k, \eta = y_n) = \sum_k x_k \underbrace{\sum_n \mathbf{P}(\xi = x_k, \eta = y_n)}_{\mathbf{P}(\xi = x_k)} + \sum_n y_n \underbrace{\sum_k \mathbf{P}(\xi = x_k, \eta = y_n)}_{\mathbf{P}(\eta = y_n)} = \mathbf{E} \xi + \mathbf{E} \eta.
\]