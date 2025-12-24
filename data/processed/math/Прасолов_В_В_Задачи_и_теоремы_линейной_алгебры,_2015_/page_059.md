---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.75
tokens: 6292
characters: 1734
timestamp: 2025-12-24T08:08:59.044721
finish_reason: stop
---

Многочлен \( f \), как и многочлен \( P_a \), имеет целые коэффициенты. Многочлен \( x^{p-1} + x^{p-2} + \ldots + x + 1 \), корнем которого является \( \varepsilon \), неприводим (см. [П2], пример 6.2 на с. 62). Поэтому если \( f(\varepsilon) = 0 \), то \( f(x) \) делится на \( x^{p-1} + x^{p-2} + \ldots + x + 1 \). В частности, \( f(1) \) делится на \( p \). Следовательно, \( P_a(1, \ldots, 1) = \frac{a_j - a_i}{j - i} \) делится на \( p \), но при этом ни одно из чисел \( a_j - a_i \) не делится на \( p \). Получено противоречие.

Задачи

2.1. Пусть \( A \) — матрица порядка \( n \). Докажите, что \( |A + \lambda I| = \lambda^n + \sum_{k=1}^n J_k \lambda^{n-k} \), где \( J_k \) — сумма всех \( \binom{n}{k} \) главных миноров \( k \)-го порядка матрицы \( A \).

2.2. Докажите, что

\[
\begin{vmatrix}
a_{11} & \ldots & a_{1n} & x_1 \\
\cdots & \cdots & \cdots & \cdots \\
a_{n1} & \ldots & a_{nn} & x_n \\
y_1 & \ldots & y_n & 0
\end{vmatrix} = - \sum_{i,j} x_i y_j A_{ij},
\]

где \( A_{ij} \) — алгебраическое дополнение элемента \( a_{ij} \) в матрице \( \|a_{ij}\|_1^n \).

2.3. Пусть \( \|a_{ij}\|_1^n \) — симметричная матрица,

\[
A_i(x) = \sum_{s=1}^n a_{is} x_s, \quad A(x, x) = \sum_{s,t=1}^n a_{st} x_s x_t.
\]

Докажите, что если \( 1 \leq p < n \), то

\[
\begin{vmatrix}
a_{11} & \ldots & a_{1p} & A_1(x) \\
\cdots & \cdots & \cdots & \cdots \\
a_{p1} & \ldots & a_{pp} & A_p(x) \\
A_1(x) & \ldots & A_n(x) & 0
\end{vmatrix} = -A(x, x) \Delta,
\]

где \( \Delta = \begin{vmatrix} a_{11} & \ldots & a_{1p} \\ \cdots & \cdots & \cdots \\ a_{p1} & \ldots & a_{pp} \end{vmatrix} \).

2.4. Докажите, что сумма главных \( k \)-миноров матрицы \( A^T A \) равна сумме квадратов всех \( k \)-миноров матрицы \( A \).