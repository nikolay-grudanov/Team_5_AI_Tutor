---
source_image: page_064.png
page_number: 64
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.83
tokens: 6738
characters: 2423
timestamp: 2025-12-24T08:09:28.434361
finish_reason: stop
---

Доказательство.

\[
\begin{pmatrix} A & B \\ C & D \end{pmatrix}
\begin{pmatrix} A_1 & B_1 \\ C_1 & D_1 \end{pmatrix}
=
\begin{pmatrix} AA_1 + BC_1 & AB_1 + BD_1 \\ CA_1 + DC_1 & CB_1 + DD_1 \end{pmatrix}
=
\begin{pmatrix} I & 0 \\ 0 & I \end{pmatrix},
\]

поэтому \( AB_1 + BD_1 = 0 \) и \( CA_1 + DC_1 = 0 \), а значит, \( B_1 = -A^{-1}BD_1 \) и \( C_1 = -D^{-1}CA_1 \). Далее, \( AA_1 + BC_1 = I \) и \( CB_1 + DD_1 = I \). Следовательно, \( AA_1 - BD^{-1}CA_1 = I \) и \( -CA^{-1}BD_1 + DD_1 = I \), т. е. \( A_1 = (A - BD^{-1}C)^{-1} \) и \( D_1 = (D - CA^{-1}B)^{-1} \).

Замечание. Если \( B \) и \( C \) — невырожденные матрицы, то аналогично получаем \( D_1 = -B^{-1}AB_1 \) и \( A_1 = -C^{-1}DC_1 \). Далее, \( -AC^{-1}DC_1 + BC_1 = I \) и \( CB_1 - DB^{-1}AB_1 = I \), т. е. \( C_1 = (B - AC^{-1}D)^{-1} \) и \( B_1 = (C - DB^{-1}A)^{-1} \).

3.3. Теорема Хейнсворта

Пусть

\[
A = \begin{pmatrix} A_{11} & A_{12} & A_{13} \\ A_{21} & A_{22} & A_{23} \\ A_{31} & A_{32} & A_{33} \end{pmatrix}, \quad B = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix} \quad \text{и} \quad C = A_{11}
\]

— квадратные матрицы, причём матрицы \( B \) и \( C \) невырождены. Матрицу \( (B | C) = A_{22} - A_{21}A_{11}^{-1}A_{12} \) можно рассматривать как подматрицу матрицы \( (A | C) = \begin{pmatrix} A_{22} & A_{23} \\ A_{32} & A_{33} \end{pmatrix} - \begin{pmatrix} A_{21} \\ A_{31} \end{pmatrix}A_{11}^{-1}(A_{12} \quad A_{13}) \).

Теорема 3.3.1 (Хейнсворт). \( (A | B) = ((A | C) | (B | C)) \).

Доказательство [Os]. Для матрицы \( A \) можно записать следующие разложения:

\[
A = \begin{pmatrix} A_{11} & 0 & 0 \\ A_{21} & I & 0 \\ A_{31} & 0 & I \end{pmatrix}
\begin{pmatrix} I & * & * \\ 0 & (A | C) \\ 0 & 0 & (A | B) \end{pmatrix},
\]
(1)

\[
A = \begin{pmatrix} A_{11} & A_{12} & 0 \\ A_{21} & A_{22} & 0 \\ A_{31} & A_{32} & I \end{pmatrix}
\begin{pmatrix} I & 0 & * \\ 0 & I & * \\ 0 & 0 & (A | B) \end{pmatrix}.
\]
(2)

Рассматривая дополнение по Шуру матрицы \( A_{11} \) в левом сомножителе разложения (2), можно записать

\[
\begin{pmatrix} A_{11} & A_{12} & 0 \\ A_{21} & A_{22} & 0 \\ A_{31} & A_{32} & I \end{pmatrix}
= \begin{pmatrix} A_{11} & 0 & 0 \\ A_{21} & I & 0 \\ A_{31} & 0 & I \end{pmatrix}
\begin{pmatrix} I & X_1 & X_2 \\ 0 & X_3 & X_4 \\ 0 & X_5 & X_6 \end{pmatrix}
= \begin{pmatrix} * & * & A_{11}X_2 \\ * & * & A_{21}X_2 + X_4 \\ * & * & A_{31}X_2 + X_6 \end{pmatrix}.
\]
(3)