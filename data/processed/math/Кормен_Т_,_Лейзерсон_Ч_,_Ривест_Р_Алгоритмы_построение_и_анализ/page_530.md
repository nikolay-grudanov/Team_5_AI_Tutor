---
source_image: page_530.png
page_number: 530
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 78.56
tokens: 12026
characters: 2344
timestamp: 2025-12-24T06:45:48.979960
finish_reason: stop
---

Для графа рис. 26.1 вычисляются матрицы \( D^{(k)} \) и \( \Pi^{(k)} \), вычисляемые алгоритмом Флойда-Уоршолла.

\[
D^{(0)} = \begin{pmatrix}
0 & 3 & 8 & \infty & -4 \\
\infty & 0 & \infty & 1 & 7 \\
\infty & 4 & 0 & \infty & \infty \\
2 & \infty & -5 & 0 & \infty \\
\infty & \infty & \infty & 6 & 0
\end{pmatrix}
\]

\[
D^{(1)} = \begin{pmatrix}
0 & 3 & 8 & \infty & -4 \\
\infty & 0 & \infty & 1 & 7 \\
\infty & 4 & 0 & \infty & \infty \\
2 & 5 & -5 & 0 & -2 \\
\infty & \infty & \infty & 6 & 0
\end{pmatrix}
\]

\[
D^{(2)} = \begin{pmatrix}
0 & 3 & 8 & 4 & -4 \\
\infty & 0 & \infty & 1 & 7 \\
\infty & 4 & 0 & 5 & 11 \\
2 & 5 & -5 & 0 & -2 \\
\infty & \infty & \infty & 6 & 0
\end{pmatrix}
\]

\[
D^{(3)} = \begin{pmatrix}
0 & 3 & 8 & 4 & -4 \\
\infty & 0 & \infty & 1 & 7 \\
\infty & 4 & 0 & 5 & 11 \\
2 & -1 & -5 & 0 & -2 \\
\infty & \infty & \infty & 6 & 0
\end{pmatrix}
\]

\[
D^{(4)} = \begin{pmatrix}
0 & 3 & -1 & 4 & -4 \\
3 & 0 & -4 & 1 & -1 \\
7 & 4 & 0 & 5 & 3 \\
2 & -1 & -5 & 0 & -2 \\
8 & 5 & 1 & 6 & 0
\end{pmatrix}
\]

\[
D^{(5)} = \begin{pmatrix}
0 & 1 & -3 & 2 & -4 \\
3 & 0 & -4 & 1 & -1 \\
7 & 4 & 0 & 5 & 3 \\
2 & -1 & -5 & 0 & -2 \\
8 & 5 & 1 & 6 & 0
\end{pmatrix}
\]

\[
\Pi^{(0)} = \begin{pmatrix}
NIL & 1 & 1 & NIL & 1 \\
NIL & NIL & NIL & 2 & 2 \\
NIL & 3 & NIL & NIL & NIL \\
4 & NIL & 4 & NIL & NIL \\
NIL & NIL & NIL & 5 & NIL
\end{pmatrix}
\]

\[
\Pi^{(1)} = \begin{pmatrix}
NIL & 1 & 1 & NIL & 1 \\
NIL & NIL & NIL & 2 & 2 \\
NIL & 3 & NIL & NIL & NIL \\
4 & 1 & 4 & NIL & 1 \\
NIL & NIL & NIL & 5 & NIL
\end{pmatrix}
\]

\[
\Pi^{(2)} = \begin{pmatrix}
NIL & 1 & 1 & 2 & 1 \\
NIL & NIL & NIL & 2 & 2 \\
NIL & 3 & NIL & 2 & 2 \\
4 & 1 & 4 & NIL & 1 \\
NIL & NIL & NIL & 5 & NIL
\end{pmatrix}
\]

\[
\Pi^{(3)} = \begin{pmatrix}
NIL & 1 & 1 & 2 & 1 \\
NIL & NIL & NIL & 2 & 2 \\
NIL & 3 & NIL & 2 & 2 \\
4 & 3 & 4 & NIL & 1 \\
NIL & NIL & NIL & 5 & NIL
\end{pmatrix}
\]

\[
\Pi^{(4)} = \begin{pmatrix}
NIL & 1 & 4 & 2 & 1 \\
4 & NIL & 4 & 2 & 1 \\
4 & 3 & NIL & 2 & 1 \\
4 & 3 & 4 & NIL & 1 \\
4 & 3 & 4 & 5 & NIL
\end{pmatrix}
\]

\[
\Pi^{(5)} = \begin{pmatrix}
NIL & 3 & 4 & 5 & 1 \\
4 & NIL & 4 & 2 & 1 \\
4 & 3 & NIL & 2 & 1 \\
4 & 3 & 4 & NIL & 1 \\
4 & 3 & 4 & 5 & NIL
\end{pmatrix}
\]

Рисунок 26.3 26.4 Матрицы \( \Pi^{(k)} \) и \( D^{(k)} \), вычисляемые алгоритмом Флойда–Уоршолла для графа рис. 26.1.