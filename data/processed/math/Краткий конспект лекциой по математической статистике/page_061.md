---
source_image: page_061.png
page_number: 61
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.05
tokens: 11493
characters: 789
timestamp: 2025-12-24T07:04:44.509842
finish_reason: stop
---

Пример 30. Посмотрим на критерий (17) в задаче о параметре нормальной выборки с известной дисперсией.

\[
\delta(\vec{X}) = H_1 \iff |\rho(\vec{X})| < C = \tau_{1-\varepsilon/2} \iff |\sqrt{n} \frac{\overline{X} - a_0}{\sigma}| < \tau_{1-\varepsilon/2}
\]
\[
\iff \overline{X} - \frac{\tau_{1-\varepsilon/2} \sigma}{\sqrt{n}} < a_0 < \overline{X} + \frac{\tau_{1-\varepsilon/2} \sigma}{\sqrt{n}}.
\]

Осталось вспомнить, что точный доверительный интервал для параметра \(a\) нормального распределения с известной дисперсией как раз и есть \((\overline{X} - \frac{\tau_{1-\varepsilon/2} \sigma}{\sqrt{n}}, \overline{X} + \frac{\tau_{1-\varepsilon/2} \sigma}{\sqrt{n}})\).

Упражнение. Какие из приведенных выше критериев можно сформулировать, используя доверительные интервалы? Сделать это.