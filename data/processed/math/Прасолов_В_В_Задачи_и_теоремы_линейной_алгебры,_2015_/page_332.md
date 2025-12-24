---
source_image: page_332.png
page_number: 332
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.21
tokens: 6465
characters: 2397
timestamp: 2025-12-24T08:16:38.033494
finish_reason: stop
---

Сумма \( \bullet\ (-1)^{(i_1,\ldots,i_m)} M_{1i_1} \cdot \ldots \cdot M_{mi_m} \) равна определителю матрицы \( \|M_{ij}\| \). Согласно задаче 1.29 этот определитель равен определителю присоединённой матрицы \( \operatorname{adj}\,A \), а определитель присоединённой матрицы равен \( |A|^{m-1} \).

Второй способ. Каждый вектор \( c_j(\omega) \) является линейной комбинацией векторов \( v_1, \ldots, v_m \), поэтому

\[
c_1(\omega) \wedge \ldots \wedge c_m(\omega) = \lambda v_1 \wedge \ldots \wedge v_m.
\]

Непосредственно из определения \( c_j \) видно, что \( \alpha_i(c_j(\omega)) = \delta_{ij} c(\omega) \). Поэтому, применив с к обеим частям равенства (2), получим \( (c(\omega))^m = \lambda c(\omega) \), т. е. \( c(\omega)(\lambda - (c(\omega))^{m-1}) = 0 \). Если \( c(\omega) \neq 0 \), то мы получаем \( \lambda = (c(\omega))^{m-1} \), что и требовалось. Если же \( c(\omega) = 0 \), то матрица \( A = \| \alpha_j(v_i) \| \) вырожденная, а потому присоединённая матрица \( \operatorname{adj}\,A \) тоже вырожденная. Из этого легко вывести, что векторы \( c_1(\omega), \ldots, c_m(\omega) \) линейно зависимы, поскольку эти векторы являются линейными комбинациями векторов \( v_1, \ldots, v_m \), коэффициентами которых служат элементы матрицы \( \operatorname{adj}\,A \). Таким образом, если \( c(\omega) = 0 \), то \( c_1(\omega) \wedge \ldots \wedge c_m(\omega) = 0 \), поэтому равенство (1) снова выполняется.

Замечание. Записав равенство (1) в координатах, мы получим систему уравнений степени \( m \).

32.4. Свойства отображения \( d = i(v) \)

Обсудим теперь некоторые свойства рассмотренного выше отображения \( d = i(v): \Lambda^k V^* \to \Lambda^{k-1} V^* \) для фиксированного \( v \in V \). Это отображение обладает тем свойством, что \( d^2 = d \circ d = 0 \). А так как

\[
\langle f_1 \wedge \ldots \wedge f_k, v \wedge v_1 \wedge \ldots \wedge v_{k-1} \rangle = \frac{1}{k!} \begin{vmatrix}
f_1(v) & \ldots & f_1(v_{k-1}) \\
\cdots & \cdots & \cdots \\
f_k(v) & \ldots & f_k(v_{k-1})
\end{vmatrix},
\]

то, разложив этот определитель по первому столбцу, получим

\[
d(f_1 \wedge \ldots \wedge f_k) = \bullet\ (-1)^{i+1} f_i(v) f_1 \wedge \ldots \wedge \hat{f}_i \wedge \ldots \wedge f_k.
\]

Теорема 32.4.1. Если \( \alpha \in \Lambda^p V^* \) и \( \beta \in \Lambda^q V^* \), то

\[
d(\alpha \wedge \beta) = (d\alpha) \wedge \beta + (-1)^p \alpha \wedge (d\beta).
\]