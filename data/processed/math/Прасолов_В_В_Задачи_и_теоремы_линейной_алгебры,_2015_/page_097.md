---
source_image: page_097.png
page_number: 97
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.48
tokens: 6447
characters: 1947
timestamp: 2025-12-24T08:10:06.353859
finish_reason: stop
---

где \( A_{ij} \) — алгебраическое дополнение элемента \( a_{ij} \) в матрице \( \|a_{ij}\|_1^p \). В правой части стоит величина

\[
- \sum_{s,t=1}^n x_s x_t a_{st} \Delta,
\]

поэтому достаточно проверить, что

\[
\sum_{i,j=1}^p A_{ij} a_{is} a_{jt} = a_{st} \Delta.
\]

Так как \( \sum_{i=1}^p A_{ij} a_{is} = \delta_{js} \Delta \), то

\[
\sum_{j=1}^p a_{jt} \sum_{i=1}^p A_{ij} a_{is} = \sum_{j=1}^p a_{jt} \delta_{js} \Delta = a_{st} \Delta.
\]

2.4. Пусть \( B = A^T A \). Тогда

\[
B \begin{pmatrix} i_1 & \ldots & i_k \\ i_1 & \ldots & i_k \end{pmatrix} = \left| \begin{array}{ccc}
b_{i_1 i_1} & \cdots & b_{i_1 i_k} \\
\ldots & \ldots & \ldots \\
b_{i_k i_1} & \cdots & b_{i_k i_k}
\end{array} \right| =
\]
\[
= \det \left[ \begin{pmatrix} a_{1i_1} & \cdots & a_{ni_1} \\ \ldots & \ldots & \ldots \\ a_{1i_k} & \cdots & a_{ni_k} \end{pmatrix} \cdot \begin{pmatrix} a_{1i_1} & \cdots & a_{1i_k} \\ \ldots & \ldots & \ldots \\ a_{ni_1} & \cdots & a_{ni_k} \end{pmatrix} \right].
\]

Поэтому, воспользовавшись формулой Бине—Коши, получаем

\[
B \begin{pmatrix} i_1 & \ldots & i_k \\ i_1 & \ldots & i_k \end{pmatrix} = \sum_{1 \leq j_1 < \ldots < j_k \leq n} A^2 \begin{pmatrix} i_1 & \ldots & i_k \\ j_1 & \ldots & j_k \end{pmatrix}.
\]

2.5. Коэффициент при \( u_1 \) в сумме определителей, стоящих в левой части, равен \( a_{11} A_{11} + \ldots + a_{n1} A_{n1} = |A| \). Для \( u_2, \ldots, u_n \) доказательство аналогично.

2.6. Пусть точка \( A \) имеет координаты \( (a_1, a_2) \); для остальных точек обозначения аналогичны. Тогда, например,

\[
S_{ABC} = \frac{1}{2} \left| \begin{array}{ccc}
1 & 1 & 1 \\
a_1 & b_1 & c_1 \\
a_2 & b_2 & c_2
\end{array} \right|.
\]

Рассмотрим определитель матрицы

\[
\frac{1}{4} \begin{pmatrix}
1 & 1 & 1 & -1 & 0 & 0 \\
a_1 & b_1 & c_1 & -d_1 & 0 & 0 \\
a_2 & b_2 & c_2 & -d_2 & 0 & 0 \\
1 & 1 & 1 & 0 & 1 & 1 \\
a_1 & b_1 & c_1 & 0 & e_1 & f_1 \\
a_2 & b_2 & c_2 & 0 & e_2 & f_2
\end{pmatrix}.
\]