---
source_image: page_089.png
page_number: 89
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 56.75
tokens: 12053
characters: 2028
timestamp: 2025-12-24T07:36:32.256395
finish_reason: stop
---

§1. Математическое ожидание случайной величины

(Е3) Постоянный множитель можно вынести за знак математического ожидания: \( \mathbf{E}(c) = c \mathbf{E} \).
Это свойство следует из свойства (Е1) при \( g(x) = c x \).

(Е4) Математическое ожидание суммы любых случайных величин равно сумме их математических ожиданий: \( \mathbf{E}(+) = \mathbf{E} + \mathbf{E} \).
Доказательство. Воспользуемся равенством (18) и теоремой 23:

\[
\mathbf{E}(+) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x + y) f(x, y) \, dx \, dy =
\]
\[
= \int_{-\infty}^{\infty} x \, dx \int_{-\infty}^{\infty} f(x, y) \, dy + \int_{-\infty}^{\infty} y \, dy \int_{-\infty}^{\infty} f(x, y) \, dx =
\]
\[
= \int_{-\infty}^{\infty} x f(x) \, dx + \int_{-\infty}^{\infty} y f(y) \, dy = \mathbf{E} + \mathbf{E}.
\]

(Е5) Если \( \geqslant 0 \), то \( \mathbf{E} \geqslant 0 \).
Доказательство. Неотрицательность означает, что \( a_i \geqslant 0 \) при всех \( i \) в случае дискретного распределения, либо \( f(x) = 0 \) при \( x < 0 \) — для абсолютно непрерывного распределения. И в том, и в другом случае имеем:
\[
\mathbf{E} = \sum a_i p_i \geqslant 0 \quad \text{или} \quad \mathbf{E} = \int_0^{\infty} x f(x) \, dx \geqslant 0.
\]

Из свойства (Е5) вытекает множество полезных утверждений, например:
Следствие 7. Если \( \leqslant \), то \( \mathbf{E} \leqslant \mathbf{E} \).
Следствие 8. Если \( a \leqslant \leqslant b \), то \( a \leqslant \mathbf{E} \leqslant b \).
Второе особенно очевидно: центр тяжести стержня не может находиться вне отрезка, если вся масса сосредоточена на этом отрезке.

(Е7) Математическое ожидание произведения независимых случайных величин равно произведению их математических ожиданий.
Доказательство. В равенстве (18) заменим сложение умножением и плотность совместного распределения произведением плотностей:

\[
\mathbf{E}(+) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} xy f(x) f(y) \, dx \, dy =
\]
\[
= \int_{-\infty}^{\infty} x f(x) \, dx \int_{-\infty}^{\infty} y f(y) \, dy = \mathbf{E} \mathbf{E}.
\]