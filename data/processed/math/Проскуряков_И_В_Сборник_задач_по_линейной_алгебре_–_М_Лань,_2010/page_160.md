---
source_image: page_160.png
page_number: 160
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.54
tokens: 5548
characters: 2140
timestamp: 2025-12-24T07:08:58.056431
finish_reason: stop
---

матрица \( A_p \), определенная в предыдущей задаче, также была треугольной с нулями по ту же сторону от диагонали.

*971. Пользуясь свойствами ассоциированных матриц, доказать, что если \( A \) — квадратная матрица порядка \( n \), то \( |A_p| = |A|^{C_{n-1}^{p-1}} \) (см. задачу 551).

*972. Пусть \( A \) — неособенная матрица порядка \( n \) и \( B = A^{-1} \) — матрица, обратная для \( A \). Доказать, что миноры любого порядка обратной матрицы выражаются через миноры исходной матрицы следующим образом:

\[
B \left( \begin{array}{c}
i_1, i_2, \ldots, i_p \\
k_1, k_2, \ldots, k_p
\end{array} \right) = \frac{(-1)^{\sum_{s=1}^p (i_s + k_s)} A \left( \begin{array}{c}
k'_1, k'_2, \ldots, k'_{n-p} \\
i'_1, i'_2, \ldots, i'_{n-p}
\end{array} \right)}{|A|},
\]

где \( i_1 < i_2 < \cdots < i_p \) вместе с \( i'_1 < i'_2 < \cdots < i'_{n-p} \) и \( k_1 < k_2 < \cdots < k_p \) вместе с \( k'_1 < k'_2 < \cdots < k'_{n-p} \) составляют полную систему индексов \( 1, 2, \ldots, n \).

*973. Доказать, что \( p \)-я ассоциированная матрица \( A_p \) (определение дано в задаче 969) для ортогональной матрицы \( A \) сама ортогональна.

*974. Доказать, что \( p \)-я ассоциированная матрица \( A_p \) для унитарной матрицы \( A \) сама унитарна.

§ 13. ПОЛИНОМИАЛЬНЫЕ МАТРИЦЫ

Следующие \( \lambda \)-матрицы привести к нормальной диагональной форме путем элементарных преобразований:

975. \( \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix} \).
976. \( \begin{pmatrix} \lambda^2 - 1 & \lambda - 1 \\ \lambda + 1 & \lambda^2 + 2\lambda + 1 \end{pmatrix} \).
977. \( \begin{pmatrix} \lambda & 0 \\ 0 & \lambda + 5 \end{pmatrix} \).
978. \( \begin{pmatrix} \lambda^2 - 1 & 0 \\ 0 & (\lambda - 1)^3 \end{pmatrix} \).
979. \( \begin{pmatrix} \lambda + 1 & \lambda^2 + 1 & \lambda^2 \\ 3\lambda - 1 & 3\lambda^2 - 1 & \lambda^2 + 2\lambda \\ \lambda - 1 & \lambda^2 - 1 & \lambda \end{pmatrix} \).
980. \( \begin{pmatrix} \lambda^2 & \lambda^2 - \lambda & 3\lambda^2 \\ \lambda^2 - \lambda & 3\lambda^2 - \lambda & \lambda^3 + 4\lambda^2 - 3\lambda \\ \lambda^2 + \lambda & \lambda^2 + \lambda & 3\lambda^2 + 3\lambda \end{pmatrix} \).