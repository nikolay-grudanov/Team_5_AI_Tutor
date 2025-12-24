---
source_image: page_058.png
page_number: 58
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.53
tokens: 11709
characters: 1934
timestamp: 2025-12-24T08:27:08.663782
finish_reason: stop
---

Из свойства (F2) функции совместного распределения вытекает следующее утверждение. Для \( n > 2 \) это утверждение, как и свойство (F2), выглядит существенно иначе!

**Теорема 22.** Если случайные величины \( \xi_1, \xi_2 \) имеют абсолютно непрерывное совместное распределение с плотностью \( f(x_1, x_2) \), то \( \xi_1 \) и \( \xi_2 \) в отдельности также имеют абсолютно непрерывное распределение с плотностями:

\[
f_{\xi_1}(s_1) = \int_{-\infty}^{\infty} f(s_1, s_2) \, ds_2; \qquad f_{\xi_2}(s_2) = \int_{-\infty}^{\infty} f(s_1, s_2) \, ds_1.
\]

**Доказательство.** По (F2),

\[
F_{\xi_1}(x_1) = \lim_{x_2 \to \infty} F_{\xi_1, \xi_2}(x_1, x_2) = \lim_{x_2 \to \infty} \int_{-\infty}^{x_1} \left( \int_{-\infty}^{x_2} f(s_1, s_2) \, ds_2 \right) ds_1 = \int_{-\infty}^{x_1} \left( \int_{-\infty}^{\infty} f(s_1, s_2) \, ds_2 \right) ds_1;
\]
аналогично
\[
F_{\xi_2}(x_2) = \lim_{x_1 \to \infty} F_{\xi_1, \xi_2}(x_1, x_2) = \lim_{x_1 \to \infty} \int_{-\infty}^{x_2} \left( \int_{-\infty}^{x_1} f(s_1, s_2) \, ds_1 \right) ds_2 = \int_{-\infty}^{x_2} \left( \int_{-\infty}^{\infty} f(s_1, s_2) \, ds_1 \right) ds_2.
\]

9.3 Независимость случайных величин

**Определение 34.** Случайные величины \( \xi_1, \ldots, \xi_n \) **независимы**, если для любого набора множеств \( B_1 \subseteq \mathbb{R}, \ldots, B_n \subseteq \mathbb{R} \) (из борелевской \( \sigma \)-алгебры — для тех, кто прочитал, что это такое, или произвольных — для тех, кто не прочитал) имеет место равенство:
\[
\mathbf{P}(\xi_1 \in B_1, \ldots, \xi_n \in B_n) = \mathbf{P}(\xi_1 \in B_1) \cdot \ldots \cdot \mathbf{P}(\xi_n \in B_n).
\]
Это определение можно сформулировать в терминах функций распределения:

**Определение 35.** Случайные величины \( \xi_1, \ldots, \xi_n \) **независимы**, если для любых \( x_1, \ldots, x_n \) имеет место равенство:
\[
F_{\xi_1, \ldots, \xi_n}(x_1, \ldots, x_n) = F_{\xi_1}(x_1) \cdot \ldots \cdot F_{\xi_n}(x_n).
\]