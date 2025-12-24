---
source_image: page_316.png
page_number: 316
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.12
tokens: 6687
characters: 2867
timestamp: 2025-12-24T08:16:14.136903
finish_reason: stop
---

Теорема 30.4.2. Имеют место следующие канонические изоморфизмы:

а) \( \Lambda^q(V \oplus W) \cong \bigoplus_{i=0}^q (\Lambda^i V \otimes \Lambda^{q-i} W); \)

б) \( S^q(V \oplus W) \cong \bigoplus_{i=0}^q (S^i V \otimes S^{q-i} W). \)

Доказательство. Ясно, что \( \Lambda^i V \subset T_0^i(V \oplus W) \) и \( \Lambda^{q-i} W \subset T_0^{q-i}(V \oplus W) \). Поэтому имеется каноническое вложение \( \Lambda^i V \otimes \Lambda^{q-i} W \subset T_0^q(V \oplus W) \). Спроектируем \( T_0^q(V \oplus W) \) на \( \Lambda^q(V \oplus W) \) с помощью оператора альтернирования. В результате получим каноническое отображение

\[
\Lambda^i V \otimes \Lambda^{q-i} W \to \Lambda^q(V \oplus W).
\]

При этом отображении элемент \( (v_1 \wedge \ldots \wedge v_i) \otimes (w_1 \wedge \ldots \wedge w_{q-i}) \) переходит в \( v_1 \wedge \ldots \wedge v_i \wedge w_1 \wedge \ldots \wedge w_{q-i} \). Выбрав в пространствах \( V \) и \( W \) базисы, легко проверить, что построенное отображение

\[
\bigoplus_{i=0}^q (\Lambda^i V \otimes \Lambda^{q-i} W) \to \Lambda^q(V \oplus W)
\]

является изоморфизмом.

Для пространства \( S^q(V \oplus W) \) доказательство аналогично.

Докажем, что это отображение — изоморфизм. Выберем в пространстве \( V \) базис \( e_1, \ldots, e_n \). Элементу \( e_{i_1} \wedge \ldots \wedge e_{i_p} \) соответствует отображение, переводящее \( e_{j_1} \wedge \ldots \wedge e_{j_{n-p}} \) в 0 или в \( \pm e_1 \wedge \ldots \wedge e_n \) в зависимости от того, пересекаются ли множества \( \{i_1, \ldots, i_p\} \) и \( \{j_1, \ldots, j_{n-p}\} \) или дополняют друг друга до \( \{1, \ldots, n\} \). Такие отображения образуют базис пространства \( \mathrm{Hom}(\Lambda^{n-p} V, \Lambda^n V) \).

Доказательство. Внешнее произведение является отображением

\[
\Lambda^p V \times \Lambda^{n-p} V \to \Lambda^n V,
\]

поэтому каждому элементу \( \Lambda^p V \) соответствует некоторое отображение \( \Lambda^{n-p} V \to \Lambda^n V \). В итоге получаем отображение

\[
\Lambda^p V \to \mathrm{Hom}(\Lambda^{n-p} V, \Lambda^n V) \cong (\Lambda^{n-p} V)^* \otimes \Lambda^n V.
\]

Докажем, что это отображение — изоморфизм. Выберем в пространстве \( V \) базис \( e_1, \ldots, e_n \). Элементу \( e_{i_1} \wedge \ldots \wedge e_{i_p} \) соответствует отображение, переводящее \( e_{j_1} \wedge \ldots \wedge e_{j_{n-p}} \) в 0 или в \( \pm e_1 \wedge \ldots \wedge e_n \) в зависимости от того, пересекаются ли множества \( \{i_1, \ldots, i_p\} \) и \( \{j_1, \ldots, j_{n-p}\} \) или дополняют друг друга до \( \{1, \ldots, n\} \). Такие отображения образуют базис пространства \( \mathrm{Hom}(\Lambda^{n-p} V, \Lambda^n V) \).

30.5. Тензорная степень оператора

Линейный оператор \( B : V \to V \) индуцирует линейный оператор \( B_q : T_0^q(V) \to T_0^q(V) \), отображающий \( v_1 \otimes \ldots \otimes v_q \) в \( Bv_1 \otimes \ldots \otimes Bv_q \).