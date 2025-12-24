---
source_image: page_431.png
page_number: 431
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.32
tokens: 6408
characters: 3786
timestamp: 2025-12-24T07:16:07.303871
finish_reason: stop
---

1491. Решение. Сначала докажем равенство

\[
\text{разм.} \mathbf{L} = \text{разм.} \varphi \mathbf{L} + \text{разм.} \mathbf{L}_0,
\]

(1)

где \( \mathbf{L}_0 \) — пересечение \( \mathbf{L} \) с ядром \( \varphi^{-1} \mathbf{0} \) преобразования \( \varphi \). Для этого базу \( a_1, a_2, \ldots, a_k \) подпространства \( \mathbf{L}_0 \) дополним векторами \( b_1, b_2, \ldots, b_l \) до базы \( \mathbf{L} \) (при \( \mathbf{L}_0 = \mathbf{0} \) отсутствуют векторы \( a_i \), при \( \mathbf{L}_0 = \mathbf{L} \) — векторы \( b_i \)). Векторы \( \varphi b_1, \varphi b_2, \ldots, \varphi b_l \) образуют базу \( \varphi \mathbf{L} \). В самом деле, если \( y \in \varphi \mathbf{L} \), то \( y = \varphi x \), где \( x \in \mathbf{L} \). Если \( x = \sum_{i=1}^k \alpha_i a_i + \sum_{i=1}^l \beta_i b_i \), то \( y = \varphi x = \sum_{i=1}^l \beta_i \varphi b_i \), так как \( \varphi a_i = 0 \) (\( i = 1, 2, \ldots, k \)). Векторы \( \varphi b_1, \varphi b_2, \ldots, \varphi b_l \) линейно независимы, так как из \( \sum_{i=1}^l \beta_i \varphi b_i = \mathbf{0} \) следует \( \sum_{i=1}^l \beta_i b_i \in \mathbf{L}_0 \), откуда \( \sum_{i=1}^l \beta_i b_i = \sum_{i=1}^k \alpha_i a_i \), и значит, \( \beta_i = 0 \) (\( i = 1, 2, \ldots, l \)).

Итак, разм. \( \mathbf{L} = l + k = \text{разм.} \varphi \mathbf{L} + \text{разм.} \mathbf{L}_0 \).

а) Из (1) в силу \( \mathbf{L}_0 \subset \varphi^{-1} \mathbf{0} \) находим

\[
\begin{align*}
\text{разм.} \mathbf{L} &= \text{разм.} \varphi \mathbf{L} + \text{разм.} \mathbf{L}_0 \leq \text{разм.} \varphi \mathbf{L} + \text{деф.} \varphi; \\
\text{разм.} \mathbf{L} - \text{деф.} \varphi &\leq \text{разм.} \varphi \mathbf{L}.
\end{align*}
\]

Далее, разм. \( \varphi \mathbf{L} = \text{разм.} \mathbf{L} - \text{разм.} \mathbf{L}_0 \leq \text{разм.} \mathbf{L} \).

б) Положим \( \varphi^{-1} \mathbf{L} = \mathbf{L}' \). Так как \( \mathbf{0} \in \mathbf{L} \), то \( \varphi^{-1} \mathbf{0} \subset \varphi^{-1} \mathbf{L} = \mathbf{L}' \) и \( \mathbf{L}' \cap \varphi^{-1} \mathbf{0} = \varphi^{-1} \mathbf{0} \). Применяя (1) с заменой \( \mathbf{L} \) на \( \mathbf{L}' \), получим

\[
\text{разм.} \mathbf{L}' = \text{разм.} \varphi \mathbf{L}' + \text{деф.} \varphi.
\]

Так как \( \varphi \mathbf{L}' \subset \mathbf{L} \), то \( \text{разм.} \varphi \mathbf{L}' \leq \text{разм.} \mathbf{L} \) и по (2) \( \text{разм.} \mathbf{L}' \leq \text{разм.} \mathbf{L} + \text{деф.} \varphi \), чем доказано второе из неравенств б).

Покажем, что \( \varphi \mathbf{L}' = \mathbf{L} \cap \varphi \mathbf{R}_n \).
Так как \( \varphi \mathbf{L}' \subset \mathbf{L} \) и \( \varphi \mathbf{L}' \subset \varphi \mathbf{R}_n \), то \( \varphi \mathbf{L}' \subset \mathbf{L} \cap \varphi \mathbf{R}_n \). Если \( x \in \mathbf{L} \cap \varphi \mathbf{R}_n \), то \( x = \varphi x' \), где \( x' \in \varphi^{-1} \mathbf{L} = \mathbf{L}' \), т. е. \( x \in \varphi \mathbf{L}' \).
Отсюда \( \mathbf{L} \cap \varphi \mathbf{R}_n \subset \varphi \mathbf{L}' \).
Так как разм. \( (\mathbf{L} + \varphi \mathbf{R}_n) \leq n \), то, используя связь размерности суммы и пересечения подпространств (задача 1316), получим

\[
\begin{align*}
\text{разм.} \varphi \mathbf{L}' &= \text{разм.} (\mathbf{L} \cap \varphi \mathbf{r}_n) = \text{разм.} \mathbf{L} + \text{разм.} \varphi \mathbf{R}_n - \text{разм.} (\mathbf{L} + \varphi \mathbf{R}_n) \geq \\
&\geq \text{разм.} \mathbf{L} + \text{разм.} \varphi \mathbf{R}_n - n = \text{разм.} \mathbf{L} - \text{деф.} \varphi.
\end{align*}
\]

Отсюда в силу (2) находим

\[
\text{разм.} \mathbf{L}' = \text{разм.} \varphi \mathbf{L}' + \text{деф.} \varphi \geq (\text{разм.} \mathbf{L} - \text{деф.} \varphi) + \text{деф.} \varphi = \text{разм.} \mathbf{L},
\]

чем доказано первое из неравенств б).