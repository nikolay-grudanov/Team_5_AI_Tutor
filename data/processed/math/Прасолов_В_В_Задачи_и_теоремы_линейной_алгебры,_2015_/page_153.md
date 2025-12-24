---
source_image: page_153.png
page_number: 153
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.42
tokens: 6764
characters: 2609
timestamp: 2025-12-24T08:11:54.445095
finish_reason: stop
---

матрица, причём длина проекции вектора \( e_i \) на подпространство \( W \) равна \( d \) тогда и только тогда, когда

\[
y_{1i}^2 + \ldots + y_{mi}^2 = \frac{x_{1i}^2 + \ldots + x_{mi}^2}{d_i^2} = \frac{d^2}{d_i^2}.
\]

Если требуемое подпространство \( W \) существует, то \( d \leq d_i \) и \( m = \sum_{k=1}^m \sum_{i=1}^n y_{ki}^2 = \sum_{i=1}^n \sum_{k=1}^m y_{ki}^2 = d^2 \left( \sum_{i=1}^n \frac{1}{d_i^2} \right) \leq d^2 \left( \frac{1}{d_1^2} + \ldots + \frac{1}{d_n^2} \right). \)

Предположим теперь, что \( m \leq d_i^2 \left( \frac{1}{d_1^2} + \ldots + \frac{1}{d_n^2} \right) \) при \( i = 1, \ldots, n \) и построим ортогональную матрицу \( \| y_{ki} \|_1^n \), обладающую свойством (1), где

\[
d^2 = \frac{m}{\frac{1}{d_1^2} + \ldots + \frac{1}{d_n^2}};
\]

подпространство \( W \) после этого строится очевидным образом. Индукцией по \( n \) докажем, что если \( 0 \leq \beta_i \leq 1 \) при \( i = 1, \ldots, n \) и \( \beta_1 + \ldots + \beta_n = m \), то существует такая ортогональная матрица \( \| y_{ki} \|_1^n \), что \( y_{1i}^2 + \ldots + y_{mi}^2 = \beta_i \). При \( n = 1 \) утверждение очевидно. Предположим, что утверждение верно для \( n - 1 \) и докажем его для \( n \). Рассмотрим два случая.

а) \( m \leq n/2 \). Можно считать, что \( \beta_1 \geq \ldots \geq \beta_n \). Тогда \( \beta_{n-1} + \beta_n \leq 2m/n \leq 1 \), а значит, существует такая ортогональная матрица \( A = \| a_{ki} \|_1^{n-1} \), что \( a_{1i}^2 + \ldots + a_{mi}^2 = \beta_i \) при \( i = 1, \ldots, n-2 \) и \( a_{1,n-1}^2 + \ldots + a_{m,n-1}^2 = \beta_{n-1} + \beta_n \). Тогда матрица

\[
\| y_{ki} \|_1^n = \begin{pmatrix}
a_{11} & \ldots & a_{1,n-2} & \alpha_1 a_{1,n-1} & -\alpha_2 a_{1,n-1} \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
a_{n-1,1} & \ldots & a_{n-1,n-2} & \alpha_1 a_{n-1,n-1} & -\alpha_2 a_{n-1,n-1} \\
0 & \ldots & 0 & \alpha_2 & \alpha_1
\end{pmatrix},
\]

где \( \alpha_1 = \sqrt{\frac{\beta_{n-1}}{\beta_{n-1} + \beta_n}} \) и \( \alpha_2 = \sqrt{\frac{\beta_n}{\beta_{n-1} + \beta_n}} \), ортогональна по столбцам, \( \sum_{k=1}^m y_{ki}^2 = \beta_i \) при \( i = 1, \ldots, n-2 \), \( y_{1,n-1}^2 + \ldots + y_{m,n-1}^2 = \alpha_1^2 (\beta_{n-1} + \beta_n) = \beta_{n-1} \) и \( y_{1n}^2 + \ldots + y_{mn}^2 = \alpha_2^2 (\beta_{n-1} + \beta_n) = \beta_n \). Кроме того, столбцы ортонормированы.

б) Пусть \( m > n/2 \). Тогда \( n - m \leq n/2 \), поэтому существует такая ортогональная матрица \( \| y_{ki} \|_1^n \), что \( y_{m+1,i}^2 + \ldots + y_{ni}^2 = 1 - \beta_i \) при \( i = 1, \ldots, n \), а значит, \( y_{1i}^2 + \ldots + y_{mi}^2 = \beta_i \).