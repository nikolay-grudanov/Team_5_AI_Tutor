---
source_image: page_121.png
page_number: 121
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 69.94
tokens: 11659
characters: 1887
timestamp: 2025-12-24T06:26:02.954789
finish_reason: stop
---

Для оценки правой части мы используем неравенство Маркова (6.32) (а наиболее выгодное значение \( \alpha \) подберём позднее):

\[
\mathrm{P}\{X - \mu \geq r\} \leq \mathrm{M}[e^{\alpha(X-\mu)}] e^{-\alpha r}.
\]

Остаётся оценить \( \mathrm{M}[e^{\alpha(X-\mu)}] \) и выбрать значение для \( \alpha \). Рассмотрим случайную величину \( X_i \), равную 1 в случае успеха \( i \)-го испытания и 0 в случае его неудачи. Тогда

\[
X = \sum_{i=1}^{n} X_i
\]
и
\[
X - \mu = \sum_{i=1}^{n} (X_i - p_i).
\]
Поскольку испытания независимы, то величины \( X_i \) независимы. Поэтому величины \( e^{\alpha(X_i-p_i)} \) независимы (упр. 6.3-4), и по формуле (6.27) можно переставить произведение и математическое ожидание:

\[
\mathrm{M}[e^{\alpha(X-\mu)}] = \mathrm{M} \left[ \prod_{i=1}^{n} e^{\alpha(X_i-p_i)} \right] = \prod_{i=1}^{n} \mathrm{M}[e^{\alpha(X_i-p_i)}].
\]
Каждый множитель можно оценить так:
\[
\begin{align*}
\mathrm{M}[e^{\alpha(X_i-p_i)}] &= e^{\alpha(1-p_i)} p_i + e^{\alpha(0-p_i)} q_i \\
&= p_i e^{\alpha q_i} + q_i e^{-\alpha p_i} \\
&\leq p_i e^{\alpha} + 1 \\
&\leq \exp(p_i e^{\alpha}),
\end{align*}
\]
где \( \exp(x) \) обозначает экспоненциальную функцию: \( \exp(x) = e^x \). (Мы воспользовались тем, что \( \alpha > 0, q_i \leq 1, e^{\alpha q_i} \leq e^{\alpha} \) и \( e^{-\alpha p_i} \leq 1 \), а также неравенством (2.7).) Следовательно,
\[
\mathrm{M}[e^{\alpha(X-\mu)}] \leq \prod_{i=1}^{n} \exp(p_i e^{\alpha}) = \exp(\mu e^{\alpha}),
\]
так как \( \mu = \sum_{i=1}^{n} p_i \). Таким образом, из неравенства (6.43) следует оценка
\[
\mathrm{P}\{X - \mu \geq r\} \leq \exp(\mu e^{\alpha} - \alpha r).
\]
Выбирая \( \alpha = \ln(r/\mu) \) (см. упр. 6.5-6), получаем
\[
\begin{align*}
\mathrm{P}\{X - \mu \geq r\} &\leq \exp(\mu e^{\ln(r/\mu)} - r \ln(r/\mu)) \\
&= \exp(r - r \ln(r/\mu)) = \frac{e^r}{(r/\mu)^r} = \left( \frac{\mu e}{r} \right)^r.
\end{align*}
\]