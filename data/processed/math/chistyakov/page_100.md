---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.31
tokens: 8475
characters: 1581
timestamp: 2025-12-24T07:28:20.575985
finish_reason: stop
---

Пример 1. Найдем закон распределения линейной функции от нормальной случайной величины. Пусть случайная величина \( \xi \) имеет нормальное распределение с параметрами \((a, \sigma)\). Покажем, что случайная величина \( \eta = A\xi + B,\ A \neq 0 \), имеет нормальное распределение с параметрами \((Aa + B, |A|\sigma)\).

Плотность распределения \( p_\xi(u) \) величины \( \xi \) задается формулой (2.3). Пусть сначала \( A > 0 \). Тогда

\[
F_\eta(x) = P(A\xi + B < x) = P\left( \xi < \frac{x - B}{A} \right) = \int_{-\infty}^{\frac{x - B}{A}} p_\xi(u) du.
\]

Отсюда, так как \( p_\xi(x) \) и \( F_\eta(x) \) непрерывны при любом \( x \), следует, что существует

\[
p_\eta(x) = F'_\eta(x) = p_\xi\left( \frac{x - B}{A} \right) \cdot \left( \frac{x - B}{A} \right)'_x = \frac{1}{A} p_\xi\left( \frac{x - B}{A} \right).
\] (5.5)

Если \( A < 0 \), то

\[
F_\eta(x) = P(A\xi + B < x) = P\left( \xi > \frac{x - B}{A} \right) =
= 1 - P\left( \xi \leq \frac{x - B}{A} \right) = 1 - \int_{-\infty}^{\frac{x - B}{A}} p_\xi(u) du
\]

и

\[
p_\eta(x) = -\frac{1}{A} p_\xi\left( \frac{x - B}{A} \right).
\]

Объединяя эту формулу с (5.5) и используя (2.3), получим

\[
p_\eta(x) = \frac{1}{|A|} p_\xi\left( \frac{x - B}{A} \right) =
= \frac{1}{|A|} \cdot \frac{1}{\sqrt{2\pi \sigma}} e^{-\frac{\left( \frac{x - B}{A} - a \right)^2}{2\sigma^2}} = \frac{1}{\sqrt{2\pi \sigma_1}} e^{-\frac{(x - a_1)^2}{2\sigma_1^2}},
\]

где

\[
a_1 = Aa + B, \quad \sigma_1 = |A|\sigma.
\]

Теорема 5.2. Если случайные величины \( \xi_1 \) и \( \xi_2 \) абсолютно непрерывны и независимы, то случайная вели-