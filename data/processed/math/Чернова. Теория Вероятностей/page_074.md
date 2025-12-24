---
source_image: page_074.png
page_number: 74
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.93
tokens: 11677
characters: 1794
timestamp: 2025-12-24T08:27:58.948979
finish_reason: stop
---

Пример 36. Распределение Пуассона \( \Pi_\lambda \)

\[
E \xi = \sum_{k=0}^{\infty} k \cdot \frac{\lambda^k}{k!} e^{-\lambda} = e^{-\lambda} \sum_{k=1}^{\infty} k \cdot \frac{\lambda^k}{k!} = e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^k}{(k-1)!} = \lambda e^{-\lambda} \sum_{k=1}^{\infty} \frac{\lambda^{k-1}}{(k-1)!} = \lambda e^{-\lambda} \sum_{j=0}^{\infty} \frac{\lambda^j}{j!} = \lambda e^{-\lambda} e^{\lambda} = \lambda.
\]

Доказать, что \( E \xi^2 = \lambda^2 + \lambda \), так что \( D \xi = \lambda \).

Пример 37. Равномерное распределение \( U_{a,b} \)

\[
E \xi = \int_{-\infty}^{\infty} x f_{\xi}(x) dx = \int_a^b x \frac{1}{b-a} dx = \frac{a+b}{2};
\]

\[
E \xi^2 = \int_{-\infty}^{\infty} x^2 f_{\xi}(x) dx = \int_a^b x^2 \frac{1}{b-a} dx = \frac{b^3 - a^3}{3(b-a)} = \frac{a^2 + ab + b^2}{3}; \quad D \xi = E \xi^2 - (E \xi)^2 = \frac{(b-a)^2}{12}.
\]

Пример 38. Стандартное нормальное распределение \( N_{0,1} \)

\[
E \xi = \int_{-\infty}^{\infty} x f_{\xi}(x) dx = \int_{-\infty}^{\infty} x \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 0,
\]

поскольку под интегралом стоит нечетная функция, и сам интеграл абсолютно сходится (за счет быстро убывающей \( e^{-x^2/2} \)).

\[
E \xi^2 = \int_{-\infty}^{\infty} x^2 \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 2 \int_0^{\infty} x^2 \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = -2 \int_0^{\infty} x \frac{1}{\sqrt{2\pi}} de^{-x^2/2} = -2x \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \Bigg|_0^{\infty} + 2 \int_0^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 1.
\]

Последнее равенство следует из того, что \( 2 \int_0^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx \), а интеграл по всей прямой от плотности любого распределения равен 1. Поэтому \( D \xi = E \xi^2 - (E \xi)^2 = 1 - 0 = 1. \)