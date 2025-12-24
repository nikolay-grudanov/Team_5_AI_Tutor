---
source_image: page_032.png
page_number: 32
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.18
tokens: 6710
characters: 2649
timestamp: 2025-12-24T08:08:34.258077
finish_reason: stop
---

Теорема 1.10.1. Пусть \( \varepsilon_1, \ldots, \varepsilon_n \) — попарно различные корни степени \( n \) из единицы. Тогда определитель циркулянта, соответствующего последовательности \( b_0, b_1, \ldots \), равен \( f(\varepsilon_1)f(\varepsilon_2)\ldots f(\varepsilon_n) \), где \( f \) — вспомогательный многочлен.

Доказательство. Легко проверить, что при \( n = 3 \)

\[
\begin{pmatrix}
1 & 1 & 1 \\
1 & \varepsilon_1 & \varepsilon_1^2 \\
1 & \varepsilon_2 & \varepsilon_2^2
\end{pmatrix}
\begin{pmatrix}
b_0 & b_2 & b_1 \\
b_1 & b_0 & b_2 \\
b_2 & b_1 & b_0
\end{pmatrix}
=
\begin{pmatrix}
f(1) & f(1) & f(1) \\
f(\varepsilon_1) & \varepsilon_1 f(\varepsilon_1) & \varepsilon_1^2 f(\varepsilon_1) \\
f(\varepsilon_2) & \varepsilon_2 f(\varepsilon_2) & \varepsilon_2^2 f(\varepsilon_2)
\end{pmatrix}
=
f(1) f(\varepsilon_1) f(\varepsilon_2)
\begin{pmatrix}
1 & 1 & 1 \\
1 & \varepsilon_1 & \varepsilon_1^2 \\
1 & \varepsilon_2 & \varepsilon_2^2
\end{pmatrix}.
\]

Поэтому

\[
V(1, \varepsilon_1, \varepsilon_2)|a_{ij}|_1^3 = f(1) f(\varepsilon_1) f(\varepsilon_2) V(1, \varepsilon_1, \varepsilon_2).
\]

Но определитель Вандермонда \( V(1, \varepsilon_1, \varepsilon_2) \) отличен от нуля, поэтому \( |a_{ij}|_1^3 = f(1) f(\varepsilon_1) f(\varepsilon_2) \). В общем случае доказательство аналогично.

Замечание. Справедливо даже более сильное утверждение: числа \( f(\varepsilon_1), \ldots, f(\varepsilon_n) \) являются собственными значениями циркулянта (теорема 13.5.2).

Рассмотрим циркулянт \( C_n \), у которого \( c_{2,1} = c_{3,2} = \ldots = c_{n,n-1} = c_{1,n} = 1 \), а все остальные элементы нулевые. Легко видеть, что матрица \( A \) порядка \( n \) является циркулянтом тогда и только тогда, когда \( A = b_0 I + b_1 C_n + b_2 C_n^2 + \ldots + b_{n-1} C_n^{n-1} \).

Теорема 1.10.2. Матрица \( \|a_{ij}\|_1^n \) является циркулянтом тогда и только тогда, когда \( AC_n = C_n A \).

Доказательство. Ясно, что если \( A = \bullet b_k C_n^k \), то \( AC_n = C_n A \). Предположим теперь, что \( AC_n = C_n A \). Пусть \( e_1 \) — столбец \( (1, 0, \ldots, 0) \). Тогда

\[
(A - a_{11} I - a_{21} C_n - \ldots - a_{n1} C_n^{n-1}) C_n^k e_1 =
= C_n^k (A - a_{11} I - a_{21} C_n - \ldots - a_{n1} C_n^{n-1}) e_1 = 0
\]

для всех \( k \). Из этого следует, что \( A = a_{11} I + a_{21} C_n + \ldots + a_{n1} C_n^{n-1} \), поскольку \( e_1, C_n e_1, \ldots, C_n^{n-1} e_1 \) — это столбцы \( (1, 0, \ldots, 0), (0, 1, 0, \ldots, 0), \ldots, (0, \ldots, 0, 1) \).

Теорема 1.10.3. Вспомогательный многочлен произведения двух циркулянтов порядка \( n \) по модулю многочлена \( x^n - 1 \) равен произведению их вспомогательных многочленов.