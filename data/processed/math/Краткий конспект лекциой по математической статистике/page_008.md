---
source_image: page_008.png
page_number: 8
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 83.58
tokens: 12503
characters: 2866
timestamp: 2025-12-24T07:03:01.017257
finish_reason: stop
---

**Лемма 2.** Выборочные дисперсии \( \sigma^{2*} \) и \( S_0^2 \) являются состоятельными оценками для дисперсии. При этом \( \sigma^{2*} \) — смещенная, а \( S_0^2 \) — несмещенная оценка дисперсии:

1) \( \mathbb{E}\sigma^{2*} = \frac{n-1}{n} D X_1 = \frac{n-1}{n} \sigma^2 \neq \sigma^2 \) — смещенная;
2) \( \mathbb{E}S_0^2 = DX_1 = \sigma^2 \) — несмещенная;
3) \( \sigma^{2*} \xrightarrow{\text{p}} DX_1 = \sigma^2, \quad S_0^2 \xrightarrow{\text{p}} DX_1 = \sigma^2 \) — обе оценки состоятельны.

**Лемма 3.** Выборочный k-й момент \( \overline{X^k} \) является несмещенной и состоятельной оценкой для теоретического k-го момента:

1) \( \mathbb{E}\overline{X^k} = \mathbb{E}X_1^k = m_k \) — несмещённость;
2) \( \overline{X^k} \xrightarrow{\text{p}} \mathbb{E}X_1^k = m_k \) при \( n \to \infty \) — состоятельность.

**Доказательство леммы 1.**

1) \( \mathbb{E}\overline{X} = \frac{1}{n} \sum_{i=1}^n \mathbb{E}X_i = \frac{1}{n} n \mathbb{E}X_1 = \mathbb{E}X_1 = a; \)
2) По ЗБЧ, \( \overline{X} = \frac{1}{n} \sum_{i=1}^n X_i \xrightarrow{\text{p}} \mathbb{E}X_1 = a. \)

Упражнение. Доказать лемму 3.

**Доказательство леммы 2.**

1) Во первых, раскрыв скобки, полезно убедиться в том что

\[
\sigma^{2*} = \frac{1}{n} \sum_{i=1}^n (X_i - \overline{X})^2 = \overline{X^2} - (\overline{X})^2.
\]

Затем,

\[
\begin{align*}
\mathbb{E}\sigma^{2*} &= \mathbb{E} \left[ \overline{X^2} - (\overline{X})^2 \right] = \mathbb{E}\overline{X^2} - \mathbb{E}(\overline{X})^2 = (\text{по лемме 3}) = \mathbb{E}X_1^2 - \mathbb{E}(\overline{X})^2 = \\
&= \mathbb{E}X_1^2 - [(\mathbb{E}\overline{X})^2 + D(\overline{X})] = [\mathbb{E}X_1^2 - (\mathbb{E}X_1)^2] - D(\frac{1}{n} \sum_{i=1}^n X_i) = \\
&= \sigma^2 - \frac{1}{n^2} n D X_1 = \sigma^2 - \frac{\sigma^2}{n} = \frac{n-1}{n} \sigma^2.
\end{align*}
\]

2) Второе утверждение следует из первого, так как \( S_0^2 = \frac{n}{n-1} \sigma^{2*} \).

3) Из (2) и ЗБЧ, \( \sigma^{2*} = \overline{X^2} - (\overline{X})^2 \xrightarrow{\text{p}} \mathbb{E}X_1^2 - (\mathbb{E}X_1)^2 = \sigma^2 \).
Кроме того, \( \frac{n}{n-1} \to 1 \), так что \( S_0^2 \xrightarrow{\text{p}} \sigma^2 \).

**1.6 Группированные данные (некоторые вводные понятия к эконометрии)**

Если объем выборки очень велик, часто работают не с элементами выборки, а с *группированными* данными. Приведем ряд понятий, связанных с группировкой. Для простоты будем делить область выборочных данных на *k одинаковых* интервалов \( A_1, \ldots, A_k \) длины \( \Delta \):

\[
A_1 = [a_0, a_1), \ldots, A_k = [a_{k-1}, a_k), \quad a_j - a_{j-1} = \Delta.
\]

Как прежде, пусть \( \nu_j \) — число элементов выборки, попавших в интервал \( A_j \) и \( w_j \) — частота попадания в интервал \( A_j \) (оценка вероятности попадания в интервал):

\[
\nu_j = \{ \text{число } X_i \in A_j \} = \sum_{i=1}^n \mathbf{I}(X_i \in A_j), \quad w_j = \frac{\nu_j}{n}.
\]