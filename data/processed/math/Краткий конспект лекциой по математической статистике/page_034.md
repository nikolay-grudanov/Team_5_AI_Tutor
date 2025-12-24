---
source_image: page_034.png
page_number: 34
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 69.15
tokens: 12484
characters: 3210
timestamp: 2025-12-24T07:04:16.690243
finish_reason: stop
---

Напоминание:

Определение 15. Пусть распределение \( \mathcal{F} \) с функцией распределения \( F \) абсолютно непрерывно. Число \( \tau_\delta \) называется квантилью уровня \( \delta \) распределения \( \mathcal{F} \), если \( F(\tau_\delta) = \delta \).

Итак, \( c = \tau_{1-\varepsilon/2} \), или \( -c = \tau_{\varepsilon/2} \) (квантили стандартного нормального распределения).

![Плотность стандартного нормального распределения и квантили](../images/chapter_3/fig_5.png)

Рис. 5: Плотность стандартного нормального распределения и квантили.

Разрешив неравенство \( -c < \eta < c \) относительно \( a \), получим ДИ

\[
1 - \varepsilon = \mathrm{P}(-c < \eta < c) = \mathrm{P}_a \left( -c < \sqrt{n} \frac{\overline{X} - a}{\sigma} < c \right) = \mathrm{P}_a \left( \overline{X} - \frac{c \sigma}{\sqrt{n}} < a < \overline{X} + \frac{c \sigma}{\sqrt{n}} \right).
\]

Можно подставить \( c = \tau_{1-\varepsilon/2} \):

\[
\mathrm{P}_a \left( \overline{X} - \frac{\tau_{1-\varepsilon/2} \sigma}{\sqrt{n}} < a < \overline{X} + \frac{\tau_{1-\varepsilon/2} \sigma}{\sqrt{n}} \right) = 1 - \varepsilon.
\]

Итак, искомый ДИ уровня доверия \( 1 - \varepsilon \) имеет вид \( \left( \overline{X} - \frac{\tau_{1-\varepsilon/2} \sigma}{\sqrt{n}}, \overline{X} + \frac{\tau_{1-\varepsilon/2} \sigma}{\sqrt{n}} \right) \).

Вопросы, наводящие на размышления.
1. Зачем симметричные квантили? Почему не брать границы для \( \eta \) вида \( \mathrm{P}(\tau_{\varepsilon/3} < \eta < \tau_{1-2\varepsilon/3}) = 1 - \varepsilon \)?
Изобразить эти квантили на графике плотности. Как изменилось расстояние между квантилями? Как изменится длина ДИ?
2. Из двух ДИ одного уровня доверия и разной длины какой следует предпочесть?
3. Какова середина полученного в примере 21 ДИ? Какова его длина? Что происходит с границами ДИ при \( n \to \infty \)?

Пример 22. Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из показательного распределения \( \mathrm{E}_\alpha \), где \( \alpha > 0 \). Требуется построить асимптотический ДИ для параметра \( \alpha \) уровня доверия \( 1 - \varepsilon \).
Вспомним ЦПТ:

\[
\frac{\sum_1^n X_i - n \mathrm{E}_\alpha X_1}{\sqrt{n} D_\alpha X_1} = \sqrt{n} \frac{\overline{X} - \frac{1}{\alpha}}{\frac{1}{\alpha}} = \sqrt{n} (\alpha \overline{X} - 1) \implies \eta \in \mathrm{N}_{0,1}.
\]

По определению слабой сходимости, при \( n \to \infty \)

\[
\mathrm{P}_\alpha \left( -c < \sqrt{n} (\alpha \overline{X} - 1) < c \right) \to \mathrm{P}(-c < \eta < c) = 1 - \varepsilon \quad \text{при } c = \tau_{1-\varepsilon/2}.
\]

То есть

\[
\mathrm{P}_\alpha \left( -\tau_{1-\varepsilon/2} < \sqrt{n} (\alpha \overline{X} - 1) < \tau_{1-\varepsilon/2} \right) =
\]
\[
= \mathrm{P}_\alpha \left( \frac{1}{\overline{X}} - \frac{\tau_{1-\varepsilon/2}}{\sqrt{n} \overline{X}} < \alpha < \frac{1}{\overline{X}} + \frac{\tau_{1-\varepsilon/2}}{\sqrt{n} \overline{X}} \right) \to 1 - \varepsilon \quad \text{при } n \to \infty.
\]

Итак, искомый асимптотический ДИ уровня доверия \( 1 - \varepsilon \) имеет вид \( \left( \frac{1}{\overline{X}} - \frac{\tau_{1-\varepsilon/2}}{\sqrt{n} \overline{X}}, \frac{1}{\overline{X}} + \frac{\tau_{1-\varepsilon/2}}{\sqrt{n} \overline{X}} \right) \).