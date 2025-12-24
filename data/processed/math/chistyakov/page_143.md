---
source_image: page_143.png
page_number: 143
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.26
tokens: 5100
characters: 1437
timestamp: 2025-12-24T07:29:30.327437
finish_reason: stop
---

§ 1] ПРОИЗВОДЯЩИЕ ФУНКЦИИ

распределением вероятностей, т. е.

\[
p_k(n) \geqslant 0, \quad \sum_{k=0}^{\infty} p_k(n) = 1.
\]

Для того чтобы при любом фиксированном \( k \)

\[
\lim_{n \to \infty} p_k(n) = p_k
\]

и

\[
\sum_{k=0}^{\infty} p_k = 1,
\]

необходимо и достаточно, чтобы при любом \( x \in [0, 1) \)

\[
\lim_{n \to \infty} \varphi_n(x) = \varphi(x),
\]

где

\[
\varphi_n(x) = \sum_{k=0}^{\infty} p_k(n) x^k, \quad \varphi(x) = \sum_{k=0}^{\infty} p_k x^k, \quad \varphi(1) = 1.
\]

Доказательство. Пусть выполнено (1.15) и (1.16). Представим разность \( \varphi_n(x) - \varphi(x) \) в виде

\[
\varphi_n(x) - \varphi(x) =
\]
\[
= \sum_{k=0}^{N} (p_k(n) - p_k) x^k + \sum_{k=N+1}^{\infty} p_k(n) x^k - \sum_{k=N+1}^{\infty} p_k x^k,
\]

где \( N \) — некоторое целое число. Пусть \( x \in [0, 1) \) фиксирован. Докажем (1.17). Так как \( 0 \leqslant p_k(n) \leqslant 1, 0 \leqslant p_k \leqslant 1 \), то для любого фиксированного \( \varepsilon > 0 \) можно подобрать \( N \) так, чтобы при любом \( n \)

\[
\sum_{k=N+1}^{\infty} p_k(n) x^k \leqslant \sum_{k=N+1}^{\infty} x^k < \frac{\varepsilon}{3}, \quad \sum_{k=N+1}^{\infty} p_k x^k < \frac{\varepsilon}{3}.
\]

Тогда при данном \( N \)

\[
|\varphi_n(x) - \varphi(x)| \leqslant \sum_{k=0}^{N} |p_k(n) - p_k| x^k + \frac{2}{3} \varepsilon.
\]

Сумма в правой части этого неравенства может быть сделана меньше \( \varepsilon/3 \) при достаточно больших \( n \), так