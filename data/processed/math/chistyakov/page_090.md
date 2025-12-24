---
source_image: page_090.png
page_number: 90
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.10
tokens: 8358
characters: 1247
timestamp: 2025-12-24T07:28:01.940716
finish_reason: stop
---

Таким образом,

\[
F_{\xi}(x) = \lim_{y \to \infty} F_{\xi, \eta}(x, y) = F_{\xi, \eta}(x, \infty),
\]
\[
F_{\eta}(y) = \lim_{x \to \infty} F_{\xi, \eta}(x, y) = F_{\xi, \eta}(\infty, y).
\]

Если \((\xi, \eta)\) — абсолютно непрерывный вектор, то

\[
F_{\xi}(x) = \int_{-\infty}^{x} \left( \int_{-\infty}^{\infty} p_{\xi, \eta}(u, v) dv \right) du = \int_{-\infty}^{x} p_{\xi}(u) du,
\]

где функция

\[
p_{\xi}(x) = \int_{-\infty}^{\infty} p_{\xi, \eta}(x, v) dv
\]

является плотностью распределения величины \(\xi\). Аналогично находим

\[
p_{\eta}(y) = \int_{-\infty}^{\infty} p_{\xi, \eta}(u, y) du.
\]

Пусть вектор \((\xi, \eta)\) дискретного типа:

\[
P(\xi = x_i, \eta = y_j) = p_{ij}, \quad i, j = 1, 2, \ldots,
\]

и \(\sum_{i, j=1}^{\infty} p_{ij} = 1\). Найдем одномерные распределения, соответствующие (3.11). Имеем

\[
P(\xi = x_i) = \sum_{j=1}^{\infty} P(\xi = x_i, \eta = y_j) = \sum_{j=1}^{\infty} p_{ij}.
\]

Пусть

\[
p_{i \cdot} = \sum_{j=1}^{\infty} p_{ij}, \quad p_{\cdot j} = \sum_{i=1}^{\infty} p_{ij}.
\]

В этих обозначениях получим

\[
P(\xi = x_i) = p_{i \cdot}, \quad P(\eta = y_j) = p_{\cdot j}.
\]

Мы получили формулы, позволяющие по совместному распределению двумерной величины находить одномерные распределения.