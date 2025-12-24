---
source_image: page_162.png
page_number: 162
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.45
tokens: 6444
characters: 1843
timestamp: 2025-12-24T08:12:00.446616
finish_reason: stop
---

Доказательство. Интегрирование по частям показывает, что

\[
\int_{-1}^{1} \frac{d^m}{dx^m}(x^2 - 1)^m \frac{d^n}{dx^n}(x^2 - 1)^n \, dx = (-1)^m \int_{-1}^{1} (x^2 - 1)^m \frac{d^{n+m}}{dx^{n+m}}(x^2 - 1)^n \, dx,
\]

поскольку \( \frac{d^k}{dx^k}(x^2 - 1)^m \) обращается в нуль, когда \( x = \pm 1 \) и \( k \leq m - 1 \).

Можно считать, что \( m \geq n \). Если \( m > n \), то \( \frac{d^{n+m}}{dx^{n+m}}(x^2 - 1)^n = 0 \). Остаётся разобрать случай, когда \( m = n \). В этом случае

\[
\int_{-1}^{1} \left( \frac{d^n}{dx^n}(x^2 - 1) \right)^2 dx = (-1)^n (2n)! \int_{-1}^{1} (x^2 - 1)^n dx =
\]
\[
= 2(2n)! \int_{0}^{1} (x^2 - 1)^n dx = 2(2n)! \int_{0}^{\pi/2} \sin^{2n+1} \theta \, d\theta;
\]

мы сделали замену \( x = \cos \theta \) и поменяли местами верхний и нижний пределы интегрирования. Пусть \( U_n = \int_{0}^{\pi/2} \sin^{2n+1} \theta \, d\theta \). Интегрируя по частям, получаем

\[
U_n = - \int_{0}^{\pi/2} \sin^{2n} \theta \, d(\cos \theta) = -\sin^{2n} \theta \cos \theta|_{0}^{\pi/2} + \int_{0}^{\pi/2} \cos \theta \, d(\sin^{2n} \theta) =
\]
\[
= 2n \int_{0}^{\pi/2} \sin^{2n-1} \theta \cos^2 \theta \, d\theta = 2n U_{n-1} - 2n U_n,
\]

т. е. \( U_n = \frac{2n}{2n+1} U_{n-1} \). Учитывая, что \( U_0 = 1 \), получаем

\[
U_n = \frac{2 \cdot 4 \cdot \ldots \cdot (2n)}{3 \cdot 5 \cdot \ldots \cdot (2n+1)}.
\]

Таким образом,

\[
\int_{-1}^{1} (P_n(x))^2 \, dx = \frac{1}{2^{2n}(n!)^2} \cdot 2(2n)! \cdot \frac{2 \cdot 4 \cdot \ldots \cdot (2n)}{3 \cdot 5 \cdot \ldots \cdot (2n+1)} = \frac{2}{2n+1},
\]

поскольку \( 2 \cdot 4 \cdot \ldots \cdot (2n) = 2^n n! \) и \( 2^n n! \left( 3 \cdot 5 \cdot \ldots \cdot (2n+1) \right) = (2n+1)! \).

Теорема 10.2.2. Любые три последовательных многочлена Лежандра связаны соотношением

\[
P_{n+1}(x) = \frac{2n+1}{n+1} x P_n(x) - \frac{n}{n+1} P_{n-1}(x), \quad n \geq 1.
\]