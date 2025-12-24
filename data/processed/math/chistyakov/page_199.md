---
source_image: page_199.png
page_number: 199
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.40
tokens: 4986
characters: 1253
timestamp: 2025-12-24T07:30:51.430352
finish_reason: stop
---

§ 4] ВЕТВЯЩИЙСЯ ПРОЦЕСС

Используя формулу Тейлора, запишем (4.7) в виде
\[
Q(t+1) = 1 - \varphi(1) + \varphi'(1) Q(t) -
\frac{Q^2(t)}{2} \varphi''(1 - \theta Q(t)), \quad 0 < \theta < 1.
\]
Отсюда
\[
Q(t+1) = a Q(t) - \frac{b_t}{2} Q^2(t),
\]
где
\[
b_t = \varphi''(1 - \theta Q(t)), \quad 0 < \theta < 1,
\]
и
\[
\frac{Q(s+1)}{Q(s)} = a \left( 1 - \frac{b_s}{2a} Q(s) \right), \quad s = 1, 2, \ldots.
\]
Перемножив эти равенства от \( s = t_0 \) до \( s = t-1 \) (\( 0 < t_0 < t-1 \)), получим
\[
Q(t) = K_t a^t,
\]
где
\[
K_t = Q(t_0) \prod_{s = t_0}^{t-1} \left( 1 - \frac{b_s}{2a} Q(s) \right).
\]
Так как
\[
Q(s) = P \left( \mu_s \geq \frac{1}{2} \right) \leq 2 M \mu_s = 2 a^s, \quad 0 < a < 1,
\]
и \( b_s \to b \) при \( s \to \infty \), то при достаточно большом \( t_0 \) сомножители в (4.11) положительны. Из неравенства (4.12) следует сходимость ряда
\[
\sum_{s = t_0}^{\infty} \ln \left( 1 - \frac{b_s}{2a} Q(s) \right) = \ln K \quad 0 < K < \infty,
\]
и оценка
\[
\sum_{s = t}^{\infty} \ln \left( 1 - \frac{b_s}{2a} Q(s) \right) = O(a^t), \quad t \to \infty.
\]
Отсюда при \( t \to \infty \)
\[
K_1 = K (1 + O(a^t)).
\]
Таким образом, если \( 0 < a < 1 \) и конечен момент (4.8), то при \( t \to \infty \)
\[
Q(t) = K a^t (1 + O(a^t)).
\]