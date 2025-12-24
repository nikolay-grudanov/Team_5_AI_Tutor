---
source_image: page_144.png
page_number: 144
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.14
tokens: 7251
characters: 1711
timestamp: 2025-12-24T07:29:35.525433
finish_reason: stop
---

как содержит конечное число стремящихся к нулю слагаемых. Равенство \( \varphi(1) = 1 \) следует из (1.16).

Пусть теперь выполнено (1.17). Докажем (1.15) от противного. Предположим, что (1.15) не выполнено. Тогда найдутся две подпоследовательности \( n'_m \) и \( n''_m \) такие, что

\[
\lim_{n'_m \to \infty} p_k(n'_m) = \tilde{p}_k, \quad \lim_{n''_m \to \infty} p_k(n''_m) = \tilde{\tilde{p}}_k,
\]

причем \( \{ \tilde{p}_k \} \) и \( \{ \tilde{\tilde{p}}_k \} \) не совпадают. Тогда по доказанной части теоремы из (1.18) следует, что

\[
\lim_{n'_m \to \infty} \varphi_{n'_m}(x) = \tilde{\varphi}(x) = \sum_{k=0}^{\infty} \tilde{p}_k x^k,
\]
\[
\lim_{n''_m \to \infty} \varphi_{n''_m}(x) = \tilde{\tilde{\varphi}}(x) = \sum_{k=0}^{\infty} \tilde{\tilde{p}}_k x^k
\]

и \( \tilde{\varphi}(x) \neq \tilde{\tilde{\varphi}}(x) \). Это невозможно, так как предел (1.17) существует. Теорема доказана.

Пример 4. Пусть \( \mu_n \) — число успехов в \( n \) испытаниях Бернулли и \( p_n \) — вероятность успеха в одном испытании. Будем предполагать, что существует \( \lim_{n \to \infty} n p_n = \lambda, 0 < \lambda < \infty \). Воспользуемся теоремой 1.5 для вычисления \( \lim_{n \to \infty} P(\mu_n = m) \). Положим \( \lambda_n = n p_n \).

По формуле (1.5)

\[
\varphi_{\mu_n}(x) = \left( \frac{\lambda_n}{n} x + 1 - \frac{\lambda_n}{n} \right)^n = \left[ 1 + \frac{\lambda_n}{n} (x-1) \right]^n.
\]

Следовательно,

\[
\lim_{n \to \infty} \varphi_{\mu_n}(x) = e^{\lambda (x-1)} = \sum_{m=0}^{\infty} \frac{\lambda^m}{m!} e^{-\lambda} x^m.
\]

Отсюда по теореме 1.5

\[
\lim_{n \to \infty} P(\mu_n = m) = \frac{\lambda^m}{m!} e^{-\lambda}.
\]

Таким образом, получили новое доказательство теоремы Пуассона.