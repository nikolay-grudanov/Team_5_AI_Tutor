---
source_image: page_050.png
page_number: 50
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 67.86
tokens: 12673
characters: 3179
timestamp: 2025-12-24T07:05:03.498102
finish_reason: stop
---

Тогда (вспомнить свойство функций распределения \( F_\xi(x+0) - F_\xi(x) = \mathbb{P}(\xi = x) \))

\[
\Delta \overset{\text{def}}{=} \phi(c-0) - \phi(c) \equiv \mathbb{P}_{H_1} \left( \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} = c \right) \geqslant 0.
\]

Возьмем \( p = \frac{\varepsilon - \phi(c)}{\Delta} \in [0, 1] \). Для такого \( p \)

\[
\varepsilon = \phi(c) + p \Delta = \mathbb{P}_{H_1} \left( \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > c \right) + p \cdot \mathbb{P}_{H_1} \left( \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} = c \right) = \alpha(\delta),
\]

что и требовалось доказать.

2. Докажем, что критерий \( \delta \) наиболее мощный. Нам потребуется следующее

Утверждение 1. Обозначим \( \Psi(\vec{y}) = \min\{ \Psi_2(\vec{y}), c \Psi_1(\vec{y}) \} \). Тогда \( \beta(\delta) + c \alpha(\delta) = \int_{\mathbb{R}^n} \Psi(\vec{y}) \, d\vec{y} \).

Действительно,

\[
\beta(\delta) + c \alpha(\delta) = \mathbb{P}_{H_2} \left( \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} < c \right) + q \cdot \mathbb{P}_{H_2} \left( \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} = c \right) + c \mathbb{P}_{H_1} \left( \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} > c \right) + c p \cdot \mathbb{P}_{H_1} \left( \frac{\Psi_2(\vec{X})}{\Psi_1(\vec{X})} = c \right)
\]
\[
= \int_{\Psi_2(\vec{y}) < c \Psi_1(\vec{y})} \Psi_2(\vec{y}) \, d\vec{y} + q \int_{\Psi_2(\vec{y}) = c \Psi_1(\vec{y})} \Psi_2(\vec{y}) \, d\vec{y} + \int_{\Psi_2(\vec{y}) > c \Psi_1(\vec{y})} c \Psi_1(\vec{y}) \, d\vec{y} + p \int_{\Psi_2(\vec{y}) = c \Psi_1(\vec{y})} c \Psi_1(\vec{y}) \, d\vec{y}
\]
\[
= \int_{\Psi_2(\vec{y}) < c \Psi_1(\vec{y})} \Psi(\vec{y}) \, d\vec{y} + q \int_{\Psi_2(\vec{y}) = c \Psi_1(\vec{y})} \Psi(\vec{y}) \, d\vec{y} + \int_{\Psi_2(\vec{y}) > c \Psi_1(\vec{y})} \Psi(\vec{y}) \, d\vec{y} + p \int_{\Psi_2(\vec{y}) = c \Psi_1(\vec{y})} \Psi(\vec{y}) \, d\vec{y} = \int_{\mathbb{R}^n} \Psi(\vec{y}) \, d\vec{y}.
\]

Пусть \( \delta_0 \in K_\varepsilon \) — другой критерий уровня \( \varepsilon \). Докажем, что его ошибка 2-го рода не меньше, чем у критерия \( \delta \).
Используя определение функции \( \Psi \) и утверждение 1, имеем:

\[
\beta(\delta_0) + c \alpha(\delta_0) = \int_{\delta_0 = H_1} \Psi_2(\vec{y}) \, d\vec{y} + \int_{\delta_0 = H_2} c \Psi_1(\vec{y}) \, d\vec{y} \geqslant \int_{\delta_0 = H_1} \Psi(\vec{y}) \, d\vec{y} + \int_{\delta_0 = H_2} \Psi(\vec{y}) \, d\vec{y} \equiv \int_{\mathbb{R}^n} \Psi(\vec{y}) \, d\vec{y} = \beta(\delta) + c \alpha(\delta).
\]

Но \( \alpha(\delta_0) = \alpha(\delta) \implies \beta(\delta_0) \geqslant \beta(\delta) \).

Пример 29. Имеется выборка \( X_1 \) объема 1. Проверяются простые гипотезы \( \begin{cases} H_1 : X_1 \in U_{1,5}, \\ H_2 : X_1 \in U_{0,2}. \end{cases} \) Требуется построить НМК уровня \( \alpha = 1/3 \) (объем выборки мал, так что ошибки не могут не быть большими). Воспользуемся леммой Неймана — Пирсона и выпишем в зависимости от \( X_1 \) отношение правдоподобия (см. рисунок).

Рис. 9: Две равномерные гипотезы.

Поскольку отношение правдоподобия постоянно на каждом из трех интервалов, для постоянной \( c \) есть лишь несколько возможностей, при которых критерии будут различаться. Перечислим все возможные