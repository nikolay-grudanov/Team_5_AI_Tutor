---
source_image: page_297.png
page_number: 297
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.70
tokens: 6773
characters: 2849
timestamp: 2025-12-24T08:15:40.638483
finish_reason: stop
---

1) Предположим сначала, что

\[
A = \begin{pmatrix} A_1 & A_2 \\ -A_2^T & A_3 \end{pmatrix},
\]

где \( A_1 = \begin{pmatrix} 0 & x \\ -x & 0 \end{pmatrix} \) и \( x \neq 0 \). Пусть \( F = \begin{pmatrix} F_1 & 0 \\ X & F_2 \end{pmatrix} \) и \( G = \begin{pmatrix} G_1 & Y \\ 0 & G_2 \end{pmatrix} \). Тогда

\[
FG = \begin{pmatrix} F_1 G_1 & F_1 Y \\ XG_1 & XY + F_2 G_2 \end{pmatrix}.
\]

Матрицы \( F_1 \) и \( G_1 \) можно выбрать так, что \( F_1 G_1 = A_1 \). Возьмём, далее, \( Y = F_1^{-1} A_2 \) и \( X = -A_2^T G_1^{-1} \). Тогда

\[
XY + F_2 G_2 = -A_2^T G_1^{-1} F_1^{-1} A_2 + F_2 G_2 = -A_2^T A_1^{-1} A_2 + F_2 G_2.
\]

Матрица \( A_3 + A_2^T A_1^{-1} A_2 \) кососимметрична, поэтому по предположению индукции матрицы \( F_2 \) и \( G_2 \) можно подобрать так, что \( F_2 G_2 = A_3 + A_2^T A_1^{-1} A_2 \) и \( \det F = \det G \).

2) Рассмотрим теперь случай, когда \( a_{12} = 0 \), но \( a_{ij} \neq 0 \) для некоторых \( i \) и \( j \). Пусть \( P \) — ортогональная матрица, соответствующая перестановке

\[
\begin{pmatrix} 1 & 2 & \ldots \\ i & j & \ldots \end{pmatrix}
\]

(см. задачу 14.3). Матрица \( PAP^T \) относится к первому случаю, поэтому существуют такие матрицы \( F_1 \) и \( G_1 \), что \( PAP^T = F_1 G_1 \). Тогда \( A = (P^{-1} F_1)(G_1 P) = FG \), где \( F = P^{-1} F_1 \) и \( G = G_1 P \).

23.6. Нам неоднократно придётся пользоваться тем, что для кососимметрической матрицы \( A \) чётного порядка число \( \dim \ker A \) чётное, так как ранг кососимметрической матрицы чётен (см. п. 23.2).

Рассмотрим сначала случай нулевого собственного значения, т. е. докажем, что если \( \dim \ker AB \geq 1 \), то \( \dim \ker AB \geq 2 \). Если \( |B| = 0 \), то

\[
\dim \ker AB \geq \dim \ker B \geq 2.
\]

Если же \( |B| \neq 0 \), то \( \ker AB = B^{-1} \ker A \), а значит, \( \dim \ker AB \geq 2 \).

Предположим теперь, что \( \dim \ker (AB - \lambda I) \geq 1 \) при \( \lambda \neq 1 \), и докажем, что \( \dim \ker (AB - \lambda I) \geq 2 \). Если \( (ABA - \lambda A)u = 0 \), то \( (AB - \lambda I)Au = 0 \), т. е. \( AU \subset \subset \ker (AB - \lambda I) \), где \( U = \ker (ABA - \lambda A) \). Поэтому достаточно доказать, что \( \dim AU \geq 2 \). Так как \( \ker A \subset U \), то \( \dim AU = \dim U - \dim \ker A \). Матрица \( ABA \) кососимметричная, поэтому числа \( \dim U \) и \( \dim \ker A \) чётные, а значит, число \( \dim AU \) тоже чётное. Остаётся проверить, что \( \ker A \neq U \). Предположим, что из равенства \( (AB - \lambda I)Ax = 0 \) следует, что \( Ax = 0 \). Тогда \( \operatorname{Im} A \cap \ker (AB - \lambda I) = 0 \). С другой стороны, если \( (AB - \lambda I)x = 0 \), то \( x = A(\lambda^{-1} Bx) \in \operatorname{Im} A \), т. е. \( \ker (AB - \lambda I) \subset \operatorname{Im} A \), причём \( \dim \ker (AB - \lambda I) \geq 1 \). Приходим к противоречию.