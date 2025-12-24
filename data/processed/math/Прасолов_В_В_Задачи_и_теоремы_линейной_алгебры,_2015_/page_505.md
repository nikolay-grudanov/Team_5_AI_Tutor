---
source_image: page_505.png
page_number: 505
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.84
tokens: 6918
characters: 3330
timestamp: 2025-12-24T08:21:25.761203
finish_reason: stop
---

(второе равенство следует из того, что \( x_1 + \ldots + x_n \in \mathbb{F}_p \)). Но \( x_1 + \ldots + x_n = \operatorname{tr} A \ (\operatorname{mod}\ p) \) и \( (x_1 + \ldots + x_n)^p = \operatorname{tr}(A^p) \ (\operatorname{mod}\ p) \). Первое равенство очевидно, а второе следует из того, что если \( f(x) = (x - \lambda_1) \ldots (x - \lambda_n) \), то \( \lambda_1^p + \ldots + \lambda_n^p \) выражается как многочлен с целыми коэффициентами через коэффициенты многочлена \( f \), причём \( x_1^p + \ldots + x_n^p \) выражается через коэффициенты многочлена \( \bar{f} \) точно так же.

Второе решение. Докажем сначала, что если \( A \) и \( B \) — матрицы с целочисленными элементами, то \( \operatorname{tr}(A + B)^p \equiv (\operatorname{tr} A^p + \operatorname{tr} B^p) \ (\operatorname{mod}\ p) \). Если из выражения для \( (A + B)^p \) исключить матрицы \( A^p \) и \( B^p \), то все остальные мономы разбиваются на наборы по \( p \) мономов в каждом, причём все мономы в одном наборе имеют один и тот же след. А именно, каждый набор состоит из матриц \( A_1 A_2 \ldots A_p, A_2 A_3 \ldots A_p A_1, \ldots, A_p A_1 A_2 \ldots A_{p-1} \), где \( A_i = A \) или \( B \). Ясно, что любые два таких набора либо совпадают, либо не пересекаются. Кроме того, \( \operatorname{tr} A_1 (A_2 \ldots A_p) = \operatorname{tr}(A_2 \ldots A_p) A_1 = \ldots \)

Индукцией по \( n \) теперь легко получить сравнение \( \operatorname{tr}(X_1 + \ldots + X_n)^p \equiv \equiv (\operatorname{tr} X_1^p + \ldots + \operatorname{tr} X_n^p) \ (\operatorname{mod}\ p) \).

Представим матрицу \( A \) в виде \( A = X_1 + \ldots + X_n \), где каждая матрица \( X_i \) имеет ровно один ненулевой элемент. Для такой матрицы имеет место сравнение \( \operatorname{tr}(X_i^p) \equiv \operatorname{tr} X_i \ (\operatorname{mod}\ p) \). Действительно, если ненулевой элемент расположен вне диагонали, то \( \operatorname{tr}(X_i^p) = 0 \) и \( \operatorname{tr} X_i = 0 \). А если ненулевой элемент расположен на диагонали и равен \( a \), то \( \operatorname{tr}(X_i^p) = a^p \) и \( \operatorname{tr} X_i = a \). Но \( a^p \equiv a \ (\operatorname{mod}\ p) \) согласно малой теореме Ферма.

§ 49. Результант

49.1. Пусть \( c_0, \ldots, c_{n+m-1} \) — столбцы матрицы Сильвестра \( S(f, g) \) и \( y_k = x^{m+n-k-1} \). Тогда \( y_0 c_0 + \ldots + y_{n+m-1} c_{n+m-1} = c \), где \( c \) — столбец
\[
(x^{m-1} f(x), \ldots, f(x), x^{n-1} g(x), \ldots, g(x)).
\]
Рассмотрим это равенство как систему линейных уравнений относительно \( y_0, \ldots, y_{n+m-1} \) и применим для нахождения \( y_{n+m-1} \) правило Крамера. В результате получим
\[
y_{n+m-1} \det(c_0, \ldots, c_{n+m-1}) = \det(c_0, \ldots, c_{n+m-2}, c).
\] (1)
Остаётся заметить, что \( y_{n+m-1} = 1 \), \( \det(c_0, \ldots, c_{n+m-1}) = R(f, g) \), а определитель, стоящий в правой части равенства (1), можно представить в требуемом виде.

49.2. Согласно теореме 49.2.1 \( R(f, g) = a_0^m \div g(x_i) \) и \( R(f, r) = a_0^k \div r(x_i) \). Кроме того, \( f(x_i) = 0 \), поэтому \( g(x_i) = f(x_i) q(x_i) + r(x_i) = r(x_i) \).

49.3. Пусть \( c_0, \ldots, c_{n+m-1} \) — столбцы матрицы Сильвестра \( S(f, g) \) и \( y_k = x^{n+m-k-1} \). Тогда \( y_0 c_0 + \ldots + y_{n+m-1} c_{n+m-1} = c \), где \( c \) — столбец
\[
(x^{m-1} f(x), \ldots, f(x), x^{n-1} g(x), \ldots, g(x)).
\]