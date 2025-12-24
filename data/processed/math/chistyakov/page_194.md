---
source_image: page_194.png
page_number: 194
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.52
tokens: 8293
characters: 1436
timestamp: 2025-12-24T07:30:46.035507
finish_reason: stop
---

По формуле (7.2.11)
\[
Me^{is\xi_h} = 1 + isM_{\xi_h} - \frac{s^2}{2} M_{\xi_h}^2 + O(|s|^3 M|\xi_h|^3).
\]
Отсюда и из свойства 4° следует
\[
Me^{is\xi_h} = 1 + is(ah) - \frac{s^2bh}{2} + o(h).
\]
Таким образом,
\[
f_{t+h}(s) = \left(1 + is(ah) - \frac{s^2bh}{2} + o(h)\right)f_t(s)
\]
и
\[
\frac{f_{t+h}(s) - f_t(s)}{h} = \left(isa - \frac{s^2b}{2}\right)f_t(s) + o(1).
\]
Переходя в этом равенстве к пределу при \( h \to 0 \), получим
\[
\frac{df_t(s)}{dt} = \left(isa - \frac{s^2b}{2}\right)f_t(s).
\]
Отсюда, учитывая начальное условие \( f_0(s) = 1 \), найдем
\[
f_t(s) = e^{is(at) - \frac{(bt)s^2}{2}}.
\]
Полученная характеристическая функция величины \( \xi_t \) соответствует нормальному распределению с параметрами \((at, \sqrt{bt})\). Теорема доказана.

Найдем совместное распределение \( \xi_{t_1}, \ldots, \xi_{t_n} \). Совместное распределение приращений \( \eta_k = \xi_{t_{k+1}} - \xi_{t_k}, k = 1, 2, \ldots, n, (\xi_{t_0} = 0) \) легко выписывается. Тогда, используя равенства
\[
\xi_{t_1} = \eta_1, \quad \xi_{t_2} = \eta_1 + \eta_2, \ldots, \quad \xi_{t_n} = \eta_1 + \eta_2 + \ldots + \eta_n,
\]
получим
\[
P(\xi_{t_1} < x_1, \xi_{t_2} < x_2, \ldots, \xi_{t_n} < x_n) =
= P(\eta_1 < x_1, \eta_1 + \eta_2 < x_2, \ldots, \eta_1 + \ldots + \eta_n < x_n) =
= \int \cdots \int \prod_{k=1}^n \frac{1}{\sqrt{2\pi b(t_k - t_{k-1})}} e^{-\frac{\left(u_k - a(t_k - t_{k-1})\right)^2}{2b(t_k - t_{k-1})}} du_1 \ldots du_n,
\]