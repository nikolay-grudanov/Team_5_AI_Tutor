---
source_image: page_070.png
page_number: 70
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.94
tokens: 7688
characters: 1145
timestamp: 2025-12-24T07:27:26.655570
finish_reason: stop
---

значения \( m \), для которых \( x_m \in [a, b] \). Применяя к слагаемым (3.8) локальную теорему, получим

\[
P_n(a, b) = S_n + T_n,
\]

где

\[
S_n = \sum_{x_m \in [a, b]} \varphi(x_m) \frac{1}{\sqrt{n p q}},
\]
\[
T_n = \sum_{x_m \in [a, b]} \alpha_n(m) \varphi(x_m) \frac{1}{\sqrt{n p q}},
\]
\[
\varphi(x) = \frac{1}{\sqrt{2 \pi}} e^{-\frac{x^2}{2}}.
\]

Так как

\[
\Delta x_m = x_{m+1} - x_m = \frac{m+1-np}{\sqrt{n p q}} - \frac{m-np}{\sqrt{n p q}} = \frac{1}{\sqrt{n p q}},
\]

то \( S_n \) можно записать в виде суммы

\[
S_n = \sum_{x_m \in [a, b]} \varphi(x_m) \Delta x_m,
\]

которая отличается не более чем двумя слагаемыми от подходящим образом выбранной интегральной суммы, соответствующей интегралу \( \int_a^b \varphi(x) dx \). Следовательно,

\[
\lim_{n \to \infty} S_n = \int_a^b \varphi(x) dx.
\]

Используя оценку для \( \alpha_n(m) \) из локальной теоремы, получим

\[
|T_n| \leq \sum_{x_m \in [a, b]} \varphi(x_m) \Delta x_m |\alpha_n(m)| \leq \frac{C}{\sqrt{n}} S_n.
\]

Таким образом, при \( n \to \infty \)

\[
T_n \to 0.
\]

Утверждение теоремы для постоянных \( a, b \) следует из формул (3.8), (3.9), (3.10), (3.11).