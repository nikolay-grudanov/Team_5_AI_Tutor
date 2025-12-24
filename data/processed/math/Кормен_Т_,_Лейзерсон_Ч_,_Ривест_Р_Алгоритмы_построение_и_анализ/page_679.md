---
source_image: page_679.png
page_number: 679
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.66
tokens: 11331
characters: 1169
timestamp: 2025-12-24T06:52:21.414463
finish_reason: stop
---

два других:

\[
P_5 + P_4 - P_2 = ae + dh + df - bh
\]
\[
= \begin{pmatrix}
+ & . & . & . \\
. & . & . & - \\
. & . & . & . \\
. & + & . & +
\end{pmatrix}.
\]

Использовав ещё одно произведение

\[
P_6 = A_6 B_6
\]
\[
= (b - d) \cdot (f + h)
\]
\[
= bf + bh - df - dh
\]
\[
= \begin{pmatrix}
. & . & . & . \\
. & + & . & + \\
. & . & . & . \\
. & - & . & -
\end{pmatrix},
\]

получим

\[
r = P_5 + P_4 - P_2 + P_6
\]
\[
= ae + bf
\]
\[
= \begin{pmatrix}
+ & . & . & . \\
. & + & . & . \\
. & . & . & . \\
. & . & . & .
\end{pmatrix}.
\]

Итак, на три матрицы ушло 6 умножений — что же в этом хорошего? А вто что: при симметричном вычислении и мы снова используем \( P_5 \) и одно умножение сэкономим. Для сначала сместим лишние слагаемые в \( P_5 \) в другом направлении при помощи \( P_1 \) и \( P_3 \):

\[
P_5 + P_1 - P_3 = ae + ag - ce + dh
\]
\[
= \begin{pmatrix}
+ & . & + & . \\
. & . & . & . \\
- & . & . & . \\
. & . & . & +
\end{pmatrix}.
\]

Вычитая дополнительное произведение

\[
P_7 = A_7 B_7
\]
\[
= (a - c) \cdot (e + g)
\]
\[
= ae + ag - ce - cg
\]
\[
= \begin{pmatrix}
+ & . & + & . \\
. & . & . & . \\
- & . & - & . \\
. & . & . & .
\end{pmatrix},
\]