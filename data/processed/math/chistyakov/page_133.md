---
source_image: page_133.png
page_number: 133
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.26
tokens: 5182
characters: 1429
timestamp: 2025-12-24T07:29:07.334451
finish_reason: stop
---

§ 2. Закон больших чисел

Во введении был отмечен экспериментальный факт, состоящий в том, что в некоторой длинной серии опытов частота появления события \( A \) сближается с определенным числом, которое можно рассматривать как вероятность события \( A \). В математической модели серии опытов этот факт будет доказан. Сначала докажем более общую теорему.

Теорема 2.1. Если случайные величины \( \xi_1, \xi_2, \ldots, \xi_n, \ldots \) попарно независимы и

\[
\lim_{n \to \infty} \frac{1}{n^2} \sum_{k=1}^n D\xi_k = 0,
\]

то для любого \( \varepsilon > 0 \)

\[
\lim_{n \to \infty} P \left( \left| \frac{\xi_1 + \xi_2 + \ldots + \xi_n}{n} - \frac{M\xi_1 + M\xi_2 + \ldots + M\xi_n}{n} \right| < \varepsilon \right) = 1.
\]

Доказательство. Положим

\[
\eta_n = \frac{\xi_1 + \xi_2 + \ldots + \xi_n}{n}.
\]

Утверждение теоремы равносильно тому, что при любом \( \varepsilon > 0 \)

\[
\lim_{n \to \infty} P(|\eta_n - M\eta_n| \geq \varepsilon) = 0.
\]

Так как случайные величины \( \xi_1, \ldots, \xi_n \) попарно независимы, то

\[
D\eta_n = \frac{1}{n^2} \sum_{k=1}^n D\xi_k.
\]

По неравенству Чебышева

\[
P(|\eta_n - M\eta_n| \geq \varepsilon) \leq \frac{D\eta_n}{\varepsilon^2}.
\]

Отсюда, воспользовавшись (2.3) и (2.1), получим (2.2).

Теорема доказана.

Случайные величины \( \xi_1, \ldots, \xi_n, \ldots \) называют некоррелированными, если \( \operatorname{cov}(\xi_i, \xi_j) = 0 \) при любых \( i, j, i \neq j \).