---
source_image: page_130.png
page_number: 130
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.77
tokens: 7826
characters: 1433
timestamp: 2025-12-24T07:29:01.321206
finish_reason: stop
---

§ 1. Неравенство Чебышева

Числовые характеристики случайных величин, введенные в предыдущей главе, позволяют давать некоторые оценки распределений случайных величин.

Теорема 1.1. Пусть \( \xi = \xi(\omega) \geq 0 \) при любом \( \omega \in \Omega \). Если \( M\xi \) существует, то при любом \( \varepsilon > 0 \)

\[
P(\xi \geq \varepsilon) \leq \frac{M\xi}{\varepsilon}.
\]

Доказательство. Проведем доказательство в случае, когда \( \xi \) задана в абсолютно непрерывном вероятностном пространстве (см. § 6 гл. 1). По определению математического ожидания имеем

\[
M\xi = \int_{\Omega} \ldots \int_{\Omega} \xi(u_1, \ldots, u_n) \pi(u_1, \ldots, u_n) du_1 du_2 \ldots du_n.
\]

Пусть

\[
\Omega_\varepsilon = \{(u_1, \ldots, u_n): \xi(u_1, \ldots, u_n) \geq \varepsilon\} \subseteq \Omega.
\]

Введем случайную величину

\[
\eta = \begin{cases}
0, & \text{если } (u_1, \ldots, u_n) \in \Omega \setminus \Omega_\varepsilon, \\
\varepsilon, & \text{если } (u_1, \ldots, u_n) \in \Omega_\varepsilon.
\end{cases}
\]

При любом \( (u_1, \ldots, u_n) \in \Omega \) имеем

\[
\xi \geq \eta.
\]

Умножим обе части этого неравенства на \( \pi(u_1, u_2, \ldots, u_n) \) и проинтегрируем по \( \Omega \). Получим, что \( M\xi \geq M\eta \). Отсюда следует утверждение теоремы, так как

\[
M\eta = \varepsilon P(\Omega_\varepsilon) = \varepsilon P(\xi \geq \varepsilon).
\]

Доказанная теорема позволяет легко получить неравенство Чебышева.