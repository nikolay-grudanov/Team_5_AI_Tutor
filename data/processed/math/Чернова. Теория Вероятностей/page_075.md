---
source_image: page_075.png
page_number: 75
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.73
tokens: 11686
characters: 2062
timestamp: 2025-12-24T08:28:02.375686
finish_reason: stop
---

Пример 39. Нормальное распределение \( \mathbf{N}_{a, \sigma^2} \)

Мы знаем, что если \( \xi \in \mathbf{N}_{a, \sigma^2} \), то \( \eta = \frac{\xi - a}{\sigma} \in \mathbf{N}_{0,1} \), и \( \mathbf{E} \eta = 0, \mathbf{D} \eta = 1 \). Поэтому

\[
\mathbf{E} \xi = \mathbf{E} (\sigma \eta + a) = \sigma \mathbf{E} \eta + a = a; \qquad \mathbf{D} \xi = \mathbf{D} (\sigma \eta + a) = \sigma^2 \mathbf{D} \eta = \sigma^2.
\]

(16)

Какими свойствами математического ожидания и дисперсии мы воспользовались в формуле (16)?

Пример 40. Показательное (экспоненциальное) распределение \( \mathbf{E}_\alpha \)

Найдем для произвольного \( k \in \mathbb{N} \) момент порядка \( k \).

\[
\mathbf{E} \xi^k = \int_{-\infty}^{\infty} x^k f_\xi(x) \, dx = \int_0^{\infty} x^k \alpha e^{-\alpha x} \, dx = \frac{1}{\alpha^k} \int_0^{\infty} (\alpha x)^k e^{-\alpha x} d(\alpha x) = \frac{k!}{\alpha^k}.
\]

В последнем равенстве мы воспользовались гамма-функцией Эйлера: \( \Gamma(k+1) = \int_0^{\infty} u^k e^{-u} du = k! \). Соответственно,

\[
\mathbf{E} \xi = \frac{1}{\alpha}, \qquad \mathbf{E} \xi^2 = \frac{2}{\alpha^2}, \qquad \mathbf{D} \xi = \mathbf{E} \xi^2 - (\mathbf{E} \xi)^2 = \frac{1}{\alpha^2}.
\]

Пример 41. Стандартное распределение Коши \( \mathbf{C}_{0,1} \)

Распределение Коши. Говорят, что \( \xi \) имеет распределение Коши с параметрами \( a, \sigma^2 \), где \( a \in \mathbb{R}, \sigma > 0 \), и пишут (по крайней мере мы так будем писать) \( \xi \in \mathbf{C}_{a, \sigma^2} \), если

\[
f_\xi(x) = \frac{\sigma}{\pi (\sigma^2 + (x - a)^2)} \quad \text{для всех} \quad x \in \mathbb{R}.
\]

Распределение Коши имеет, например, абсцисса точки пересечения луча, посланного из точки \( (a, \sigma) \) под наугаду выбранным углом \( \varphi \in \mathbf{U}_{-\pi/2, \pi/2} \), с осью \( OX \). Это полезно доказать!

Математическое ожидание для распределения Коши не существует, поскольку \( \mathbf{E} |\xi| = \int_{-\infty}^{\infty} |x| \frac{1}{\pi (1 + x^2)} dx \) расходится (подынтегральная функция ведет себя на бесконечности как \( 1/x \)).