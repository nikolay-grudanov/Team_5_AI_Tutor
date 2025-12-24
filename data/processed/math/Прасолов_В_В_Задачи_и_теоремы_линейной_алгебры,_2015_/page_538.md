---
source_image: page_538.png
page_number: 538
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.09
tokens: 6537
characters: 2462
timestamp: 2025-12-24T08:22:12.049556
finish_reason: stop
---

Выберем в \( \mathbb{C}^{2n} \) базис \( e_1, \ldots, e_n, e_1j, \ldots, e_nj \). При естественном отождествлении пространства \( \mathbb{C}^{2n} \) с кватернионным пространством \( \mathbb{H}^n \) с базисом \( e_1, \ldots, e_n \) кватернионная структура — это отображение

\[
R_j(z_1, \ldots, z_n, w_1, \ldots, w_n) = (-\overline{w}_1, \ldots, -\overline{w}_n, \overline{z}_1, \ldots, \overline{z}_n).
\]

Отметим ещё раз, что это отображение не является линейным над \( \mathbb{C} \). Но линейное над \( \mathbb{C} \) отображение \( A : \mathbb{C}^{2n} \to \mathbb{C}^{2n} \) является линейным над \( \mathbb{H} \) отображением пространства \( \mathbb{H}^n \) тогда и только тогда, когда оно коммутирует с кватернионной структурой, т. е. \( AR_j = R_jA \).

Если мы запишем матрицу линейного над \( \mathbb{H} \) отображения пространства \( \mathbb{H}^n \) в виде \( A + jB \), где \( A \) и \( B \) — комплексные матрицы, то матрица того же самого отображения, рассматриваемого как отображение пространства \( \mathbb{C}^{2n} \), имеет вид \( \begin{pmatrix} A & -\overline{B} \\ B & \overline{A} \end{pmatrix} \). Действительно,

\[
(A + jB)e_p = \bullet\ e_qa_{qp} + \bullet\ e_qjb_{qp},
\]
\[
(A + jB)e_pj = \bullet\ e_qa_{qp}j + \bullet\ e_qjb_{qp}j = \bullet\ e_qj\overline{a}_{qp} - \bullet\ e_q\overline{b}_{qp}.
\]

Это выражение можно получить и по-другому. В пространстве \( \mathbb{C}^{2n} \) отображение \( R_j \) можно записать в виде \( R_j(v) = \overline{Jv} \), где \( J = \begin{pmatrix} 0 & -I_n \\ I_n & 0 \end{pmatrix} \). Поэтому если мы запишем соотношение \( R_jX = XR_j \) для комплексной матрицы \( X = \begin{pmatrix} A & C \\ B & D \end{pmatrix} \), то получим, что \( \overline{JXv} = X\overline{Jv} \) для любого \( v \in \mathbb{C}^{2n} \). Учитывая, что \( X\overline{Jv} = \overline{XJv} \), получаем, что комплексная матрица \( X \) порядка \( 2n \) соответствует кватернионно линейному отображению тогда и только тогда, когда \( JX = \overline{XJ} \). Это соотношение показывает, что \( C = -\overline{B} \) и \( D = \overline{A} \).

59.2. Гиперэрмитовы матрицы

Квадратную кватернионную матрицу \( A = \| a_{ij} \|_1^n \) называют гиперэрмитовой, если \( a_{ij} = \overline{a}_{ji} \), т. е. \( A = A^* \), где \( A^* \) — кватернионно сопряжённая матрица.

Каждой гиперэрмитовой матрице \( A = \| a_{ij} \|_1^n \) можно сопоставить гиперэрмитову полулинейную форму

\[
A(x, y) = \sum_{i,j=1}^n \overline{x}_i a_{ij} y_j
\]