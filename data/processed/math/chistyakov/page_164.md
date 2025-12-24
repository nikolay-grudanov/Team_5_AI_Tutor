---
source_image: page_164.png
page_number: 164
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.41
tokens: 8006
characters: 1846
timestamp: 2025-12-24T07:30:10.595917
finish_reason: stop
---

Докажем основное свойство цепи Маркова, определенной формулами (1.1) — (1.4).

Теорема 1.1. Если \( \xi_t \) — номер состояния цепи Маркова в момент \( t \), то

\[
P(\xi_{t+1} = j | \xi_0 = i_0, \xi_i = i_1, \ldots, \xi_{t-1} = i_{t-1}, \xi_t = i) =
= P(\xi_{t+1} = j | \xi_t = i)
\]

и, кроме того,

\[
P(\xi_{t+1} = j | \xi_t = i) = p_{ij}
\]

при любых \( t = 0, 1, 2, \ldots, T-1 \) и любых \( i_0, i_1, \ldots, i_{t-1}, i, j = 1, 2, \ldots, N \).

Доказательство. Используя определение условной вероятности и (1.5), получим

\[
\begin{align*}
P(\xi_{t+1} = j | \xi_0 = i_0, \ldots, \xi_{t-1} = i_{t-1}, \xi_t = i) &= \\
&= \frac{P(\xi_0 = i_0, \ldots, \xi_{t-1} = i_{t-1}, \xi_t = i, \xi_{t+1} = j)}{P(\xi_0 = i_0, \ldots, \xi_{t-1} = i_{t-1}, \xi_t = i)} = \\
&= \frac{q_{i_0} p_{i_0 i_1} \cdots p_{i_{t-1} i} p_{ij}}{q_{i_0} p_{i_0 i_1} \cdots p_{i_{t-1} i}} = p_{ij}.
\end{align*}
\]

Правую часть (1.6) запишем в виде

\[
\begin{align*}
P(\xi_{t+1} = j | \xi_t = i) &= \frac{P(\xi_t = i, \xi_{t+1} = j)}{P(\xi_t = i)} = \\
&= \frac{\sum P(\xi_0 = i_0, \ldots, \xi_{t-1} = i_{t-1}, \xi_t = i, \xi_{t+1} = j)}{\sum P(\xi_0 = i_0, \ldots, \xi_{t-1} = i_{t-1}, \xi_t = i)} = \\
&= \frac{\sum q_{i_0} p_{i_0 i_1} \cdots p_{i_{t-1} i} p_{ij}}{\sum q_{i_0} p_{i_0 i_1} \cdots p_{i_{t-1} i}} = p_{ij},
\end{align*}
\]

где суммирование проводится по каждому из индексов \( i_0, i_1, \ldots, i_{t-1} \) от 1 до \( N \). Утверждение теоремы следует из (1.7) и (1.8). Свойство (1.6) можно интерпретировать следующим образом: состояние системы в момент \( t+1 \) при известном состоянии в момент \( t \) не зависит от поведения системы в более далеком прошлом (в моменты \( s < t \)).

Так же, как (1.6), можно доказать следующее равенство:

\[
P(\xi_{t+s} = j | \xi_u \in B_u, u = 0, 1, \ldots, s-1, \xi_s = i) =
= P(\xi_{t+s} = j | \xi_s = i),
\]