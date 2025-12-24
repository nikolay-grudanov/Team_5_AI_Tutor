---
source_image: page_161.png
page_number: 161
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.78
tokens: 6404
characters: 2006
timestamp: 2025-12-24T08:11:56.189530
finish_reason: stop
---

Теорема 10.1.2. Любые три последовательных ортогональных многочлена связаны соотношением

\[
\varphi_{n+1}(x) = (a_n x + b_n) \varphi_n(x) + c_n \varphi_{n-1}(x), \quad n = 1, 2, \ldots,
\]

где \( a_n, b_n \) и \( c_n \) — некоторые константы.

Доказательство. Пусть \( \varphi_n(x) = k_n x^n + k'_n x^{n-1} + \ldots \). Коэффициент многочлена \( \varphi_{n+1}(x) - a_n x \varphi_n(x) \) при \( x^{n+1} \) равен \( k_{n+1} - a_n k_n \), поэтому если \( a_n = k_{n+1}/k_n \), то этот многочлен имеет степень не выше \( n \), а значит,

\[
\varphi_{n+1}(x) - a_n x \varphi_n(x) = \lambda_0 \varphi_0(x) + \ldots + \lambda_n \varphi_n(x)
\]

для некоторых констант \( \lambda_0, \ldots, \lambda_n \).

Из условия ортогональности следует, что \( (\varphi_m(x), x^k) = 0 \) при \( k \leq m - 1 \). Поэтому \( (x \varphi_n(x), x^k) = (\varphi_n(x), x^{k+1}) = 0 \) при \( k \leq n - 2 \). Таким образом,

\[
(\lambda_0 \varphi_0(x) + \ldots + \lambda_n \varphi_n(x), x^k) = 0
\]

при \( k \leq n - 2 \). Любой многочлен \( \varphi_0, \ldots, \varphi_{n-2} \) линейно выражается через \( 1, x, \ldots, x^{n-2} \), поэтому

\[
(\lambda_0 \varphi_0(x) + \ldots + \lambda_n \varphi_n(x), \varphi_k(x)) = 0
\]

при \( k \leq n - 2 \). Следовательно, \( \lambda_0 = \ldots = \lambda_{n-2} = 0 \). В итоге получаем

\[
\varphi_{n+1}(x) - a_n x \varphi_n(x) = \lambda_{n-1} \varphi_{n-1}(x) + \lambda_n \varphi_n(x).
\]

Остаётся положить \( b_n = \lambda_n \) и \( c_n = \lambda_{n-1} \).

Замечание. Удобно считать, что \( \varphi_{-1}(x) = 0 \). Тогда рекуррентное соотношение из теоремы 10.1.2 будет выполняться и при \( n = 0 \).

10.2. Многочлены Лежандра

Многочлены

\[
P_n(x) = \frac{1}{2^n n!} \frac{d^n}{dx^n} (x^2 - 1)^n
\]

называют многочленами Лежандра. Следующее утверждение показывает, что многочлены Лежандра образуют ортогональную систему относительно скалярного произведения \( (f, g) = \int_{-1}^1 f(x)g(x)\, dx \).

Теорема 10.2.1. \( \int_{-1}^1 P_m(x)P_n(x)\, dx = \frac{2}{2n+1} \delta_{mn} \).