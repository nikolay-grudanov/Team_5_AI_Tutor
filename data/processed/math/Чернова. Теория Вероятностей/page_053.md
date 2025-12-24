---
source_image: page_053.png
page_number: 53
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.81
tokens: 11613
characters: 2085
timestamp: 2025-12-24T08:26:49.053278
finish_reason: stop
---

Мы часто будем использовать обозначение \( \Phi_{a, \sigma^2}(x) \) для функции распределения нормального распределения с параметрами \( a \) и \( \sigma^2 \).

Исключительно полезно нарисовать график плотности и функции распределения (отметив точки экстремума, перегибов, посчитав значение в точке максимума плотности и расстояние между точками перегибов). График плотности и функции распределения нормального распределения можно также посмотреть здесь: http://www.nsu.ru/mmf/tvims/chernova/PlotDist.html.

**Стандартное нормальное распределение**

Нормальное распределение \( N_{a, \sigma^2} \) при \( a = 0 \) и \( \sigma^2 = 1 \) называется *стандартным нормальным распределением*. Плотность стандартного нормального распределения имеет вид \( f_\xi(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2} \) при любом \( x \in \mathbb{R} \), а функция распределения \( \Phi_{0,1}(x) = \int_{-\infty}^{x} \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt \) табулирована (то есть ее значения вычислены при многих \( x \)) почти во всех математических справочниках. Установим связь между \( \Phi_{a, \sigma^2} \) и \( \Phi_{0,1} \).

**Свойство 7.** Для любого \( x \in \mathbb{R} \) справедливо соотношение \( \Phi_{a, \sigma^2}(x) = \Phi_{0,1}\left( \frac{x-a}{\sigma} \right) \).

**Доказательство.**

\[
\Phi_{a, \sigma^2}(x) = \int_{-\infty}^{x} \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(t-a)^2}{2\sigma^2}} dt = \begin{bmatrix}
\text{замена переменных} \\
y = \frac{t-a}{\sigma}, \quad dt = \sigma dy \\
t = x \implies y = \frac{x-a}{\sigma}
\end{bmatrix} = \int_{-\infty}^{\frac{x-a}{\sigma}} \frac{1}{\sqrt{2\pi}} e^{-y^2/2} dy = \Phi_{0,1}\left( \frac{x-a}{\sigma} \right).
\]

То же самое на языке случайных величин можно сформулировать так:

**Следствие 6.** Если \( \xi \in N_{a, \sigma^2} \), то \( \eta = \frac{\xi - a}{\sigma} \in N_{0,1} \).

**Доказательство.**

\[
F_\eta(x) = \mathbf{P}(\eta < x) = \mathbf{P}\left( \frac{\xi - a}{\sigma} < x \right) = \mathbf{P}(\xi < \sigma x + a) = \Phi_{a, \sigma^2}(\sigma x + a) = \Phi_{0,1}\left( \frac{\sigma x + a - a}{\sigma} \right) = \Phi_{0,1}(x).
\]