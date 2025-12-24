---
source_image: page_364.png
page_number: 364
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.25
tokens: 6592
characters: 2266
timestamp: 2025-12-24T08:17:30.802892
finish_reason: stop
---

прина́длежит одному из кругов

\[
|z| \leqslant \frac{|a_0|}{A_1}, \quad |z| \leqslant \frac{A_1 + |a_1|}{A_2}, \quad \ldots, \quad |z| \leqslant \frac{A_{n-2} + |a_{n-2}|}{A_{n-1}}, \quad \left| z + \frac{a_{n-1}}{A_n} \right| \leqslant \frac{A_{n-1}}{A_n}.
\]

Остаётся заметить, что последний круг содержится в круге

\[
|z| \leqslant \frac{A_{n-1} + |a_{n-1}|}{A_n}.
\]

**Следствие 1 (Коши).** Корни многочлена (1) по абсолютной величине не превосходят наибольшего из чисел \(|a_0|, 1 + |a_1|, \ldots, 1 + |a_{n-1}|.\)

**Доказательство.** Достаточно положить \(A_1 = A_2 = \ldots = A_{n-1} = 1.\)

**Следствие 2.** Корни многочлена (1) по абсолютной величине не превосходят наибольшего из чисел \(\frac{|a_0|}{|a_1|}, 2\frac{|a_1|}{|a_2|}, \ldots, 2\frac{|a_{n-2}|}{|a_{n-1}|}, 2|a_{n-1}|.\)

**Доказательство.** Положим \(A_i = |a_i|\) для \(i = 1, \ldots, n-1\). Тогда \(\frac{A_i + |a_i|}{A_{i+1}} = 2\frac{|a_i|}{|a_{i+1}|}\) при \(i \geqslant 1\) (мы полагаем \(a_n = 1\)).

**Теорема 37.5.3 (Коши).** Корни многочлена (1) по абсолютной величине не превосходят положительного корня многочлена

\[
z^n - |a_{n-1}|z^{n-1} - |a_{n-2}|z^{n-2} - \ldots - |a_0|.
\] (2)

**Доказательство.** Как и при доказательстве теоремы 37.5.2, рассмотрим матрицу \(DCD^{-1}\). Пусть \(\rho\) — положительный корень многочлена (2). Положим \(A_i = \rho^{n-i}, i = 1, 2, \ldots, n\), т. е. \(D = \operatorname{diag}(\rho^{n-1}, \rho^{n-2}, \ldots, \rho, 1)\). В таком случае

\[
DCD^{-1} = \begin{pmatrix}
0 & \rho & 0 & \ldots & 0 \\
0 & 0 & \rho & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \ldots & \rho \\
-a_0/\rho^{n-1} & -a_1/\rho^{n-2} & -a_2/\rho^{n-3} & \ldots & -a_{n-1}
\end{pmatrix}.
\] (3)

На этот раз применим теорему Гершгорина не для столбцов матрицы, а для строк. В результате получим неравенства \(|z| \leqslant \rho, \ldots, |z| \leqslant \rho,\)
\[
|z| \leqslant |a_{n-1}| + \frac{|a_{n-2}|}{\rho} + \ldots + \frac{|a_0|}{\rho^{n-1}} = \rho.
\]

**Теорема 37.5.4.** Пусть \(\lambda_1, \ldots, \lambda_n\) — положительные числа, причём \(\lambda_1 + \ldots + \lambda_n = 1\). Тогда корни многочлена (1) по абсолютной величине не превосходят \(\max_{1 \leqslant j \leqslant n} \left| \frac{a_{n-j}}{\lambda_j} \right|^{1/j}.\)