---
source_image: page_206.png
page_number: 206
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.67
tokens: 8210
characters: 1665
timestamp: 2025-12-24T07:31:04.139154
finish_reason: stop
---

§ 2. Двумерное нормальное распределение

В § 4 гл. 4 было дано определение n-мерного нормального распределения (см. (4.4.14)). Рассмотрим более детально случай n = 2. В формуле (4.4.14) положим n = 2,

\[
a_{11} = \frac{1}{(1 - \rho^2) \sigma_1^2}, \quad a_{22} = \frac{1}{(1 - \rho^2) \sigma_2^2},
\]
\[
a_{12} = a_{21} = -\frac{\rho}{(1 - \rho^2) \sigma_1 \sigma_2}, \quad |\rho| < 1.
\]

Тогда
\[
|A| = \begin{vmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{vmatrix} = \frac{1}{(1 - \rho^2) \sigma_1^2 \sigma_2^2}.
\]

Формула (4.4.14) в случае двумерного нормального распределения запишется в виде
\[
p_{\xi_1 \xi_2}(x_1, x_2) = \frac{1}{2 \pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} e^{-\frac{1}{2} Q(x_1, x_2)},
\]
где
\[
Q(x_1, x_2) = \frac{1}{1 - \rho^2} \left[ \frac{(x_1 - a_1)^2}{\sigma_1^2} + \frac{(x_2 - a_2)^2}{\sigma_2^2} - 2\rho \frac{(x_1 - a_1)(x_2 - a_2)}{\sigma_1 \sigma_2} \right].
\]

Найдем одномерные плотности распределения. По формуле (4.3.9)
\[
p_{\xi_1}(x_1) = \int_{-\infty}^{\infty} \frac{1}{2 \pi \sigma_1 \sigma_2 \sqrt{1 - \rho^2}} e^{-\frac{1}{2} Q(x_1, x_2)} dx_2.
\]

Отсюда, воспользовавшись заменой \( v = \frac{x_2 - a_2}{\sigma_2} \) и формулой
\[
Q(x_1, x_2) = \frac{1}{1 - \rho^2} \left[ \frac{(x_1 - a_1)^2}{\sigma_1^2} + v^2 - 2\rho v \frac{x_1 - a_1}{\sigma_1} \right] =
= \frac{1}{1 - \rho^2} \left( v - \rho \frac{x_1 - a_1}{\sigma_1} \right)^2 + \left( \frac{x_1 - a_1}{\sigma_1} \right)^2,
\]
получим
\[
p_{\xi_1}(x_1) = \frac{1}{2 \pi \sigma_1 \sqrt{1 - \rho^2}} e^{-\frac{(x_1 - a_1)^2}{2 \sigma_1^2}} \int_{-\infty}^{\infty} e^{-\frac{1}{2 (1 - \rho^2)} \left( v - \rho \frac{x_1 - a_1}{\sigma_1} \right)^2} dv.
\]