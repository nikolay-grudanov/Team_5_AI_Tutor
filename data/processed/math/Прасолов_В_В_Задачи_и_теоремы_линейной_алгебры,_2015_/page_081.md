---
source_image: page_081.png
page_number: 81
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.18
tokens: 6379
characters: 2111
timestamp: 2025-12-24T08:09:39.234991
finish_reason: stop
---

Доказательство. Согласно задаче 1.9

\[
\left| \frac{1}{1 - x_i y_j} \right|_1^n = a_\delta(x) a_\delta(y) \div_{i, j=1}^n (1 - x_i y_j),
\]

поэтому достаточно доказать, что

\[
\left| \frac{1}{1 - x_i y_j} \right|_1^n = \bigotimes_\lambda a_{\lambda + \delta}(x) a_{\lambda + \delta}(y).
\]

Равенство

\[
\frac{1}{1 - x_i y_j} = 1 + x_i y_j + x_i^2 y_j^2 + x_i^3 y_j^3 + \ldots
\]

показывает, что в выражении для определителя \( \left| \frac{1}{1 - x_i y_j} \right|_1^n \) коэффициент при \( y_1^{\lambda_1} y_2^{\lambda_2} \ldots y_n^{\lambda_n} \) равен \( |x_i^{\lambda_j}|_1^n \). Ясно также, что этот определитель симметричен по \( x \) и \( y \), поэтому

\[
\left| \frac{1}{1 - x_i y_j} \right|_1^n = |x_i^{\lambda_j}|_1^n |y_i^{\lambda_j}|_1^n = \bigotimes_\lambda a_\lambda(x) a_\lambda(y).
\]

Если \( \lambda \) нельзя представить в виде \( \overline{\lambda} + \delta \), то \( a_\lambda = 0 \). Поэтому

\[
\bigotimes_\lambda a_\lambda(x) a_\lambda(y) = \bigotimes_\lambda a_{\lambda + \delta}(x) a_{\lambda + \delta}(y).
\]

Каждому разбиению \( \lambda = (\lambda_1, \ldots, \lambda_n) \) можно сопоставить симметрические многочлены \( p_\lambda = p_{\lambda_1} \ldots p_{\lambda_n} \) и \( m_\lambda = m_{\lambda_1 \ldots \lambda_n} \). Если \( \lambda \) пробегают все разбиения длины \( n \) числа \( d = |\lambda| \), то как многочлены \( p_\lambda \), так и многочлены \( m_\lambda \) образуют базис в пространстве \( V_d \) симметрических многочленов степени \( d \) от \( n \) переменных. Поэтому формула \( B(p_\lambda, m_\mu) = \delta_{\lambda, \mu} = \delta_{\lambda_1, \mu_1} \ldots \delta_{\lambda_n, \mu_n} \) определяет билинейную форму \( B \) в пространстве \( V_d \).

Теорема 4.8.2. Функции Шура образуют ортонормированный базис относительно формы \( B \), т. е. \( B(s_\lambda, s_\mu) = \delta_{\lambda, \mu} \).

Доказательство. Прежде всего заметим, что

\[
\div_{i, j=1}^n \frac{1}{1 - x_i y_j} = \div_{j=1}^n \div_{i=1}^n (1 + x_i y_j + x_i^2 y_j^2 + \ldots) =
\]
\[
= \div_{j=1}^n \bigotimes_{k=0}^\infty p_k(x) y_j^k = \bigotimes_\lambda p_\lambda(x) m_\lambda(y),
\]