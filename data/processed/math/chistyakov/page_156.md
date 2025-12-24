---
source_image: page_156.png
page_number: 156
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.86
tokens: 7740
characters: 1962
timestamp: 2025-12-24T07:29:49.675265
finish_reason: stop
---

Заменяя в этом равенстве \( f(t/n) \) по формуле (1.1), при любом фиксированном \( t \) и \( n \to \infty \) получим

\[
f_{n_n}(t) = \left[ 1 + i \frac{t}{n} a + \frac{t}{n} \varepsilon \left( \frac{t}{n} \right) \right]^n \to e^{ita},
\]

так как \( \varepsilon (t/n) \to 0 \) при \( n \to \infty \). Таким образом, при любом \( t \) последовательность \( f_{n_n}(t) \) сходится к функции \( e^{ita} \), являющейся характеристикой функцией постоянной величины \( a \). Функция распределения \( F(x) \) постоянной \( a \) равна

\[
F(x) = \begin{cases}
1, & \text{если } x > a, \\
0, & \text{если } x \leq a.
\end{cases}
\]

По теореме 2.5 гл. 7 при любом \( x \neq a \)

\[
\lim_{n \to \infty} F_{n_n}(x) = F(x),
\]

так как \( x = a \) — единственная точка разрыва функции \( F(x) \). Пусть задано \( \varepsilon > 0 \). Тогда

\[
P(|\eta_n - a| < \varepsilon) = P(a - \varepsilon < \eta_n < a + \varepsilon) \geq
\]
\[
\geq P \left( a - \frac{\varepsilon}{2} \leq \eta_n < a + \varepsilon \right) = F_{n_n}(a + \varepsilon) - F_{n_n}\left( a - \frac{\varepsilon}{2} \right).
\]

Точки \( x = a + \varepsilon \) и \( x = a - \varepsilon/2 \) являются точками непрерывности функции (1.3). Следовательно, при \( n \to \infty \)

\[
F_{n_n}(a + \varepsilon) - F_{n_n}\left( a - \frac{\varepsilon}{2} \right) \to F(a + \varepsilon) - F\left( a - \frac{\varepsilon}{2} \right) = 1.
\]

Отсюда и из неравенств

\[
1 \geq P(|\eta_n - a| < \varepsilon) \geq F_{n_n}(a + \varepsilon) - F_{n_n}\left( a - \frac{\varepsilon}{2} \right)
\]

следует утверждение теоремы.

§ 2. Центральная предельная теорема

В § 3 гл. 3 была доказана теорема Муавра — Лапласа, согласно которой число успехов \( \mu_n \) в \( n \) испытаниях схемы Бернулли при больших \( n \) имеет распределение, близкое к нормальному. Если воспользоваться тем, что \( \mu_n \) представляется в виде суммы независимых слагаемых (4.4.18), то теорему Муавра — Лапласа можно сформулировать в следующем виде.