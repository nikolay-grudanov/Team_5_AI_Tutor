---
source_image: page_192.png
page_number: 192
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.25
tokens: 8135
characters: 1506
timestamp: 2025-12-24T07:30:38.907117
finish_reason: stop
---

Доказательство. Пусть \( \varphi_t(x) = M x^{\xi_t} \) — производящая функция \( \xi_t \). По свойству 1° величины \( \xi_{t+h} - \xi_t, \xi_t \) независимы. Следовательно,
\[
\varphi_{t+h}(x) = M x^{\xi_{t+h}} = M x^{(\xi_{t+h} - \xi_t) + \xi_t} = \varphi_t(x) M x^{\xi_{t+h} - \xi_t}.
\]
Так как по свойству 2° величины \( \xi_{t+h} - \xi_t \) и \( \xi_h - \xi_0 = \xi_h \) одинаково распределены, то
\[
M x^{\xi_{t+h} - \xi_t} = M x^{\xi_h}
\]
и при \( h \to 0 \) согласно 4°
\[
M x^{\xi_h} = 1 - \lambda h + x \lambda h + o(h), \quad |x| \leq 1.
\]
Таким образом,
\[
\varphi_{t+h}(x) = \varphi_t(x) (1 - \lambda h + x \lambda h + o(h)).
\]
Отсюда
\[
\frac{\varphi_{t+h}(x) - \varphi_t(x)}{h} = -\lambda (x-1) \varphi_t(x) + o(1).
\]
Переходя к пределу при фиксированном \( x \) и \( h \to 0 \), получим
\[
\frac{d \varphi_t(x)}{dt} = -\lambda (x-1) \varphi_t(x).
\]
Решение этого уравнения с начальным условием \( \varphi_0(x) = 1 \) определяется формулой
\[
\varphi_t(x) = e^{\lambda t (x-1)} = \sum_{k=0}^{\infty} \frac{(\lambda t)^k}{k!} e^{-\lambda t} x^k.
\]
Полученная производящая функция является производящей функцией распределения Пуассона. Теорема доказана.

Используя доказанную теорему, можно найти совместные распределения \( \xi_{t_1}, \ldots, \xi_{t_n} \) при любых \( t_1 < \ldots < t_n \). Очевидно, что
\[
(\xi_{t_1} = k_1, \xi_{t_2} = k_2, \ldots, \xi_{t_n} = k_n) =
= (\xi_{t_1} = k_1, \xi_{t_2} - \xi_{t_1} = k_2 - k_1, \ldots, \xi_{t_n} - \xi_{t_{n-1}} = k_n - k_{n-1}),
\]
(2.1)