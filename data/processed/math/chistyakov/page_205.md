---
source_image: page_205.png
page_number: 205
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.06
tokens: 5468
characters: 1829
timestamp: 2025-12-24T07:31:05.458597
finish_reason: stop
---

ПРИЛОЖЕНИЯ

Так как в условиях теоремы 9.3.1 вероятности перехода \( P_{ij}(t_0) > 0 \) при всех \( i, j \), то при любых \( i, j \)

\[
\sum_k^+ \Delta_k(i, j) = \sum_k^+ (P_{ik}(t_0) - P_{jk}(t_0)) < \sum_{k=1}^N P_{ik}(t_0) = 1
\] (2)

и в силу конечности числа состояний

\[
\delta = \max_{i, j} \sum_k^+ (P_{ik}(t_0) - P_{jk}(t_0)) < 1.
\] (3)

Оценим теперь разность \( V_j(nt_0) - v_j(nt_0) \). Используя уравнение (9.2.4) с \( s = t_0, t = nt_0 \), получим

\[
V_t((n+1)t_0) - v_t((n+1)t_0) = \max_{i, j} [P_{ii}((n+1)t_0) - P_{jj}((n+1)t_0)] =
\]
\[
= \max_{i, j} \sum_{k=1}^N [P_{ik}(t_0) - P_{jk}(t_0)] P_{kl}(nt_0) =
\]
\[
= \max_{i, j} \sum_{k=1}^N \Delta_k(i, j) P_{kl}(nt_0) \leq
\]
\[
\leq \max_{i, j} \left\{ \sum_k^+ \Delta_k(i, j) V_t(nt_0) + \sum_k^- \Delta_k(i, j) v_t(nt_0) \right\}.
\]

Отсюда, используя (1), (2) и (3), найдем

\[
V_t((n+1)t_0) - v_t((n+1)t_0) \leq
\]
\[
\leq \max_{i, j} \left\{ (V_t(nt_0) - v_t(nt_0)) \sum_k^+ \Delta_k(i, j) \right\} =
\]
\[
= \delta (V_t(nt_0) - v_t(nt_0)).
\]

Отсюда и из неравенства (3) следует утверждение леммы.

Перейдем к доказательству теоремы. Так как последовательности \( v_t(t), V_t(t) \) монотоны, то

\[
0 < v_t(t) \leq q_t \leq Q_t \leq V_t(t).
\] (4)

Отсюда и из леммы 2 находим

\[
0 \leq Q_t - q_t \leq U_1(nt_0) - v_t(nt_0) \leq C \delta^n.
\]

Следовательно, при \( n \to \infty \) получим \( Q_t = q_t = q_t^* \) и

\[
|P_{ij}(t) - q_t^*| \leq V_j(t) - v_j(t) \leq
\]
\[
\leq V_j\left( \left[ \frac{t}{t_0} \right] t_0 \right) - v_j\left( \left[ \frac{t}{t_0} \right] t_0 \right) \leq C \delta^{\frac{t}{t_0} - 1}.
\] (5)

Положительность \( q_t^* \) следует из неравенств (4). Переходя к пределу при \( t \to \infty \) и \( s = 1 \) в уравнении (9.2.4), получим, что \( q_t^* \) удовлетворяют уравнению (9.3.2). Таким образом, теорема доказана.