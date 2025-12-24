---
source_image: page_706.png
page_number: 706
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 54.58
tokens: 11642
characters: 1844
timestamp: 2025-12-24T06:53:39.964425
finish_reason: stop
---

Положительно определённые симметрические матрицы и метод наименьших квадратов

вычисления преобразования Фурье вектора \( a = (a_0, a_1, \ldots, a_{n-1}) \) (где \( n — степень 2 \)):

\textsc{Recursive-FFT}$(a)$ % Рекурсивное БПФ

1 $n\leftarrow length[a]$ $qqquad n$ --- степень $2$
2 if $n=1$
3 \quad then return $a$
4 $\omega_n\leftarrow e^{2\pi i/n}$
5 $\omega\leftarrow 1$
6 $a^{[0]}\leftarrow (a_0, a_2, \ldots, a_{n-2})$
7 $a^{[1]}\leftarrow (a_1, a_3, \ldots, a_{n-1})$
8 $y^{[0]}\leftarrow$ \textsc{Recursive-FFT}$(a^{[0]})$
9 $y^{[1]}\leftarrow$ \textsc{Recursive-FFT}$(a^{[1]})$
10 for $k\leftarrow 0$ to $n/2-1$
11 \quad do $y_k\leftarrow y_k^{[0]} + \omega y_k^{[1]}$
12 \quad $y_{k+(n/2)}\leftarrow y_k^{[0]} - \omega y_k^{[1]}$
13 \quad $\omega\leftarrow \omega\omega_n\omega_n$
14 return $y$

Процедура Recursive-FFT работает следующим образом. Строки 2–3 образуют "базис рекурсии": дискретным преобразованием Фурье для вектора длины 1 является сам этот вектор, так как
\[
y_0 = a_0 \omega_1^0 = a_0 1 = a_0.
\]
В строках 6–7 формируются вектора коэффициентов многочленов \( A^{[0]} \) и \( A^{[1]} \). Строки 4, 5 и 13 гарантируют, что \( \omega = \omega_n^k \) в момент выполнения строк 11–12 (мы экономим время, не вычисляя значение \( \omega_n^k \) каждый раз заново) В строках 8–9 рекурсивно вычисляются значения
\[
y_k^{[0]} = A^{[0]}(\omega_{n/2}^k),
\]
\[
y_k^{[1]} = A^{[1]}(\omega_{n/2}^k),
\]
или (поскольку \( \omega_{n/2}^k = \omega_n^{2k} \) по лемме о сокращении)
\[
y_k^{[0]} = A^{[0]}(\omega_n^{2k}),
\]
\[
y_k^{[1]} = A^{[1]}(\omega_n^{2k}).
\]
В строках 11–12 собираются вместе результаты рекурсивных вычислений DFT$_{n/2}$. В строке 11 для \( y_0, y_1, \ldots, y_{n/2-1} \) получается
\[
y_k = y_k^{[0]} + \omega_n^k y_k^{[1]} = A^{[0]}(\omega_n^{2k}) + \omega_n^k A^{[1]}(\omega_n^{2k}) = A(\omega_n^k);
\]