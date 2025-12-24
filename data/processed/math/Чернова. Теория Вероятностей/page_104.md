---
source_image: page_104.png
page_number: 104
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 52.62
tokens: 11760
characters: 2133
timestamp: 2025-12-24T08:29:21.428208
finish_reason: stop
---

Решение. Согласно ЗБЧ, последовательность \( \frac{S_n}{n} \) сходится по вероятности (а, следовательно, и слабо) к \( \mathbf{E} \xi_1 \).

Слабая сходимость означает, что последовательность функций распределения \( F_n(c) = \mathrm{P}\left( \frac{S_n}{n} < c \right) \) сходится к функции распределения \( F(c) = \mathrm{P}(\mathbf{E} \xi_1 < c) \), если \( F(x) \) непрерывна в точке \( c \) (и ничего не означает, если \( F(x) \) разрывна в точке \( c \)). Но

\[
F(c) = \mathrm{P}(\mathbf{E} \xi_1 < c) = \begin{cases}
0, & c \leq \mathbf{E} \xi_1; \\
1, & c > \mathbf{E} \xi_1
\end{cases}
\]

есть функция распределения вырожденного закона и непрерывна в любой точке \( c \), кроме \( c = \mathbf{E} \xi_1 \). Итак, первый вывод: сходимость \( \mathrm{P}\left( \frac{S_n}{n} < c \right) \to \mathrm{P}(\mathbf{E} \xi_1 < c) \) имеет место для любого \( c \), кроме, возможно, \( c = \mathbf{E} \xi_1 \). Убедимся, что для \( c = \mathbf{E} \xi_1 \) такой сходимости быть не может. Пусть \( \eta \in \mathbb{N}_{0,1} \). Согласно ЦПТ,

\[
\mathrm{P}\left( \frac{S_n}{n} < \mathbf{E} \xi_1 \right) = \mathrm{P}\left( \frac{\sqrt{n}}{\sqrt{\mathbf{D} \xi_1}} \left( \frac{S_n}{n} - \mathbf{E} \xi_1 \right) < 0 \right) \to \mathrm{P}(\eta < 0) = \Phi_{0,1}(0) = \frac{1}{2} \neq \mathrm{P}(\mathbf{E} \xi_1 < \mathbf{E} \xi_1) = 0.
\]

Аналогично, кстати, ведет себя и вероятность \( \mathrm{P}\left( \frac{S_n}{n} \leq \mathbf{E} \xi_1 \right) \). Она тоже стремится к \( \frac{1}{2} \), а не к \( \mathrm{P}(\mathbf{E} \xi_1 \leq \mathbf{E} \xi_1) = 1 \).

И изящное упражнение на ту же тему:

Упражнение 29. Доказать, что

\[
\lim_{n \to \infty} \int_0^{0.999999n} \frac{1}{(n-1)!} y^{n-1} e^{-y} dy = 0; \quad \lim_{n \to \infty} \int_0^n \frac{1}{(n-1)!} y^{n-1} e^{-y} dy = \frac{1}{2}; \quad \lim_{n \to \infty} \int_0^{1.000001n} \frac{1}{(n-1)!} y^{n-1} e^{-y} dy = 1.
\]

Указание. Каждый из интегралов равен функции распределения суммы независимых случайных величин с каким-то показательным распределением в некоторой точке. Вспомнить, что такое гамма-распределение и что такое «устойчивость относительно суммирования».