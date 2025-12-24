---
source_image: page_044.png
page_number: 44
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.52
tokens: 6239
characters: 1678
timestamp: 2025-12-24T08:08:30.151896
finish_reason: stop
---

1.42. Докажите, что определитель

\[
\begin{vmatrix}
x & a & 0 & \ldots & 0 & 0 \\
-a & x & a & \ldots & 0 & 0 \\
0 & -a & x & \ldots & 0 & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \ldots & x & a \\
0 & 0 & 0 & \ldots & -a & x
\end{vmatrix}
\]

порядка \( n \) равен

\[
x^n + \binom{n-1}{1} a^2 x^{n-2} + \binom{n-2}{2} a^4 x^{n-4} + \binom{n-3}{3} a^6 x^{n-6} + \ldots
\]

1.43. Докажите, что

\[
F_{n+1} = 1 + \binom{n-1}{1} + \binom{n-2}{2} + \binom{n-3}{3} + \ldots
\]

§ 2. Миноры и алгебраические дополнения

2.1. Определение минора

Во многих случаях для матрицы \( A \) бывает полезно рассмотреть определитель матрицы, элементы которой стоят на пересечениях некоторых \( p \) строк и \( p \) столбцов матрицы \( A \). Такой определитель называют минором \( p \)-го порядка матрицы \( A \). Для удобства введем следующее обозначение:

\[
A\left(\begin{array}{cccc}
i_1 & i_2 & \ldots & i_p \\
k_1 & k_2 & \ldots & k_p
\end{array}\right) = \begin{vmatrix}
a_{i_1 k_1} & a_{i_1 k_2} & \cdots & a_{i_1 k_p} \\
\cdots & \cdots & \cdots & \cdots \\
a_{i_p k_1} & a_{i_p k_2} & \cdots & a_{i_p k_p}
\end{vmatrix}.
\]

Если \( i_1 = k_1, \ldots, i_p = k_p \), то минор называют главным, а если \( i_1 = k_1 = 1, \ldots, i_p = k_p = p \), то угловым.

2.2. Ранг матрицы

Ненулевой минор максимального порядка называют базисным, а его порядок называют рангом матрицы.

Теорема 2.2.1. Если \( A\left(\begin{array}{cccc}
i_1 & \ldots & i_p \\
k_1 & \ldots & k_p
\end{array}\right) \) — базисный минор матрицы \( A \), то все её строки являются линейными комбинациями строк с номерами \( i_1, \ldots, i_p \), причём сами эти строки линейно независимы.