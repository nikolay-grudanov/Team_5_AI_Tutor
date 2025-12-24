---
source_image: page_381.png
page_number: 381
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.61
tokens: 5701
characters: 2164
timestamp: 2025-12-24T07:14:25.922851
finish_reason: stop
---

852.
\[
\begin{pmatrix}
2-n & 1 & 1 & \ldots & 1 \\
1 & -1 & 0 & \ldots & 0 \\
1 & 0 & -1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & 0 & 0 & \ldots & -1
\end{pmatrix}.
\]

853. \(\frac{1}{n-1}\)
\[
\begin{pmatrix}
2-n & 1 & 1 & \ldots & 1 \\
1 & 2-n & 1 & \ldots & 1 \\
1 & 1 & 2-n & \ldots & 1 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & 1 & 1 & \ldots & 2-n
\end{pmatrix}.
\]

854. \(-\frac{1}{a(n+a)}\)
\[
\begin{pmatrix}
1-n-a & 1 & 1 & \ldots & 1 \\
1 & 1-n-a & 1 & \ldots & 1 \\
1 & 1 & 1-n-a & \ldots & 1 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
1 & 1 & 1 & \ldots & 1-n-a
\end{pmatrix}.
\]

855. \(-\frac{1}{s}\)
\[
\begin{pmatrix}
\frac{1-a_1 s}{a_1^2} & \frac{1}{a_1 a_2} & \frac{1}{a_1 a_3} & \ldots & \frac{1}{a_1 a_n} \\
\frac{1}{a_2 a_1} & \frac{1}{a_2^2} & \frac{1}{a_2 a_3} & \ldots & \frac{1}{a_2 a_n} \\
\frac{1}{a_3 a_1} & \frac{1}{a_3 a_2} & \frac{1}{a_3^2} & \ldots & \frac{1}{a_3 a_n} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
\frac{1}{a_n a_1} & \frac{1}{a_n a_2} & \frac{1}{a_n a_3} & \ldots & \frac{1-a_n s}{a_n^2}
\end{pmatrix},
\]
где \(s = 1 + \frac{1}{a_1} + \frac{1}{a_2} + \ldots + \frac{1}{a_n}\).

857.
\[
\begin{pmatrix}
-7 & 5 & 12 & -19 \\
3 & -2 & -5 & 8 \\
41 & -30 & -69 & 111 \\
-59 & 43 & 99 & -159
\end{pmatrix}.
\]

858. \(\frac{1}{ns}\)
\[
\begin{pmatrix}
1-s & 1+s & 1 & \ldots & 1 & 1 \\
1 & 1-s & 1+s & \ldots & 1 & 1 \\
1 & 1 & 1-s & \ldots & 1 & 1 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
1+s & 1 & 1 & \ldots & 1 & 1-s
\end{pmatrix},
\]
где \(s = \frac{n(n+1)}{2}\).

Указание. В системе уравнений для элементов \(k\)-го столбца обратной матрицы из каждого уравнения от первого до \((n-1)\)-го вычесть следующее и полученные \(n-1\) уравнений сложить. Все неизвестные выразить через \(k\)-е.

859. \(\frac{1}{nh s}\)
\[
\begin{pmatrix}
h-s & h+s & h & \ldots & h & h \\
h & h-s & h+s & \ldots & h & h \\
h & h & h-s & \ldots & h & h \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
h+s & h & h & \ldots & h & h-s
\end{pmatrix},
\]
где \(s = n a + h \cdot \frac{n(n-1)}{2}\) — сумма элементов какой-нибудь строки (или столбца) данной матрицы.