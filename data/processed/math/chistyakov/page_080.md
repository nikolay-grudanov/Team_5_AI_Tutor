---
source_image: page_080.png
page_number: 80
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.51
tokens: 7932
characters: 1117
timestamp: 2025-12-24T07:27:41.493269
finish_reason: stop
---

где \( 0 \leq a \leq b \leq 1 \). Положим

\[
P(\{\Gamma\}) = \frac{1}{2}, \quad P(\{(P, u): a \leq u < b\}) = \frac{b-a}{2}.
\]

По вероятностям этих событий однозначно определяется вероятность на \( \mathcal{F} \). Рассмотрим случайную величину \( \xi \), определяемую равенствами

\[
\xi(\Gamma) = -1, \quad \xi(P, u) = u.
\]

Так как

\[
\{\xi < x\} = \begin{cases}
\varnothing, & \text{если } x \leq -1, \\
\{\Gamma\}, & \text{если } -1 < x \leq 0, \\
\{\Gamma\} + \{(P, u): 0 \leq u < x\}, & \text{если } 0 < x < 1,
\end{cases}
\]

то (рис. 6)

\[
F_{\xi}(x) = \begin{cases}
0, & \text{если } x \leq -1, \\
\frac{1}{2}, & \text{если } -1 < x \leq 0, \\
\frac{x+1}{2}, & \text{если } 0 < x \leq 1, \\
1, & \text{если } x > 1.
\end{cases}
\]

§ 2. Свойства функций распределения

Пусть \( F(x) \) — функция распределения некоторой случайной величины \( \xi \). По определению функция \( \xi(\omega) \) принимает только конечные значения. Формула (1.3) определяет \( F(x) \) при любом действительном \( x \), при \( x = +\infty \) и при \( x = -\infty \). Очевидно, что

\[
F(-\infty) = 0, \quad F(+\infty) = 1.
\]