---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.01
tokens: 12512
characters: 2918
timestamp: 2025-12-24T07:05:06.681708
finish_reason: stop
---

2. Из леммы Фишера следует, что

\[
\frac{(n-1)}{\sigma^2} S_0^2(\vec{X}) \in \chi_{n-1}^2, \quad \frac{(m-1)}{\sigma^2} S_0^2(\vec{Y}) \in \chi_{m-1}^2
\]

\[
\implies S \overset{\text{def}}{=} \frac{1}{\sigma^2} \left( (n-1)S_0^2(\vec{X}) + (m-1)S_0^2(\vec{Y}) \right) \in \chi_{n+m-2}^2,
\]

и не зависит от \( \overline{X}, \overline{Y} \).

3. Тогда (см. распределение Стьюдента) \( \frac{\xi_0}{\sqrt{S/(n+m-2)}} \in T_{n+m-2} \). Осталось подставить в эту дробь \( \xi_0 \) и \( S \) и убедиться, что \( \sigma \) сократится и что получится в точности \( t_{n+m-2} \) из теоремы 16.

Введем функцию отклонения \( \rho(\vec{X}, \vec{Y}) \):

\[
\rho = \sqrt{\frac{nm}{n+m}} \frac{\overline{X} - \overline{Y}}{\sqrt{\frac{(n-1)S_0^2(\vec{X}) + (m-1)S_0^2(\vec{Y})}{n+m-2}}}.
\]

Из теоремы 16 следует свойство **K1(a)**:
Если \( H_1 \) верна (\( a_1 = a_2 \)) \( \implies \rho = t_{n+m-2} \in T_{n+m-2} \).
**Упражнение.** Доказать свойство **K1(b)**:
Если \( H_2 \) верна (\( a_1 \neq a_2 \)) \( \implies |\rho| \xrightarrow{\text{p}} \infty \).

**Указания.** Воспользовавшись ЗБЧ или утверждениями лемм 1-3 из 1-й лекции, доказать, что числитель и знаменатель сходятся к постоянным: \( \overline{X} - \overline{Y} \xrightarrow{\text{p}} \text{const} \neq 0, \frac{(n-1)S_0^2(\vec{X}) + (m-1)S_0^2(\vec{Y})}{n+m-2} \xrightarrow{\text{p}} \text{const} \neq 0 \), тогда как корень перед дробью неограниченно возрастает.

Поэтому остается по \( \varepsilon \) выбрать \( C \) такое, что для величины \( t_{n+m-2} \in T_{n+m-2} \), в силу симметричности распределения Стьюдента,

\[
\varepsilon = \mathbb{P}(|t_{n+m-2}| > C) = 2\mathbb{P}(t_{n+m-2} > C) \implies \mathbb{P}(t_{n+m-2} > C) = \varepsilon/2 \implies C = \tau_{1-\varepsilon/2},
\]

где \( \tau_{1-\varepsilon/2} \) — квантиль распределения \( T_{n+m-2} \).
И критерий Стьюдента выглядит как все критерии согласия:

\[
\delta(\vec{X}) = \begin{cases}
H_1, & \text{если } |\rho(\vec{X})| < C \\
H_2, & \text{если } |\rho(\vec{X})| \geq C.
\end{cases}
\]

**Упражнение.** Доказать, что этот критерий имеет точный уровень \( \varepsilon \).

8.9 Гипотеза о среднем нормальной совокупности с известной дисперсией

Имеется выборка \( \vec{X} = (X_1, \ldots, X_n), X_i \in N_{a, \sigma^2} \), и дисперсия \( \sigma^2 \) известна. Проверяется простая гипотеза \( H_1: a = a_0 \) против сложной альтернативы \( H_2: a \neq a_0 \).
Можно построить критерий Колмогорова (или \( \chi^2 \)) асимптотического уровня \( \varepsilon \). Но мы (как и в предыдущей задаче) построим критерий *точного* уровня \( \varepsilon \).
Введем функцию отклонения \( \rho(\vec{X}) \):

\[
\rho = \sqrt{n} \frac{\overline{X} - a_0}{\sigma}.
\]

Очевидно свойство **K1(a)**:
Если \( H_1 \) верна (\( a = a_0 \)) \( \implies \rho \in N_{0,1} \).
**Упражнение.** Доказать свойство **K1(b)**:
Если \( H_2 \) верна (\( a \neq a_0 \)) \( \implies |\rho| \xrightarrow{\text{p}} \infty \).