---
source_image: page_391.png
page_number: 391
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.69
tokens: 6578
characters: 2343
timestamp: 2025-12-24T08:18:16.094396
finish_reason: stop
---

Поэтому

\[
(\operatorname{tr} \Lambda + \operatorname{tr} C)^2 - 4 \operatorname{tr}(\Lambda C) =
= (\lambda_1 + c_{11})^2 + \ldots + (\lambda_n + c_{nn})^2 + 2 \sum_{i \neq j} \lambda_i c_{jj} - 4\lambda_1 c_{11} - \ldots - 4\lambda_n c_{nn} >
> (\lambda_1 - c_{11})^2 + \ldots + (\lambda_n - c_{nn})^2 \geqslant 0.
\]

37.8. Если матрица \( A \) невырожденная, то достаточно заметить, что

\[
A^*A = A^{-1}(AA^*)A.
\]

В случае вырожденной матрицы можно воспользоваться полярным разложением \( A = SU \) (теорема 18.1.1); здесь матрица \( S \) эрмитова, а \( U \) унитарная. Ясно, что \( AA^* = SUU^*S = S^2 \) и \( A^*A = U^*SSU = U^{-1}S^2U \).

37.9. Собственные значения эрмитовой матрицы \( A^*A \) равны, поэтому \( A^*A = tI \), где \( t \in \mathbb{R} \). Следовательно, матрица \( U = \frac{1}{\sqrt{t}}A \) унитарная.

37.10. Достаточно применить результат задачи 13.10 к матрице \( A^*A \).

37.11. Достаточно заметить, что
\[
\begin{vmatrix}
-\lambda I & A \\
A^* & -\lambda I
\end{vmatrix} = |\lambda^2 I - A^*A| = \pm |A^*A - \lambda^2 I|
\]
(см. теорему 3.1.2).

37.12. Запишем матрицу \( A \) в блочном виде:
\[
A = \begin{pmatrix} 0 & I_{n-1} \\ a_0 & d \end{pmatrix},
\]
где \( d = (a_1, \ldots, a_{n-1}) \). Тогда
\[
AA^* = \begin{pmatrix} 0 & I_{n-1} \\ a_0 & d \end{pmatrix} \begin{pmatrix} 0 & \overline{a}_0 \\ I_{n-1} & d^* \end{pmatrix} = \begin{pmatrix} I_{n-1} & d^* \\ d & |a_0|^2 + \|d\|^2 \end{pmatrix}.
\]
Поэтому согласно теореме 3.1.4 характеристический многочлен матрицы \( AA^* \) равен
\[
(|a_0|^2 + \ldots + |a_{n-1}|^2 - \lambda)(1 - \lambda)^{n-1} - d \operatorname{adj}((1 - \lambda)I_{n-1})d^*.
\]
Согласно теореме 2.5.1 (в) \( \operatorname{adj}((1 - \lambda)I_{n-1}) = (1 - \lambda)^{n-2}I_{n-1} \). Деля характеристический многочлен на \( (1 - \lambda)^{n-2} \), после несложных вычислений получаем требуемое.

37.13. Рассмотрим матрицу \( \Lambda^m C = (\Lambda^m A)(\Lambda^m B) \). Здесь \( \Lambda^m C \) и \( \Lambda^m B \) — столбцы длиной \( \binom{n}{m} \), а \( \Lambda^m A \) — квадратная матрица порядка \( \binom{n}{m} \). Согласно теореме 37.4.1
\[
\sigma_{\min} \|\Lambda^m B\| \leqslant \|(\Lambda^m A)(\Lambda^m B)\| \leqslant \sigma_{\max} \|\Lambda^m B\|,
\]
где \( \sigma_{\max} \) и \( \sigma_{\min} \) — наибольшее и наименьшее сингулярные значения матрицы \( \Lambda^m A \).