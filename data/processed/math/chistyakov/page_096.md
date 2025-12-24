---
source_image: page_096.png
page_number: 96
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.65
tokens: 8323
characters: 1615
timestamp: 2025-12-24T07:28:16.435583
finish_reason: stop
---

абсолютно непрерывного типа независимы тогда и только тогда, когда

\[
p_{\xi_1 \xi_2 \ldots \xi_n}(x_1, \ldots, x_n) = p_{\xi_1}(x_1) \ldots p_{\xi_n}(x_n)
\] (4.12)

в точках непрерывности рассматриваемых функций. Положим

\[
p_{\xi_1 \xi_2 \ldots \xi_n}(x_1, x_2, \ldots, x_n) = \prod_{k=1}^n \frac{1}{\sqrt{2 \pi \sigma_k}} e^{-\frac{(x-a_k)^2}{2 \sigma_k^2}}
\] (4.13)

Так как \( p_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) > 0 \) и

\[
\int_{-\infty}^{\infty} \ldots \int_{-\infty}^{\infty} p_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) dx_1 \ldots dx_n =
\]
\[
= \prod_{k=1}^n \int_{-\infty}^{\infty} \frac{1}{\sqrt{2 \pi \sigma_k}} e^{-\frac{(x-a_k)^2}{2 \sigma_k^2}} dx_k = 1,
\]

то функция \( p_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) \) является плотностью распределения. Если (4.13) проинтегрировать по всем переменным от \(-\infty\) до \(+\infty\), кроме \(x_i\), то получится плотность распределения \( \xi_i \):

\[
p_{\xi_i}(x_i) = \frac{1}{\sqrt{2 \pi \sigma_i}} e^{-\frac{(x-a_i)^2}{2 \sigma_i^2}}.
\]

Таким образом, случайные величины с плотностью распределения (4.13) независимы и каждая из них имеет нормальное распределение.

Многомерным нормальным распределением называется распределение с плотностью

\[
p_{\xi_1 \ldots \xi_n}(x_1, \ldots, x_n) = \frac{\sqrt{|A|}}{(2 \pi)^{n/2}} e^{-\frac{1}{2} Q(x_1, \ldots, x_n)},
\] (4.14)

где \( Q = \sum_{i,j=1}^n a_{ij}(x_i - a_i)(x_j - a_j) \) — положительно определенная квадратичная форма, \( |A| \) — определитель матрицы \( A = [a_{ij}] \). Плотность распределения (4.13) является частным случаем (4.14). Случай \( n = 2 \) рассмотрен в приложении 2.