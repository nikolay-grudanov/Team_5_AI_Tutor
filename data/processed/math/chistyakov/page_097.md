---
source_image: page_097.png
page_number: 97
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.27
tokens: 5566
characters: 2096
timestamp: 2025-12-24T07:28:30.609618
finish_reason: stop
---

Условие (4.5) обобщается на случай n дискретных величин \( \xi_1, \xi_2, \ldots, \xi_n \) следующим образом. Случайные величины с законом распределения (3.2) независимы тогда и только тогда, когда

\[
P(\xi_1 = x_{k_1}, \ldots, \xi_n = x_{kn}) =
= P(\xi_1 = x_{k_1}) \ldots P(\xi_n = x_{kn})
\] (4.15)

при любых \( x_{k_1}, \ldots, x_{kn} \).

Рассмотрим пример, связанный со схемой Бернулли. В схеме Бернулли с n испытаниями элементарными событиями являются последовательности вида (3.2.3). Пусть \( \xi_k = 1, k = 1, 2, \ldots, n \), если в последовательности (3.2.3) на k-м месте был успех (Y) и \( \xi_k = 0 \) в противном случае. Событие \( (\xi_1 = \varepsilon_1, \xi_2 = \varepsilon_2, \ldots, \xi_n = \varepsilon_n) \), где \( \varepsilon_k \) принимают значение 0 или 1, однозначно определяет элементарное событие II, следовательно,

\[
P(\xi_1 = \varepsilon_1, \xi_2 = \varepsilon_2, \ldots, \xi_n = \varepsilon_n) =
= p^{\varepsilon_1} q^{1-\varepsilon_1} p^{\varepsilon_2} q^{1-\varepsilon_2} \ldots p^{\varepsilon_n} q^{1-\varepsilon_n},
\] (4.16)

так как \( p^{\varepsilon_k} q^{1-\varepsilon_k} = p \) при \( \varepsilon_k = 1, \quad p^{\varepsilon_k} q^{1-\varepsilon_k} = q \) при \( \varepsilon_k = 0 \). Заметим, что

\[
\sum_{\varepsilon_i = 0}^1 p^{\varepsilon_i} q^{1-\varepsilon_i} = p + q = 1.
\]

Учитывая это замечание из (4.16), легко получить одномерные распределения. Например,

\[
P(\xi_1 = \varepsilon_1) =
= \sum_{\varepsilon_2 = 0}^1 \sum_{\varepsilon_3 = 0}^1 \ldots \sum_{\varepsilon_n = 0}^1 P(\xi_1 = \varepsilon_1, \xi_2 = \varepsilon_2, \ldots, \xi_n = \varepsilon_n) =
= p^{\varepsilon_1} q^{1-\varepsilon_1} \sum_{\varepsilon_2 = 0}^1 \ldots \sum_{\varepsilon_n = 0}^1 p^{\varepsilon_2} q^{1-\varepsilon_2} \ldots p^{\varepsilon_n} q^{1-\varepsilon_n} = p^{\varepsilon_1} q^{1-\varepsilon_1}.
\]

Аналогично находим

\[
P(\xi_k = \varepsilon_k) = p^{\varepsilon_k} q^{1-\varepsilon_k}, \quad k = 1, 2, \ldots, n. \tag{4.17}
\]

Используя (4.16), (4.17) для проверки (4.15), получим, что величины \( \xi_1, \xi_2, \ldots, \xi_n \) независимы. В § 2 гл. 3