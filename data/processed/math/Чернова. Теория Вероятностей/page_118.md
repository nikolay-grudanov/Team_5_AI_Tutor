---
source_image: page_118.png
page_number: 118
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 19.44
tokens: 11835
characters: 2258
timestamp: 2025-12-24T08:29:33.295415
finish_reason: stop
---

Для равномерного распределения на отрезке \([0, 1]\)

\[
F_{\xi_1}(x) = \begin{cases}
0, & x < 0; \\
x, & 0 \leq x \leq 1 \\
1, & x > 1,
\end{cases}
\]
поэтому \( F_{\varphi_n}(x) = (F_{\xi_1}(x))^n = \begin{cases}
0, & x < 0; \\
x^n, & 0 \leq x \leq 1 \\
1, & x > 1.
\end{cases} \)

А если еще заметить, что \( 1 - \varepsilon < 1 \), то

\[
\mathbf{P}(|\varphi_n - 1| > \varepsilon) = F_{\varphi_n}(1 - \varepsilon) = \begin{cases}
0, & 1 - \varepsilon < 0, \text{ то есть } \varepsilon > 1; \\
(1 - \varepsilon)^n, & 0 \leq 1 - \varepsilon < 1, \text{ то есть } 0 < \varepsilon \leq 1
\end{cases} \longrightarrow 0 \text{ при } n \to \infty.
\]

**1(б). Оценим вероятность сверху.** Поскольку \( 1 - \varphi_n \geq 0 \), по неравенству Маркова

\[
\mathbf{P}(1 - \varphi_n > \varepsilon) \leq \frac{\mathbf{E}(1 - \varphi_n)}{\varepsilon} = \frac{1 - \mathbf{E}\varphi_n}{\varepsilon}.
\] (27)

Найдем плотность распределения с. в. \( \varphi_n \) и математическое ожидание \( \mathbf{E}\varphi_n \).

\[
f_{\varphi_n}(x) = (F_{\varphi_n}(x))' = \begin{cases}
0, & x < 0; \\
nx^{n-1}, & 0 \leq x \leq 1 \\
0, & x > 1;
\end{cases}
\]
\[
\mathbf{E}\varphi_n = \int_0^1 x nx^{n-1} dx = \frac{n}{n+1}.
\]

Подставляя математическое ожидание в неравенство (27), получим

\[
\mathbf{P}(1 - \varphi_n > \varepsilon) \leq \frac{1 - \mathbf{E}\varphi_n}{\varepsilon} = \frac{1 - \frac{n}{n+1}}{\varepsilon} = \frac{1}{(n+1)\varepsilon} \to 0 \text{ при } n \to \infty.
\]

**Способ 2. Используем связь со слабой сходимостью.** Сходимость по вероятности к константе равносильна слабой сходимости (свойство **19**). Докажем поэтому, что \( \varphi_n \) слабо сходится к единице. Требуется доказать, что функция распределения \( F_{\varphi_n}(x) \) сходится к \( F_1(x) = \mathbf{P}(1 < x) \) для любого \( x \neq 1 \) (*почему кроме 1*?*?*).

При любом \( x \neq 1 \) имеем:

\[
F_{\varphi_n}(x) = \begin{cases}
0, & x < 0; \\
x^n, & 0 \leq x \leq 1 \\
1, & x > 1
\end{cases} \quad \to \quad F_1(x) = \begin{cases}
0, & x \leq 1 \\
1, & x > 1,
\end{cases}
\]

и только при \( x = 1 \) сходимости нет: \( F_{\varphi_n}(1) = 1 \), тогда как \( F_1(1) = 0 \).

Таким образом, \( \varphi_n \) сходится слабо к единице, и, следовательно, сходится к ней же по вероятности.