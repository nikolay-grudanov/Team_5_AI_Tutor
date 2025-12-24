---
source_image: page_200.png
page_number: 200
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.15
tokens: 8274
characters: 1404
timestamp: 2025-12-24T07:30:52.600157
finish_reason: stop
---

Рассмотрим критический процесс. В этом случае \( a = 1, b > 0 \) и уравнение (4.9) запишется в виде

\[
Q(t+1) = Q(t) - \frac{b_t}{2} Q^2(t),
\]

где \( b_t \to b \) при \( t \to \infty \). Отсюда

\[
\frac{Q(t+1)}{Q(t)} = 1 - \frac{b_t}{2} Q(t) \to 1, \quad t \to \infty.
\]

Равенство (4.13) запишем в виде

\[
Q(t+1) = Q(t) - \frac{b}{2} Q(t) Q(t+1) + e(t),
\]

где

\[
e(t) = \frac{b}{2} Q(t) Q(t+1) - \frac{b_t}{2} Q^2(t).
\]

Используя (4.14), при \( t \to \infty \) получим

\[
\frac{e(t)}{Q(t) Q(t+1)} = \frac{b}{2} - \frac{b_t}{2} \frac{Q(t)}{Q(t+1)} \to 0.
\]

Отсюда и из (4.15) вытекает, что

\[
\frac{1}{Q(s+1)} = \frac{1}{Q(s)} + \frac{b}{2} + \delta(s),
\]

где \( \delta(s) \to 0 \) при \( s \to \infty \).

Суммируя последнее равенство от \( s = 1 \) до \( s = t-1 \), при \( t \to \infty \) получим

\[
\frac{1}{Q(t)} = 1 + \frac{bt}{2} + \sum_{s=1}^{t-1} \delta(s) =
\]
\[
= \frac{bt}{2} \left( 1 + \frac{2}{bt} + \frac{2}{bt} \sum_{s=1}^{t-1} \delta(s) \right) = \frac{bt}{2} (1 + o(1)).
\]

Таким образом, для критических ветвящихся процессов с конечным моментом (4.8) при \( t \to \infty \) имеем

\[
Q(t) = \frac{2}{bt} (1 + o(1)).
\]

Мы рассматривали ветвящийся процесс, начинающийся с одной частицы. Общее число частиц \( \mu_t \) в процессе, начавшемся с \( n \) частиц, можно представить в виде

\[
\mu_t = \mu_t^{(1)} + \mu_t^{(2)} + \ldots + \mu_t^{(n)}, \quad \mu_0 = n,
\]