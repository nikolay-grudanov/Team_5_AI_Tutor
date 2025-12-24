---
source_image: page_677.png
page_number: 677
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.12
tokens: 11403
characters: 1548
timestamp: 2025-12-24T06:52:14.279653
finish_reason: stop
---

Компоненты результирующей матрицы \( C \) запишутся так:

\[
s = ag + bh \\
= \begin{pmatrix}
\cdot & \cdot & + & \cdot \\
\cdot & \cdot & \cdot & + \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot
\end{pmatrix},
\]

\[
t = ce + df \\
= \begin{pmatrix}
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot \\
+ & \cdot & \cdot & \cdot \\
\cdot & + & \cdot & \cdot
\end{pmatrix},
\]

\[
u = cg + dh \\
= \begin{pmatrix}
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & + & \cdot \\
\cdot & \cdot & \cdot & +
\end{pmatrix}.
\]

[Видно, что ни одну из матриц \( s, t, u, v \) нельзя вычислить за одно умножение по формуле (31.16) — нужно два. Если делать это независимо для каждой из четырёх матриц, потребуется 8 умножений. Однако, как мы увидим, одно умножение можно сэкономить, используя одни и те же произведения для нескольких матриц.]

Начнём со следующего наблюдения: \( s \) можно вычислить как \( s = P_1 + P_2 \), где каждая из матриц \( P_1 \) и \( P_2 \) требует одного умножения:

\[
P_1 = A_1 B_1 \\
= a \cdot (g - h) \\
= ag - ah \\
= \begin{pmatrix}
\cdot & \cdot & + & - \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot
\end{pmatrix}.
\]

\[
P_2 = A_2 B_2 \\
= (a + b) \cdot h \\
= ah + bh \\
= \begin{pmatrix}
\cdot & \cdot & \cdot & + \\
\cdot & \cdot & \cdot & + \\
\cdot & \cdot & \cdot & \cdot \\
\cdot & \cdot & \cdot & \cdot
\end{pmatrix}.
\]

Аналогичным образом можно вычислить \( t \). Именно, \( t = P_3 + P_4 \),