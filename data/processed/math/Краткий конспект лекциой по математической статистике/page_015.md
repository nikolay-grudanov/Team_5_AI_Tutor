---
source_image: page_015.png
page_number: 15
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 105.48
tokens: 12695
characters: 3524
timestamp: 2025-12-24T07:03:23.201967
finish_reason: stop
---

Замечание 9. Поскольку функция \( \ln y \) монотонна, то точки максимума \( \Psi(\vec{X}, \theta) \) и \( L(\vec{X}, \theta) \) совпадают. Поэтому оценкой максимального правдоподобия (ОМП) можно называть точку максимума (по \( \theta \)) функции \( L(\vec{x}, \theta) \):
\[
\hat{\theta} = \text{точка максимума (по переменной } \theta \text{) функции } L(\vec{X}, \theta).
\]
Напомним, что точки экстремума функции — это либо точки, в которых производная обращается в нуль, либо точки разрыва функции/производной, либо крайние точки области определения функции.

Пример 6. Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из распределения Пуассона: \( X_i \in \Pi_\lambda \), где \( \lambda > 0 \). Найдем ОМП \( \hat{\lambda} \) неизвестного параметра \( \lambda \).

\[
P_\lambda(X_1 = y) = \frac{\lambda^y}{y!} e^{-\lambda}, \quad y = 0, 1, 2, \ldots
\]

\[
\Psi(\vec{X}, \lambda) = \prod_{i=1}^n \frac{\lambda^{X_i}}{X_i!} e^{-\lambda} = \frac{\lambda^{\sum_{i=1}^n X_i}}{\prod_{i=1}^n X_i!} e^{-n\lambda} = \frac{\lambda^{n \overline{X}}}{\prod_{i=1}^n X_i!} e^{-n\lambda}.
\]
Поскольку эта функция при всех \( \lambda > 0 \) непрерывно дифференцируема по \( \lambda \), можно искать точки экстремума, приравнивая к нулю частную производную по \( \lambda \). Но удобнее это делать для логарифмической функции правдоподобия:

\[
L(\vec{X}, \lambda) = \ln \Psi(\vec{X}, \lambda) = \ln \left( \frac{\lambda^{n \overline{X}}}{\prod_{i=1}^n X_i!} e^{-n\lambda} \right) = n \overline{X} \ln \lambda - \ln \prod_{i=1}^n X_i! - n\lambda.
\]

\[
\frac{\partial}{\partial \lambda} L(\vec{X}, \lambda) = \frac{n \overline{X}}{\lambda} - n, \text{ и точка экстремума } \hat{\lambda} — решение уравнения: \frac{n \overline{X}}{\lambda} - n = 0, \text{ то есть } \hat{\lambda} = \overline{X}.
\]

Упражнение.
1) Убедиться, что \( \hat{\lambda} = \overline{X} \) — точка максимума, а не минимума.
2) Убедиться, что \( \hat{\lambda} = \overline{X} \) совпадает с одной из оценок метода моментов (*по какому моменту?*).

Пример 7. Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из нормального распределения \( N_{a, \sigma^2} \), где \( a \in \mathbb{R} \), \( \sigma > 0 \); и оба параметра \( a, \sigma^2 \) неизвестны.
Выпишем плотность, функцию правдоподобия и логарифмическую функцию правдоподобия. Плотность:
\[
f_{(a, \sigma^2)}(y) = \frac{1}{\sqrt{2 \pi \sigma^2}} \exp \left( \frac{-(y - a)^2}{2 \sigma^2} \right),
\]
функция правдоподобия:
\[
\Psi(\vec{X}, a, \sigma^2) = \prod_{i=1}^n \frac{1}{\sqrt{2 \pi \sigma^2}} \exp \left( -\frac{(X_i - a)^2}{2 \sigma^2} \right) = \frac{1}{(2 \pi \sigma^2)^{n/2}} \exp \left( -\frac{\sum_{i=1}^n (X_i - a)^2}{2 \sigma^2} \right),
\]
логарифмическая функция правдоподобия:
\[
L(\vec{X}, a, \sigma^2) = \ln \Psi(\vec{X}, a, \sigma^2) = -\ln (2 \pi)^{n/2} - \frac{n}{2} \ln \sigma^2 - \frac{\sum_{i=1}^n (X_i - a)^2}{2 \sigma^2}.
\]
В точке экстремума (по \( (a, \sigma^2) \)) гладкой функции \( L \) обращаются в нуль обе частные производные:
\[
\frac{\partial}{\partial a} L(\vec{X}, a, \sigma^2) = \frac{2 \sum_{i=1}^n (X_i - a)}{2 \sigma^2} = \frac{n \overline{X} - n a}{\sigma^2}; \quad \frac{\partial}{\partial \sigma^2} L(\vec{X}, a, \sigma^2) = -\frac{n}{2 \sigma^2} + \frac{\sum_{i=1}^n (X_i - a)^2}{2 \sigma^4}.
\]
Оценка максимального правдоподобия \( (\hat{a}, \hat{\sigma^2}) \) для \( (a, \sigma^2) \) — решение системы уравнений
\[
\frac{n \overline{X} - n a}{\sigma^2} = 0; \quad -\frac{n}{2 \sigma^2} + \frac{\sum_{i=1}^n (X_i - a)^2}{2 (\sigma^2)^2} = 0.
\]