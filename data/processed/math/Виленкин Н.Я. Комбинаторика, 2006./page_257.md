---
source_image: page_257.png
page_number: 257
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.49
tokens: 6675
characters: 2018
timestamp: 2025-12-24T07:47:37.610135
finish_reason: stop
---

при положительных и отрицательных значениях \( p \), докажите, что
\[
2 \sum_s C_p^{2s} C_{p}^{2m-2s} = C_{2p}^{2m} + (-1)^m C_p^m, \quad 2 \sum_s C_p^{2s} C_{p}^{2m-2s+1} = C_{2p}^{2m+1},
\]
\[
2 \sum_s C_p^{2s+1} C_{p}^{2m-2s+1} = C_{2p}^{2m+2} + (-1)^m C_p^{m+1},
\]
\[
2 \sum_s C_{p+2s}^p C_{p+2m-2s}^p = C_{2p+2m+1}^{2p+1} + C_{p+m'}^p,
\]
\[
2 \sum_s C_{p+2s}^{p-1} C_{p+2m-2s}^{p-1} = C_{2p+2m+1}^{2p-1} - C_{p+m'}^p, \quad 2 \sum_s C_{p+2s}^p C_{p+2m-2s+1}^p = C_{2p+2m+2}^{2p+1}.
\]

36. Из соотношения \( \left(1 - \frac{1}{x}\right)^m (1 - x)^{-n-1} = \frac{(-1)^m}{x^m} (1 - x)^{m-n-1} \) выведите, что \( \sum_s (-1)^s C_m^{m-k+s} C_n^{n+s} = C_{m-n-1}^k \).

37. Докажите, что \( \sum_s (-1)^s C_m^s C_n^n = \begin{cases} 0, & \text{если } m \neq n, \\ (-1)^n, & \text{если } m = n. \end{cases} \)

38. Из равенства \( (1 - x)^{-n} (1 - x^h)^n = (1 + x + \ldots + x^{h-1})^n \) выведите, что \( \sum_s (-1)^s C_{m-sh}^{n-1} C_n^s = \begin{cases} 0, & \text{если } m > h n - 1, \\ 1, & \text{если } m = h n - 1. \end{cases} \)

39. Из тождества \( (1 - x)^{-n-1} (1 - x^h)^n = \frac{(1 + x + \ldots + x^{h-1})^n}{1 - x} \) выведите, что \( \sum_s (-1)^s C_{m-sh}^n C_n^s = h^n \) при \( m \geq h n \).

40. Из тождеств \( (1 + x)^k (1 - x)^k = (1 - x^2)^k \) при \( k = p \) и \( k = -p \) выведите, что
\[
\sum_s (-1)^s C_p^{m-s} C_p^s = \begin{cases} (-1)^{\frac{m}{2}} C_p^{\frac{m}{2}}, & \text{если } m \text{ четно}, \\ 0, & \text{если } m \text{ нечетно}; \end{cases}
\]
\[
\sum_s (-1)^s C_{p+m-s}^p C_{p+s}^p = \begin{cases} (-1)^{\frac{m}{2}} C_{p+\frac{m}{2}}^{\frac{m}{2}}, & \text{если } m \text{ четно}, \\ 0, & \text{если } m \text{ нечетно}. \end{cases}
\]

41. Докажите, что \( \sum_s (-1)^s (C_m^s)^2 = \begin{cases} (-1)^{\frac{m}{2}} C_m^{\frac{m}{2}}, & \text{если } m \text{ четно}, \\ 0, & \text{если } m \text{ нечетно}. \end{cases} \)

42. Обозначим выражение \( a(a+1)(a+2)\ldots(a+n-1) \) через \( (a)_n \).
Докажите, что \( (a+b)_n = \sum_{m=0}^n C_n^m (a+m)_{n-m} (b-m+1)_m \).