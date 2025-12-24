---
source_image: page_049.png
page_number: 49
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 67.71
tokens: 12634
characters: 3136
timestamp: 2025-12-24T07:05:02.834126
finish_reason: stop
---

Если использовать определение 27, критерий отношения правдоподобия в лемме Неймана - Пирсона примет вид:

\[
\pi(\vec{X}) = \begin{cases}
0, & \text{если } \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} < c \\
1, & \text{если } \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > c \\
p, & \text{если } \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} = c,
\end{cases}
\]

где \(c\) и \(p\) по-прежнему определяются из уравнения \(\alpha(\pi) = \varepsilon\), которое можно записать так:

\[
\alpha(\pi) = P_{H_1}\left(\frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > c\right) + p \cdot P_{H_1}\left(\frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} = c\right) = E_{H_1}(\pi(\vec{X})) = \varepsilon.
\]

**7.5 Доказательство леммы Неймана - Пирсона**

1. Докажем, что уравнение 12 разрешимо относительно \(c\) и \(p\).

Рассмотрим невозрастающую (*почему?*) функцию \(\phi(c) = P_{H_1}\left(\frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > c\right)\).

\[
\phi(c) = P_{H_1}\left(\frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > c\right) = \int_{\frac{\Psi_2(\vec{y})}{\Psi_1(\vec{y})} > c} \Psi_1(\vec{y})\ d\vec{y}.
\]

Поскольку интегрирование ведется по области \(\frac{\Psi_2(\vec{y})}{\Psi_1(\vec{y})} > c\), то под интегралом \(\Psi_1(\vec{y}) < \Psi_2(\vec{y})/c\). Поэтому

\[
\phi(c) = \int_{\frac{\Psi_2(\vec{y})}{\Psi_1(\vec{y})} > c} \Psi_1(\vec{y})\ d\vec{y} < \frac{1}{c} \int_{\frac{\Psi_2(\vec{y})}{\Psi_1(\vec{y})} > c} \Psi_2(\vec{y})\ d\vec{y} = \frac{1}{c} P_{H_2}\left(\frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > c\right) \to 0
\]
при \(c \to \infty\).

Рассмотрим \(\phi(0)\):

\[
\phi(0) = P_{H_1}\left(\frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > 0\right) = P_{H_1}\left(\Psi_2(\vec{X}) > 0\right)
\]

Возможны два случая: (а) \(\phi(0) = P_{H_1}\left(\Psi_2(\vec{X}) > 0\right) < \varepsilon\) и (б) \(\phi(0) = P_{H_1}\left(\Psi_2(\vec{X}) > 0\right) \geqslant \varepsilon\).

В случае (а) положим \(c = 0\), обозначим через \(\Delta\) разницу \(\Delta = \varepsilon - P_{H_1}\left(\Psi_2(\vec{X}) > 0\right) > 0\) и возьмем \(p = \Delta/(1 + \Delta - \varepsilon)\). Тогда

\[
\alpha(\delta) = P_{H_1}\left(\frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > 0\right) + p \cdot P_{H_1}\left(\frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} = 0\right) =
P_{H_1}\left(\Psi_2(\vec{X}) > 0\right) + p \cdot P_{H_1}\left(\Psi_2(\vec{X}) = 0\right) = (\varepsilon - \Delta) + \frac{\Delta}{1 + \Delta - \varepsilon}(1 - (\varepsilon - \Delta)) = \varepsilon.
\]

Заметим сразу, что в случае (а) мы хоть и нашли критерий заданного уровня \(\varepsilon > P_{H_1}\left(\Psi_2(\vec{X}) > 0\right)\), но для этого пришлось принимать (с вероятностью \(p\)) гипотезу \(H_2\) там, где она быть верна не может — в области \(\Psi_2(\vec{X}) = 0\).

Это означает лишь, что с самого начала наше желание найти критерий уровня \(\varepsilon\), если \(\varepsilon > P_{H_1}\left(\Psi_2(\vec{X}) > 0\right)\) — абсурд: все разумные критерии имеют меньший уровень.

В случае (б) имеем: \(\phi(0) \geqslant \varepsilon, \phi(c)\) не возрастает и стремится к нулю с ростом \(c\). Тогда найдется \(c\) такое, что \(\phi(c - 0) \geqslant \varepsilon, \phi(c) \leqslant \varepsilon\) (\(c\) может быть точкой разрыва).