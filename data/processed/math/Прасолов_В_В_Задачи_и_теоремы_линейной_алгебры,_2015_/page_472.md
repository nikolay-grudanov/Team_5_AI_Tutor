---
source_image: page_472.png
page_number: 472
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.59
tokens: 6389
characters: 2114
timestamp: 2025-12-24T08:20:20.840944
finish_reason: stop
---

Рассмотрим пространство

\[
Z = \{ (U_{21}, U_{22}, W_{21}, W_{22}) \mid BU_{21} = W_{21}A, \ BU_{22} = W_{22}B \}
\]

и определим отображения \( \nu_i : \operatorname{Ker} \varphi_i \to Z \), где

\[
\nu_i(U, W) = (U_{21}, U_{22}, W_{21}, W_{22}).
\]

Тогда \( \operatorname{Im} \nu_1 \subset \operatorname{Im} \nu_0 = Z \) и \( \operatorname{Ker} \nu_1 = \operatorname{Ker} \nu_0 \). Поэтому \( \operatorname{Im} \nu_1 = \operatorname{Im} \nu_0 \).

Матрица \( (U, W) \), где \( U = W = \begin{pmatrix} I & 0 \\ 0 & -I \end{pmatrix} \), лежит в \( \operatorname{Ker} \psi_0 \). Поэтому в \( \operatorname{Ker} \psi_1 \) тоже существует элемент, для которого \( U_{22} = -I \). Для этого элемента равенство \( AU_{12} + CU_{22} = W_{12}B \) эквивалентно равенству \( AU_{21} - W_{12}B = C \).

Обратно, если решение \( X, Y \) данного уравнения существует, то

\[
\begin{pmatrix} I & -Y \\ 0 & I \end{pmatrix} \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \begin{pmatrix} I & X \\ 0 & I \end{pmatrix} = \begin{pmatrix} A & AX - YB \\ 0 & B \end{pmatrix} = \begin{pmatrix} A & C \\ 0 & B \end{pmatrix}.
\]

Задачи

51.1. Докажите, что если \( C = AX = YB \), то существует такая матрица \( Z \), что \( C = AZB \).

51.2. Докажите, что любое решение системы матричных уравнений \( AX = 0, \ XB = 0 \) имеет вид \( X = (I - A^+A)Y(I - BB^+) \), где \( Y \) — произвольная матрица.

51.3. Докажите, что система уравнений \( AX = C, \ XB = D \) имеет решение тогда и только тогда, когда каждое из уравнений \( AX = C \) и \( XB = D \) имеет решение и \( AD = CB \).

51.4. Операторы \( A \) и \( B \) аннулируют пространство \( V^\perp \), а их ограничения на пространство \( V \) являются взаимно обратными операторами. Докажите, что \( A^+ = B \) и \( B^+ = A \).

51.5. Докажите, что если \( A \) — ненулевая нильпотентная матрица, то матрицы \( A \) и \( A^+ \) не коммутируют.

51.6 [Wi2]. Пусть \( A \in M_{m,m}, \ B \in M_{n,n} \) и \( C \in M_{m,n} \). Докажите, что уравнение \( X - AXB = C \) имеет решение \( X \in M_{m,n} \) тогда и только тогда, когда матрицы \( A + xI_m \) и \( I_n + xB \) одного ранга.