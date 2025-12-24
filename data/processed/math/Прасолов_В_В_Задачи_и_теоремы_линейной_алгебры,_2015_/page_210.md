---
source_image: page_210.png
page_number: 210
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.14
tokens: 6572
characters: 2497
timestamp: 2025-12-24T08:13:16.778854
finish_reason: stop
---

Следствие. Если \( \lambda \) — собственное значение матрицы \( A \) и \( f(A) = 0 \), то \( f(\lambda) = 0 \).

Доказательство. Число \( f(\lambda) \) является собственным значением нулевой матрицы \( f(A) \), поэтому \( f(\lambda) = 0 \). \( \square \)

В качестве примера применения теоремы 13.5.1 вычислим собственные значения циркулянта.

Рассмотрим сначала простейший циркулянт

\[
C_n = \begin{pmatrix}
0 & 0 & 0 & \ldots & 0 & 1 \\
1 & 0 & 0 & \ldots & 0 & 0 \\
0 & 1 & 0 & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & 1 & 0
\end{pmatrix}.
\]

Так как \( C_n e_k = e_{k+1} \), то \( C_n^s e_k = e_{k+s} \). Поэтому \( C_n^n = I \). Следовательно, собственные значения являются корнями уравнения \( x^n = 1 \). Пусть \( \varepsilon = \exp(2\pi i / n) \). Докажем, что векторы \( u_s = \sum_{k=1}^n \varepsilon^{ks} e_k \ (s = 1, \ldots, n) \) являются собственными векторами \( C_n \), соответствующими собственным значениям \( \varepsilon^{-s} \). В самом деле, \( C_n u_s = \sum_{k=1}^n \varepsilon^{ks} C_n e_k = \sum_{k=1}^n \varepsilon^{ks} e_{k+1} = \sum_{k=1}^n \varepsilon^{-s} \varepsilon^{s(k+1)} e_{k+1} = \varepsilon^{-s} u_s \).

Теорема 13.5.2. Пусть \( \varepsilon_1, \ldots, \varepsilon_n \) — попарно различные корни степени \( n \) из единицы и \( f(x) = b_0 + b_1 x + b_2 x^2 + \ldots + b_{n-1} x^{n-1} \). Тогда собственные значения циркулянта \( A = b_0 I + b_1 C_n + b_2 C_n^2 + \ldots + b_{n-1} C_n^{n-1} \) равны \( f(\varepsilon_1), \ldots, f(\varepsilon_n) \).

Доказательство. Мы уже убедились, что собственные значения матрицы \( C_n \) равны \( \varepsilon_1, \ldots, \varepsilon_n \). Воспользовавшись теоремой 13.5.1, получаем требуемое. \( \square \)

В качестве другого примера вычислим собственные значения и собственные векторы сопровождающей матрицы

\[
A = \begin{pmatrix}
0 & 1 & 0 & \ldots & 0 \\
0 & 0 & 1 & \ldots & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & 0 & \ldots & 1 \\
p_0 & p_1 & p_2 & \ldots & p_{n-1}
\end{pmatrix}
\]

многочлена \( \lambda^n - p_{n-1} \lambda^{n-1} - \ldots - p_0 \). Пусть \( x \) — столбец \( (x_1, \ldots, x_n) \). Уравнение \( Ax = \lambda x \) можно переписать в виде \( x_2 = \lambda x_1, x_3 = \lambda x_2, \ldots, x_n = \lambda x_{n-1} \). Поэтому собственные векторы матрицы \( A \) имеют вид \( (\alpha, \lambda \alpha, \lambda^2 \alpha, \ldots, \lambda^{n-1} \alpha) \), где \( p_0 + p_1 \lambda + \ldots + p_{n-1} \lambda^{n-1} = \lambda^n \).