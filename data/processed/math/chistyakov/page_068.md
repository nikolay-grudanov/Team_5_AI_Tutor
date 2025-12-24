---
source_image: page_068.png
page_number: 68
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.14
tokens: 7394
characters: 1344
timestamp: 2025-12-24T07:27:31.471848
finish_reason: stop
---

\[
(-\infty < a \leq x_m \leq b < +\infty), \text{ то}
\]
\[
P(\mu_n = m) = \frac{1}{\sqrt{2\pi npq}} e^{-\frac{x_m^2}{2}} (1 + \alpha_n(m)),
\]
где \(|\alpha_n| < C/\sqrt{n}\) при \(x_m \in [a, b]\), \(C > 0\) — постоянная.

Доказательство. Коэффициент \(C_n^m\) в (2.6) запишем в виде
\[
C_n^m = \frac{n!}{m! (n-m)!}.
\]
Так как
\[
m = n\rho + x_m \sqrt{npq}, \quad n - m = nq - x_m \sqrt{npq},
\]
то, воспользовавшись формулой Стирлинга
\[
\ln n! = \ln \sqrt{2\pi n} + n \ln n - n + O\left(\frac{1}{n}\right),
\]
получим
\[
\ln m! = \ln \sqrt{2\pi m} + (n\rho + x_m \sqrt{npq}) \ln (n\rho + x_m \sqrt{npq}) -
-n\rho - x_m \sqrt{npq} + O\left(\frac{1}{n}\right),
\]
\[
\ln (n-m)! = \ln \sqrt{2\pi (n-m)} +
+(nq - x_m \sqrt{npq}) \ln (nq - x_m \sqrt{npq}) -
-nq + x_m \sqrt{npq} + O\left(\frac{1}{n}\right).
\]
Логарифмы в (3.5) при помощи формулы \(\ln (1 + x) = x - x^2/2 + O(x^3)\) запишем в виде
\[
\ln (n\rho + x_m \sqrt{npq}) = \ln n\rho + \ln \left(1 + x_m \sqrt{\frac{q}{n\rho}}\right) =
\approx \ln n\rho + x_m \sqrt{\frac{q}{n\rho}} - \frac{x_m^2}{2} \frac{q}{n\rho} + O\left(\frac{q^3}{n^{3/2} \rho^3}\right),
\]
\[
\ln (nq - x_m \sqrt{npq}) =
\approx \ln nq - x_m \sqrt{\frac{p}{nq}} - \frac{x_m^2}{2} \frac{p}{nq} + O\left(\frac{p^3}{n^{3/2} q^3}\right).
\]
Утверждение теоремы можно получить из (2.6), (3.3), (3.4), (3.5), (3.6).