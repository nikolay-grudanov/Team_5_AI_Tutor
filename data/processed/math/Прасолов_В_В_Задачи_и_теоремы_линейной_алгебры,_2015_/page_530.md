---
source_image: page_530.png
page_number: 530
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.73
tokens: 6532
characters: 2630
timestamp: 2025-12-24T08:22:05.830205
finish_reason: stop
---

II. Если строка \( A_i \) заменяется на \( A_i + A_j \), то \( \lambda_j \) заменяется на \( \lambda_j - \lambda_i \), а все остальные элементы \( \lambda_k \) не изменяются, потому что

\[
\lambda_i (A_i + A_j) + (\lambda_j - \lambda_i) A_j = \lambda_i A_i + \lambda_j A_j.
\]

Если \( \lambda_k \neq 0 \) для некоторого \( k \), отличного от \( i \) и \( j \), то именно этот элемент \( \lambda_k \) мы применим для вычисления определителя. Ясно, что при этом \( \det C_k \) не изменяется, так как к одной строке прибавляется другая строка. Если \( \lambda_i \neq 0 \), то для вычисления определителя можно применить и этот элемент: ясно, что элемент \( \lambda_i \) и матрица \( C_i \) не изменяются. Осталось рассмотреть случай, когда \( \lambda_j \neq 0 \), а все стальные элементы \( \lambda_k \) равны нулю. В этом случае \( \lambda_j B_j = 0 \), а значит, \( B_j = 0 \). Строка \( B_i \) заменяется на \( B_i + B_j \), поэтому матрица \( C_j \) не изменяется. Элемент \( \lambda_j \) заменяется на \( \lambda_j - \lambda_i \); он тоже не изменяется.

III. Для единичной матрицы \( \lambda_1 = 1 \), а все остальные \( \lambda_k \) равны 0. Матрица \( C_1 \) единичная.

Вычислим для примера определитель Дьёдонне невырожденной матрицы \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \). Если \( a \neq 0 \), то

\[
\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ ca^{-1} & 1 \end{pmatrix} \begin{pmatrix} a & 0 \\ 0 & d-ca^{-1}b \end{pmatrix} \begin{pmatrix} 1 & a^{-1}b \\ 0 & 1 \end{pmatrix},
\]

поэтому \( \det \begin{pmatrix} a & b \\ c & d \end{pmatrix} = ad - aca^{-1}b \). А в случае, когда \( a = 0 \), мы получаем

\[
\begin{pmatrix} 0 & b \\ c & d \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ db^{-1} & 1 \end{pmatrix} \begin{pmatrix} b & 0 \\ 0 & c \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},
\]

поэтому \( \det \begin{pmatrix} 0 & b \\ c & d \end{pmatrix} = -bc \).

Теорема 58.1.1. При \( n \geq 2 \) определитель Дьёдонне матрицы \( A \in \mathrm{GL}(n, K) \) равен 1 тогда и только тогда, когда \( A \in \mathrm{SL}(n, K) \).

Доказательство. Представим матрицу \( A \) в виде \( A = BD(\mu) \), где \( B \in \mathrm{SL}(n, K) \). Тогда \( \det A = \overline{\mu} \), поэтому \( \det A = 1 \) тогда и только тогда, когда элемент \( \mu \) принадлежит коммутанту группы \( K^\times \), т. е. он равен произведению коммутаторов. Но в таком случае \( D(\mu) \in \mathrm{SL}(n, K) \) согласно теореме 57.4.1.

Теорема 58.1.2. Пусть \( A = \begin{pmatrix} B & 0 \\ C & D \end{pmatrix} \), где \( B \) и \( D \) — квадратные матрицы. Тогда \( \det A = \det B \cdot \det D \).