---
source_image: page_314.png
page_number: 314
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.23
tokens: 6431
characters: 2130
timestamp: 2025-12-24T08:16:06.782607
finish_reason: stop
---

Остаётся заметить, что

\[
\bullet \sum_{\sigma \in S_p} (-1)^{\sigma \tau} x_{\tau(\sigma(1))} \otimes \ldots \otimes x_{\tau(p+q)} = p! \bullet (-1)^{\tau_1} x_{\tau_1(1)} \otimes \ldots \otimes x_{\tau_1(p+q)},
\]

где \( \tau_1 = (\tau(\sigma(1)), \ldots, \tau(\sigma(p)), \tau(p+1), \ldots, \tau(p+q)) \).

Аналогично доказывается, что \( A(T_1 \otimes T_2) = A(T_1 \otimes A(T_2)) \), поэтому

\[
(T_1 \wedge T_2) \wedge T_3 = A(A(T_1 \otimes T_2) \otimes T_3) = A(T_1 \otimes T_2 \otimes T_3) =
= A(T_1 \otimes A(T_2 \otimes T_3)) = T_1 \wedge (T_2 \wedge T_3).
\]

Ясно, что

\[
x_{p+1} \otimes \ldots \otimes x_{p+q} \otimes x_1 \otimes \ldots \otimes x_p = x_{\sigma(1)} \otimes \ldots \otimes x_{\sigma(p+q)},
\]

где \( \sigma = (p+1, \ldots, p+q, 1, \ldots, p) \). Чтобы в \( \sigma \) последовательно переставить элемент 1 на первое место, ..., элемент \( p \) на \( p \)-е место, требуется совершить \( pq \) транспозиций. Следовательно, \( (-1)^{\sigma} = (-1)^{pq} \) и \( A(T_1 \otimes T_2) = (-1)^{pq} A(T_2 \otimes T_1) \).

В алгебре \( \Lambda(V) \) \( k \)-я степень элемента \( \omega \) обозначается \( \Lambda^k \omega \), иными словами, \( \Lambda^k \omega = \omega \wedge \ldots \wedge \omega \) (к раз).

30.3. Кососимметрические функции

Кососимметрической функцией на \( V \times \ldots \times V \) называют полилинейную функцию \( f(v_1, \ldots, v_q) \), для которой

\[
f(v_{\sigma(1)}, \ldots, v_{\sigma(q)}) = (-1)^{\sigma} f(v_1, \ldots, v_q)
\]

для любой перестановки \( \sigma \).

Теорема 30.3.1. Пространство \( \Lambda^q V^* \) канонически изоморфно пространству кососимметрических функций на \( V \times \ldots \times V \), а также пространству \( (\Lambda^q V)^* \).

Доказательство. Легко проверить, что функция

\[
(f_1 \wedge \ldots \wedge f_q)(v_1, \ldots, v_q) =
= A(f_1 \otimes \ldots \otimes f_q)(v_1, \ldots, v_q) = \frac{1}{q!} \sum_{\sigma} (-1)^{\sigma} f_1(v_{\sigma(1)}) \ldots f_q(v_{\sigma(q)})
\]

— кососимметрическая. Если \( e_1, \ldots, e_n \) — базис пространства \( V \), то кососимметрическая функция \( f \) задаётся значениями \( f(e_{i_1}, \ldots, e_{i_q}) \),