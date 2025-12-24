---
source_image: page_036.png
page_number: 36
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 72.35
tokens: 12568
characters: 3376
timestamp: 2025-12-24T07:04:20.485195
finish_reason: stop
---

Пример 24. Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из распределения Пуассона \( \Pi_\lambda \), где \( \lambda > 0 \). Требуется построить асимптотический ДИ для параметра \( \lambda \) уровня доверия \( 1 - \varepsilon \).

Вспомним ЦПТ:
\[
\frac{\sum_{i=1}^n X_i - n \mathbb{E}_\lambda X_1}{\sqrt{n D_\lambda X_1}} = \sqrt{n} \frac{\overline{X} - \lambda}{\sqrt{\lambda}} \Rightarrow \eta \in N_{0,1}.
\]
По определению слабой сходимости, при \( n \to \infty \)
\[
P_\lambda \left( -c < \sqrt{n} \frac{\overline{X} - \lambda}{\sqrt{\lambda}} < c \right) \to P(-c < \eta < c) = 1 - \varepsilon \quad \text{при } c = \tau_{1-\varepsilon/2}.
\]
Но разрешить неравенство под знаком вероятности относительно \( \lambda \) не просто — получается квадратное неравенство из-за корня в знаменателе. Заменим \( \sqrt{\lambda} \) на \( \sqrt{\overline{X}} \). Не испортится ли сходимость?
По свойствам слабой сходимости, если \( \xi_n \xrightarrow{p} 1 \) и \( \eta_n \Rightarrow \eta \), то \( \xi_n \eta_n \Rightarrow \eta \). Воспользуемся этим.
Оценка \( \lambda^* = \overline{X} \) состоятельна \( \implies \frac{\lambda}{\overline{X}} \xrightarrow{p} 1 \implies \sqrt{\frac{\lambda}{\overline{X}}} \xrightarrow{p} 1 \). Тогда
\[
\sqrt{\frac{\lambda}{\overline{X}}} \cdot \sqrt{n} \frac{\overline{X} - \lambda}{\sqrt{\lambda}} = \sqrt{n} \frac{\overline{X} - \lambda}{\sqrt{\overline{X}}} \Rightarrow \eta \in N_{0,1}.
\]
\[
P_\lambda \left( -\tau_{1-\varepsilon/2} < \sqrt{n} \frac{\overline{X} - \lambda}{\sqrt{\overline{X}}} < \tau_{1-\varepsilon/2} \right) \to P(-\tau_{1-\varepsilon/2} < \eta < \tau_{1-\varepsilon/2}) = 1 - \varepsilon.
\]
Разрешая неравенство под знаком вероятности относительно \( \lambda \), получим
\[
P_\lambda \left( \overline{X} - \frac{\tau_{1-\varepsilon/2} \sqrt{\overline{X}}}{\sqrt{n}} < \lambda < \overline{X} + \frac{\tau_{1-\varepsilon/2} \sqrt{\overline{X}}}{\sqrt{n}} \right) \to 1 - \varepsilon \quad \text{при } n \to \infty.
\]
Итак, искомый асимптотический ДИ уровня доверия \( 1 - \varepsilon \) имеет вид \( \left( \overline{X} - \frac{\tau_{1-\varepsilon/2} \sqrt{\overline{X}}}{\sqrt{n}}, \overline{X} + \frac{\tau_{1-\varepsilon/2} \sqrt{\overline{X}}}{\sqrt{n}} \right) \).

Вместо ЦПТ для построения асимптотических ДИ можно использовать асимптотически нормальные оценки (что по сути — та же ЦПТ):
Если \( \theta^* \) — АНО параметра \( \theta \) с коэффициентом \( \sigma^2(\theta) \), то
\[
G(\vec{X}, \theta) = \sqrt{n} \frac{\theta^* - \theta}{\sigma(\theta)} \Rightarrow \eta \in N_{0,1}.
\]

Замечание 18. Если \( \sigma(\theta) \) в знаменателе мешает, то (как в примере 24) ее можно заменить состоятельной оценкой \( \sigma(\theta^*) \). Достаточно, чтобы функция \( \sigma(\theta) \) была непрерывной. Требуется лишь ответить: почему \( \theta^* \) — состоятельная оценка для \( \theta \)?

5.2 Вопросы и упражнения

1. Задачник [1], т 8.2, 8.7 (а) — по ЦПТ.

2. Задачник [1], т 8.7 (б) (доказать, что \( \frac{n}{\theta}(X_{(n)} - \theta) \Rightarrow \eta \), где \( -\eta \in E_1 \), см. также упражнение к примеру 10).

3. Задачник [1], т 8.9. См. задачу 8.8 и пример 23. В п. (а) искать ДИ вида \( X_{(1)} - \delta < \theta < X_{(1)} \), в п. (б) искать ДИ вида \( X_{(1)} \cdot \delta < \theta < X_{(1)} \).

4. Объяснить, как додуматься до вида ДИ в предыдущей задаче. Исходить из вида распределений.