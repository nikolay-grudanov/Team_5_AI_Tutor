---
source_image: page_100.png
page_number: 100
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.13
tokens: 11773
characters: 2334
timestamp: 2025-12-24T08:29:18.588270
finish_reason: stop
---

Пользуясь определением и свойствами слабой сходимости, и заметив, что функция распределения \( \Phi_{a,\sigma^2}(x) \) любого нормального закона непрерывна всюду на \( \mathbb{R} \) (почему?), утверждение ЦПТ можно сформулировать любым из следующих способов:

**Следствие 19.** Пусть \( \xi_1, \xi_2, \ldots \) — независимые и одинаково распределенные случайные величины с конечной и ненулевой дисперсией. Следующие утверждения эквивалентны друг другу и равносильны утверждению ЦПТ.

• Для любых вещественных \( x < y \) при \( n \to \infty \) имеет место сходимость

\[
\mathrm{P}\left( x < \frac{S_n - n \mathbf{E} \xi_1}{\sqrt{n} \mathbf{D} \xi_1} < y \right) \to \Phi_{0,1}(y) - \Phi_{0,1}(x) = \int_x^y \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt;
\]

• Для любых вещественных \( x < y \) при \( n \to \infty \) имеет место сходимость

\[
\mathrm{P}\left( x \leqslant \frac{S_n - n \mathbf{E} \xi_1}{\sqrt{n} \mathbf{D} \xi_1} \leqslant y \right) \to \Phi_{0,1}(y) - \Phi_{0,1}(x) = \int_x^y \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt;
\]

• Для любых вещественных \( x < y \) при \( n \to \infty \) имеет место сходимость

\[
\mathrm{P}\left( x \leqslant \frac{S_n - n \mathbf{E} \xi_1}{\sqrt{n}} \leqslant y \right) \to \Phi_{0,\mathbf{D} \xi_1}(y) - \Phi_{0,\mathbf{D} \xi_1}(x) = \frac{1}{\sqrt{\mathbf{D} \xi_1}} \int_x^y \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt;
\]

• Если \( \eta \) — произвольная с. в. со стандартным нормальным распределением, то

\[
\frac{S_n - n \mathbf{E} \xi_1}{\sqrt{n} \mathbf{D} \xi_1} \Rightarrow \eta \in \mathbf{N}_{0,1}, \quad \frac{S_n - n \mathbf{E} \xi_1}{\sqrt{n}} \Rightarrow \sqrt{\mathbf{D} \xi_1} \cdot \eta \in \mathbf{N}_{0,\mathbf{D} \xi_1}, \quad \sqrt{n} \left( \frac{S_n}{n} - \mathbf{E} \xi_1 \right) \Rightarrow \sqrt{\mathbf{D} \xi_1} \cdot \eta \in \mathbf{N}_{0,\mathbf{D} \xi_1}.
\]

Замечание 25. Еще раз напомним, что функция распределения стандартного нормального закона ищется либо по соответствующей таблице в справочнике, либо с помощью какого-либо программного обеспечения, но никак не путем нахождения первообразной.

Мы докажем ЦПТ и ЗБЧ в форме Хинчина несколькими главами позднее. Нам потребуется для этого познакомиться с мощным математическим инструментом, который в математике обычно называют «преобразованиями Фурье», а в теории вероятностей — «характеристическими функциями».