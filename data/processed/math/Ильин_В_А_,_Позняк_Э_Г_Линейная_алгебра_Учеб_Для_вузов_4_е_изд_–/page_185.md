---
source_image: page_185.png
page_number: 185
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.05
tokens: 11576
characters: 2391
timestamp: 2025-12-24T05:55:29.925762
finish_reason: stop
---

новых клеток и все ее внедиагональные элементы являются величинами порядка \( \varepsilon \) и малы по сравнению с числом \( \rho = \min |\lambda_i - \lambda_j| \), В. В. Воеводин получил следующие оценки:

а) для собственных значений оценку \( \lambda_l = a_{il} + \sum_{p=1}^n \frac{a_{lp} a_{pi}}{a_{li} - a_{pp}} + O(\varepsilon^3) \)
(из указанной суммы исключаются значения \( p \), принадлежащие множеству \( R_l \) тех чисел \( j = 1, 2, \ldots, n \), для которых \( \lambda_j = \lambda_l \));
б) если \( T \) — матрица, столбцы которой являются собственными векторами матрицы \( A \) и \( T = E + H \), где \( E \) — единичная матрица, то для элементов \( h_{ij} \) матрицы \( H \) справедливы оценки

\[
h_{ij} = \begin{cases}
0, & \text{если } \lambda_i = \lambda_j, \\
\frac{a_{ij}}{a_{jj} - a_{ii}} + O(\varepsilon^2), & \text{если } \lambda_i \neq \lambda_j.
\end{cases}
\]

Если \( A \) — комплексная эрмитова матрица, то вместо матрицы (6.31) следует взять унитарную матрицу

\[
T_{ij}(\varphi, \psi) = \begin{pmatrix}
1 & \cdots & 0 \\
\vdots & \ddots & \vdots \\
1 & \cos \varphi & -\sin \varphi e^{i\psi} \\
\vdots & \vdots & \vdots \\
\sin \varphi e^{-i\psi} & \cdots & \cos \varphi \\
0 & \cdots & 1
\end{pmatrix}
\]
(i-я строка),
(j-я строка).

При этом вместо равенства (6.34) мы приходим к равенству

\[
\sum_{k=1}^n \sum_{l=1}^n |a_{kl}|^2 = \sum_{k=1}^n \sum_{l=1}^n |a_{kl}|^2 - 2|a_{ij}|^2 +
+ 2|a_{ij}| \cdot |\cos^2 \varphi \cdot e^{i\alpha} - \sin^2 \varphi \cdot e^{i(2\psi-\alpha)} + (a_{jj} - a_{ii}) \cos \varphi \sin \varphi e^{i\psi}|^2,
\]

в котором через \( \alpha \) обозначен аргумент комплексного числа \( a_{ij} \).

Для максимального уменьшения суммы квадратов модулей внедиагональных элементов следует у матрицы (6.42) выбрать такие номера \( i \) и \( j \), чтобы элемент \( a_{ij} \) был наибольшим по модулю внедиагональным элементом матрицы \( A \), а выбор углов \( \varphi \) и \( \psi \) подчинить условию

\[
|a_{ij}| (\cos^2 \varphi \cdot e^{i\alpha} - \sin^2 \varphi \cdot e^{i(2\psi-\alpha)} + (a_{jj} - a_{ii}) \cos \varphi \cdot \sin \varphi \cdot e^{i\psi}) = 0.
\]

Последнее условие приводит к соотношениям

\[
\psi = \arg a_{ij}, \quad \tg 2\varphi = \frac{2|a_{ij}|}{a_{ii} - a_{jj}}, \quad |\varphi| < \frac{\pi}{4}.
\]

Доказательство сходимости метода вращений проводится точно так же, как и для случая вещественной матрицы.