---
source_image: page_348.png
page_number: 348
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.65
tokens: 6989
characters: 3152
timestamp: 2025-12-24T08:17:16.640689
finish_reason: stop
---

30.7. Легко проверить, что \( \sigma_k = \operatorname{tr}(\wedge^k A) \). Если в жордановом базисе диагональ матрицы \( A \) имеет вид \( (\lambda_1, \ldots, \lambda_n) \), то \( s_k = \lambda_1^k + \ldots + \lambda_n^k \) и \( \sigma_k = \cdot \lambda_{i_1} \ldots \lambda_{i_k} \). Требуемое тождество для функций \( s_k \) и \( \sigma_k \) доказано в п. 4.1.

30.8. Пусть \( e_j \) и \( \varepsilon_j \), где \( 1 \leq j \leq m \), — двойственные базисы. Величину
\[
n! \langle v_1 \wedge \ldots \wedge v_n, f_1 \wedge \ldots \wedge f_n \rangle,
\]
где \( v_i = \cdot a_{ij} e_j \) и \( f_i = \cdot b_{ji} \varepsilon_j \), можно вычислить двумя способами. С одной стороны, она равна
\[
\begin{vmatrix}
f_1(v_1) & \ldots & f_n(v_1) \\
\cdots & \cdots & \cdots \\
f_1(v_n) & \ldots & f_n(v_n)
\end{vmatrix}
= \begin{vmatrix}
\cdot a_{1j} b_{j1} & \ldots & \cdot a_{1j} b_{jn} \\
\cdots & \cdots & \cdots \\
\cdot a_{nj} b_{j1} & \ldots & \cdot a_{nj} b_{jn}
\end{vmatrix} = \det AB.
\]
С другой стороны, она равна
\[
n! \left\langle \cdot \prod_{k_1 \ldots k_n} a_{1k_1} \ldots a_{nk_n} e_{k_1} \wedge \ldots \wedge e_{k_n}, \cdot \prod_{l_1 \ldots l_n} b_{l_1 1} \ldots b_{l_n n} \varepsilon_{l_1} \wedge \ldots \wedge \varepsilon_{l_n} \right\rangle =
\]
\[
= \cdot \sum_{k_1 \leq \ldots \leq k_n} A_{k_1 \ldots k_n} B^{l_1 \ldots l_n} n! \langle e_{k_1} \wedge \ldots \wedge e_{k_n}, \varepsilon_{l_1} \wedge \ldots \wedge \varepsilon_{l_n} \rangle =
\]
\[
= \cdot \sum_{k_1 < \ldots < k_n} A_{k_1 \ldots k_n} B^{l_1 \ldots l_n}.
\]

30.9. Легко проверить, что следующие формы образуют ортогональный базис для \( Q \):
\[
\omega_1 = \frac{e_1 \wedge e_2 + e_3 \wedge e_4}{\sqrt{2}}, \quad \omega_4 = \frac{e_1 \wedge e_2 - e_3 \wedge e_4}{\sqrt{2}},
\]
\[
\omega_2 = \frac{e_1 \wedge e_3 - e_2 \wedge e_4}{\sqrt{2}}, \quad \omega_5 = \frac{e_1 \wedge e_3 + e_2 \wedge e_4}{\sqrt{2}},
\]
\[
\omega_3 = \frac{e_1 \wedge e_4 + e_2 \wedge e_3}{\sqrt{2}}, \quad \omega_6 = \frac{e_1 \wedge e_4 - e_2 \wedge e_3}{\sqrt{2}}.
\]
При этом \( Q(\omega_i, \omega_i) = 1 \) при \( i \leq 3 \) и \( Q(\omega_i, \omega_i) = -1 \) при \( i \geq 4 \). Таким образом, сигнатура формы \( Q \) равна \( (3, 3) \).

§ 31. Пфаффиан

31.1. Так как \( \operatorname{Pf}(A) = \cdot (-1)^{\sigma} a_{i_1 i_2} \ldots a_{i_{2n-1} i_{2n}} \), причём суммирование ведётся по всем разбиениям множества \( \{1, \ldots, 2n\} \) на пары \( \{i_{2k-1}, i_{2k}\} \), где \( i_{2k-1} < i_{2k} \), то \( a_{i_1 i_2} C_{i_1 i_2} = a_{i_1 i_2} \cdot (-1)^{\sigma} a_{i_3 i_4} \ldots a_{i_{2n-1} i_{2n}} \). Остаётся заметить, что знаки перестановок
\[
\sigma = \begin{pmatrix} 1 & 2 & \ldots & 2n \\ i_1 & i_2 & \ldots & i_{2n} \end{pmatrix} \quad \text{и} \quad \tau = \begin{pmatrix} i_1 & i_2 & 1 & 2 & \ldots & \hat{i}_1 & \hat{i}_2 & \ldots & 2n \\ i_1 & i_2 & i_3 & i_4 & \ldots & \ldots & \ldots & i_{2n} \end{pmatrix}
\]
отличаются на \( (-1)^{i_1 + i_2 + 1} \). В самом деле, для перемещения элемента \( i_1 \) в верхней строке \( \sigma \) на первое место требуется \( i_1 - 1 \) транспозиций, а для перемещения \( i_2 \) на второе место требуется \( i_2 - 2 \) транспозиций.