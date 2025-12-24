---
source_image: page_207.png
page_number: 207
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.88
tokens: 5201
characters: 2068
timestamp: 2025-12-24T07:31:07.165470
finish_reason: stop
---

Полагая \( z = \left( v - \rho \frac{x_1 - a_1}{\sigma_1} \right) / \sqrt{1 - \rho^2} \), найдем

\[
p_{\xi_1}(x_1) = \frac{1}{\sqrt{2\pi}} e^{-\frac{(x_1 - a_1)^2}{2\sigma_1^2}} \cdot \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\frac{z^2}{2}} dz
\]

и, следовательно,

\[
p_{\xi_1}(x_1) = \frac{1}{\sqrt{2\pi}} e^{-\frac{(x_1 - a_1)^2}{2\sigma_1^2}}
\]

Из этой формулы получим заменой \( a_1, \sigma_1 \) на \( a_2, \sigma_2 \) формулу плотности распределения \( \xi_2 \). Таким образом, одномерные распределения величин \( \xi_1, \xi_2 \) являются нормальными с параметрами \( (a_1, \sigma_1), (a_2, \sigma_2) \) соответственно. Следовательно,

\[
M_{\xi_1} = a_1, \quad D_{\xi_1} = \sigma_1^2, \quad M_{\xi_2} = a_2, \quad D_{\xi_2} = \sigma_2^2.
\]

Полагая в формуле (5.1.7)

\[
n = 2, \quad g(x_1, x_2) = (x_1 - a_1)(x_2 - a_2),
\]

получим

\[
\operatorname{cov}(\xi_1, \xi_2) = M((\xi_1 - a_1)(\xi_2 - a_2)) =
\]
\[
= \frac{1}{2\pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} (x_1 - a_1)(x_2 - a_2) e^{-\frac{1}{2} Q(x_1, x_2)} dx_1 dx_2.
\]

Отсюда заменой переменных

\[
y_1 = \frac{x_1 - a_1}{\sigma_1 \sqrt{1 - \rho^2}}, \quad y_2 = \frac{x_2 - a_2}{\sigma_2 \sqrt{1 - \rho^2}}
\]

получим

\[
\operatorname{cov}(\xi_1, \xi_2) = \frac{(1 - \rho^2) \sigma_1 \sigma_2}{2\pi} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} y_1 y_2 e^{-\frac{1}{2} (y_1^2 - 2\rho y_1 y_2 + y_2^2)} dy_1 dy_2 =
\]
\[
= \frac{(1 - \rho^2) \sigma_1 \sigma_2}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \left\{ y_2 e^{-\frac{y_2^2}{2} (1 - \rho^2)} \left( \int_{-\infty}^{\infty} \frac{y_1}{\sqrt{2\pi}} e^{-\frac{(y_1 - \rho y_2)^2}{2}} dy_1 \right) \right\} dy_2.
\]

Интеграл в круглых скобках можно рассматривать как математическое ожидание нормально распределенной случайной величины с параметрами \( (\rho y_2, 1) \). Следовательно, этот интеграл равен \( \rho y_2 \) и

\[
\operatorname{cov}(\xi_1, \xi_2) = (1 - \rho^2) \sigma_1 \sigma_2 \int_{-\infty}^{\infty} \frac{y_2^2}{\sqrt{2\pi}} e^{-\frac{y_2^2}{2} (1 - \rho^2)} dy_2.
\]