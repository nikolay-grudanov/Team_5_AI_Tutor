---
source_image: page_022.png
page_number: 22
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.96
tokens: 11771
characters: 2180
timestamp: 2025-12-24T08:25:32.150434
finish_reason: stop
---

\[
\mathbf{P}\left(A_k \cap \bigcup_{i=1}^{k-1} A_i\right) = \mathbf{P}\left(\bigcup_{i=1}^{k-1} (A_i \cap A_k)\right) = \sum_{i=1}^{k-1} \mathbf{P}(A_i \cap A_k) - \sum_{1 \leq i < j \leq k-1} \mathbf{P}(A_i \cap A_j \cap A_k) + 
\]
\[
+ \sum_{1 \leq i < j < m \leq k-1} \mathbf{P}(A_i \cap A_j \cap A_m \cap A_k) - \ldots + (-1)^{k-2} \mathbf{P}(A_1 \cap A_2 \cap \ldots \cap A_{k-1} \cap A_k).
\] (5)

Подставить (4),(5) в (3) и довести до конца шаг индукции.

Приведем пример задачи, в которой использование свойства 9 — самый простой путь решения.

Пример 12. Есть \( n \) писем и \( n \) подписанных конвертов. Письма раскладываются в конверты наудачу. Найти вероятность того, что хотя бы одно письмо попадет в предназначенный ему конверт и предел этой вероятности при \( n \to \infty \).

Решение. Пусть событие \( A_i,\ i = 1, \ldots, n \) означает, что \( i \)-е письмо попало в свой конверт. Тогда \( A = \{\text{хотя бы одно письмо попадет в свой конверт}\} = A_1 \cup \ldots \cup A_n \). И так как события \( A_1, \ldots, A_n \) совместны, придется использовать формулу (2). Нетрудно убедиться, что

\[
\mathbf{P}(A_i) = \frac{1}{n} \quad \text{для всех } i,
\]
\[
\mathbf{P}(A_i \cap A_j) = \frac{(n-2)!}{n!} = \frac{1}{n(n-1)} \quad \text{для всех } i \neq j,
\]
\[
\mathbf{P}(A_i \cap A_j \cap A_m) = \frac{(n-3)!}{n!} = \frac{1}{n(n-1)(n-2)} \quad \text{для всех } i \neq j \neq m, \ldots,
\]
\[
\mathbf{P}(A_1 \cap \ldots \cap A_n) = \frac{1}{n!}
\]

Вычислим количество слагаемых в каждой сумме в формуле (2). Например, в сумме \( \sum_{1 \leq i < j < m \leq n} \) ровно \( C_n^3 \) слагаемых — ровно столько трех-элементных множеств можно образовать из \( n \) элементов, и каждое такое множество \( \{i, j, m\} \) встречается в индексах данной суммы единажды.
Подставляя все вероятности в формулу (2), получим:

\[
\mathbf{P}(A) = n \cdot \frac{1}{n} - C_n^2 \cdot \frac{1}{n(n-1)} + C_n^3 \cdot \frac{1}{n(n-1)(n-2)} - \ldots + (-1)^{n-1} \frac{1}{n!} = 1 - \frac{1}{2!} + \frac{1}{3!} - \ldots + (-1)^{n-1} \frac{1}{n!}
\]

Выписать разложение \( e^{-1} \) в ряд Тейлора и убедиться, что \( \mathbf{P}(A) \longrightarrow 1 - e^{-1} \) при \( n \to \infty \).