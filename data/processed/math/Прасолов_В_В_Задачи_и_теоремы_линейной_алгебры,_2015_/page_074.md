---
source_image: page_074.png
page_number: 74
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.86
tokens: 6181
characters: 1421
timestamp: 2025-12-24T08:09:19.947034
finish_reason: stop
---

4.5. Числа Бернулли

Во многих теоремах анализа и теории чисел встречаются числа Бернулли \( B_k \), возникающие при разложении в ряд функции

\[
\frac{x}{e^x - 1} = \sum_{k=0}^{\infty} B_k \frac{x^k}{k!} \quad (\text{при } |x| < 2\pi).
\]

Легко проверить, что \( B_0 = 1 \) и \( B_1 = -1/2 \). С помощью чисел Бернулли можно представить сумму степеней \( S_k(n) = 1^k + 2^k + \ldots + (n-1)^k \) в виде многочлена от \( n \).

Теорема 4.5.1. \((m+1)S_m(n) = \sum_{k=0}^{m} \binom{m+1}{k} B_k n^{m+1-k}\).

Доказательство. Представим произведение рядов

\[
\prod_{k=0}^{\infty} \frac{B_k x^k}{k!} \cdot \prod_{s=1}^{\infty} \frac{(nx)^s}{s!}
\]

в виде ряда двумя способами. С одной стороны, это произведение равно

\[
\frac{x}{e^x - 1}(e^{nx} - 1) = x \prod_{r=1}^{n-1} e^{rx} = nx + \prod_{m=1}^{\infty} \left( \prod_{r=1}^{m-1} r^m \right) \frac{x^{m+1}}{m!} =
= nx + \prod_{m=1}^{\infty} \frac{(m+1)S_m(n)}{(m+1)!} x^{m+1}.
\]

С другой стороны, это произведение равно

\[
\prod_{k=0, s=1}^{\infty} \frac{B_k n^s x^{s+k}}{k! s!} = B_0 nx + \prod_{m=1}^{\infty} \prod_{k=0}^{m} \frac{\binom{m+1}{k} B_k n^{m+1-k}}{(m+1)!} x^{m+1}.
\]

Приведём некоторые детерминантные выражения для \( B_k \). Пусть \( b_k = B_k / k! \). Тогда согласно определению

\[
x = (e^x - 1) \left( \sum_{k=0}^{\infty} b_k x^k \right) =
= \left( x + \frac{x^2}{2!} + \frac{x^3}{3!} + \ldots \right)(1 + b_1 x + b_2 x^2 + b_3 x^3 + \ldots),
\]