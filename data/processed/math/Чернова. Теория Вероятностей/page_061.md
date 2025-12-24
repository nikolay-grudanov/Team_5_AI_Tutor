---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.25
tokens: 11745
characters: 2092
timestamp: 2025-12-24T08:27:21.653648
finish_reason: stop
---

\[
= \left[ \begin{array}{l}
\text{Замена: } t = \frac{y - b}{a}, \quad dt = \frac{dy}{a} \\
t = \frac{x - b}{a} \mapsto y = x, \quad t = -\infty \mapsto y = -\infty
\end{array} \right] = \int_{-\infty}^{x} \frac{1}{a} \cdot f_{\xi} \left( \frac{y - b}{a} \right) dy,
\]

то есть при \( a > 0 \) случайная величина \( \eta = a\xi + b \) имеет абсолютно непрерывное распределение с плотностью
\[
f_{\eta}(x) = \frac{1}{a} \cdot f_{\xi} \left( \frac{x - b}{a} \right) = \frac{1}{|a|} \cdot f_{\xi} \left( \frac{x - b}{a} \right).
\]
Пусть теперь \( a < 0 \).

\[
F_{\eta}(x) = F_{a\xi+b}(x) = \mathbf{P}(a\xi + b < x) = \mathbf{P} \left( \xi > \frac{x - b}{a} \right) = \int_{(x-b)/a}^{\infty} f_{\xi}(t) \, dt = \left[ \begin{array}{l}
\text{Замена: } t = \frac{y - b}{a}, \quad dt = \frac{dy}{a} \\
t = \frac{x - b}{a} \mapsto y = x, \quad t = \infty \mapsto y = -\infty
\end{array} \right] =
\]
\[
= \int_{x}^{-\infty} \frac{1}{a} \cdot f_{\xi} \left( \frac{y - b}{a} \right) dy = \int_{-\infty}^{x} \frac{1}{|a|} \cdot f_{\xi} \left( \frac{y - b}{a} \right) dy,
\]

то есть при \( a < 0 \) случайная величина \( \eta = a\xi + b \) имеет абсолютно непрерывное распределение с плотностью
\[
f_{\eta}(x) = \frac{1}{|a|} \cdot f_{\xi} \left( \frac{x - b}{a} \right).
\]

Для произвольной монотонной функции \( g \) (то есть такой, что для любых \( x_1 < x_2 \) либо \( g(x_1) < g(x_2) \) (монотонно возрастающая функция), либо \( g(x_1) > g(x_2) \) (монотонно убывающая функция)) справедливо аналогичное теореме 23 утверждение.

**Теорема 24.** Пусть \( \xi \) имеет функцию распределения \( F_{\xi}(x) \) и плотность распределения \( f_{\xi}(x) \), и функция \( g : \mathbb{R} \to \mathbb{R} \) монотонна. Тогда случайная величина \( \eta = g(\xi) \) имеет плотность распределения
\[
f_{\eta}(x) = \frac{1}{|g'(g^{-1}(x))|} \cdot f_{\xi} \left( g^{-1}(x) \right).
\]
Здесь \( g^{-1} \) — функция, обратная к \( g \), а \( g'(g^{-1}(x)) = (g^{-1}(x))' \) — производная функции \( g \) в точке \( g^{-1}(x) \), она же производная функции \( g^{-1}(x) \).

**Упражнение 17.** Доказать теорему 24.