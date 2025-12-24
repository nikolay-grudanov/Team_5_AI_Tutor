---
source_image: page_088.png
page_number: 88
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.69
tokens: 6638
characters: 2575
timestamp: 2025-12-24T08:09:59.952014
finish_reason: stop
---

числа \( p \) и \( q \) так, что \( d_{n-1}p - a_nq = d \). Рассмотрим целочисленную матрицу

\[
D = \begin{pmatrix}
D_{n-1} & a_n \\
\cdots & \cdots \\
\frac{qa_1}{d_{n-1}} & \frac{qa_2}{d_{n-1}} & \cdots & \frac{qa_{n-1}}{d_{n-1}} & p
\end{pmatrix}.
\]

Раскладывая определитель по последнему столбцу, получаем \( \det D = d_{n-1}p + + (-1)^n a_n \det E_{n-1} \), где матрица \( E_{n-1} \) получается из матрицы \( D \) вычёркиванием первой строки и последнего столбца. Если последнюю строку матрицы \( E_{n-1} \) умножить на \( \frac{d_{n-1}}{q} \) и переставить её на место первой строки (совершив при этом \( n-2 \) транспозиции), то в результате получим матрицу \( D_{n-1} \). Таким образом, \( \det E_{n-1} = (-1)^{n-2} \frac{q}{d_{n-1}} \det D_{n-1} = (-1)^{n-2}q \), поэтому \( \det D = d_{n-1}p - a_nq = d \), т. е. \( D \) — требуемая матрица.

**1.14.** Пусть \( s = x_1 + \ldots + x_n \). Тогда \( k \)-й элемент последнего столбца имеет вид \( (s - x_k)^{n-1} = (-x_k)^{n-1} + \sum_{i=0}^{n-2} p_i x_k^i \). Следовательно, прибавляя к последнему столбцу линейную комбинацию остальных столбцов с коэффициентами \( -p_0, \ldots, -p_{n-2} \), приходим к определителю

\[
\left| \begin{array}{cccc}
1 & x_1 & \ldots & x_1^{n-2} & (-x_1)^{n-1} \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
1 & x_n & \ldots & x_n^{n-2} & (-x_n)^{n-1}
\end{array} \right| = (-1)^{n-1} V(x_1, \ldots, x_n).
\]

**1.15.** Пусть \( \Delta \) — искомый определитель. Умножая первую строку на \( x_1, \ldots, n \)-ю строку на \( x_n \), получаем

\[
\sigma \Delta = \left| \begin{array}{cccc}
x_1 & x_1^2 & \ldots & x_1^{n-1} & \sigma \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
x_n & x_n^2 & \ldots & x_n^{n-1} & \sigma
\end{array} \right|,
\]

где \( \sigma = x_1 \ldots x_n \). Переставляя последний столбец нового определителя на первое место, получаем \( \sigma \Delta = (-1)^{n-1} \sigma V(x_1, \ldots, x_n) \), т. е. \( \Delta = (-1)^{n-1} V(x_1, \ldots, x_n) \) при \( \sigma \neq 0 \). Определитель \( \Delta \) непрерывно зависит от \( x_1, \ldots, x_n \), поэтому равенство остаётся справедливым и при \( \sigma = 0 \).

**1.16.** Так как \( \lambda_i^{n-k}(1 + \lambda_i^2)^k = \lambda_i^n ((1 + \lambda_i^2)/\lambda_i)^k \), то \( |a_{ik}|_0^n = \sigma^n V(\mu_0, \ldots, \mu_n) \), где \( \mu_i = \lambda_i + \frac{1}{\lambda_i} \) и \( \sigma = \lambda_0 \ldots \lambda_n \). Учитывая, что \( \mu_i - \mu_j = (\lambda_j - \lambda_i)(1 - \lambda_i \lambda_j)/\lambda_i \lambda_j \), получаем \( |a_{ik}|_0^n = \div (\lambda_j - \lambda_i)(1 - \lambda_i \lambda_j) \).