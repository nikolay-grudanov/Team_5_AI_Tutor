---
source_image: page_250.png
page_number: 250
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.42
tokens: 6448
characters: 2062
timestamp: 2025-12-24T08:14:17.650619
finish_reason: stop
---

нимают любые целые значения (если хотя бы одно из чисел \( b'_k \) не делится на \( g_k \), то целочисленных решений нет). Решения исходного уравнения получаются по формуле \( x = Cx' \).

Покажем, как работает этот алгоритм, на примере системы линейных уравнений

\[
\begin{cases}
x_1 + 5x_2 + 3x_3 = 8, \\
7x_1 - 13x_2 + 12x_3 = 2.
\end{cases}
\]

Основная трудность состоит в вычислении матриц \( B \) и \( C \) для матрицы \( A = \begin{pmatrix} 1 & 5 & 3 \\ 7 & -13 & 12 \end{pmatrix} \). Мы начинаем с того, что вычитаем из второй строки первую строку, умноженную на 7, т. е. рассматриваем преобразование

\[
\begin{pmatrix} 1 & 0 \\ -7 & 1 \end{pmatrix} \begin{pmatrix} 1 & 5 & 3 \\ 7 & -13 & 12 \end{pmatrix} = \begin{pmatrix} 1 & 5 & 3 \\ 0 & -48 & -9 \end{pmatrix}.
\]

Затем с помощью первого столбца уничтожаем второй и третий элемент первой строки, а заодно меняем знак второй строки:

\[
\begin{pmatrix} 1 & 5 & 3 \\ 0 & -48 & -9 \end{pmatrix} \begin{pmatrix} 1 & 5 & 3 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 48 & 9 \end{pmatrix}.
\]

Оставшиеся преобразования относятся только к строке (48 9); они заключаются в нахождении наибольшего общего делителя чисел 48 и 9:

\[
(48 \ 9) \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = (9 \ 48);
\]
\[
(9 \ 48) \begin{pmatrix} 1 & -5 \\ 0 & 1 \end{pmatrix} = (9 \ 3);
\]
\[
(9 \ 3) \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = (3 \ 9);
\]
\[
(3 \ 9) \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} = (3 \ 0).
\]

Легко проверить, что

\[
\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -5 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} 1 & -3 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & -3 \\ -5 & 16 \end{pmatrix}.
\]

Таким образом,

\[
C = \begin{pmatrix} 1 & 5 & 3 \\ 0 & -1 & 0 \\ 0 & 0 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & -3 \\ 0 & -5 & 16 \end{pmatrix} = \begin{pmatrix} 1 & -10 & 33 \\ 0 & -1 & 3 \\ 0 & 5 & -16 \end{pmatrix}
\]
и \( B = \begin{pmatrix} 1 & 0 \\ -7 & 1 \end{pmatrix} \).