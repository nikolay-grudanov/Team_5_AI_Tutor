---
source_image: page_049.png
page_number: 49
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.11
tokens: 6537
characters: 2442
timestamp: 2025-12-24T08:08:52.589225
finish_reason: stop
---

§ 2. Миноры и алгебраические дополнения

многочлен от \( \lambda \) со старшим коэффициентом 1; этот многочлен имеет конечное число корней. Если матрица \( A + \lambda I \) невырождена, то выполняется равенство \( X(\lambda) = Y(\lambda) \). Элементы матриц \( X(\lambda) \) и \( Y(\lambda) \) являются многочленами от \( \lambda \), поэтому \( X(\lambda) = Y(\lambda) \) для всех \( \lambda \). В частности, \( X(0) = Y(0) \), т. е. \( (\operatorname{adj} A)B = B(\operatorname{adj} A) \).

\subsection*{2.6. Миноры присоединённой матрицы. Тождество Якоби}

Миноры матрицы \( A \) и дополнительные к ним миноры матрицы \( (\operatorname{adj} A)^T \) связаны весьма простыми соотношениями. Мы сначала рассмотрим угловые миноры, а уже затем произвольные.

**Теорема 2.6.1.** *Пусть \( A = \|a_{ij}\|_1^n \), \( (\operatorname{adj} A)^T = \|A_{ij}\|_1^n \) и \( p \) — натуральное число, причём \( 1 \leq p < n \). Тогда*

\[
\begin{vmatrix}
A_{11} & \ldots & A_{1p} \\
\cdots & \cdots & \cdots \\
A_{p1} & \ldots & A_{pp}
\end{vmatrix}
= |A|^{p-1}
\begin{vmatrix}
a_{p+1, p+1} & \cdots & a_{p+1, n} \\
\cdots & \cdots & \cdots \\
a_{n, p+1} & \cdots & a_{nn}
\end{vmatrix}.
\]

**Доказательство.** При \( p = 1 \) утверждение совпадает с определением алгебраического дополнения \( A_{11} \). Пусть теперь \( p > 1 \). Легко проверить, что

\[
\begin{pmatrix}
A_{11} & \ldots & A_{1p} & A_{1, p+1} & \ldots & A_{1n} \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
A_{p1} & \ldots & A_{pp} & A_{p, p+1} & \ldots & A_{pn} \\
\ldots & 0 & \ldots & I
\end{pmatrix}
A =
\begin{pmatrix}
|A| & 0 & \cdots & 0 \\
\vdots & \ddots & & \vdots \\
0 & |A| & & 0 \\
a_{1, p+1} & \cdots & a_{n, p+1} & \\
\cdots & \cdots & \cdots & \cdots \\
a_{1n} & \cdots & a_{nn}
\end{pmatrix}.
\]

Следовательно,

\[
\begin{vmatrix}
A_{11} & \ldots & A_{1p} \\
\cdots & \cdots & \cdots \\
A_{p1} & \ldots & A_{pp}
\end{vmatrix}
\cdot |A| = |A|^p
\begin{vmatrix}
a_{p+1, p+1} & \cdots & a_{p+1, n} \\
\cdots & \cdots & \cdots \\
a_{n, p+1} & \cdots & a_{nn}
\end{vmatrix}.
\]

Если \( |A| \neq 0 \), то мы можем сократить на \( |A| \). В результате получим требуемое. В случае, когда \( |A| = 0 \), можно воспользоваться тем, что обе части требуемого равенства непрерывно зависят от \( a_{ij} \), а любая вырожденная матрица является пределом невырожденных матриц.

Выясним теперь, как преобразуется присоединённая матрица при перестановке двух строк (столбцов).