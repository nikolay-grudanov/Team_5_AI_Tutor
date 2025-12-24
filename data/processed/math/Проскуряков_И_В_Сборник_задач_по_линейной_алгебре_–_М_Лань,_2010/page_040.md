---
source_image: page_040.png
page_number: 40
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.04
tokens: 5589
characters: 2160
timestamp: 2025-12-24T07:06:31.932090
finish_reason: stop
---

По формуле для \((n-1)\)-го члена геометрической прогрессии из равенств (2) и (3) находим

\[
D_n - \beta D_{n-1} = \alpha^{n-2}(D_2 - \beta D_1) \quad \text{и} \quad D_n - \alpha D_{n-1} = \beta^{n-2}(D_2 - \alpha D_1),
\]

откуда \(D_n = \frac{\alpha^{n-1}(D_2 - \beta D_1) - \beta^{n-1}(D_2 - \alpha D_1)}{\alpha - \beta}\), или

\[
D^n = C_1 \alpha^n + C_2 \beta^n, \quad \text{где} \quad C_1 = \frac{D_2 - \beta D_1}{\alpha (\alpha - \beta)}, \quad C_2 = -\frac{D_2 - \alpha D_1}{\beta (\alpha - \beta)}. \tag{4}
\]

Последнее выражение для \(D_n\) легко запоминается. Оно выводилось для \(n > 2\), но непосредственно проверяется для \(n = 1\) и \(n = 2\). Значение \(C_1\) и \(C_2\) можно находить не из приведенных выражений (4), а из начальных условий \(D_1 = C_1 \alpha + C_2 \beta, D_2 = C_1 \alpha^2 + C_2 \beta^2\).

Пусть теперь \(\alpha = \beta\). Равенства (2) и (3) обращаются в одно и то же

\[
D_n - \alpha D_{n-1} = \alpha (D_{n-1} - \alpha D_{n-2}),
\]

откуда

\[
D_n - \alpha D_{n-1} = A \alpha^{n-2}, \tag{5}
\]

где

\[
A = D_2 - \alpha D_1.
\]

Заменяя здесь \(n\) на \(n-1\), получим \(D_{n-1} - \alpha D_{n-2} = A \alpha^{n-3}\), откуда \(D_{n-1} = \alpha D_{n-2} + A \alpha^{n-3}\). Вставляя это выражение в равенство (5), найдем \(D_n = \alpha^2 D_{n-2} + 2A \alpha^{n-2}\). Повторяя тот же прием несколько раз, получим \(D_n = \alpha^{n-1} D_1 + (n-1)A \alpha^{n-2}\) или \(D_n = \alpha^n [(n-1)C_1 + C_2]\), где \(C_1 = \frac{A}{\alpha^2}, C_2 = \frac{D_1}{\alpha}\) (здесь \(\alpha \neq 0\), так как \(q \neq 0\)).

Пример 5: Вычислить методом рекуррентных соотношений определитель примера 2.

Представив элемент в правом нижнем углу в виде \(a_n = x + (a_n - x)\), мы можем определитель \(D_n\) разбить на сумму двух определителей:

\[
D_n = \begin{vmatrix}
a_1 & x & \ldots & x & x \\
x & a_2 & \ldots & x & x \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
x & x & \ldots & a_{n-1} & x \\
x & x & \ldots & x & x
\end{vmatrix} =
\begin{vmatrix}
a_1 & x & \ldots & x & 0 \\
x & a_2 & \ldots & x & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
x & x & \ldots & a_{n-1} & 0 \\
x & x & \ldots & x & a_n - x
\end{vmatrix}.
\]