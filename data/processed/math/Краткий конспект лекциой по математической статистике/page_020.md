---
source_image: page_020.png
page_number: 20
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 101.47
tokens: 12612
characters: 3212
timestamp: 2025-12-24T07:03:19.263493
finish_reason: stop
---

Но оценка \( \theta^* \) принадлежит \( K_b \), то есть она не лучше, например, эффективной оценки \( \theta_1^* \). Поэтому

\[
\mathbb{E}_\theta (\theta^* - \theta)^2 \geq \mathbb{E}_\theta (\theta_1^* - \theta)^2.
\]

Сравнивая это неравенство с равенством (5), видим, что

\[
\mathbb{E}_\theta \left( \frac{\theta_1^* - \theta_2^*}{2} \right)^2 = \frac{1}{4} \mathbb{E}_\theta (\theta_1^* - \theta_2^*)^2 \leq 0 \implies \mathbb{E}_\theta (\theta_1^* - \theta_2^*)^2 = 0.
\]

Тогда (*почему?*) \( P_\theta (\theta_1^* = \theta_2^*) = 1 \), что и требовалось доказать.

Для примера рассмотрим сравнение двух оценок. Разумеется, сравнивая оценки попарно между собой, наилучшей оценки в целом классе не найти, но выбрать лучшую из двух тоже полезно. А способами поиска наилучшей в целом классе мы тоже скоро займемся.

**Пример 10.** Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из равномерного распределения \( U_{0,\theta} \), где \( \theta > 0 \). Тогда \( \hat{\theta} = X_{(n)} = \max\{X_1, \ldots, X_n\} \) — оценка максимального правдоподобия, а \( \theta^* = 2\overline{X} \) — оценка метода моментов, полученная по первому моменту. Сравним их в среднеквадратичном. Оценка \( \theta^* = 2\overline{X} \) несмещенная (см. пример 4), поэтому

\[
\mathbb{E}_\theta (\theta^* - \theta)^2 = D_\theta \theta^* = D_\theta 2\overline{X} = 4D_\theta \overline{X} = 4 \frac{D_\theta X_1}{n} = 4 \frac{\theta^2}{12n} = \frac{\theta^2}{3n}.
\]

Для \( \hat{\theta} = X_{(n)} = \max\{X_1, \ldots, X_n\} \) имеем

\[
\mathbb{E}_\theta (\hat{\theta} - \theta)^2 = \mathbb{E}_\theta \hat{\theta}^2 - 2\theta \mathbb{E}_\theta \hat{\theta} + \theta^2.
\]

Посчитаем первый и второй момент случайной величины \( \hat{\theta} = X_{(n)} \). Найдем (полезно вспомнить, как это делалось в прошлом семестре!) функцию распределения и плотность \( \hat{\theta} \):

\[
P_\theta (X_{(n)} < y) = P_\theta (X_1 < y)^n = \begin{cases}
0, & y < 0 \\
\frac{y^n}{\theta^n}, & y \in [0, \theta] \\
1, & y > \theta,
\end{cases}
\]
\[
f_{X_{(n)}} (y) = \begin{cases}
0, & y \notin [0, \theta] \\
n \frac{y^{n-1}}{\theta^n}, & y \in [0, \theta]
\end{cases}.
\]

\[
\mathbb{E}_\theta X_{(n)} = \int_0^\theta y n \frac{y^{n-1}}{\theta^n} dy = \frac{n}{n+1} \theta, \quad \mathbb{E}_\theta X_{(n)}^2 = \int_0^\theta y^2 n \frac{y^{n-1}}{\theta^n} dy = \frac{n}{n+2} \theta^2.
\]

Поэтому

\[
\mathbb{E}_\theta (X_{(n)} - \theta)^2 = \frac{n}{n+2} \theta^2 - 2 \frac{n}{n+1} \theta^2 + \theta^2 = \frac{2}{(n+1)(n+2)} \theta^2.
\]

При \( n = 1 \) квадратические отклонения равны, а при \( n > 1 \)

\[
\mathbb{E}_\theta (X_{(n)} - \theta)^2 = \frac{2\theta^2}{(n+1)(n+2)} < \frac{\theta^2}{3n} = \mathbb{E}_\theta (2\overline{X} - \theta)^2,
\]

то есть \( X_{(n)} \) лучше, чем \( 2\overline{X} \). При этом \( \mathbb{E}_\theta (X_{(n)} - \theta)^2 \to 0 \) со скоростью \( n^{-2} \), тогда как \( \mathbb{E}_\theta (2\overline{X} - \theta)^2 \to 0 \) со скоростью \( n^{-1} \).

**Упражнение.**
1. Доказать, что \( X_{(n)} \in K_b \), где \( b(\theta) = -\frac{\theta}{n+1} \).
2. Доказать, что \( \frac{n+1}{n} X_{(n)} \in K_0 \) (несмещенная).
3. Сравнить оценки \( \frac{n+1}{n} X_{(n)} \) и \( X_{(n)} \) в среднеквадратичном.