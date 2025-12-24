---
source_image: page_317.png
page_number: 317
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.25
tokens: 6736
characters: 2594
timestamp: 2025-12-24T08:16:18.923635
finish_reason: stop
---

Если \( T = v_1 \otimes \ldots \otimes v_q \), то \( B_q f_\sigma(T) = f_\sigma B_q(T) \), поэтому

\[
B_q f_\sigma(T) = f_\sigma B_q(T) \quad \text{для любого } T \in T^q_0(V).
\] (1)

Следовательно, \( B_q \) переводит симметрические тензоры в симметрические, а кососимметрические — в кососимметрические. Ограничения \( B_q \) на \( S^q(V) \) и \( \Lambda^q(V) \) обозначим \( S^q B \) и \( \Lambda^q B \) соответственно. Пусть \( S \) и \( A \) — операторы симметризации и альтернирования. Из равенства (1) следует, что \( B_q S = SB_q \) и \( B_q A = AB_q \). Поэтому \( B_q(e_1^{k_1} \ldots e_n^{k_n}) = (Be_1)^{k_1} \ldots (Be_n)^{k_n} \) и

\[
B_q(e_{i_1} \wedge \ldots \wedge e_{i_q}) = (Be_{i_1}) \wedge \ldots \wedge (Be_{i_q}).
\]

**Теорема 30.5.1.** *Пусть*

\[
B_q(e_{j_1} \wedge \ldots \wedge e_{j_q}) = \sum_{1 \leq i_1 < \ldots < i_q \leq n} b_{j_1 \ldots j_q}^{i_1 \ldots i_q} e_{i_1} \wedge \ldots \wedge e_{i_q}.
\]

*Тогда* \( b_{j_1 \ldots j_q}^{i_1 \ldots i_q} \) — минор \( B \left( \begin{array}{ccc} i_1 & \ldots & i_q \\ j_1 & \ldots & j_q \end{array} \right) \) матрицы оператора \( B \).

**Доказательство.** Ясно, что

\[
\begin{align*}
Be_{j_1} \wedge \ldots \wedge Be_{j_q} &= \left( \sum_{i_1} b_{i_1 j_1} e_{i_1} \right) \wedge \ldots \wedge \left( \sum_{i_q} b_{i_q j_q} e_{i_q} \right) = \\
&= \sum_{i_1, \ldots, i_q} b_{i_1 j_1} \ldots b_{i_q j_q} e_{i_1} \wedge \ldots \wedge e_{i_q} = \\
&= \sum_{1 \leq i_1 < \ldots < i_q \leq n} \left( \sum_{\sigma} (-1)^{\sigma} b_{i_{\sigma(1)} j_1} \ldots b_{i_{\sigma(q)} j_q} \right) e_{i_1} \wedge \ldots \wedge e_{i_q}. \tag*{\qedhere}
\end{align*}
\]

**Следствие.** \( \Lambda^q(B) = C_q(B) \) — *ассоциированная матрица* (см. п. 2.8).

Введём на множестве наборов индексов \( (i_1, \ldots, i_q) \) лексикографический порядок, т. е. будем считать, что \( (i_1, \ldots, i_q) < (j_1, \ldots, j_q) \), если \( i_1 = j_1, \ldots, i_r = j_r \) и \( i_{r+1} < j_{r+1} \). В соответствии с лексикографическим порядком упорядочим базисные векторы \( \{e_1^{k_1} \ldots e_n^{k_n}\} \) и \( \{e_{i_1} \wedge \ldots \wedge e_{i_q}\} \).

**Теорема 30.5.2.** *Если матрица оператора \( B \) треугольна в базисе \( e_1, \ldots, e_n \), то матрицы \( S^q B \) и \( \Lambda^q B \) треугольны в базисах \( \{e_1^{k_1} \ldots e_n^{k_n}\} \) и \( \{e_{i_1} \wedge \ldots \wedge e_{i_q}\} \), упорядоченных лексикографически.*

**Доказательство.** Пусть, например, \( Be_i \in \langle e_1, \ldots, e_i \rangle \), т. е. в соответствии с нашим отношением порядка \( Be_i \leq e_i \). Если \( i_1 \leq j_1, \ldots, i_q \leq j_q \),