---
source_image: page_504.png
page_number: 504
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.57
tokens: 6820
characters: 2836
timestamp: 2025-12-24T08:21:19.823255
finish_reason: stop
---

А так как \( \bar{v}v = v\bar{v} \) и \( u + \bar{u} \) — действительные числа, то

\[
a(u^2 - \bar{v}v) - (\overline{v\bar{u}} + \overline{vu})b = au^2 - a\bar{v}v - (u + \bar{u})\bar{v}b =
\]
\[
= au^2 - \bar{v}va - \bar{v}b(u + \bar{u}) = (au - \bar{v}b)u - \bar{v}(b\bar{u} + va),
\]
\[
b(u^2 - \bar{v}v) + (v\bar{u} + vu)a = b\bar{u}^2 - b\bar{v}v + v(\bar{u} + u)a =
\]
\[
= b\bar{u}^2 - v\bar{v}b + va(\bar{u} + u) = (b\bar{u} + va)\bar{u} + v(au - \bar{v}b).
\]

Равенство \( x(xy) = (xx)y \) доказывается аналогично.

б) Рассмотрим трилинейное отображение \( f(a, x, y) = (ax)y - a(xy) \). Подставив \( b = x + y \) в равенство \( (ab)b = a(bb) \) и учитя, что \( (ax)x = a(xx) \) и \( (ay)y = a(yy) \), получим \( (ax)y - a(yx) = a(xy) - (ay)x \), т. е. \( f(a, x, y) = -f(a, y, x) \). Аналогично, подставив \( b = x + y \) в равенство \( b(ba) = (bb)a \), получим \( f(x, y, a) = -f(y, x, a) \). Значит, \( f(a, x, y) = -f(a, y, x) = f(y, a, x) = -f(y, x, a) \), т. е. \( (ax)y + (yx)a = a(xy) + y(xa) \). При \( a = y \) получаем \( (yx)y = y(xy) \).

§ 47. Матричные алгебры

47.1. Так как \( A_i S = \bullet \quad A_j A_j = \bullet \quad A_k = S \), то \( S^2 = \bullet \quad A_i S = nS \). Поэтому все собственные значения матрицы \( S \) равны 0 или \( n \), а так как \( \operatorname{tr} S = 0 \), то все собственные значения равны 0. Следовательно, матрица \( S - nI \) невырождена и из равенства \( S(S - nI) = 0 \) получаем \( S = 0 \).

§ 48. Конечные поля

48.1. Легко проверить, что \( 2|A| = 0 \) (см. задачу 1.1). Для поля нечётной характеристики из этого равенства следует, что \( |A| = 0 \).

Для поля характеристики 2 аналогичное утверждение неверно; в этом случае, например, единичная матрица является кососимметрической.

48.2. Матрицы

\[
X = \begin{pmatrix}
0 & 1 & 0 & \ldots & 0 \\
0 & 0 & 1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & 1 \\
0 & 0 & 0 & \ldots & 0
\end{pmatrix}
\text{ и }
Y = \begin{pmatrix}
0 & 0 & 0 & \ldots & 0 \\
1 & 0 & 0 & \ldots & 0 \\
0 & 2 & 0 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & \ldots & p-1 & 0
\end{pmatrix}
\]

удовлетворяют требуемому соотношению.

48.3. Первое решение. Пусть \( f(x) = \det(xI - A) \), где \( I \) — единичная матрица. Любому многочлену \( f \) с целыми коэффициентами соответствует многочлен \( \bar{f} \) над полем \( \mathbb{F}_p \) (конечное поле из \( p \) элементов). Присоединим к \( \mathbb{F}_p \) корни \( x_1, \ldots, x_n \) многочлена \( \bar{f} \). В результате получим поле \( \mathbb{F}_{p^k} \).

Для любых элементов \( x, y \in \mathbb{F}_{p^k} \) выполняется равенство \( (x + y)^p = x^p + y^p \), поскольку \( \binom{p}{m} \equiv 0 \pmod{p} \) при \( m = 1, 2, \ldots, p-1 \). Поэтому
\[
x_1^p + \ldots + x_n^p = (x_1 + \ldots + x_n)^p = x_1 + \ldots + x_n
\]