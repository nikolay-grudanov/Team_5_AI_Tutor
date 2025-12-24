---
source_image: page_253.png
page_number: 253
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.60
tokens: 6762
characters: 3045
timestamp: 2025-12-24T08:14:29.668988
finish_reason: stop
---

б) Первый столбец матрицы \((S^{-1}AS)^T = S^TA^T(S^T)^{-1}\) имеет вид

\[(\lambda, 0, 0, \ldots, 0),\]

поэтому можно воспользоваться результатом задачи а).

13.9. Легко проверить, что \(|A - \lambda I| = \sum_{k=0}^{n} (-1)^k \lambda^k \Delta_{n-k}(A)\), где \(\Delta_m(A)\) — сумма всех главных миноров порядка \(m\) матрицы \(A\). Поэтому \(\prod_{i=1}^{n} |A_i - \lambda I| = \prod_{i=1}^{n} \prod_{k=0}^{n-1} (-1)^k \lambda^k \Delta_{n-k-1}(A_i)\). Остаётся заметить, что \(\prod_{i=1}^{n} \Delta_p(A_i) = (n-p)\Delta_p(A)\).
В самом деле, любой главный минор порядка \(p\) матрицы \(A\) является главным минором для \(n-p\) матриц \(A_i\).

13.10. Так как \(\operatorname{adj}(P^{-1}XP) = P^{-1}(\operatorname{adj} X)P\), то можно считать, что матрица \(A\) жорданова. В этом случае матрица \(\operatorname{adj} A\) верхняя треугольная (см. задачу 2.8); её диагональные элементы легко вычисляются.

13.11. Пусть \(S = \|\delta_{i,n-j}\|_0^n\) — матрица с единичной побочной диагональю. Тогда \(AS = \|b_{ij}\|_0^n\) и \(SA = \|c_{ij}\|_0^n\), где \(b_{ij} = a_{i,n-j}\) и \(c_{ij} = a_{n-i,j}\). Поэтому центральная симметричность матрицы \(A\) означает, что \(AS = SA\). Легко проверить также, что вектор \(x\) симметричен, если \(Sx = x\), и антисимметричен, если \(Sx = -x\).

Пусть \(\lambda\) — собственное значение матрицы \(A\) и \(Ay = \lambda y\), где \(y \neq 0\). Тогда \(A(Sy) = S(Ay) = S(\lambda y) = \lambda S(y)\). Если \(Sy = -y\), то можно положить \(x = y\). Если \(Sy \neq -y\), то можно положить \(x = y + Sy\); тогда \(Ax = \lambda x\) и \(Sx = x\).

13.12. а)
\[
\begin{vmatrix}
A-\lambda I & B \\
B & A-\lambda I
\end{vmatrix}
\cdot
\begin{vmatrix}
I & I \\
I & -I
\end{vmatrix}
=
\begin{vmatrix}
A+B-\lambda I & A-B-\lambda I \\
A+B-\lambda I & -(A-B-\lambda I)
\end{vmatrix}
=
\begin{vmatrix}
A+B-\lambda I & A-B-\lambda I \\
0 & -2(A-B-\lambda I)
\end{vmatrix}.
\]

б)
\[
\begin{vmatrix}
A-\lambda I & B \\
-B & A-\lambda I
\end{vmatrix}
\cdot
\begin{vmatrix}
I & iI \\
iI & I
\end{vmatrix}
=
\begin{vmatrix}
A+iB-\lambda I & i(A-iB-\lambda I) \\
i(A+iB-\lambda I) & A-iB-\lambda I
\end{vmatrix}
=
\begin{vmatrix}
A+iB-\lambda I & i(A-iB-\lambda I) \\
0 & 2(A-iB-\lambda I)
\end{vmatrix}.
\]

в) \[
\left(
\begin{array}{cc}
A & B \\
B & -A
\end{array}
\right)^2 =
\left(
\begin{array}{cc}
A^2 + B^2 & AB - BA \\
BA - AB & A^2 + B^2
\end{array}
\right),
\]
поэтому можно воспользоваться результатом задачи б).

13.13. Так как \(Ae_i = x_{n-i+1}e_{n-i+1}\) и \(Ae_{n-i+1} = x_ie_i\), то подпространства \(V_i = \langle e_i, e_{n-i+1} \rangle\) инвариантны относительно оператора \(A\). При \(i \neq n-i+1\) матрица ограничения оператора \(A\) на подпространство \(V_i\) имеет вид \(B = \begin{pmatrix} 0 & \lambda \\ \mu & 0 \end{pmatrix}\).

Собственные значения матрицы \(B\) равны \(\pm \sqrt{\lambda \mu}\). Если \(\lambda \mu = 0\) и \(B\) диагонализируема, то \(B = 0\). Поэтому матрица \(B\) диагонализируема тогда и только тогда, когда оба числа \(\lambda\) и \(\mu\) равны или не равны нулю одновременно.