---
source_image: page_330.png
page_number: 330
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.12
tokens: 6585
characters: 2620
timestamp: 2025-12-24T08:16:32.951661
finish_reason: stop
---

**Следствие (соотношения Плюккера).** Кососимметрический тензор \( \omega = \sum_{i_1 < \ldots < i_k} a_{i_1 \ldots i_k} e_{i_1} \wedge \ldots \wedge e_{i_k} \) разложим тогда и только тогда, когда
\[
\left( \sum_{i_1 < \ldots < i_k} a_{i_1 \ldots i_k} e_{i_1} \wedge \ldots \wedge e_{i_k} \right) \wedge \left( \sum_j a_{j_1 \ldots j_{k-1} j} e_j \right) = 0
\]
для любого набора чисел \( j_1 < \ldots < j_{k-1} \).

**Доказательство.** Пусть \( W \) — минимальное обёртывающее пространство для \( \omega \). Вычисление из теоремы 32.2.1 показывает, что \( W \) состоит из векторов \( \sum_j a_{j_1 \ldots j_{k-1} j} e_j \) (подразумевается, что коэффициент \( a_{j_1 \ldots j_{k-1} j} \) меняет знак при перестановке любых двух индексов). Согласно теореме 32.2.2 кососимметрический тензор \( \omega \) разложим тогда и только тогда, когда \( \omega \wedge w = 0 \) для всех \( w \in W \).

Рассмотрим подробнее случай \( k = 2 \). Коэффициент при \( e_i \wedge e_j \wedge e_p \) в левой части соотношения Плюккера для фиксированного \( j_1 = q \) равен \( a_{ij} a_{qp} + a_{pi} a_{qj} + a_{jp} a_{qi} \). Легко также проверить, что соотношение \( a_{ij} a_{qp} + a_{pi} a_{qj} + a_{jp} a_{qi} = 0 \) нетривиально, только если индексы \( i, j, p, q \) попарно различны.

Критерий разложимости кососимметрического тензора (теорема 32.2.2) можно записать и по-другому.

**Теорема 32.2.3.** а) *Кососимметрический тензор \( \omega \in \Lambda^k V \) разложим тогда и только тогда, когда \( i(\alpha)\omega \wedge \omega = 0 \) для любого \( \alpha \in \Lambda^{k-1} V^* \).
б) *Кососимметрический тензор \( \omega \in \Lambda^k V \) разложим тогда и только тогда, когда \( i(i(\omega)\beta)\omega = 0 \) для любого \( \beta \in \Lambda^{k+1} V^* \).

**Доказательство.** а) Согласно теореме 32.2.1 минимальное обёртывающее пространство \( W \) состоит из векторов вида \( i(\alpha)\omega \).
б) Это условие эквивалентно условию а). Действительно, \( i(\omega)\beta \in \Lambda^1 V^* \) и \( i(i(\omega)\beta)\omega \in \Lambda^{k-1} V \). Поэтому для \( \alpha \in \Lambda^{k-1} V^* \) можно рассмотреть
\[
\langle i(i(\omega)\beta)\omega, \alpha \rangle = \langle \omega, (i(\omega)\beta) \wedge \alpha \rangle =
= (-1)^{k-1} \langle \omega, \alpha \wedge (i(\omega)\beta) \rangle =
= (-1)^{k-1} \langle i(\alpha)\omega, i(\omega)\beta \rangle =
= (-1)^{k-1} \langle \omega \wedge i(\alpha)\omega, \beta \rangle.
\]
Таким образом, \( i(i(\omega)\beta)\omega = 0 \) для всех \( \beta \in \Lambda^{k+1} V^* \) тогда и только тогда, когда \( i(\alpha)\omega \wedge \omega = 0 \) для всех \( \alpha \in \Lambda^{k-1} V^* \).