---
source_image: page_116.png
page_number: 116
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.47
tokens: 8537
characters: 1347
timestamp: 2025-12-24T07:28:45.251701
finish_reason: stop
---

Теорема 2.2. Если \( A_1, A_2, \ldots, A_n \) — произвольные события, то

\[
P(A_1 + \ldots + A_n) = \sum_{k=1}^n P(A_k) -
\]
\[
- \sum_{1 \leq k_1 < k_2 \leq n} P(A_{k_1} A_{k_2}) + \ldots (-1)^{n+1} P(A_1 \ldots A_n) =
\]
\[
= \sum_{m=1}^n (-1)^{m+1} \sum_{1 \leq k_1 < k_2 < \ldots < k_m \leq n} P(A_{k_1} A_{k_2} \ldots A_{k_m}).
\]

Доказательство. Из равенства
\[
A_1 + A_2 + \ldots + A_n = \overline{A}_1 \overline{A}_2 \ldots \overline{A}_n
\]
следует, что
\[
P(A_1 + A_2 + \ldots + A_n) = 1 - P(\overline{A}_1 \overline{A}_2 \ldots \overline{A}_n). \tag{2.3}
\]

Введем случайные величины \( \eta_k, k = 1, 2, \ldots, n \), положив
\[
\eta_k = \eta_k(\omega) = \begin{cases}
1, & \text{если } \omega \in A_k, \\
0, & \text{если } \omega \in \overline{A}_k.
\end{cases}
\]

Очевидно, что случайная величина \( \prod_{k=1}^n (1 - \eta_k) \) принимает два значения: значение 1, если все \( \eta_k = 0 \), и значение 0 в остальных случаях. Событие \( (\eta_1 = \eta_2 = \ldots = \eta_n = 0) = \overline{A}_1 \overline{A}_2 \ldots \overline{A}_n \). Следовательно,
\[
M \prod_{k=1}^n (1 - \eta_k) = P(\overline{A}_1 \overline{A}_2 \ldots \overline{A}_n). \tag{2.4}
\]

Так как
\[
\prod_{k=1}^n (1 - \eta_k) =
\]
\[
= 1 - \sum_{k=1}^n \eta_k + \sum_{1 \leq k_1 < k_2 \leq n} \eta_{k_1} \eta_{k_2} - \ldots (-1)^n \eta_1 \eta_2 \ldots \eta_n,
\]