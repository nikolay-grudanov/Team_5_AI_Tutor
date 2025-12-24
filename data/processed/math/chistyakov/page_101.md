---
source_image: page_101.png
page_number: 101
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.21
tokens: 5484
characters: 1415
timestamp: 2025-12-24T07:28:26.792122
finish_reason: stop
---

§ 51 ФУНКЦИИ ОТ СЛУЧАЙНЫХ ВЕЛИЧИН

сумма \( \xi_1 + \xi_2 \) также абсолютно непрерывна и ее плотность распределения определяется по формуле

\[
p_{\xi_1 + \xi_2}(x) = \int_{-\infty}^{x} p_{\xi_1}(u) p_{\xi_2}(x-u) du.
\] (5.6)

Доказательство. Найдем сначала

\[
F_{\xi_1 + \xi_2}(x) = P(\xi_1 + \xi_2 < x) = P((\xi_1, \xi_2) \in D_x),
\]

где \( D_x = \{(u, v): u + v < x\} \). Так как по условию теоремы величины \( \xi_1 \) и \( \xi_2 \) независимы, то их плотность совместного распределения согласно (4.9) равна

\[
p_{\xi_1 \xi_2}(u, v) = p_{\xi_1}(u) p_{\xi_2}(v),
\]

и, следовательно, по формуле (3.3) найдем

\[
F_{\xi_1 + \xi_2}(x) = \iint_{D_x} p_{\xi_1}(u) p_{\xi_2}(v) du dv =
\]
\[
= \int_{-\infty}^{\infty} p_{\xi_1}(u) \left( \int_{-\infty}^{-u+x} p_{\xi_2}(v) dv \right) du.
\]

Отсюда, полагая \( v = z - u \), получим

\[
F_{\xi_1 + \xi_2}(x) = \int_{-\infty}^{\infty} p_{\xi_1}(u) du \int_{-\infty}^{x} p_{\xi_2}(z-u) dz =
\]
\[
= \int_{-\infty}^{x} \left( \int_{-\infty}^{\infty} p_{\xi_1}(u) p_{\xi_2}(z-u) du \right) dz = \int_{-\infty}^{x} p_{\xi_1 + \xi_2}(z) dz,
\]

где

\[
p_{\xi_1 + \xi_2}(x) = \int_{-\infty}^{x} p_{\xi_1}(u) p_{\xi_2}(x-u) du.
\]

Теорема доказана.

Отметим, что вместе с (5.6) верна формула

\[
p_{\xi_1 + \xi_2}(x) = \int_{-\infty}^{x} p_{\xi_1}(x-u) p_{\xi_2}(u) du.
\]

Используя формулу (5.6), можно показать, что сумма независимых нормально распределенных слу-