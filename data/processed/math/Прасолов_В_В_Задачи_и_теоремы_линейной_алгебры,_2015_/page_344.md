---
source_image: page_344.png
page_number: 344
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.85
tokens: 6305
characters: 1823
timestamp: 2025-12-24T08:16:52.542871
finish_reason: stop
---

Доказательство. Пусть \( f(u_1, \ldots, u_k) \neq 0 \) и \( f(v_1, \ldots, v_k) \neq 0 \). Тогда в силу линейности в каждой строке таблицы

<table>
  <tr>
    <th>\( f(u_1, u_2, \ldots, u_k) \)</th>
    <th>\( f(v_1, u_2, \ldots, u_k) \)</th>
    <th>\( f(u_1 + v_1, u_2, \ldots, u_k) \)</th>
  </tr>
  <tr>
    <th>\( f(u_1, v_2, \ldots, v_k) \)</th>
    <th>\( f(v_1, v_2, \ldots, v_k) \)</th>
    <th>\( f(u_1 + v_1, v_2, \ldots, v_k) \)</th>
  </tr>
</table>

не более одного нулевого вектора, поэтому найдётся столбец с ненулевыми векторами. Следовательно, можно выбрать \( t_1 \in V_1 \) так, что \( f(t_1, u_2, \ldots, u_k) \neq 0 \) и \( f(t_1, v_2, \ldots, v_k) \neq 0 \). Пространство \( \langle f(u_1, u_2, \ldots, u_k) \rangle \) имеет размерность 1, поэтому \( \langle f(u_1, u_2, \ldots, u_k) \rangle = \langle f(t_1, u_2, \ldots, u_k) \rangle \). Аналогично \( \langle f(v_1, v_2, \ldots, v_k) \rangle = \langle f(t_1, v_2, \ldots, v_k) \rangle \). Затем аналогично выбираем \( t_2 \in V_2 \) так, что \( \langle f(t_1, u_2, \ldots, u_k) \rangle = \langle f(t_1, t_2, u_3, \ldots, u_k) \rangle \) и \( \langle f(t_1, v_2, \ldots, v_k) \rangle = \langle f(t_1, t_2, v_3, \ldots, v_k) \rangle \). Продолжая такие рассуждения, получаем

\[
\langle f(u_1, u_2, \ldots, u_k) \rangle = \langle f(t_1, t_2, \ldots, t_k) \rangle = \langle f(v_1, v_2, \ldots, v_k) \rangle,
\]

что и требовалось.

Следствие. Если \( \dim V = 2 \), то образ полилинейного отображения

\[
f : V_1 \times \ldots \times V_k \to V
\]

является линейным подпространством.

Доказательство. Если размерность хотя бы одного ассоциированного линейного отображения равна 2, то образ полилинейного отображения \( f \) совпадает с \( V \). Если же размерности всех ассоциированных линейных отображений меньше 2, то можно применить теорему 35.2.1.