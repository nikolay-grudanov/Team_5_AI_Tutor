---
source_image: page_023.png
page_number: 23
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 76.91
tokens: 12576
characters: 3130
timestamp: 2025-12-24T07:03:55.052870
finish_reason: stop
---

3.7 Асимптотическая нормальность оценок вида \( H(\overline{g(X)}) \)

Следующая теорема утверждает асимптотическую нормальность оценок вида

\[
\theta^* = H(\overline{g(X)}) = H \left( \frac{\sum_1^n g(X_i)}{n} \right).
\]

Такие оценки получаются обычно (найти примеры!) при использовании метода моментов, при этом всегда \( \theta = H(\mathbb{E}_\theta g(X_1)) \).

**Теорема 9.** Пусть функция \( g \) такова, что \( 0 \neq D_\theta g(X_1) < \infty \), функция \( H \) непрерывно дифференцируема в точке \( a = \mathbb{E}_\theta g(X_1) \), и \( H'(a) \neq 0 \). Тогда оценка \( \theta^* = H(\overline{g(X)}) \) является асимптотически нормальной оценкой для \( \theta = H(\mathbb{E}_\theta g(X_1)) = H(a) \) с коэффициентом \( \sigma^2(\theta) = (H'(a))^2 D_\theta g(X_1) \).

**Доказательство теоремы 9.** Разложим \( H(\overline{g(X)}) \) в ряд Тейлора в точке \( a \):

\[
H(\overline{g(X)}) - H(a) = H'(a)(\overline{g(X)} - a) + \delta_n,
\]

где \( \delta_n = O((\overline{g(X)} - a)^2) \xrightarrow{p} 0 \) при \( n \to \infty \). Последнее верно, так как по ЗБЧ при \( n \to \infty \)

\[
\overline{g(X)} = \frac{\sum_1^n g(X_i)}{n} \xrightarrow{p} \mathbb{E}_\theta g(X_1) = a.
\]

Вспомним свойства слабой сходимости:
1) если \( \xi_n \Rightarrow \xi \) и \( \eta_n \xrightarrow{p} c = \text{const} \), то \( \xi_n \eta_n \Rightarrow c\xi \);
2) если \( \xi_n \Rightarrow \xi \) и \( \eta_n \xrightarrow{p} c = \text{const} \), то \( \xi_n + \eta_n \Rightarrow \xi + c \).

По лемме 4, \( \sqrt{n}(\overline{g(X)} - a) \Rightarrow \xi \in N_{0, D_\theta g(X_1)} \), и по свойству (1) слабой сходимости

\[
\sqrt{n}\delta_n = O(\sqrt{n}(\overline{g(X)} - a)(\overline{g(X)} - a)) \xrightarrow{p} 0 \cdot \xi = 0.
\]

Отсюда (и по свойству (2) слабой сходимости)

\[
\sqrt{n}(H(\overline{g(X)}) - H(a)) = \sqrt{n}H'(a)(\overline{g(X)} - a) + \sqrt{n}\delta_n \Rightarrow N_{0, (H'(a))^2 D_\theta g(X_1)},
\]

что и требовалось доказать.

**Пример 12.** Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из равномерного распределения \( U_{0,\theta} \), где \( \theta > 0 \).

Проверим, являются ли оценки \( \theta_k^* = \sqrt[k]{(k+1)\overline{X^k}}, k = 1, 2, \ldots \), полученные методом моментов, асимптотически нормальными.

Пусть \( g(x) = (k+1)x^k, H(y) = \sqrt[k]{y} \). Тогда

\[
\theta_k^* = \sqrt[k]{(k+1)\overline{X^k}} = \sqrt[k]{\frac{\sum_1^n (k+1)X_i^k}{n}} = H \left( \frac{\sum_1^n g(X_i)}{n} \right).
\]

При этом

\[
\theta = H(\mathbb{E}_\theta g(X_1)) = \sqrt[k]{\mathbb{E}_\theta (k+1)X_1^k} = \sqrt[k]{(k+1) \frac{\theta^k}{k+1}}.
\]

Впрочем, иначе быть не могло по определению метода моментов (*верно?*). Проверим другие условия теоремы 9:

\[
a = \mathbb{E}_\theta g(X_1) = (k+1) \frac{\theta^k}{k+1} = \theta^k,
\]
\[
D_\theta g(X_1) = \mathbb{E}_\theta (k+1)^2 X_1^{2k} - a^2 = (k+1)^2 \frac{\theta^{2k}}{2k+1} - \theta^{2k} = \frac{k^2}{2k+1} \theta^{2k}
\]

конечна и отлична от нуля. Функция \( H(y) \) непрерывно дифференцируема в точке \( a \):

\[
H'(y) = \frac{1}{k} y^{\frac{1-k}{k}}, \quad H'(a) = H'(\theta^k) = \frac{1}{k} \theta^{1-k} \text{ непрерывна для } \theta > 0.
\]