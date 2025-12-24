---
source_image: page_470.png
page_number: 470
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.06
tokens: 6496
characters: 2336
timestamp: 2025-12-24T08:20:23.185177
finish_reason: stop
---

Теорема 51.2.2. Матричное уравнение \( AXB = C \) имеет решение тогда и только тогда, когда \( AA^+CB^+B = C \). Решения этого уравнения имеют вид \( X = A^+CB^+ + Y - A^+AYBB^+ \), где \( Y \) — произвольная матрица.

Доказательство. Если \( AXB = C \), то
\[
C = AXB = AA^+(AXB)B^+B = AA^+CB^+B.
\]
Наоборот, если \( C = AA^+CB^+B \), то \( X_0 = A^+CB^+ \) — частное решение уравнения \( AXB = C \). Остаётся доказать, что общее решение уравнения \( AXB = 0 \) имеет вид \( X = Y - A^+AYBB^+ \). Ясно, что
\[
A(Y - A^+AYBB^+)B = 0.
\]
С другой стороны, если \( AXB = 0 \), то \( X = Y - A^+AYBB^+ \), где \( Y = X \).

Следствие. а) Матричное уравнение \( AX = C \) разрешимо тогда и только тогда, когда \( AA^+C = C \); решения этого уравнения имеют вид \( X = A^+C + Y - A^+AY \), где \( Y \) — произвольная матрица.
б) Матричное уравнение \( XA = C \) разрешимо тогда и только тогда, когда \( CA^+A = C \); решения этого уравнения имеют вид \( X = CA^+ + Y - YA^+A \), где \( Y \) — произвольная матрица.

51.3. Матричные уравнения

Теорема 51.3.1 [Ro2]. Пусть \( A \in M_{m,m} \), \( B \in M_{n,n} \) и \( C \in M_{m,n} \).
а) Уравнение \( AX - XB = C \) имеет решение \( X \in M_{m,n} \) тогда и только тогда, когда матрицы \( \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \) и \( \begin{pmatrix} A & C \\ 0 & B \end{pmatrix} \) подобны.
б) Уравнение \( AX - YB = C \) имеет решение \( X, Y \in M_{m,n} \) тогда и только тогда, когда матрицы \( \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} \) и \( \begin{pmatrix} A & C \\ 0 & B \end{pmatrix} \) одного ранга.

Доказательство [Fl2]. а) Пусть \( U = \begin{pmatrix} P & Q \\ R & S \end{pmatrix} \). Предположим сначала, что указанные матрицы подобны. Рассмотрим для \( i = 0, 1 \) отображения \( \varphi_i : M_{m,n} \to M_{m,n} \), заданные формулами
\[
\varphi_0(U) = \begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix}U - U\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} = \begin{pmatrix} AP - PA & AQ - QB \\ BR - RA & BS - SB \end{pmatrix},
\]
\[
\varphi_1(U) = \begin{pmatrix} A & C \\ 0 & B \end{pmatrix}U - U\begin{pmatrix} A & 0 \\ 0 & B \end{pmatrix} = \begin{pmatrix} AP + CR - PA & AQ + CS - QB \\ BR - RA & BS - SB \end{pmatrix}.
\]
Уравнения \( FU = UF \) и \( GFG^{-1}U' = U'F \) имеют изоморфные пространства решений; этот изоморфизм задаётся формулой \( U = G^{-1}U' \). По-