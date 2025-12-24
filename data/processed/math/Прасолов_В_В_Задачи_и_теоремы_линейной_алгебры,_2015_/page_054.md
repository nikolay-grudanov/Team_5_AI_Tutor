---
source_image: page_054.png
page_number: 54
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.54
tokens: 6786
characters: 2736
timestamp: 2025-12-24T08:09:11.022247
finish_reason: stop
---

2.10. Миноры матрицы Якоби

Любой минор матрицы Якоби \( J \) равен некоторому произведению её главных миноров и элементов \( b_i, c_i \). А именно, справедливо следующее утверждение.

Теорема 2.10.1. Пусть \( 1 \leq i_1 < i_2 < \ldots < i_m \leq n, 1 \leq j_1 < j_2 < \ldots < j_m \leq n \) и \( i_1 = j_1, \ldots, i_{p_1} = j_{p_1}, i_{p_1+1} \neq j_{p_1+1}, i_{p_2} \neq j_{p_2}, i_{p_2+1} = j_{p_2+1}, \ldots, i_{p_3} = j_{p_3}, \ldots \). Тогда

\[
J\left( \begin{array}{c} i_1 \ldots i_m \\ j_1 \ldots j_m \end{array} \right) = J\left( \begin{array}{c} i_1 \ldots i_{p_1} \\ j_1 \ldots j_{p_1} \end{array} \right) J\left( \begin{array}{c} i_{p_1+1} \\ j_{p_1+1} \end{array} \right) \ldots J\left( \begin{array}{c} i_{p_2} \\ j_{p_2} \end{array} \right) J\left( \begin{array}{c} i_{p_2+1} \ldots i_{p_3} \\ j_{p_2+1} \ldots j_{p_3} \end{array} \right) \ldots
\]

Доказательство. Достаточно проверить, что если \( i_p \neq j_p \), то

\[
J\left( \begin{array}{c} i_1 \ldots i_m \\ j_1 \ldots j_m \end{array} \right) = J\left( \begin{array}{c} i_1 \ldots i_{p-1} \\ j_1 \ldots j_{p-1} \end{array} \right) J\left( \begin{array}{c} i_p \\ j_p \end{array} \right) J\left( \begin{array}{c} i_{p+1} \ldots i_m \\ j_{p+1} \ldots j_m \end{array} \right).
\]

Это равенство следует из того, что матрица, соответствующая рассматриваемому минору, имеет блочно-треугольный вид.

2.11. Миноры матрицы Грина

Пусть \( a_1, \ldots, a_n \) и \( b_1, \ldots, b_n \) — некоторые ненулевые числа. Матрицей Грина называют матрицу \( G = \| g_{ij} \|_1^n \), где

\[
g_{ij} = \begin{cases}
a_i b_j & \text{при } i \leq j; \\
a_j b_i & \text{при } i \geq j.
\end{cases}
\]

Теорема 2.11.1. Пусть \( 1 \leq i_1 < i_2 < \ldots < i_m \leq n \) и \( 1 \leq j_1 < j_2 < \ldots < j_m \leq n \). Тогда если \( i_1, j_1 < i_2, j_2 < \ldots < i_m, j_m \), то

\[
G\left( \begin{array}{c} i_1 \ldots i_m \\ j_1 \ldots j_m \end{array} \right) = a_{k_1} \left| \begin{array}{cc} a_{k_2} & a_{l_1} \\ b_{k_2} & b_{l_1} \end{array} \right| \ldots \left| \begin{array}{cc} a_{k_m} & a_{l_{m-1}} \\ b_{k_m} & b_{l_{m-1}} \end{array} \right| b_{l_m},
\]

где \( k_p = \min(i_p, j_p) \) и \( l_p = \max(i_p, j_p) \). Если же условие \( i_1, j_1 < i_2, j_2 < \ldots < i_m, j_m \) не выполняется, то указанный минор равен 0.

Доказательство. Если \( i_1 < i_2 \leq j_1 \), то рассматриваемый минор является определителем матрицы, у которой первые две строки пропорциональны. Если же \( j_1 < j_2 \leq i_1 \), то пропорциональны первые два столбца. Поэтому можно считать, что \( \max(i_1, j_1) < \min(i_2, j_2) \). Пусть для определённости \( i_2 \leq j_2 \) (если \( i_2 \geq j_2 \), то вместо операций с первыми двумя строками нужно проделать аналогичные операции с первыми