---
source_image: page_067.png
page_number: 67
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.35
tokens: 5555
characters: 1816
timestamp: 2025-12-24T07:27:34.372191
finish_reason: stop
---

Что число успехов \( \mu_n \) лежит, например, между \( a \) и \( b \), приходится находить числовые значения сумм вероятностей \( P_m(b) \) вида (2.6). Действительно,

\[
P(a < \mu_n < b) = \sum_{a < m < b} P(\mu_n = m) = \sum_{a < m < b} P_n(m).
\] (3.1)

Затруднения при вычислениях возникают также при малых значениях \( p \) или \( q \).

Иногда при больших \( n \) удается заменить формулу (2.6) какой-либо приближенной асимптотической формулой. Приведем три предельные теоремы, содержащие асимптотические формулы для вероятностей (2.6) и (3.1) при \( n \to \infty \).

Теорема 3.1 (теорема Пуассона). Если \( n \to \infty \) и \( p \to 0 \) так, что \( np \to \lambda, \ 0 < \lambda < \infty, \) то

\[
P(\mu_n = m) = C_n^m p^m q^{n-m} \to \frac{\lambda^m}{m!} e^{-\lambda}
\]

при любом постоянном \( m, \ m = 0, 1, 2, \ldots \).

Доказательство. Положив \( np = \lambda_n \), представим вероятность \( P(\mu_n = m) \) в виде

\[
P(\mu_n = m) = \frac{n(n-1)\ldots(n-m+1)}{m!} \left( \frac{\lambda_n}{n} \right)^m \left( 1 - \frac{\lambda_n}{n} \right)^{n-m} =
\]
\[
= \frac{\lambda_n^m}{m!} \left( 1 - \frac{\lambda_n}{n} \right)^n \cdot \left( 1 - \frac{1}{n} \right) \left( 1 - \frac{2}{n} \right) \cdots \left( 1 - \frac{m-1}{n} \right) \left( 1 - \frac{\lambda_n}{n} \right)^{-m}.
\]

Отсюда при \( n \to \infty \) получим утверждение теоремы.

Таким образом, при больших \( n \) и малых \( p \) мы можем воспользоваться приближённой формулой

\[
\cdot P(\mu_n = m) \approx \frac{\lambda_n^m}{m!} e^{-\lambda_n}, \quad \lambda_n = np.
\] (3.2)

Часто эта формула используется при \( n > 100 \) и \( np < 30 \).

Теорема 3.2 (локальная теорема Муавра—Лапласа). Если \( n \to \infty, \ p \ (0 < p < 1) \) постоянно, величина \( x_m = \frac{m - np}{\sqrt{npq}} \) ограничена равномерно по \( m \) и \( n \),