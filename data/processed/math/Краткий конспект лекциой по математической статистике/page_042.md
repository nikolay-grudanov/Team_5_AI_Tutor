---
source_image: page_042.png
page_number: 42
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 71.33
tokens: 12713
characters: 3187
timestamp: 2025-12-24T07:04:39.511446
finish_reason: stop
---

3. \( \sum_{i=1}^n \left( \frac{X_i - \overline{X}}{\sigma} \right)^2 = \frac{(n-1)S_0^2}{\sigma^2} \in H_{n-1} — для \ \sigma^2 \ при \ a \ неизвестном; \)

4. \( \sqrt{n} \frac{\overline{X} - a}{\sqrt{S_0^2}} = \sqrt{n} \frac{\overline{X} - a}{S_0} \in T_{n-1} — для \ a \ при \ \sigma \ неизвестном. \)

Доказательство следствия 5. 1) и 3) — из леммы Фишера, 2) — из следствия 4, осталось воспользоваться леммой Фишера и определением 18 распределения Стьюдента, чтобы доказать 4).

\[
\sqrt{n} \frac{\overline{X} - a}{\sqrt{S_0^2}} = \underbrace{\sqrt{n} \frac{\overline{X} - a}{\sigma}}_{N_{0,1}} \text{ независ. } \underbrace{\frac{1}{\sqrt{\frac{(n-1)S_0^2}{\sigma^2} \frac{1}{n-1}}} = \frac{\xi_0}{\sqrt{\chi_{n-1}^2 / (n-1)}}}_{H_{n-1}} \in T_{n-1}.
\]

6.5 Построение точных доверительных интервалов для параметров нормально-го распределения

1. Для \( a \) при известном \( \sigma^2 \). Это мы уже построили:

\[
P_{a,\sigma^2} \left( \overline{X} - \frac{\tau_{1-\varepsilon/2}\sigma}{\sqrt{n}} < a < \overline{X} + \frac{\tau_{1-\varepsilon/2}\sigma}{\sqrt{n}} \right) = 1 - \varepsilon, \text{ где } \Phi_{0,1}(\tau_{1-\varepsilon/2}) = 1 - \varepsilon/2.
\]

2. Для \( \sigma^2 \) при известном \( a \): по п.2 из следствия 5, \( \frac{n\sigma^{2*}}{\sigma^2} \in H_n \), где \( \sigma^{2*} = \frac{1}{n} \sum_{i=1}^n (X_i - a)^2 \). Пусть \( g_1 = \chi_{n,\varepsilon/2}^2 \) и \( g_2 = \chi_{n,1-\varepsilon/2}^2 \) — квантили распределения \( H_n \) уровня \( \varepsilon/2 \) и \( 1 - \varepsilon/2 \). Тогда

\[
1 - \varepsilon = P_{a,\sigma^2} \left( g_1 < \frac{n\sigma^{2*}}{\sigma^2} < g_2 \right) = P_{a,\sigma^2} \left( \frac{n\sigma^{2*}}{g_2} < \sigma^2 < \frac{n\sigma^{2*}}{g_1} \right).
\]

Искомый интервал построен.

3. Для \( \sigma^2 \) при неизвестном \( a \): по п.3 из следствия 5, \( \frac{(n-1)S_0^2}{\sigma^2} \in H_{n-1} \), где \( S_0^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \overline{X})^2 \). Пусть \( g_1 = \chi_{n-1,\varepsilon/2}^2 \) и \( g_2 = \chi_{n-1,1-\varepsilon/2}^2 \) — квантили распределения \( H_{n-1} \) уровня \( \varepsilon/2 \) и \( 1 - \varepsilon/2 \). Тогда

\[
1 - \varepsilon = P_{a,\sigma^2} \left( g_1 < \frac{(n-1)S_0^2}{\sigma^2} < g_2 \right) = P_{a,\sigma^2} \left( \frac{(n-1)S_0^2}{g_2} < \sigma^2 < \frac{(n-1)S_0^2}{g_1} \right).
\]

Искомый интервал построен.

Упражнение. Найти 17 отличий п.2 от п.3.

4. Для \( a \) при неизвестном \( \sigma \): по п.4 из следствия 5, \( \sqrt{n} \frac{\overline{X} - a}{S_0} \in T_{n-1} \), где \( S_0^2 = \frac{1}{n-1} \sum_{i=1}^n (X_i - \overline{X})^2 \). Пусть \( a_1 = t_{n-1,\varepsilon/2} \) и \( a_2 = t_{n-1,1-\varepsilon/2} \) — квантили распределения \( T_{n-1} \) уровня \( \varepsilon/2 \) и \( 1 - \varepsilon/2 \). Заметим, что в силу симметричности распределения Стьюдента \( a_1 = -a_2 = -t_{n-1,1-\varepsilon/2} \). Тогда

\[
1 - \varepsilon = P_{a,\sigma^2} \left( -t_{n-1,1-\varepsilon/2} < \sqrt{n} \frac{\overline{X} - a}{S_0} < t_{n-1,1-\varepsilon/2} \right) =
P_{a,\sigma^2} \left( \overline{X} - \frac{t_{n-1,1-\varepsilon/2} S_0}{\sqrt{n}} < a < \overline{X} + \frac{t_{n-1,1-\varepsilon/2} S_0}{\sqrt{n}} \right).
\]

Искомый интервал построен.