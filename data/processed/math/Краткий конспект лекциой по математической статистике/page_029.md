---
source_image: page_029.png
page_number: 29
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 70.56
tokens: 12444
characters: 3180
timestamp: 2025-12-24T07:04:06.255413
finish_reason: stop
---

Используя свойства (7) и (8), имеем

\[
\operatorname{cov}(\theta^*, \frac{\partial}{\partial \theta} L(\vec{X}, \theta)) = \mathbb{E}_\theta \theta^* \cdot \frac{\partial}{\partial \theta} L(\vec{X}, \theta) - \mathbb{E}_\theta \theta^* \mathbb{E}_\theta \frac{\partial}{\partial \theta} L(\vec{X}, \theta) =
\]
\[
= \mathbb{E}_\theta \theta^* \cdot \frac{\partial}{\partial \theta} L(\vec{X}, \theta) = 1 \leq \sqrt{\mathbb{D}_\theta \theta^* \mathbb{D}_\theta \frac{\partial}{\partial \theta} L(\vec{X}, \theta)}.
\] (9)

Найдем \( \mathbb{D}_\theta \frac{\partial}{\partial \theta} L(\vec{X}, \theta) \):
\[
\mathbb{D}_\theta \frac{\partial}{\partial \theta} L(\vec{X}, \theta) = \mathbb{D}_\theta \sum \frac{\partial}{\partial \theta} \ln f_\theta(X_i) = n \mathbb{D}_\theta \frac{\partial}{\partial \theta} \ln f_\theta(X_1) = n \mathbb{E}_\theta (\frac{\partial}{\partial \theta} \ln f_\theta(X_1))^2 = n I(\theta).
\]

Подставляя дисперсию в неравенство (9), получим
\[
1 \leq \mathbb{D}_\theta \theta^* \cdot n I(\theta) \quad \text{или} \quad \mathbb{D}_\theta \theta^* \geq \frac{1}{n I(\theta)},
\]
что и требовалось доказать.

Следующий пример показывает, что условие регулярности является существенным для выполнения равенства, помеченного (?) в лемме 5.

Пример 16. Нерегулярное семейство. Рассмотрим равномерное распределение \( U_{0,\theta} \) с параметром \( \theta > 0 \). Выпишем при \( n = 1 \) какой-нибудь интеграл и сравним производную от него и интеграл от производной:
\[
\frac{\partial}{\partial \theta} \int_0^\theta \frac{1}{\theta} dy = \frac{\partial}{\partial \theta} 1 = 0; \quad \int_0^\theta \frac{\partial}{\partial \theta} \frac{1}{\theta} dy = -\frac{1}{\theta} \neq 0.
\]

Заметим, что и само утверждение неравенства Рао-Крамера для данного семейства распределений не выполнено: найдется оценка, дисперсия которой ведет себя как \( 1/n^2 \), а не \( 1/n \), как в неравенстве Рао-Крамера.

Упражнение. Проверить, что в качестве этой «выдающейся» из неравенства Рао-Крамера оценки можно брать \( X_{(n)} \), или \( \frac{n+1}{n} X_{(n)} \in K_0 \).

4.4 Неравенство Рао-Крамера как способ проверки эффективности оценок

Сформулируем очевидное следствие из неравенства Рао-Крамера.

Следствие 1. Если семейство распределений \( \mathcal{F}_\theta \) удовлетворяет условиям регулярности (R) и (RR), и оценка \( \theta^* \in K_b \) такова, что в неравенстве Рао-Крамера достигается равенство:
\[
\mathbb{E}_\theta (\theta^* - \theta)^2 = \frac{(1 + b'(\theta))^2}{n I(\theta)} + b^2(\theta) \quad \text{или} \quad \mathbb{D}_\theta \theta^* = \frac{(1 + b'(\theta))^2}{n I(\theta)},
\]
то оценка \( \theta^* \) эффективна в классе \( K_b \).

Пример 17. Для выборки \( X_1, \ldots, X_n \) из распределения Пуассона \( \Pi_\lambda \) оценка \( \lambda^* = \overline{X} \) эффективна (в классе \( K_0 \)), так как для нее достигается равенство в неравенстве Рао-Крамера (см. [1], Пример на с. 42, решение 2).

Пример 18. Пусть \( X_1, \ldots, X_n \) — выборка объема \( n \) из нормального распределения \( N_{a, \sigma^2} \), где \( a \in \mathbb{R} \), \( \sigma > 0 \). Проверим, является ли оценка \( a^* = \overline{X} \in K_0 \) эффективной.