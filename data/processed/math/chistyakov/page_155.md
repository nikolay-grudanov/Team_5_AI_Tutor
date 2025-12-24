---
source_image: page_155.png
page_number: 155
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.92
tokens: 5163
characters: 1244
timestamp: 2025-12-24T07:29:35.640687
finish_reason: stop
---

§ 1. Закон больших чисел

В этом параграфе будет доказана теорема 2.3 гл. 6 без предположения конечности дисперсии. Случайные величины бесконечной последовательности \( \xi_1, \xi_2, \ldots, \xi_n, \ldots \) называются независимыми, если при любом \( n \) независимы величины \( \xi_1, \xi_2, \ldots, \xi_n \).

Теорема 1.1. Пусть случайные величины \( \xi_1, \xi_2, \ldots, \xi_n, \ldots \) независимы, одинаково распределены и имеют математическое ожидание \( M\xi_k = a, k = 1, 2, \ldots \). Тогда при любом \( \varepsilon > 0 \)

\[
\lim_{n \to \infty} P \left( \left| \frac{\xi_1 + \xi_2 + \ldots + \xi_n}{n} - a \right| < \varepsilon \right) = 1.
\]

Доказательство. Характеристические функции \( f_{\xi_k}(t), k = 1, 2, \ldots \), одинаковы. Поэтому можно положить \( f_{\xi_k}(t) = f(t) \). Из существования \( M\xi_k \) следует, что верно разложение (7.2.9):

\[
f(t) = 1 + ita + t\varepsilon(t),
\]
где \( \varepsilon(t) \to 0 \) при \( t \to 0 \). Положим
\[
\eta_n = \frac{\xi_1 + \xi_2 + \ldots + \xi_n}{n}.
\]
Так как случайные величины независимы, то по теореме 2.3 гл. 7
\[
f_{\xi_1 + \ldots + \xi_n}(t) = [f(t)]^n.
\]
Отсюда по теореме 2.1 (3°) гл. 7 находим
\[
f_{\eta_n}(t) = \left[ f \left( \frac{t}{n} \right) \right]^n.
\]