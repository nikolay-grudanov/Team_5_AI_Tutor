---
source_image: page_029.png
page_number: 29
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 86.53
tokens: 11794
characters: 2375
timestamp: 2025-12-24T06:21:56.881798
finish_reason: stop
---

**o- и ω-обозначения**

Запись \( f(n) = O(g(n)) \) означает, что с ростом \( n \) отношение \( f(n)/g(n) \) остаётся ограниченным. Если к тому же

\[
\lim_{n \to \infty} \frac{f(n)}{g(n)} = 0,
\]

то мы пишем \( f(n) = o(g(n)) \) (читается "эф от эн есть о малое от же от эн"). Формально говоря, \( f(n) = o(g(n)) \), если для всякого положительного \( \varepsilon > 0 \) найдётся такое \( n_0 \), что \( 0 \leq f(n) \leq \varepsilon g(n) \) при всех \( n \geq n_0 \). (Тем самым запись \( f(n) = o(g(n)) \) предполагает, что \( f(n) \) и \( g(n) \) неотрицательны для достаточно больших \( n \).)

Пример: \( 2n = o(n^2) \), но \( 2n^2 \neq o(n^2) \).

Аналогичным образом вводится \( \omega \)-обозначение: говорят, что \( f(n) \) есть \( \omega(g(n)) \) ("эф от эн есть омега малая от же от эн"), если для любого положительного \( c \) существует такое \( n_0 \), что \( 0 \leq c g(n) \leq f(n) \) при всех \( n \geq n_0 \). Другими словами, \( f(n) = \omega(g(n)) \) означает, что \( g(n) = o(f(n)) \).

Пример: \( n^2/2 = \omega(n) \), но \( n^2/2 \neq \omega(n^2) \).

**Сравнение функций**

Введённые нами определения обладают некоторыми свойствами транзитивности, рефлексивности и симметричности:

**Транзитивность:**
\[
\begin{align*}
f(n) = \Theta(g(n)) \text{ и } g(n) = \Theta(h(n)) &\implies f(n) = \Theta(h(n)), \\
f(n) = O(g(n)) \text{ и } g(n) = O(h(n)) &\implies f(n) = O(h(n)), \\
f(n) = \Omega(g(n)) \text{ и } g(n) = \Omega(h(n)) &\implies f(n) = \Omega(h(n)), \\
f(n) = o(g(n)) \text{ и } g(n) = o(h(n)) &\implies f(n) = o(h(n)), \\
f(n) = \omega(g(n)) \text{ и } g(n) = \omega(h(n)) &\implies f(n) = \omega(h(n)).
\end{align*}
\]

**Рефлексивность:**
\[
f(n) = \Theta(f(n)), \quad f(n) = O(f(n)), \quad f(n) = \Omega(f(n)).
\]

**Симметричность:**
\[
f(n) = \Theta(g(n)) \text{ если и только если } g(n) = \Theta(f(n)).
\]

**Обращение:**
\[
\begin{align*}
f(n) = O(g(n)) &\text{ если и только если } g(n) = \Omega(f(n)), \\
f(n) = o(g(n)) &\text{ если и только если } g(n) = \omega(f(n)).
\end{align*}
\]

Можно провести такую параллель: отношения между функциями \( f \) и \( g \) подобны отношениям между числами \( a \) и \( b \):

\[
\begin{align*}
f(n) = O(g(n)) &\approx a \leq b \\
f(n) = \Omega(g(n)) &\approx a \geq b \\
f(n) = \Theta(g(n)) &\approx a = b \\
f(n) = o(g(n)) &\approx a < b \\
f(n) = \omega(g(n)) &\approx a > b
\end{align*}
\]