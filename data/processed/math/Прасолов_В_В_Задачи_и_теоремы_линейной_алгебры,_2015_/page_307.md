---
source_image: page_307.png
page_number: 307
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.09
tokens: 6584
characters: 2622
timestamp: 2025-12-24T08:15:55.273650
finish_reason: stop
---

зисе \( \{e_i\} \). Несколько иную интерпретацию закона преобразования координат тензоров типа (0, 1) и (1, 0) см. в п. 7.1.

Для тензоров типа (1, 1), которые можно отождествить с линейными операторами, определено отображение свёртки, переводящее \( v^* \otimes w \) в \( v^*(w) \). При этом отображении оператору сопоставляется его след (см. теорему 29.3.2).

Общее отображение свёртки определяется следующим образом. Пусть \( 1 \leq i \leq p \) и \( 1 \leq j \leq q \). Рассмотрим линейное отображение \( T_p^q(V) \to T_{p-1}^{q-1}(V) \), переводящее \( f_1 \otimes \ldots \otimes f_p \otimes v_1 \otimes \ldots \otimes v_q \) в \( f_i(v_j)f_i \otimes v_j \), где \( f_i \) и \( v_j \) — тензорные произведения элементов \( f_1, \ldots, f_p \) и \( v_1, \ldots, v_q \) без \( f_i \) и \( v_j \) соответственно. Это отображение называют свёрткой тензора по \( i \)-му нижнему индексу и \( j \)-му верхнему индексу.

**29.5. Тензорное произведение отображений**

Линейные отображения \( A_i : V_i \to W_i \) (\( i = 1, \ldots, k \)) индуцируют линейное отображение \( A_1 \otimes \ldots \otimes A_k : V_1 \otimes \ldots \otimes V_k \to W_1 \otimes \ldots \otimes W_k \), переводящее элемент \( e_{1i} \otimes \ldots \otimes e_{kj} \) в \( A_1 e_{1i} \otimes \ldots \otimes A_k e_{kj} \). Легко проверить, что при этом элемент \( v_1 \otimes \ldots \otimes v_k \) переходит в \( A_1 v_1 \otimes \ldots \otimes A_k v_k \). Отображение \( A_1 \otimes \ldots \otimes A_k \) называют тензорным произведением отображений \( A_1, \ldots, A_k \), или произведением Кронекера.

Если \( Ae_j = \bullet\ a_{ij}\varepsilon_i \) и \( Be'_q = \bullet\ b_{pq}\varepsilon'_p \), то

\[
A \otimes B(e_j \otimes e'_q) = \bullet\ a_{ij}b_{pq}\varepsilon_i \otimes \varepsilon'_p.
\]

Поэтому, упорядочив соответствующим образом базисы \( e_j \otimes e'_q \) и \( \varepsilon_i \otimes \varepsilon'_p \), матрицу \( A \otimes B \) можно записать в виде

\[
\begin{pmatrix}
a_{11}B & \ldots & a_{1n}B \\
\cdots & \cdots & \cdots \\
a_{m1}B & \ldots & a_{mn}B
\end{pmatrix}
\]

или в виде

\[
\begin{pmatrix}
b_{11}A & \ldots & b_{1l}A \\
\cdots & \cdots & \cdots \\
b_{k1}A & \ldots & b_{kl}A
\end{pmatrix};
\]

матрицу \( A \otimes B \) называют кронекеровским произведением матриц \( A \) и \( B \).

**Теорема 29.5.1.** *Пусть собственные значения квадратных матриц \( A \) и \( B \) равны \( \alpha_1, \ldots, \alpha_m \) и \( \beta_1, \ldots, \beta_n \). Тогда собственные значения матрицы \( A \otimes B \) равны \( \alpha_i \beta_j \), а собственные значения матрицы \( A \otimes I_n + I_m \otimes B \) равны \( \alpha_i + \beta_j \).*