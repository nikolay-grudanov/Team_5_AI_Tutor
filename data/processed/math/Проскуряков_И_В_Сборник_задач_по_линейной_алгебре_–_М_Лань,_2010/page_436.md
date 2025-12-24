---
source_image: page_436.png
page_number: 436
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.89
tokens: 5602
characters: 1774
timestamp: 2025-12-24T07:15:55.657065
finish_reason: stop
---

на диагонали в матрице \( A_J \) отсутствуют, то \( r_k = r_{k+1} \), и при \( h = k \) соотношение (3) дает: \( x_k = r_{k-1} - r_k = r_{k-1} - 2r_k + r_{k+1} \), т. е. соотношение (\( \alpha \)) верно и для \( h = k \).

**1530.**

\[
f_1 = (1, 4, 3), \quad f_2 = (1, 0, 0), \quad f_3 = (3, 0, 1),
\]
\[
A_J = \begin{pmatrix}
2 & 1 & 0 \\
0 & 2 & 0 \\
0 & 0 & 2
\end{pmatrix}.
\]

**1531.**

\[
f_1 = (1, -3, -2), \quad f_2 = (1, 0, 0), \quad f_3 = (1, 0, 1),
\]
\[
A_J = \begin{pmatrix}
0 & 1 & 0 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{pmatrix}.
\]

**1532.**

\[
f_1 = (6, 6, -8), \quad f_2 = (3, 1, 0), \quad f_3 = (2, 1, -1),
\]
\[
A_J = \begin{pmatrix}
-1 & 1 & 0 \\
0 & -1 & 0 \\
0 & 0 & 0
\end{pmatrix}.
\]

**1533.**

\[
f_1 = (3, 1, 1), \quad f_2 = (1, 0, 0), \quad f_3 = (5, 0, 1),
\]
\[
A_J = \begin{pmatrix}
3 & 1 & 0 \\
0 & 3 & 0 \\
0 & 0 & 3
\end{pmatrix}.
\]

**1534.**

\[
f_1 = (1, 1, 1, 1), \quad f_2 = (-1, 0, 0, 0), \quad f_3 = (1, 1, 0, 0), \quad f_4 = (0, 0, -1, 0),
\]
\[
A_J = \begin{pmatrix}
1 & 1 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 1
\end{pmatrix}.
\]

**1535.**

\[
f_1 = (-1, -1, -1, 0), \quad f_2 = (2, 1, 0, 0), \quad f_3 = (1, 0, 0, -1), \quad f_4 = (3, 6, 7, 1),
\]
\[
A_J = \begin{pmatrix}
2 & 1 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 2 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}.
\]

**1536.** При четном \( n \):

\[
f_1 = e_1, \quad f_2 = e_3, \quad f_3 = e_5, \ldots, \quad f_{\frac{n}{2}} = e_{n-1}, \quad f_{\frac{n}{2}+1} = e_2, \ldots, \quad f_n = e_n.
\]

Матрица \( A_j \) состоит из двух клеток Жордана порядка \( n/2 \) с нулем по главной диагонали. При нечетном \( n \):

\[
f_1 = e_1, \quad f_2 = e_3, \quad f_3 = e_5, \ldots, \quad f_{\frac{n+1}{2}} = e_n, \quad f_{\frac{n+1}{2}+1} = e_2, \ldots, \quad f_n = e_{n-1}.
\]