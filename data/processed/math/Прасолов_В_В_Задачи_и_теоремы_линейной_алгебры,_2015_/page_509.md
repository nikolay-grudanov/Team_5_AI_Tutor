---
source_image: page_509.png
page_number: 509
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.87
tokens: 6810
characters: 3077
timestamp: 2025-12-24T08:21:33.866916
finish_reason: stop
---

б) Так как

\[
e^{(A+B)t} = I + (A+B)t + (A^2 + AB + BA + B^2)t^2/2 + \ldots
\]

и

\[
e^{At} e^{Bt} = I + (A+B)t + (A^2 + 2AB + B^2)t^2/2 + \ldots,
\]

то \( A^2 + AB + BA + B^2 = A^2 + 2AB + B^2 \), а значит, \( AB = BA \).

53.3. Существует унитарная матрица \( V \), для которой \( U = VDV^{-1} \), где \( D = \operatorname{diag}(\exp(i\alpha_1), \ldots, \exp(i\alpha_n)) \). Пусть \( \Lambda = \operatorname{diag}(\alpha_1, \ldots, \alpha_n) \). Тогда \( U = e^{iH} \), где \( H = V\Lambda V^{-1} = V\Lambda V^* \) — эрмитова матрица.

53.4. а) Пусть \( U = e^X \) и \( X^T = -X \). Тогда \( UU^T = e^X e^{X^T} = e^X e^{-X} = I \), так как матрицы \( X \) и \( -X \) коммутируют.
   б) Для матрицы \( U \) существует такая ортогональная матрица \( V \), что \( U = V \operatorname{diag}(A_1, \ldots, A_k, I)V^{-1} \), где \( A_i = \begin{pmatrix} \cos \varphi_i & -\sin \varphi_i \\ \sin \varphi_i & \cos \varphi_i \end{pmatrix} \) (см. теорему 13.3.3).
Ясно также, что матрицу \( A_i \) можно представить в виде \( e^X \), где \( X = \begin{pmatrix} 0 & -\varphi_i \\ \varphi_i & 0 \end{pmatrix} \) (см. задачу 53.1).

53.5. а) Достаточно заметить, что \( \det(e^A) = e^{\operatorname{tr} A} \) (см. теорему 53.1.2) и \( \operatorname{tr} A \) — вещественное число.
   б) Пусть \( \lambda_1 \) и \( \lambda_2 \) — собственные значения вещественной матрицы \( A \) и \( \lambda_1 + \lambda_2 = \operatorname{tr} A = 0 \). Числа \( \lambda_1 \) и \( \lambda_2 \) либо оба вещественные, либо \( \lambda_1 = \overline{\lambda}_2 \), т. е. \( \lambda_1 = -\overline{\lambda}_1 \). Поэтому собственные значения матрицы \( e^A \) равны либо \( e^\alpha \) и \( e^{-\alpha} \), либо \( e^{i\alpha} \) и \( e^{-i\alpha} \), где в обоих случаях \( \alpha \) — вещественное число. Следовательно, матрица \( B = \begin{pmatrix} -2 & 0 \\ 0 & -1/2 \end{pmatrix} \) не является экспонентой вещественной матрицы.

53.6. а) Пусть \( A_{ij} \) — алгебраическое дополнение элемента \( a_{ij} \). Тогда

\[
\operatorname{tr} (\dot{A} \operatorname{adj} A^T) = \sum_{i,j} \dot{a}_{ij} A_{ij}.
\]

Так как \( \det A = a_{ij} A_{ij} + \ldots \), где многоточием обозначены члены, не содержащие \( a_{ij} \), то \( (\det A)' = \dot{a}_{ij} A_{ij} + a_{ij} \dot{A}_{ij} + \ldots = \dot{a}_{ij} A_{ij} + \ldots \), где многоточием обозначены члены, не содержащие \( \dot{a}_{ij} \). Поэтому \( (\det A)' = \sum_{i,j} \dot{a}_{ij} A_{ij} \). Кроме того, \( \operatorname{adj} A^T = (\det A)A^{-1} \).
   б) Так как \( A \operatorname{adj} A^T = (\det A)I \), то \( \operatorname{tr}(A \operatorname{adj} A^T) = n \det A \), а значит,

\[
n(\det A)' = \operatorname{tr} (\dot{A} \operatorname{adj} A^T) + \operatorname{tr}(A (\operatorname{adj} A^T)').
\]

Остаётся воспользоваться результатом задачи а).

53.7. Требуется доказать, что если матрица \( A \) нильпотентна, то матрица \( e^A - I \) тоже нильпотентна. Пусть \( \lambda_1, \ldots, \lambda_n \) — собственные значения матрицы \( A \). Тогда \( e^{\lambda_1} - 1, \ldots, e^{\lambda_n} - 1 \) — собственные значения матрицы \( e^A - I \).