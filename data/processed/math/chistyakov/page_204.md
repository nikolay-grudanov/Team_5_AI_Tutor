---
source_image: page_204.png
page_number: 204
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.54
tokens: 8259
characters: 1411
timestamp: 2025-12-24T07:30:59.895758
finish_reason: stop
---

1. Доказательство теоремы о предельных вероятностях в цепи Маркова

Приведем доказательство теоремы 3.1 гл. 9 без использования теории матриц. Докажем сначала две леммы.

Положим
\[
v_l(t) = \min_i P_{il}(t), \quad V_l(t) = \max_j P_{jl}(t).
\]

Лемма 1. При любых \( l \) существуют пределы
\[
\lim_{t \to \infty} v_l(t) = q_l, \quad \lim_{t \to \infty} V_l(t) = Q_l
\]
и
\[
q_l \leq Q_l.
\]

Доказательство. Используя уравнение (9.2.4) с \( s = 1 \), получим
\[
v_j(t+1) = \min_i \sum_{k=1}^N p_{ik} P_{kj}(t) \geq \min_i \sum_{k=1}^N p_{ik} v_j(t) = v_j(t),
\]
\[
V_j(t+1) = \max_i \sum_{k=1}^N p_{ik} P_{kj}(t) \leq \max_i \sum_{k=1}^N p_{ik} V_j(t) = V_j(t).
\]

Таким образом, последовательности \( v_j(t) \) и \( V_j(t) \) монотонны и ограничены. Отсюда следует утверждение леммы 1.

Лемма 2. Если выполнены условия теоремы 9.3.1, то существуют постоянные \( C, \delta \) (\( C > 0, 0 < \delta < 1 \)) такие, что
\[
V_j(nt_0) - v_j(nt_0) \leq C \delta^n, \quad n = 1, 2, \ldots
\]

Доказательство. Для любых \( i, j \)
\[
0 = \sum_{k=1}^N P_{ik}(t_0) - \sum_{k=1}^N P_{jk}(t_0) = \sum_k + \Delta_k(i, j) + \sum_k - \Delta_k(j, i),
\]
где \( \Delta_k(i, j) = P_{ik}(t_0) - P_{jk}(t_0) \), \( \sum^+ \) означает суммирование по всем \( k \), при которых \( \Delta_k(i, j) \) положительны, а \( \sum^- \) — суммирование по остальным \( k \). Отсюда
\[
\sum_k^+ \Delta_k(i, j) = - \sum_k^- \Delta_k(i, j).
\]