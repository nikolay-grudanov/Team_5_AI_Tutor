---
source_image: page_062.png
page_number: 62
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.42
tokens: 6344
characters: 2064
timestamp: 2025-12-24T08:09:09.235434
finish_reason: stop
---

Первое доказательство. Достаточно заметить, что

\[
\begin{pmatrix} A & B \\ C & D \end{pmatrix}
\begin{pmatrix} I & -A^{-1}B \\ 0 & I \end{pmatrix}
=
\begin{pmatrix} A & 0 \\ C & D - CA^{-1}B \end{pmatrix}.
\]

Второе доказательство. Матрицу \( X \) можно записать в виде

\[
X = \begin{pmatrix} I & 0 \\ U & I \end{pmatrix}
\begin{pmatrix} A & 0 \\ 0 & W \end{pmatrix}
\begin{pmatrix} I & V \\ 0 & I \end{pmatrix}
= \begin{pmatrix} A & AV \\ UA & UAV + W \end{pmatrix}.
\]

Для этого нужно положить \( U = CA^{-1} \), \( V = A^{-1}B \) и \( W = D - CA^{-1}B \).

Аналогично доказывается следующее утверждение.

Теорема 3.1.2. Если \( |D| \neq 0 \), то

\[
|X| = |D| \cdot |A - BD^{-1}C|.
\]

Матрицы \( (X|A) = D - CA^{-1}B \) и \( (X|D) = A - BD^{-1}C \) называют дополнениями по Шуру матриц \( A \) и \( D \) в матрице \( X \).

Теорема 3.1.3. Если \( A \) и \( D \) — матрицы одного порядка и \( AC = CA \), то

\[
|X| = |AD - CB|.
\]

Доказательство. Рассмотрим сначала случай, когда \( |A| \neq 0 \). Согласно теореме 3.1.1

\[
|X| = |AD - ACA^{-1}B| = |AD - CB|.
\]

Теперь рассмотрим случай, когда \( |A| = 0 \). Равенство \( |X| = |AD - CB| \) представляет собой полиномиальное тождество для элементов матрицы \( X \). Поэтому если существуют невырожденные матрицы \( A_\varepsilon \), для которых \( A_\varepsilon C = CA_\varepsilon \) и \( \lim_{\varepsilon \to 0} A_\varepsilon = A \), то требуемое равенство верно и для матрицы \( A \). Положим \( A_\varepsilon = A + \varepsilon I \). Ясно, что \( |A + \varepsilon I_n| = \varepsilon^n + \ldots \) — многочлен степени \( n \) от \( \varepsilon \). Этот многочлен имеет конечное число корней, поэтому для почти всех \( \varepsilon \) матрица \( A + \varepsilon I_n \) невырожденная. В частности, эта матрица невырожденная для достаточно малых ненулевых \( \varepsilon \).

Замечание. По поводу обобщения теоремы 3.1.3 см. задачу 42.11.

Теорема 3.1.4. Если \( a \) — число, \( u \) — строка, \( v \) — столбец, то

\[
\begin{vmatrix} A & v \\ u & a \end{vmatrix} = a|A| - u(\operatorname{adj} A)v.
\]