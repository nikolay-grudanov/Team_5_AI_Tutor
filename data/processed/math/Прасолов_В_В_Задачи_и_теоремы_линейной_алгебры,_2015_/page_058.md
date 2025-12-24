---
source_image: page_058.png
page_number: 58
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.42
tokens: 6566
characters: 2206
timestamp: 2025-12-24T08:09:07.350225
finish_reason: stop
---

поэтому он полностью определяется своей степенью и многочленом \( P_a(1, x_2, \ldots, x_n) \).

Перейдём теперь к вычислению суммы коэффициентов многочлена \( P_a \). Ясно, что

\[
V_a(1, x, x^2, \ldots, x^{n-1}) = |x^{(i-1)a_j}|_1^n = |x^{(j-1)a_i}|_1^n = V(x^{a_1}, \ldots, x^{a_n}).
\]

Поэтому \( P_a(1, x, x^2, \ldots, x^{n-1})V(1, x, x^2, \ldots, x^{n-1}) = V(x^{a_1}, \ldots, x^{a_n}), \) т. е.

\[
P_a(1, x, x^2, \ldots, x^{n-1}) = \frac{V(x^{a_1}, \ldots, x^{a_n})}{V(1, x, x^2, \ldots, x^{n-1})} = \div_{i<j} \frac{x^{a_j} - x^{a_i}}{x^j - x^i}.
\]

Ясно, что

\[
\lim_{x \to 1} \frac{x^m - x^n}{x - 1} = \lim_{x \to 1} (x^{m-1} + x^{m-2} + \ldots + x + 1) = m - n.
\]

Поэтому

\[
P_a(1, 1, \ldots, 1) = \div_{i<j} \lim_{x \to 1} \frac{x^{a_j} - x^{a_i}}{x - 1} \cdot \frac{x - 1}{x^j - x^i} = \div_{i<j} \frac{a_j - a_i}{j - i}.
\]

Остаётся заметить, что \( P_a(1, 1, \ldots, 1) \) — это и есть сумма коэффициентов многочлена \( P_a \).

\(\square\)

**2.14. Теорема Чеботарёва**

С помощью теоремы Митчелла легко получить доказательство следующего утверждения.

**Теорема 2.14.1 (Чеботарёв [Ч]).** *Пусть \( p \) — простое число и \( \varepsilon = e^{2\pi i / p} \). Тогда все миноры матрицы Вандермонда \( \|a_{ij}\|_0^{p-1} \), где \( a_{ij} = \varepsilon^{ij} \), отличны от нуля.*

**Доказательство.** Любой минор рассматриваемой матрицы можно записать в виде \( |\varepsilon^{a_ib_j}|_1^n \), где \( 0 \leq a_1 < a_2 < \ldots < a_n \leq p-1 \) и \( 0 \leq b_1 < b_2 < \ldots < b_n \leq p-1 \). Таким образом, в обозначениях теоремы Митчелла нужно доказать, что \( V_a(\varepsilon^{b_1}, \ldots, \varepsilon^{b_n}) \neq 0 \). Числа \( \varepsilon^{b_1}, \ldots, \varepsilon^{b_n} \) попарно различны, поэтому \( V(\varepsilon^{b_1}, \ldots, \varepsilon^{b_n}) \neq 0 \). Следовательно, достаточно доказать, что \( P_a(\varepsilon^{b_1}, \ldots, \varepsilon^{b_n}) \neq 0 \).

Предположим, что \( P_a(\varepsilon^{b_1}, \ldots, \varepsilon^{b_n}) = 0 \). Сопоставим многочлену \( P_a(x_1, \ldots, x_n) \) многочлен \( f(x) = P_a(x^{b_1}, \ldots, x^{b_n}) \). Тогда

\[
f(\varepsilon) = P_a(\varepsilon^{b_1}, \ldots, \varepsilon^{b_n}) = 0 \quad \text{и} \quad f(1) = P_a(1, \ldots, 1).
\]