---
source_image: page_327.png
page_number: 327
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.45
tokens: 6799
characters: 3065
timestamp: 2025-12-24T08:16:33.769233
finish_reason: stop
---

§ 32. Разложимые тензоры

Следствие. Любому разложимому кососимметрическому тензору \( \omega = x_1 \wedge \ldots \wedge x_k \) можно сопоставить \( k \)-мерное подпространство \( \langle x_1, \ldots, x_k \rangle \); это подпространство не зависит от разложения, а зависит лишь от самого тензора \( \omega \).

Теорема 32.1.2. Пусть \( W_1 \) и \( W_2 \) — подпространства в \( V \) размерности \( p_1 \) и \( p_2 \); им соответствуют \( \omega_1 \in \Lambda^{p_1}(V) \) и \( \omega_2 \in \Lambda^{p_2}(V) \).
а) \( W_1 \subset W_2 \) тогда и только тогда, когда существует \( \omega \in \Lambda^{p_2 - p_1}(V) \), для которого \( \omega_1 \wedge \omega = \omega_2 \).
б) \( W_1 \cap W_2 = 0 \) тогда и только тогда, когда \( \omega_1 \wedge \omega_2 \neq 0 \). При этом \( \omega_1 \wedge \omega_2 \) соответствует подпространству \( W_1 \oplus W_2 \).

Доказательство. а) Пусть \( W_1 \subset W_2 \). Выберем в \( W_1 \) базис \( e_1, \ldots, e_{p_1} \) и дополним его до базиса \( e_1, \ldots, e_{p_2} \) пространства \( W_2 \). Тогда \( \omega_1 = e_1 \wedge \ldots \wedge e_{p_1}, \omega_2 = e_1 \wedge \ldots \wedge e_{p_2} \) и \( \omega = e_{p_1} \wedge \ldots \wedge e_{p_2} \). Обратное утверждение очевидно.
б) Пусть \( W_1 = \langle e_1, \ldots, e_p \rangle \) и \( W_2 = \langle e_{p+1}, \ldots, e_q \rangle \). Векторы \( e_1, \ldots, e_{p+q} \) линейно независимы тогда и только тогда, когда
\[
e_1 \wedge \ldots \wedge e_{p+q} \neq 0.
\]

Теорема 32.1.3. Если \( S(x_1 \otimes \ldots \otimes x_k) = S(y_1 \otimes \ldots \otimes y_k) \neq 0 \), то
\[
\langle x_1, \ldots, x_k \rangle = \langle y_1, \ldots, y_k \rangle.
\]

Доказательство [Ме]. Предположим, например, что \( y_1 \notin \langle x_1, \ldots, x_k \rangle \). Пусть \( T = S(x_1 \otimes \ldots \otimes x_k) \) — ненулевой тензор. Любой полилинейной функции \( f : V \times \ldots \times V \to K \) соответствует линейная функция \( \tilde{f} : V \otimes \ldots \otimes V \to K \). Тензор \( T \) ненулевой, поэтому существует такая линейная функция \( \tilde{f} \), что \( \tilde{f}(T) \neq 0 \). Полилинейная функция \( f \) является линейной комбинацией произведений линейных функций, поэтому существуют такие линейные функции \( g_1, \ldots, g_k \), что \( \tilde{g}(T) \neq 0 \), где \( g = g_1 \ldots g_k \). Рассмотрим линейные функции \( h_1, \ldots, h_k \), совпадающие с \( g_1, \ldots, g_k \) на подпространстве \( \langle x_1, \ldots, x_k \rangle \) и принимающие значение 0 на векторе \( y_1 \); пусть \( h = h_1 \ldots h_k \). Тогда \( \tilde{h}(T) = \tilde{g}(T) \neq 0 \). С другой стороны, \( T = S(y_1 \otimes \ldots \otimes y_k) \), поэтому
\[
\tilde{h}(T) = \bigotimes_{\sigma} h_1(y_{\sigma(1)}) \ldots h_k(y_{\sigma(k)}) = 0,
\]
так как в любое произведение входит \( h_i(y_1) = 0 \). Получено противоречие, поэтому \( y_1 \in \langle x_1, \ldots, x_k \rangle \). Аналогичные рассуждения показывают, что \( \langle y_1, \ldots, y_k \rangle \subset \langle x_1, \ldots, x_k \rangle \) и \( \langle x_1, \ldots, x_k \rangle \subset \langle y_1, \ldots, y_k \rangle \).