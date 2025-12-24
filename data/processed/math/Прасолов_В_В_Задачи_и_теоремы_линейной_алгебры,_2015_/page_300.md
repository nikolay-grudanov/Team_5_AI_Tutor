---
source_image: page_300.png
page_number: 300
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.80
tokens: 6949
characters: 3328
timestamp: 2025-12-24T08:15:50.942138
finish_reason: stop
---

Остаётся доказать, что \( AT = SA \). Ясно, что \( AT^2 = S^2A \), поэтому по индукции получаем, что \( AT^{2n} = S^{2n}A \) для \( n = 0, 1, 2, \ldots \), а значит, \( Ap(T^2) = p(S^2)A \) для любого многочлена \( p \). Если мы выберем многочлен \( p \) степени \( 2n \) так, что \( p(\lambda_i^2) = \lambda_i \) для каждого числа \( \lambda_i \), которое является собственным значением матрицы \( T \) или \( S \), то получим \( p(T^2) = T \) и \( p(S^2) = S \). Таким образом, \( AT = SA \).
Замечание. Для вещественных матриц другое доказательство приведено в решении задачи 18.3.

§ 25. Нормальные матрицы

25.1. Если \( A^* = AU \), где \( U \) — унитарная матрица, то \( A = U^*A^* \), а значит, \( UA = UU^*A^* = A^* \). Следовательно, \( AU = UA \) и \( A^*A = AAU = AAU = AA^* \).
Если оператор \( A \) нормален, то для него существует ортонормированный собственный базис \( e_1, \ldots, e_n \). При этом \( Ae_i = \lambda_i e_i \) и \( A^*e_i = \overline{\lambda}_i e_i \). Пусть \( U = \operatorname{diag}(d_1, \ldots, d_n) \), где \( d_i = \overline{\lambda}_i / \lambda_i \) при \( \lambda_i \neq 0 \) и \( d_i = 1 \) при \( \lambda_i = 0 \). Тогда \( A^* = AU \).

25.2. Пусть \( A = U\Lambda U^* \), где \( U \) — унитарная матрица, \( \Lambda = \operatorname{diag}(\lambda_1, \ldots, \lambda_n) \). Тогда
\[
B = UDU^*, \quad \text{где } D = \operatorname{diag}(\pm \sqrt{\lambda_1}, \ldots, \pm \sqrt{\lambda_n}).
\]

25.3. По условию \( \operatorname{Im} B \subset (\operatorname{Im} A)^{\perp} = \operatorname{Ker} A^* \), т. е. \( A^*B = 0 \). Аналогично \( B^*A = 0 \). Поэтому \( (A^* + B^*)(A + B) = A^*A + B^*B \). Учитывая, что для нормального оператора \( \operatorname{Ker} A = \operatorname{Ker} A^* \) и \( \operatorname{Im} A = \operatorname{Im} A^* \), аналогично получаем \( (A + B)(A^* + B^*) = AA^* + BB^* \).

25.4. Рассмотрим ортонормированный базис, в котором оператор \( A \) диагонален. Можно считать, что \( A = \operatorname{diag}(d_1, \ldots, d_k, 0, \ldots, 0) \), причём \( d_i \neq 0 \). Тогда
\[
S = \operatorname{diag}(|d_1|, \ldots, |d_k|, 0, \ldots, 0).
\]
Пусть \( D = \operatorname{diag}(d_1, \ldots, d_k) \) и \( D_+ = \operatorname{diag}(|d_1|, \ldots, |d_k|) \). Равенство
\[
\begin{pmatrix}
D & 0 \\
0 & 0
\end{pmatrix}
=
\begin{pmatrix}
D_+ & 0 \\
0 & 0
\end{pmatrix}
\begin{pmatrix}
U_1 & U_2 \\
U_3 & U_4
\end{pmatrix}
=
\begin{pmatrix}
D_+U_1 & D_+U_2 \\
0 & 0
\end{pmatrix}
\]
выполняется, только если \( U_1 = D_+^{-1}D = \operatorname{diag}(e^{i\varphi_1}, \ldots, e^{i\varphi_k}) \), поэтому матрица \( \begin{pmatrix} U_1 & U_2 \\ U_2 & U_4 \end{pmatrix} \) унитарна, только если \( U_2 = 0 \) и \( U_3 = 0 \). Ясно, что
\[
\begin{pmatrix}
D_+ & 0 \\
0 & 0
\end{pmatrix}
\begin{pmatrix}
U_1 & 0 \\
0 & U_4
\end{pmatrix}
=
\begin{pmatrix}
U_1 & 0 \\
0 & U_4
\end{pmatrix}
\begin{pmatrix}
D_+ & 0 \\
0 & 0
\end{pmatrix}.
\]

25.5. Матрица \( X \) нормальна тогда и только тогда, когда \( \operatorname{tr}(X^*X) = \cdot |\lambda_i|^2 \), где \( \lambda_i \) — собственные значения матрицы \( X \) (теорема 37.1.1).
Кроме того, собственные значения матриц \( X = AB \) и \( Y = BA \) совпадают (теорема 13.6.1). Остаётся проверить, что \( \operatorname{tr}(X^*X) = \operatorname{tr}(Y^*Y) \). Это легко сделать, если учесть, что \( A^*A = AA^* \) и \( B^*B = BB^* \).