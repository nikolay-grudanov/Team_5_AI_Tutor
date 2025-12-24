---
source_image: page_324.png
page_number: 324
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.94
tokens: 6759
characters: 2773
timestamp: 2025-12-24T08:16:29.805138
finish_reason: stop
---

Поэтому \( f(A) = f(XJX^T) = (\det X)f(J) \) и
\[
\det A = (\det X)^2 = (f(A)/f(J))^2.
\]
Докажем, что \( f(A) = n! \cdot \sum_{\sigma} (-1)^{\sigma} a_{i_1 i_2} a_{i_3 i_4} \cdots a_{i_{2n-1} i_{2n}} \), где
\[
\sigma = \begin{pmatrix}
1 & \ldots & 2n \\
i_1 & \ldots & i_{2n}
\end{pmatrix}
\]
и суммирование ведётся по всем разбиениям множества \( \{1, \ldots, 2n\} \) на пары \( \{i_k, i_{k+1}\} \), где \( i_k < i_{k+1} \) (но не по всем перестановкам \( \sigma \)). Пусть \( \omega_{ij} = a_{ij} e_i \wedge e_j \), тогда \( \omega_{ij} \wedge \omega_{kl} = \omega_{kl} \wedge \omega_{ij} \), причём \( \omega_{ij} \wedge \omega_{kl} = 0 \), если среди индексов \( i, j, k, l \) есть совпадающие. Поэтому
\[
\wedge^n \left( \bullet \ \omega_{ij} \right) = \bullet \ \omega_{i_1 i_2} \wedge \ldots \wedge \omega_{i_{2n-1} i_{2n}} =
= \bullet \ a_{i_1 i_2} \cdots a_{i_{2n-1} i_{2n}} e_{i_1} \wedge \ldots \wedge e_{i_{2n}} =
= \bullet \ (-1)^{\sigma} a_{i_1 i_2} \cdots a_{i_{2n-1} i_{2n}} e_1 \wedge \ldots \wedge e_{2n},
\]
причём слагаемых, соответствующих коэффициенту \( a_{i_1 i_2} \cdots a_{i_{2n-1} i_{2n}} \), ровно \( n! \); в самом деле, каждый из \( n \) элементов \( \omega_{i_1 i_2}, \ldots, \omega_{i_{2n-1} i_{2n}} \) можно выбрать в любом из \( n \) сомножителей \( \wedge^n(\bullet \ \omega_{ij}) \), причём в каждом сомножителе выбирается ровно один элемент. В частности, \( f(J) = n! \).

Многочлен \( \mathrm{Pf}(A) = f(A)/f(J) = \pm \sqrt{\det A} \), рассматриваемый как многочлен от переменных \( a_{ij} \), где \( i < j \), называют пфаффианом. Легко проверить, что для матриц порядка 2 и 4 соответственно пфаффиан равен \( a_{12} \) и \( a_{12}a_{34} - a_{13}a_{24} + a_{14}a_{23} \).

**31.2. Пфаффиан матриц специального вида**

Пусть \( 1 \leq \sigma_1 < \ldots < \sigma_{2k} \leq 2n \). Множество \( \{\sigma_1, \ldots, \sigma_{2k}\} \) можно дополнить до множества \( \{1, 2, \ldots, 2n\} \) множеством \( \{\bar{\sigma}_1, \ldots, \bar{\sigma}_{2(n-k)}\} \), где \( \bar{\sigma}_1 < \ldots < \bar{\sigma}_{2(n-k)} \). В результате множеству \( \{\sigma_1, \ldots, \sigma_{2k}\} \) сопоставим перестановку \( \sigma = (\sigma_1 \ldots \sigma_{2k} \bar{\sigma}_1 \ldots \bar{\sigma}_{2(n-k)}) \). Легко проверить, что \( (-1)^{\sigma} = (-1)^a \), где \( a = (\sigma_1 - 1) + (\sigma_2 - 2) + \ldots + (\sigma_{2k} - 2k) \).

Пфаффиан подматрицы кососимметрической матрицы \( M = \| m_{ij} \|_{1}^{2n} \), где \( m_{ij} = (-1)^{i+j+1} \) при \( i < j \), обладает следующим свойством.

**Теорема 31.2.1. Пусть**
\[
P_{\sigma_1 \ldots \sigma_{2k}} = \mathrm{Pf} \left( M \begin{pmatrix}
\sigma_1 & \ldots & \sigma_{2k} \\
\sigma_1 & \ldots & \sigma_{2k}
\end{pmatrix} \right).
\]
*Тогда* \( P_{\sigma_1 \ldots \sigma_{2k}} = (-1)^{\sigma} \).