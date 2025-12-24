---
source_image: page_511.png
page_number: 511
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.22
tokens: 6699
characters: 2679
timestamp: 2025-12-24T08:21:38.895493
finish_reason: stop
---

Предположим теперь, что \( m < 0 \). Пусть \( X^{-1} = \| y_{ij} \|_1^n \). Тогда \( y_{ij} = X_{ji}/\Delta \), где \( X_{ij} \) — алгебраическое дополнение элемента \( x_{ij} \) в матрице \( X \) и \( \Delta = \det X \). Согласно теореме Якоби (теорема 2.6.3)

\[
\begin{vmatrix}
X_{i_1 j_1} & X_{i_1 j_2} \\
X_{i_2 j_1} & X_{i_2 j_2}
\end{vmatrix} = (-1)^{\sigma}
\begin{vmatrix}
x_{i_3 j_3} & \ldots & x_{i_3 j_n} \\
\ldots & \ldots & \ldots \\
x_{i_n j_3} & \ldots & x_{i_n j_n}
\end{vmatrix}
\]

и

\[
X_{i_1 j_1} = (-1)^{\sigma}
\begin{vmatrix}
x_{i_2 j_2} & \ldots & x_{i_2 j_n} \\
\ldots & \ldots & \ldots \\
x_{i_n j_2} & \ldots & x_{i_n j_n}
\end{vmatrix},
\]

где \( \sigma = \begin{pmatrix} i_1 & \ldots & i_n \\ j_1 & \ldots & j_n \end{pmatrix} \). Поэтому

\[
\begin{vmatrix}
X_{i_1 j_1} & X_{i_1 j_2} \\
X_{i_2 j_1} & X_{i_2 j_2}
\end{vmatrix} = \Delta \frac{\partial}{\partial x_{i_2 j_2}} (X_{i_1 j_1}).
\]

Следовательно, \( -X_{j\alpha} X_{\beta i} = \Delta \frac{\partial}{\partial x_{ji}} (X_{\beta \alpha}) - X_{\beta \alpha} X_{ji} = \Delta \frac{\partial}{\partial x_{ji}} (X_{\beta \alpha}) - X_{\beta \alpha} \frac{\partial}{\partial x_{ji}} (\Delta) = \Delta^2 \frac{\partial}{\partial x_{ji}} \left( \frac{X_{\beta \alpha}}{\Delta} \right) \), т. е. \( \frac{\partial}{\partial x_{ij}} y_{\alpha \beta} = -y_{\alpha j} y_{i \beta} \). А так как

\[
(X^m)_{ij} = \sum_{a, b, \ldots, q} y_{ia} y_{ab} \cdots y_{qj}
\]

и

\[
\operatorname{tr} X^m = \sum_{a, b, \ldots, q, r} y_{ra} y_{ab} \cdots y_{qr},
\]

то

\[
\frac{\partial}{\partial x_{ji}} (\operatorname{tr} X^m) =
- \sum_{a, b, \ldots, q, r} y_{rj} y_{ia} y_{ab} \cdots y_{qr} - \ldots - \sum_{a, b, \ldots, q, r} y_{ra} y_{ab} \cdots y_{qj} y_{ir} = m (X^{m-1})_{ij}.
\]

§ 56. Числовой образ оператора

56.1. Пусть \( e_i = (0, \ldots, 1, \ldots, 0)^T \), где 1 стоит на \( i \)-м месте. Тогда \( e_i^* A e_i = a_{ii} \).

56.2. Мы приведём два решения этой задачи; оба решения используют следующие факты. Согласно теореме Шура (теорема 19.1.1) квадратную матрицу \( A \) можно представить в виде \( A = U T U^* \), где \( U \) — унитарная, \( T \) — треугольная матрица. Унитарное преобразование переводит единичную сферу в единичную сферу, поэтому \( W(A) = W(T) \). Кроме того, если оператор \( A \) заменить на \( A' = \lambda A + \mu I \), то \( W(A') = \lambda W(A) + \mu \). Легко проверить, что при замене оператора \( A \) на \( U T U^* \) величина \( \sqrt{\operatorname{tr}(A^* A) - |\lambda_1|^2 - |\lambda_2|^2} \) не изменяется, а при замене на \( \lambda A + \mu I \) умножается на \( |\lambda| \). Поэтому достаточно доказать требуемое утверждение для преобразованных матриц.