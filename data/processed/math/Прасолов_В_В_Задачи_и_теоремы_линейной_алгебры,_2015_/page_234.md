---
source_image: page_234.png
page_number: 234
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.61
tokens: 6502
characters: 2307
timestamp: 2025-12-24T08:13:58.513326
finish_reason: stop
---

Теорема 15.4.2. Если в характеристическом многочлене \( f(x_1, \ldots, x_m) \) заменить \( x^z \) на \( A^z \), то получим нулевую матрицу.

Доказательство [Wa]. Пусть \( \operatorname{adj} B(x_1, \ldots, x_m) = \bullet_{z} B_z x^z \), где элементы матриц \( B_z \) не зависят от \( x \). Из равенства \( f(x_1, \ldots, x_m) \cdot I = |B| \cdot I = (\operatorname{adj} B)B \) получаем

\[
\bullet_{z} b_z x^z I = \left( \bullet_{z} B_z x^z \right) \left( A - \bullet_{i=1}^{m} x_i I^{\delta(i)} \right).
\]

Так как \( \bullet_{i=1}^{m} I^{\delta(i)} = I \), то \( x^z A = \bullet_{i=1}^{m} I^{\delta(i)} x^z A \), а значит,

\[
\bullet_{z} b_z x^z I = \bullet_{z} B_z \bullet_{i=1}^{m} I^{\delta(i)} (A x^z - x^{z+\delta(i)}).
\]

Поэтому \( b_z I = \bullet_{i=1}^{m} (B_z I^{\delta(i)} A - B_{z-\delta(i)} I^{\delta(i)}) \). Следовательно, если \( x^z \) заменить на \( A^z \), то получим матрицу \( \bullet_{z} B_z \bullet_{i=1}^{m} I^{\delta(i)} (A A^z - A^{z+\delta(i)}) \). Пусть \( J_z = \bullet_{i=1}^{m} I^{\delta(i)} (A A^z - A^{z+\delta(i)}) \). Достаточно доказать, что \( J_z = 0 \). По определению \( A^{z+\delta(i)} = \bullet_{j=1}^{m} A^{\delta(j)} A^{z+\delta(i)-\delta(j)} \), а так как \( I^{\delta(i)} A^{\delta(j)} = \delta_{ij} A^{\delta(i)} = \delta_{ij} I^{\delta(i)} A \), то получаем

\[
\bullet_{i=1}^{m} I^{\delta(i)} A^{z+\delta(i)} = \bullet_{i,j=1}^{m} \delta_{ij} I^{\delta(i)} A A^{z+\delta(i)-\delta(j)} = \bullet_{i=1}^{m} I^{\delta(i)} A A^z.
\]

Задачи

15.1. Пусть \( A \) — матрица порядка \( n \); \( f_1(A) = A - (\operatorname{tr} A)I \), \( f_{k+1}(A) = = f_k(A)A - \frac{1}{k+1} \operatorname{tr}(f_k(A)A)I \). Докажите, что \( f_n(A) = 0 \).

15.2. Пусть \( A \) и \( B \) — матрицы порядка \( n \). Докажите, что если \( \operatorname{tr} A^m = = \operatorname{tr} B^m \) при \( m = 1, \ldots, n \), то собственные значения матриц \( A \) и \( B \) совпадают.

15.3. Пусть \( p_A \) — минимальный многочлен матрицы \( A \). Докажите, что если матрицы \( A \) и \( B \) не имеют общих собственных значений, то матрица \( p_A(B) \) невырожденная.

15.4. Матрица \( A \) невырождена и её минимальный многочлен \( p(\lambda) \) совпадает с характеристическим. Докажите, что минимальный многочлен матрицы \( A^{-1} \) равен \( p(0)^{-1} \lambda^n p(\lambda^{-1}) \).