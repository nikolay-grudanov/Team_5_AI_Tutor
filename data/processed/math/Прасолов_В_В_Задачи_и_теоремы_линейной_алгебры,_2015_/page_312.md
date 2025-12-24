---
source_image: page_312.png
page_number: 312
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.98
tokens: 6845
characters: 3006
timestamp: 2025-12-24T08:16:11.887312
finish_reason: stop
---

но кососимметрическим), если \( f_{\sigma}(T) = T \) (соответственно \( f_{\sigma}(T) = = (-1)^{\sigma} T \)) для любой перестановки \( \sigma \). Симметрические тензоры образуют в \( T_0^q(V) \) подпространство \( S^q(V) \), а кососимметрические — подпространство \( \Lambda^q(V) \). Ясно, что \( S^q(V) \cap \Lambda^q(V) = 0 \) при \( q \geqslant 2 \).

Оператор \( S = \frac{1}{q!} \sum_{\sigma} f_{\sigma} \) называют симметризацией, а оператор \( A = \frac{1}{q!} \sum_{\sigma} (-1)^{\sigma} f_{\sigma} \) — антисимметризацией или альтернированием.

**Теорема 30.1.1.** *Оператор \( S \) является проектором \( T_0^q(V) \) на \( S^q(V) \), а оператор \( A \) — проектором на \( \Lambda^q(V) \).*

**Доказательство.** Очевидно, что симметризация любого тензора симметрична и на симметрических тензорах оператор действует тождественно.

Так как для любого \( T \in T_0^q(V) \) имеем

\[
f_{\sigma}(AT) = \frac{1}{q!} \sum_{\tau} (-1)^{\tau} f_{\sigma} f_{\tau}(T) = (-1)^{\sigma} \frac{1}{q!} \sum_{\rho=\sigma\tau} (-1)^{\rho} f_{\rho}(T) = (-1)^{\sigma} AT,
\]

то \( \operatorname{Im} A \subset \Lambda^q(V) \). Если тензор \( T \) кососимметричен, то

\[
AT = \frac{1}{q!} \sum_{\sigma} (-1)^{\sigma} f_{\sigma}(T) = \frac{1}{q!} \sum_{\sigma} (-1)^{\sigma}(-1)^{\sigma} T = T.
\]

Введём обозначения

\[
S(e_{i_1} \otimes \ldots \otimes e_{i_q}) = e_{i_1} \ldots e_{i_q} \quad \text{и} \quad A(e_{i_1} \otimes \ldots \otimes e_{i_q}) = e_{i_1} \wedge \ldots \wedge e_{i_q}.
\]

Например, \( e_i e_j = (e_i \otimes e_j + e_j \otimes e_i)/2 \) и \( e_i \wedge e_j = (e_i \otimes e_j - e_j \otimes e_i)/2 \). Если \( e_1, \ldots, e_n \) — базис \( V \), то тензоры \( e_{i_1} \ldots e_{i_q} \) порождают \( S^q(V) \), а тензоры \( e_{i_1} \wedge \ldots \wedge e_{i_q} \) порождают \( \Lambda^q(V) \). Тензор \( e_{i_1} \ldots e_{i_q} \) зависит лишь от того, сколько раз \( e_i \) встречается в этой записи, поэтому можно ввести обозначение \( e_{i_1} \ldots e_{i_q} = e_1^{k_1} \ldots e_n^{k_n} \), где вектор \( e_i \) встречается в записи \( e_{i_1} \ldots e_{i_q} \) ровно \( k_i \) раз. Тензор \( e_{i_1} \wedge \ldots \wedge e_{i_q} \) при перестановке любых двух векторов \( e_{i_{\alpha}} \) и \( e_{i_{\beta}} \) меняет знак, поэтому \( e_{i_1} \wedge \ldots \wedge e_{i_q} = 0 \), если \( e_{i_{\alpha}} = e_{i_{\beta}} \), и тензоры \( e_{i_1} \wedge \ldots \wedge e_{i_q} \), где \( 1 \leqslant i_1 < \ldots < i_q \leqslant n \), порождают пространство \( \Lambda^q(V) \). В частности, \( \Lambda^q(V) = 0 \) при \( q > n \).

**Теорема 30.1.2.** *Элементы \( e_1^{k_1} \ldots e_n^{k_n} \), где \( k_1 + \ldots + k_n = q \), образуют базис пространства \( S^q(V) \), а элементы \( e_{i_1} \wedge \ldots \wedge e_{i_q} \), где \( 1 \leqslant i_1 < \ldots < i_q \leqslant n \), образуют базис пространства \( \Lambda^q(V) \).*

**Доказательство.** Достаточно проверить линейную независимость этих векторов. Если наборы \( (k_1, \ldots, k_n) \) и \( (l_1, \ldots, l_n) \) различны, то тензоры