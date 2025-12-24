---
source_image: page_298.png
page_number: 298
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.47
tokens: 6648
characters: 2493
timestamp: 2025-12-24T08:15:36.837824
finish_reason: stop
---

§ 24. Ортогональные матрицы и преобразование Кэли

24.1. Корни многочлена \( p(\lambda) \) таковы, что если \( z \) — корень, то и \( 1/z = \overline{z}/z\overline{z} = \overline{z} \) — тоже корень. Поэтому многочлен \( q(\lambda) = \lambda^n p(1/\lambda) \) имеет те же корни, что и \( p \) (и с теми же кратностями). Кроме того, свободный член многочлена \( p(\lambda) \) равен \( \pm 1 \), поэтому старшие коэффициенты многочленов \( p(\lambda) \) и \( q(\lambda) \) могут отличаться лишь знаком.

24.2. Пусть \( \begin{pmatrix} a & b \\ c & d \end{pmatrix} \) — унитарная матрица с определителем 1. Тогда
\[
\begin{pmatrix} \overline{a} & \overline{b} \\ \overline{c} & \overline{d} \end{pmatrix} = \begin{pmatrix} a & c \\ b & d \end{pmatrix}^{-1} = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix},
\]
т. е. \( \overline{a} = d \) и \( \overline{b} = -c \). Кроме того, \( ad - bc = 1 \), т. е. \( |a|^2 + |b|^2 = 1 \).

24.3. Рассмотрим матрицу
\[
A^{-1} = \begin{pmatrix} A_{11}^T & A_{12}^T \\ A_{21}^T & A_{22}^T \end{pmatrix}.
\]
Согласно задаче 3.3 \( \det A \det A_{22}^T = \det A_{11} \), поэтому \( \det A_{22} = \det A_{11} \).

24.4. а) Оператор \( A \) является поворотом на некоторый угол \( \varphi \), поэтому \( \operatorname{tr} A = 1 + 2 \cos \varphi \) и \( \operatorname{tr}(A^2) = 1 + 2 \cos 2\varphi = 4 \cos^2 \varphi - 1 \).
   б) Ясно, что
\[
\bullet \sum_{i<j} (a_{ij} - a_{ji})^2 = \bullet \sum_{i \neq j} a_{ij}^2 - 2 \bullet \sum_{i<j} a_{ij} a_{ji} \quad \text{и} \quad \operatorname{tr}(A^2) = \bullet \sum_i a_{ii}^2 + 2 \bullet \sum_{i<j} a_{ij} a_{ji}.
\]
С другой стороны, согласно задаче а)
\[
\operatorname{tr}(A^2) = \operatorname{tr}(A)^2 - 2 \operatorname{tr} A = (\operatorname{tr} A - 1)^2 - 1 = \left( \bullet \sum_i a_{ii} - 1 \right)^2 - 1.
\]
Поэтому
\[
\bullet \sum_{i<j} (a_{ij} - a_{ji})^2 + \left( \bullet \sum_i a_{ii} - 1 \right)^2 - 1 = \bullet \sum_{i \neq j} a_{ij}^2 + \bullet \sum_i a_{ii}^2 = 3.
\]

24.5. Введём обозначение \( \frac{A}{B} = AB^{-1} \); тогда правило сокращения выглядит следующим образом: \( \frac{AB}{CB} = \frac{A}{C} \). Если \( A^T = JA^{-1}J^{-1} \), то
\[
(A^\#)^T = \frac{I - A^T}{I + A^T} = \frac{I - JA^{-1}J^{-1}}{I + JA^{-1}J^{-1}} = \frac{J(A - I)A^{-1}J^{-1}}{J(A + I)A^{-1}J^{-1}} = \frac{J(A - I)}{J(A + I)} = -JA^\# J^{-1}.
\]
Если \( A^T = -JAJ^{-1} \), то
\[
(A^\#)^T = \frac{I - A^T}{I + A^T} = \frac{I + JAJ^{-1}}{I - JAJ^{-1}} = \frac{J(I + A)J^{-1}}{J(I - A)J^{-1}} = J(A^\#)^{-1}J^{-1}.
\]