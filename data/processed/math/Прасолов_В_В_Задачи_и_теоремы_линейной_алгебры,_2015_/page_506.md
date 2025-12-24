---
source_image: page_506.png
page_number: 506
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.81
tokens: 6761
characters: 2635
timestamp: 2025-12-24T08:21:24.038538
finish_reason: stop
---

Ясно, что если \( k \leq n - 1 \), то \( x^k g(x) = \cdot \lambda_i x^i f(x) + r_k(x) \), где \( \lambda_i \) — некоторые числа и \( i \leq m - 1 \). Поэтому, прибавляя к последним \( n \) элементам столбца с линейные комбинации первых \( m \) элементов, этот столбец можно привести к виду \( (x^{m-1} f(x), \ldots, f(x), r_{n-1}(x), \ldots, r_0(x)) \). Аналогичные преобразования строк матрицы \( S(f, g) \) приводят эту матрицу к виду

\[
\begin{pmatrix}
A & B \\
0 & C
\end{pmatrix},
\quad
\text{где }
A = \begin{pmatrix}
a_0 & * \\
0 & \cdots & a_0
\end{pmatrix},
\quad
C = \begin{pmatrix}
a_{n-1,0} & \cdots & a_{n-1,n-1} \\
\cdots & \cdots & \cdots \\
a_{00} & \cdots & a_{0,n-1}
\end{pmatrix}.
\]

49.4. Рассматриваемому оператору соответствует оператор \( I_m \otimes A - B^T \otimes I_n \) (см. п. 29.6). Собственные значения этого оператора равны \( \alpha_i - \beta_j \), где \( \alpha_i \) — корни многочлена \( f \), \( \beta_j \) — корни многочлена \( g \) (см. п. 29.5). Поэтому его определитель равен \( \div (\alpha_i - \beta_j) = \pm R(f, g) \).

49.5. Легко проверить, что \( S = V^T V \), где

\[
V = \begin{pmatrix}
1 & \alpha_1 & \ldots & \alpha_1^{n-1} \\
\cdots & \cdots & \cdots & \cdots \\
1 & \alpha_n & \ldots & \alpha_n^{n-1}
\end{pmatrix}.
\]

Поэтому \( \det S = (\det V)^2 = \div (\alpha_i - \alpha_j)^2 \).

49.6. Воспользуемся теоремой 49.3.1. Ясно, что

\[
\lim_{x \to y} \frac{f(x)g(y) - f(y)g(x)}{x - y} = \lim_{\varepsilon \to 0} \frac{f(y + \varepsilon)g(y) - f(y)g(y + \varepsilon)}{\varepsilon} =
= f'(y)g(y) - f(y)g'(y).
\]

Значит, если безутиана многочленов \( f \) и \( g \) равна нулю, то \( f'g = g'f \) и \( (f/g)' = (f'g - g'f)/g^2 \equiv 0 \). Обратное утверждение очевидно.

49.7. Пусть \( z_1, \ldots, z_n \) — строки матрицы \( Z \), \( r_1, \ldots, r_n \) — строки матрицы \( R \), \( s_1, \ldots, s_n \) — строки матрицы \( TR \). Тогда

\[
s_n = r_1 = (b_n - b_0 a_n, \ldots, b_1 - b_0 a_1) = z_n
\]

И \( s_i = a_{n-i} r_1 + a_{n-i-1} r_2 + \ldots + r_{n-i+1} = a_{n-i} r_1 + (a_{n-i-1} r_1 A + \ldots + r_{n-i} A) = a_{n-i} s_n + s_{i+1} A \) при \( i = n - 1, \ldots, 2, 1 \). Поэтому остаётся проверить, что \( z_i = a_{n-i} z_n + z_{i+1} A \) при \( i = 1, 2, \ldots, n - 1 \). Ясно, что

\[
z_{ij} - a_{n-i} z_{nj} - (z_{i+1} A)_j = z_{ij} - a_{n-i} c_{0,n+1-j} - z_{i+1,j-1} + a_{n+1-j} c_{0,n-i}
\]

И \( a_{n+1-j} c_{0,n-i} - a_{n-i} c_{0,n+1-j} = c_{n+1-j,n-i} \). При \( i = j - 1, i > j - 1 \) и \( i < j - 1 \) величина \( z_{i+1,j-1} - z_{ij} \) равна соответственно 0, \( c_{n-j+1,n-i} \) и \( -c_{n-i,n-j+1} \). Поэтому \( z_{i+1,j-1} - z_{ij} = c_{n-j+1,n-i} \).