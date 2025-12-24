---
source_image: page_295.png
page_number: 295
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.65
tokens: 6782
characters: 2909
timestamp: 2025-12-24T08:15:38.975158
finish_reason: stop
---

21.13. Для матриц \( A \) и \( B \) выберем неотрицательно определённые матрицы \( S \) и \( T \) так, что \( A = S^2 \) и \( B = T^2 \) (теорема 21.4.1). Тогда

\[
\operatorname{tr}(AB) = \operatorname{tr}(SSTT) = \operatorname{tr}(TSST) = \operatorname{tr}((ST)^*ST) \geqslant 0.
\]

21.14. Ясно, что \( \operatorname{tr}(A^2) - \operatorname{tr}(B^2) = \operatorname{tr}((A - B)A) + \operatorname{tr}(B(A - B)) \). Остаётся воспользоваться результатом задачи 21.13.

21.15. Достаточно воспользоваться тождеством

\[
\begin{pmatrix}
\lambda I_n & 0 \\
0 & I_m
\end{pmatrix}
\begin{pmatrix}
A & B \\
B^* & 0
\end{pmatrix}
\begin{pmatrix}
\lambda I_n & 0 \\
0 & I_m
\end{pmatrix} = \lambda \begin{pmatrix}
\lambda A & B \\
B^* & 0
\end{pmatrix}.
\]

21.16. а) Эквивалентность этих форм над \( \mathbb{Q} \) следует из того, что они имеют одинаковую сигнатуру. Предположим, что эти формы эквивалентны над \( \mathbb{Z} \). Тогда существует целочисленная матрица \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \), для которой

\[
\begin{pmatrix}
-1 & 0 \\
0 & 1
\end{pmatrix} =
\begin{pmatrix}
a & c \\
b & d
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
a & b \\
c & d
\end{pmatrix} =
\begin{pmatrix}
2ac & ad + bc \\
ad + bc & 2bd
\end{pmatrix}.
\]

Но если \( b \) и \( d \) — целые числа, то \( 2bd \neq 1 \).

б) Равенства

\[
\begin{pmatrix}
1 & 0 \\
k & 1
\end{pmatrix}
\begin{pmatrix}
0 & 1 \\
1 & 0
\end{pmatrix}
\begin{pmatrix}
1 & k \\
0 & 1
\end{pmatrix} =
\begin{pmatrix}
0 & 1 \\
1 & 2k
\end{pmatrix},
\]
\[
\begin{pmatrix}
1 & 1 \\
k & k+1
\end{pmatrix}
\begin{pmatrix}
-1 & 0 \\
0 & 1
\end{pmatrix}
\begin{pmatrix}
1 & k \\
1 & k+1
\end{pmatrix} =
\begin{pmatrix}
0 & 1 \\
1 & 2k+1
\end{pmatrix}
\]

показывают, что квадратичная форма с матрицей \( \begin{pmatrix} 0 & 1 \\ 1 & n \end{pmatrix} \) эквивалентна квадратичной форме с матрицей \( \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \) при \( n \) чётном и квадратичной форме с матрицей \( \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix} \) при \( n \) нечётном.

§ 22. Одновременное приведение пары эрмитовых форм к диагональному виду

22.1. Пусть \( a_{ii} = 0 \) и \( a_{ij} \neq 0 \). Рассмотрим вектор \( u \), \( i \)-я и \( j \)-я координаты которого равны \( x_i \) и \( x_j \), а все остальные координаты равны нулю. Тогда \( B(u, u) = a_{ij}x_j \overline{x}_i + \overline{a}_{ij}\overline{x}_j x_i + a_{jj}|x_j|^2 \). Фиксируем \( x_j \neq 0 \), и пусть \( x_i = \lambda a_{ij} x_j \), где \( \lambda \in \mathbb{R} \). Тогда \( B(u, u) = 2\lambda|a|^2 + b \), где \( a = a_{ij} x_j \neq 0 \) и \( b = a_{jj}|x_j|^2 \). Величина \( 2\lambda|a|^2 + b \) принимает как положительные, так и отрицательные значения, поэтому форма \( B \) не является знакопределённой.

22.2. Выберем матрицу \( T \) так, что \( A = T^*T \) и \( B = T^*DT \), где

\[
D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)
\]