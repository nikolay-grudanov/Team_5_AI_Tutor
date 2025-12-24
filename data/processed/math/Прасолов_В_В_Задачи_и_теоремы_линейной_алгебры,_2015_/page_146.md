---
source_image: page_146.png
page_number: 146
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.49
tokens: 6458
characters: 2230
timestamp: 2025-12-24T08:11:28.047826
finish_reason: stop
---

образуют ортогональный базис, причём квадрат длины вектора \( \varepsilon_k \) равен \( G_{k-1} G_k \), где \( G_k = \begin{vmatrix} g_{11} & \cdots & g_{1k} \\ \cdots & \cdots & \cdots \\ g_{k1} & \cdots & g_{kk} \end{vmatrix} \) при \( k = 1, \ldots, n \) и \( G_0 = 1 \).

Доказательство. Ясно, что

\[
(e_i, \varepsilon_k) = \begin{vmatrix} g_{11} & \cdots & g_{1k} \\ \cdots & \cdots & \cdots \\ g_{k-1,1} & \cdots & g_{k-1,k} \\ g_{i1} & \cdots & g_{ik} \end{vmatrix}.
\]

Поэтому \( (e_i, \varepsilon_k) = 0 \) при \( i = 1, \ldots, k-1 \) и \( (e_k, \varepsilon_k) = G_k \).

Непосредственно из формулы для \( \varepsilon_k \) видно, что \( \varepsilon_k = G_{k-1} e_k + e \), где \( e \in \langle e_1, \ldots, e_{k-1} \rangle \). Поэтому \( (\varepsilon_k - G_{k-1} e_k, \varepsilon_k) = 0 \). Следовательно, \( (\varepsilon_k, \varepsilon_k) = G_{k-1} (e_k, \varepsilon_k) = G_{k-1} G_k \).

Чтобы завершить доказательство, нужно убедиться, что все векторы \( \varepsilon_1, \ldots, \varepsilon_n \) ненулевые, т. е. \( G_k \neq 0 \) для \( k = 1, \ldots, n \). Выберем произвольный ортонормированный базис и рассмотрим матрицу \( X \), образованную столбцами координат векторов \( e_1, \ldots, e_k \) относительно этого базиса. Ясно, что

\[
X^T X = \begin{pmatrix} g_{11} & \cdots & g_{1k} \\ \cdots & \cdots & \cdots \\ g_{k1} & \cdots & g_{kk} \end{pmatrix},
\]

поэтому \( G_k = (\det X)^2 \). Остаётся заметить, что \( \det X \neq 0 \), поскольку векторы \( e_1, \ldots, e_k \) линейно независимы.

Матрицу

\[
\begin{pmatrix}
(e_1, e_1) & \ldots & (e_1, e_k) \\
\cdots & \cdots & \cdots \\
(e_k, e_1) & \ldots & (e_k, e_k)
\end{pmatrix},
\]

возникшую при доказательстве теоремы 9.2.2, называют матрицей Грама системы векторов \( e_1, \ldots, e_k \), а её определитель — определителем Грама. Как только что было доказано, определитель Грама системы линейно независимых векторов положителен, а определитель Грама системы линейно зависимых векторов равен 0.

9.3. Ортогональные проекции

Пусть в пространстве \( V \) задано скалярное произведение и \( W \) — подпространство в \( V \). Вектор \( w \in W \) называют ортогональной проекцией вектора \( v \in V \) на подпространство \( W \), если \( v - w \perp W \).