---
source_image: page_069.png
page_number: 69
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.08
tokens: 6629
characters: 2457
timestamp: 2025-12-24T08:09:33.525035
finish_reason: stop
---

§ 4. Симметрические функции. Суммы степеней. Числа Бернулли

Аналогично с помощью соотношений (2) получаем

\[
s_k = (-1)^{k-1} \left| \begin{array}{cccc}
p_1 & 1 & 0 & \ldots & 0 \\
2p_2 & p_1 & 1 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
kp_k & p_{k-1} & p_{k-2} & \ldots & p_1
\end{array} \right|,
\]

\[
p_k = \frac{1}{k!} \left| \begin{array}{cccc}
s_1 & -1 & 0 & \ldots & 0 \\
s_2 & s_1 & -2 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
s_{k-1} & s_{k-2} & \ldots & \ldots & -k+1 \\
s_k & s_{k-1} & \ldots & \ldots & s_1
\end{array} \right|.
\]

С помощью соотношений (3) получаем

\[
s_k = \left| \begin{array}{cccc}
\sigma_1 & 1 & 0 & \ldots & 0 \\
2\sigma_2 & \sigma_1 & 1 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
k\sigma_k & \sigma_{k-1} & \sigma_{k-2} & \ldots & \sigma_1
\end{array} \right|,
\]

\[
\sigma_k = \frac{1}{k!} \left| \begin{array}{cccc}
s_1 & 1 & 0 & \ldots & 0 \\
s_2 & s_1 & 2 & \ldots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
s_{k-1} & s_{k-2} & \ldots & \ldots & k-1 \\
s_k & s_{k-1} & \ldots & \ldots & s_1
\end{array} \right|.
\]

4.2. Основная теорема о симметрических многочленах

Теорема 4.2.1. Пусть \( f(x_1, \ldots, x_n) \) — симметрический многочлен. Тогда существует такой многочлен \( g(y_1, \ldots, y_n) \), что \( f(x_1, \ldots, x_n) = g(\sigma_1, \ldots, \sigma_n) \). При этом многочлен \( g \) единственный.

Доказательство. Достаточно рассмотреть случай, когда \( f \) — однородный многочлен. Будем говорить, что моном \( x_1^{\lambda_1} \ldots x_n^{\lambda_n} \) имеет более высокий порядок, чем моном \( x_1^{\mu_1} \ldots x_n^{\mu_n} \), если \( \lambda_1 = \mu_1, \ldots, \lambda_k = \mu_k \) и \( \lambda_{k+1} > \mu_{k+1} \) (возможно \( k = 0 \)). Пусть \( ax_1^{\lambda_1} \ldots x_n^{\lambda_n} \) — старший моном многочлена \( f \). Тогда \( \lambda_1 \geq \ldots \geq \lambda_n \). Рассмотрим симметрический многочлен

\[
f_1 = f - a \sigma_1^{\lambda_1-\lambda_2} \sigma_2^{\lambda_2-\lambda_3} \ldots \sigma_n^{\lambda_n}.
\] (1)

Старший член монома \( \sigma_1^{\lambda_1-\lambda_2} \ldots \sigma_n^{\lambda_n} \) равен

\[
x_1^{\lambda_1-\lambda_2} (x_1 x_2)^{\lambda_2-\lambda_3} \ldots (x_1 \ldots x_n)^{\lambda_n} = x_1^{\lambda_1} x_2^{\lambda_2} \ldots x_n^{\lambda_n},
\]

поэтому порядок старшего монома многочлена \( f_1 \) строго ниже порядка старшего монома многочлена \( f \). Применим к многочлену \( f_1 \) снова