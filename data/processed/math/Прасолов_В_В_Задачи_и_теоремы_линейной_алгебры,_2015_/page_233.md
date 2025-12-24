---
source_image: page_233.png
page_number: 233
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.79
tokens: 6416
characters: 2023
timestamp: 2025-12-24T08:13:49.606502
finish_reason: stop
---

§ 15. Минимальный многочлен и характеристический многочлен

\( p(\lambda)I \) пропорциональна единичной. Следовательно, \( p_A(X) = \sum_{k=0}^n X^k A'_k \).

Если матрица \( X \) коммутирует с \( A \) и \( A_k \), то \( p_A(X) = \left( \sum_{k=0}^{n-1} A_k X^k \right)(A - X) \). Но матрицы \( A_k \) полиномиально выражаются через \( A \) (см. задачу 2.13), поэтому если \( X \) коммутирует с \( A \), то \( X \) коммутирует с \( A_k \).

Аналог теоремы Гамильтона—Кэли можно доказать для квадратной блочной матрицы

\[
A = \begin{pmatrix}
A_{11} & \cdots & A_{1m} \\
\cdots & \cdots & \cdots \\
A_{m1} & \cdots & A_{mm}
\end{pmatrix},
\]

где \( A_{ij} \) — матрица размера \( n_i \times n_j \) (в обычную теорему Гамильтона—Кэли эта теорема превращается при \( m = 1 \)). Предварительно введём некоторые обозначения.

Пусть \( \delta(i) = (0, \ldots, 0, 1, 0, \ldots, 0) \) — набор из \( m \) цифр с единицей на \( i \)-м месте,

\[
A^{\delta(i)} = \begin{pmatrix}
A_{i1} & \cdots & A_{im} \\
0 & \cdots & 0
\end{pmatrix}.
\]

Тогда \( A = \prod_{i=1}^m A^{\delta(i)} \). Для мультииндекса \( z = (z_1, \ldots, z_m) \) индукцией по \( |z| = z_1 + \ldots + z_m \) определим \( A^z = \prod_{i=1}^m A^{\delta(i)} A^{z-\delta(i)} \); предполагается, что \( A^z = 0 \), если \( z_i < 0 \) для некоторого \( i \), и \( A^z = I \) для \( z = (0, 0, \ldots, 0) \).

Пусть, далее,

\[
I^{\delta(i)} = \begin{pmatrix}
0 & \cdots & 0 \\
\vdots & \ddots & \vdots \\
0 & I_{ii} & 0 \\
& \ddots & \\
& & 0
\end{pmatrix},
\]

где \( I_{ii} \) — единичная матрица порядка \( n_i \). Тогда \( I = \prod_{i=1}^m I^{\delta(i)} \). Рассмотрим матрицу \( B(x_1, \ldots, x_m) = A - \prod_{i=1}^m x_i I^{\delta(i)} \). Характеристическим многочленом блочной матрицы \( A \) называют многочлен

\[
f(x_1, \ldots, x_m) = |B(x_1, \ldots, x_m)| = \sum_{z_1 \ldots z_m} b_{z_1 \ldots z_m} x_1^{z_1} \ldots x_m^{z_m} = \sum_z b_z x^z
\]

(суммирование ведётся по значениям мультииндекса \( z = (z_1, \ldots, z_m) \), где \( 0 \leq z_i \leq n_i \)).