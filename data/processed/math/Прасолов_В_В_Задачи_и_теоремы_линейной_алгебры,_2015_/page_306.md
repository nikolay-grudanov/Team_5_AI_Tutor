---
source_image: page_306.png
page_number: 306
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.53
tokens: 6614
characters: 2607
timestamp: 2025-12-24T08:15:50.823897
finish_reason: stop
---

Замечание. Пространство \( V^* \otimes V \) и отображения \( \alpha \) и \( \varepsilon \) определены инвариантно, поэтому теорема 29.3.2 даёт инвариантное определение следа оператора.

Теорема 29.3.3. Имеет место канонический изоморфизм

\[
\operatorname{Hom}(V \otimes W, U) \cong \operatorname{Hom}(V, \operatorname{Hom}(W, U)).
\]

Доказательство. Согласно теореме 29.3.1

\[
\operatorname{Hom}(V \otimes W, U) \cong (V \otimes W)^* \otimes U,
\]
\[
\operatorname{Hom}(V, \operatorname{Hom}(W, U)) \cong V^* \otimes (W^* \otimes U).
\]

Остаётся заметить, что тензорное произведение ассоциативно и имеет место канонический изоморфизм \( V^* \otimes W^* \cong (V \otimes W)^* \).

29.4. Валентность тензора

Тензором типа \((p, q)\) на пространстве \(V\) называют элемент пространства \(T_p^q(V) = V^* \otimes \ldots \otimes V^* \otimes V \otimes \ldots \otimes V\) (\(p\) экземпляров пространства \(V^*\) и \(q\) экземпляров пространства \(V\)), изоморфного пространству линейных функций на \(V \times \ldots \times V \times V^* \times \ldots \times V^*\). Число \(p\) называют ковариантной валентностью тензора, \(q\) — контравариантной валентностью, \(p + q\) — общей валентностью. Векторы являются тензорами типа \((0, 1)\), а ковекторы — тензорами типа \((1, 0)\).

Пусть в пространстве \(V\) выбран базис \(e_1, \ldots, e_n\) и \(e_1^*, \ldots, e_n^*\) — двойственный ему базис пространства \(V^*\). Каждый тензор типа \((p, q)\) имеет вид

\[
T_{i_1 \ldots i_p}^{j_1 \ldots j_q} e_{i_1}^* \otimes \ldots \otimes e_{i_p}^* \otimes e_{j_1} \otimes \ldots \otimes e_{j_q};
\]

числа \(T_{i_1 \ldots i_p}^{j_1 \ldots j_q}\) называют координатами (или компонентами) тензора относительно базиса \(e_1, \ldots, e_n\).

Выясним, как изменяются координаты тензора при переходе к другому базису. Пусть \(\varepsilon_j = Ae_j = \bullet\ a_{ij}e_i\) и \(\varepsilon_j^* = \bullet\ b_{ij}e_i^*\). Легко проверить, что \(B = (A^T)^{-1}\) (см. п. 5.4). Введём обозначения \(a_j^i = a_{ij}\) и \(b_i^j = b_{ij}\); тензор (1) для краткости обозначим \(\bullet\ T_\alpha^\beta e_\alpha^* \otimes e_\beta\). Тогда \(\bullet\ T_\alpha^\beta e_\alpha^* \otimes e_\beta = \bullet\ S_\mu^\nu \varepsilon_\mu^* \otimes \varepsilon_\nu = \bullet\ S_\mu^\nu b_\alpha^\mu a_\nu^\beta e_\alpha^* \otimes e_\beta\), т. е.
\[
T_{i_1 \ldots i_p}^{j_1 \ldots j_q} = b_{i_1}^{l_1} \ldots b_{i_p}^{l_p} a_{k_1}^{j_1} \ldots a_{k_q}^{j_q} S_{l_1 \ldots l_p}^{k_1 \ldots k_q}
\]
(по одинаковым индексам производится суммирование). Формула (2) связывает координаты \(S\) тензора в базисе \(\{\varepsilon_i\}\) и координаты \(T\) в ба-