---
source_image: page_524.png
page_number: 524
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.99
tokens: 6625
characters: 2617
timestamp: 2025-12-24T08:21:55.851660
finish_reason: stop
---

57.4. Коммутант группы \( \mathrm{GL}(n, K) \)

Напомним, что коммутант группы \( G \) — это подгруппа \( G' \subset G \), порождённая элементами вида \( aba^{-1}b^{-1},\ a, b \in G \).

Теорема 57.4.1. Если \( n \geqslant 2 \), то матрица \( D(\mu) = \mathrm{diag}(1, \ldots, 1, \mu) \), где \( \mu = aba^{-1}b^{-1} \) и \( a, b \in K \), лежит в группе \( \mathrm{SL}(n, K) \).

Доказательство. Запишем последовательность элементарных преобразований (которые заключаются в прибавлении к одной строке левого кратного другой строки), переводящую единичную матрицу в матрицу \( D(\mu) \):

\[
\begin{pmatrix}
1 & 0 \\
0 & 1
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & 0 \\
a^{-1} & 1
\end{pmatrix}
\rightarrow
\begin{pmatrix}
0 & -a \\
a^{-1} & 1
\end{pmatrix}
\rightarrow
\begin{pmatrix}
0 & -a \\
a^{-1} & b^{-1}
\end{pmatrix}
\rightarrow
\begin{pmatrix}
aba^{-1} & 0 \\
a^{-1} & b^{-1}
\end{pmatrix}
\rightarrow
\begin{pmatrix}
aba^{-1} & 0 \\
1 & b^{-1}
\end{pmatrix}
\rightarrow
\begin{pmatrix}
0 & -\mu \\
1 & b^{-1}
\end{pmatrix}
\rightarrow
\begin{pmatrix}
0 & -\mu \\
1 & \mu
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & 0 \\
1 & \mu
\end{pmatrix}
\rightarrow
\begin{pmatrix}
1 & 0 \\
0 & \mu
\end{pmatrix}.
\]

Эти преобразования записаны для матриц порядка 2, но их можно записать и для матриц произвольного порядка, подразумевая, что в преобразованиях участвуют только две последние строки.

Теорема 57.4.2. Для любого \( n \geqslant 2 \) коммутантом группы \( \mathrm{GL}(n, K) \) является группа \( \mathrm{SL}(n, K) \), за исключением того случая, когда \( n = 2 \) и \( K = \mathbb{F}_2 \).

Доказательство. Докажем сначала, что коммутант группы \( \mathrm{GL}(n, K) \) содержится в \( \mathrm{SL}(n, K) \). Легко проверить, что если \( D = \mathrm{diag}(\lambda_1, \ldots, \lambda_n) \), то \( DB_{ij}(\lambda)D^{-1} = B_{ij}(\lambda_i \lambda_j \lambda_j^{-1}) \). Поэтому для любой диагональной матрицы \( D \) и любой матрицы \( B \in \mathrm{SL}(n, K) \) матрица \( DBD^{-1} \) тоже лежит в \( \mathrm{SL}(n, K) \), т. е. \( DB = B'D \), где \( B' \in \mathrm{SL}(n, K) \).

Согласно теореме 57.2.1 любую невырожденную матрицу \( A \) можно представить в виде \( A = BD(\mu) \), где \( B \in \mathrm{SL}(n, K) \) и \( D(\mu) = \mathrm{diag}(1, \ldots, 1, \mu) \). Поэтому

\[
A_1^{-1}A_2^{-1}A_1A_2 = D_1^{-1}B_1^{-1}D_2^{-1}B_2^{-1}B_1D_1B_2D_2 = D_1^{-1}D_2^{-1}D_1D_2B,
\]

где \( B \in \mathrm{SL}(n, K) \). Если \( D_1 = D(\mu_1) \) и \( D_2 = D(\mu_2) \), то согласно теореме 57.4.1 матрица \( D_1^{-1}D_2^{-1}D_1D_2 = D(\mu_1^{-1}\mu_2^{-1}\mu_1\mu_2) \) лежит в \( \mathrm{SL}(n, K) \).