---
source_image: page_028.png
page_number: 28
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 74.85
tokens: 12487
characters: 3331
timestamp: 2025-12-24T07:04:05.862671
finish_reason: stop
---

Замечание 13. Доказательство неравенства Рао-Крамера при первом, втором и третьем прочтении можно опустить.

Доказательство неравенства Рао-Крамера. Мы докажем только неравенство для класса \( K_0 \) (теорему 10). Необходимые изменения в доказательство для класса \( K_b \) читатель может внести самостоятельно.
Нам понадобится следующее утверждение.

Лемма 5. При выполнении условий (R) и (RR) для любой статистики \( T = T(\vec{X}) \), дисперсия которой ограничена на компактах,

\[
\frac{\partial}{\partial \theta} \mathbb{E}_\theta T = \mathbb{E}_\theta T \cdot \frac{\partial}{\partial \theta} L(\vec{X}, \theta).
\]

Упражнение. Вспомнить, что такое функция правдоподобия (\( \Psi \)) (определение 6), логарифмическая функция правдоподобия (\( L \)) (определение 7) и как они связаны друг с другом, с плотностью \( X_1 \) и совместной плотностью выборки.

Доказательство леммы 5. Напоминание: математическое ожидание функции от нескольких случайных величин есть (многомерный) интеграл от этой функции помноженной на совместную плотность этих с.в.

\[
\mathbb{E}_\theta T(X_1, \ldots, X_n) = \int_{\mathbb{R}^n} T(y_1, \ldots, y_n) \Psi(y_1, \ldots, y_n, \theta) \, dy_1 \ldots dy_n.
\]

В следующей цепочке равенств равенство, помеченное (?), мы доказывать не будем, поскольку его доказательство требует несколько более основательных знаний математического анализа, нежели имеющиеся у студентов 2 курса ЭФ 1997 г. Это равенство — смена порядка дифференцирования и интегрирования — то единственное, ради которого и введены условия регулярности (см. пример ниже).
Напоминание: \( \ln f(x) \) — сложная функция (см. правила дифференцирования суперпозиции).

\[
\begin{align*}
\frac{\partial}{\partial \theta} \mathbb{E}_\theta T(\vec{X}) &= \frac{\partial}{\partial \theta} \int T(\vec{y}) \Psi(\vec{y}, \theta) \, d\vec{y} \stackrel{?}{=} \int \frac{\partial}{\partial \theta} T(\vec{y}) \Psi(\vec{y}, \theta) \, d\vec{y} \\
&= \int T(\vec{y}) \frac{\partial}{\partial \theta} \frac{\Psi(\vec{y}, \theta)}{\Psi(\vec{y}, \theta)} \cdot \Psi(\vec{y}, \theta) \, d\vec{y} \\
&= \int T(\vec{y}) \frac{\partial}{\partial \theta} L(\vec{y}, \theta) \cdot \Psi(\vec{y}, \theta) \, d\vec{y} = \mathbb{E}_\theta T(\vec{X}) \cdot \frac{\partial}{\partial \theta} L(\vec{X}, \theta).
\end{align*}
\]

Воспользуемся леммой 5. Будем брать в качестве \( T \) разные функции и получать полезные формулы, которые потом соберем вместе.

1. Пусть \( T(\vec{X}) \equiv 1 \). Тогда

\[
0 = \frac{\partial}{\partial \theta} 1 = \mathbb{E}_\theta \frac{\partial}{\partial \theta} L(\vec{X}, \theta).
\]

Далее, поскольку \( \Psi(\vec{X}, \theta) = \prod f_\theta(X_i) \), то \( L(\vec{X}, \theta) = \sum \ln f_\theta(X_i) \), и

\[
0 = \mathbb{E}_\theta \frac{\partial}{\partial \theta} L(\vec{X}, \theta) = \mathbb{E}_\theta \sum \ln f_\theta(X_i) = n \mathbb{E}_\theta \ln f_\theta(X_1). \tag{7}
\]

2. Пусть \( T(\vec{X}) = \theta^* \in K_0 \). Тогда

\[
\frac{\partial}{\partial \theta} \mathbb{E}_\theta \theta^* = \frac{\partial}{\partial \theta} \theta = 1 = \mathbb{E}_\theta \theta^* \cdot \frac{\partial}{\partial \theta} L(\vec{X}, \theta). \tag{8}
\]

Вспомним свойство коэффициента корреляции:

\[
\operatorname{cov}(\xi, \eta) = \mathbb{E}\xi \eta - \mathbb{E}\xi \mathbb{E}\eta \leq \sqrt{\operatorname{D}\xi \operatorname{D}\eta}.
\]