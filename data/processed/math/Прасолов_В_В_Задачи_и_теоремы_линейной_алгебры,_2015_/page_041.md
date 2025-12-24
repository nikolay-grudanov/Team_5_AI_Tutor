---
source_image: page_041.png
page_number: 41
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.49
tokens: 6609
characters: 2187
timestamp: 2025-12-24T08:08:40.772735
finish_reason: stop
---

1.18. Пусть \( P_k(x) \) — многочлен степени \( k - 1 \) со старшим коэффициентом \( a_k \), т. е. \( P_k(x) = a_k x^{k-1} + \ldots \). Вычислите определитель \( |a_{ij}|_1^n \), где \( a_{ij} = P_j(x_i) \).

1.19 [Gr4]. Пусть \( f(x) = (x - x_1) \ldots (x - x_n) \), причём числа \( x_1, \ldots, x_n \) попарно различны. Докажите, что:
а) \( f'(x_i) = (-1)^{n-i} \frac{V(x_1, \ldots, x_n)}{V(x_1, \ldots, \hat{x}_i, \ldots, x_n)}; \)
б) \( \prod_{i=1}^n \frac{x_i^k}{f'(x_i)} = \frac{1}{V(x_1, \ldots, x_n)} \left| \begin{array}{cccc}
1 & x_1 & \ldots & x_1^{n-2} & x_1^k \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
1 & x_n & \ldots & x_n^{n-2} & x_n^k
\end{array} \right|; \)
в) \( \prod_{i=1}^n \frac{x_i^k}{f'(x_i)} = \begin{cases} 0 & \text{при } 0 \leq k \leq n-2,\ k \in \mathbb{Z}; \\ 1 & \text{при } k = n-1. \end{cases} \)

1.20. Пусть \( \binom{x}{k} = \frac{x(x-1)\ldots(x-k+1)}{k!} \). Докажите, что
\[
\left| \begin{array}{ccc}
1 & \binom{x_1}{1} & \ldots & \binom{x_1}{n-1} \\
1 & \binom{x_2}{1} & \ldots & \binom{x_2}{n-1} \\
\cdots & \cdots & \cdots & \cdots \\
1 & \binom{x_n}{1} & \ldots & \binom{x_n}{n-1}
\end{array} \right| = \prod_{1 \leq i < j \leq n} \frac{x_i - x_j}{i - j}.
\]

1.21. Пусть \( a_{ij} = \binom{in}{j} \). Докажите, что \( |a_{ij}|_1^n = n^{r(r+1)/2} \) при \( r \leq n \).

1.22. Пусть \( x_1, \ldots, x_n \) — произвольные целые числа. Докажите, что число \( \prod_{1 \leq i < j \leq n} \frac{x_i - x_j}{i - j} \) целое.

1.23. Даны целые числа \( k_1, \ldots, k_n \). Вычислите определитель \( |a_{ij}|_1^n \), где \( a_{ij} = 1/(k_i + j - i)! \) при \( k_i + j - i \geq 0 \) и \( a_{ij} = 0 \) при \( k_i + j - i < 0 \).

1.24. Пусть \( s_k = p_1 x_1^k + \ldots + p_n x_n^k \), \( a_{ij} = s_{i+j} \). Докажите, что \( |a_{ij}|_1^n = p_1 \ldots p_n \prod_{i > j} (x_i - x_j)^2 \).

1.25. Пусть \( s_k = x_1^k + \ldots + x_n^k \). Вычислите определитель
\[
\left| \begin{array}{cccccc}
s_0 & s_1 & s_2 & \ldots & s_{n-1} & 1 \\
s_1 & s_2 & s_3 & \ldots & s_n & y \\
s_2 & s_3 & s_4 & \ldots & s_{n+1} & y^2 \\
\cdots & \cdots & \cdots & \cdots & \cdots & \cdots \\
s_n & s_{n+1} & s_{n+2} & \ldots & s_{2n-1} & y^n
\end{array} \right|.
\]