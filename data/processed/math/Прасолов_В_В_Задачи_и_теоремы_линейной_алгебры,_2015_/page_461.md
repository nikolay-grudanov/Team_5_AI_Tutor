---
source_image: page_461.png
page_number: 461
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.47
tokens: 6659
characters: 2503
timestamp: 2025-12-24T08:20:12.293200
finish_reason: stop
---

Ясно также, что коэффициент многочлена \( f(x)g(y) - f(y)g(x) \) при \( x^\alpha y^\beta - x^\beta y^\alpha \) равен \( a_{n-\alpha} b_{n-\beta} - a_{n-\beta} b_{n-\alpha} \). Поэтому

\[
\frac{f(x)g(y) - f(y)g(x)}{x - y}
\]

— многочлен, причём если \( p \geq q \), то его коэффициент при \( x^p y^q \) равен
• \( (a_{n-\alpha} b_{n-\beta} - a_{n-\beta} b_{n-\alpha}) \), где суммирование ведётся по таким парам \( (\alpha, \beta) \), что \( p + q = \beta + \alpha - 1 \), причём \( \alpha \leq n \) и \( \beta \leq q \), т. е. \( p + 1 \leq \alpha \leq n \). Результат суммирования не изменится, если нижнюю границу заменить на \( \max(p + 1, q + 1) \). Остаётся заметить, что коэффициенты при \( x^p y^q \) и \( x^q y^p \) равны и \( z_{p+1, q+1} = c_{n-\alpha, n-\beta} \), где \( n - \alpha + n - \beta = 2n - p - q - 1 \), т. е. \( \alpha + \beta = p + q + 1 \), и \( 0 \leq n - \alpha \leq \min(n - p - 1, n - q - 1) \), т. е. \( \max(p + 1, q + 1) \leq \alpha \leq n \).

49.4. Понижение порядка матрицы для вычисления результанта

Опишем ещё один способ понижения порядка матрицы для вычисления результанта. Для простоты будем считать, что \( a_0 = 1 \), т. е. \( f(x) = x^n + a_1 x^{n-1} + \ldots + a_n \) и \( g(x) = b_0 x^m + b_1 x^{m-1} + \ldots + b_m \). Рассмотрим матрицу

\[
A = \begin{pmatrix}
0 & 1 & 0 & \ldots & 0 \\
0 & 0 & 1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & 1 \\
-a_n & -a_{n-1} & -a_{n-2} & \ldots & -a_1
\end{pmatrix}.
\]

Теорема 49.4.1. Пусть \( R = g(A) \). Тогда \( \det R = R(f, g) \).

Доказательство. Пусть \( \alpha_i \) и \( \beta_i \) — корни многочленов \( f \) и \( g \). Тогда \( g(x) = b_0 (x - \beta_1) \ldots (x - \beta_m) \). Поэтому \( g(A) = b_0 (A - \beta_1 I) \ldots (A - \beta_m I) \). А так как \( |A - \lambda I| = \div \sum_{i} (\alpha_i - \lambda) \) (см. п. 1.5), то

\[
\det g(A) = b_0^m \div_{i, j} (\alpha_i - \beta_j) = R(f, g).
\]

Теорема 49.4.2. При \( m \leq n \) матрицу \( R \) можно вычислять следующим рекуррентным способом. Пусть \( r_1, \ldots, r_n \) — строки матрицы \( R \). Тогда \( r_1 = (b_m, b_{m-1}, \ldots, b_1, b_0, 0, \ldots, 0) \) при \( m < n \), а если \( m = n \), то \( r_1 = (d_n, \ldots, d_1) \), где \( d_i = b_i - b_0 a_i \). Кроме того, \( r_i = r_{i-1} A \) для \( i = 2, \ldots, n \).

Доказательство. Пусть \( e_i = (0, \ldots, 1, \ldots, 0) \), где 1 стоит на \( i \)-м месте. При \( k < n \) первая строка матрицы \( A^k \) равна \( e_{k+1} \). Поэтому строение