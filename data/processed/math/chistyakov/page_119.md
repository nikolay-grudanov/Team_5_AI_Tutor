---
source_image: page_119.png
page_number: 119
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.41
tokens: 5419
characters: 1614
timestamp: 2025-12-24T07:28:54.480035
finish_reason: stop
---

Вычислим дисперсии некоторых случайных величин.

1. Нормальное распределение. По формулам (4.2.3) и (3.3) в этом случае имеем

\[
D\xi = \frac{1}{\sqrt{2\pi}\sigma} \int_{-\infty}^{\infty} (x-a)^2 e^{-\frac{(x-a)^2}{2\sigma^2}} dx.
\]

Отсюда, полагая \( x = \sigma y + a \), получим

\[
D\xi = \sigma^2 \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} y^2 e^{-\frac{y^2}{2}} dy = \sigma^2 \frac{1}{\sqrt{2\pi}} \left( -\int_{-\infty}^{\infty} y d\left(e^{-\frac{y^2}{2}}\right) \right) =
\]
\[
= \sigma^2 \left[ -y \frac{e^{-\frac{y^2}{2}}}{\sqrt{2\pi}} \Bigg|_{-\infty}^{\infty} + \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{-\frac{y^2}{2}} dy \right].
\]

Первое слагаемое в квадратных скобках равно 0, а второе равно 1. Таким образом,

\[
D\xi = \sigma^2.
\]

В § 5 гл. 4 было показано, что линейная функция \( \eta = A\xi + B \) от нормально распределенной случайной величины \( \xi \) имеет нормальное распределение. В § 2 был указан способ вычисления \( M\eta \), не связанный с доказательством нормальности \( \eta \) (см. формулу (2.2)). Найдем теперь \( D\eta \). Нетрудно показать, что случайная величина, являющаяся постоянной, независима с любой случайной величиной. Следовательно, при вычислении \( D\eta = D(A\xi + B) \) можно воспользоваться формулой (3.5). Тогда

\[
D\eta = D(A\xi + B) = D(A\xi) + DB = A^2 D\xi = A^2 \sigma^2.
\]

2. Равномерное распределение. По формулам (4.2.5), (3.3) и (1.13)

\[
D\xi = \int_{-\infty}^{\infty} \left( x - \frac{a+b}{2} \right)^2 p_{\xi}(x) dx = \frac{1}{b-a} \int_{a}^{b} \left( x - \frac{a+b}{2} \right)^2 dx.
\]

Отсюда

\[
D\xi = \frac{(b-a)^2}{12},
\]