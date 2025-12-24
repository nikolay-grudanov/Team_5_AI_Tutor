---
source_image: page_303.png
page_number: 303
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.82
tokens: 6203
characters: 1723
timestamp: 2025-12-24T08:15:32.040286
finish_reason: stop
---

Глава 5
Полилинейная алгебра

§ 29. Полилинейные отображения.
Тензорные произведения

29.1. Определения

Пусть \( V, V_1, \ldots, V_k \) — линейные пространства; \( \dim V_i = n_i \). Отображение \( f : V_1 \times \ldots \times V_k \to V \), где \( V_1 \times \ldots \times V_k \) — прямое произведение множеств \( V_1, \ldots, V_k \), называют полилинейным (или \( k \)-линейным), если оно линейно по каждой из \( k \) переменных при фиксированных остальных переменных.

Выберем в пространствах \( V_1, \ldots, V_k \) базисы \( \{e_{1i}\}, \ldots, \{e_{kj}\} \). Если \( f \) — полилинейное отображение, то

\[
f(\bullet x_{1i} e_{1i}, \ldots, \bullet x_{kj} e_{kj}) = \bullet x_{1i} \ldots x_{kj} f(e_{1i}, \ldots, e_{kj}).
\]

Отображение \( f \) задаётся своими \( n_1 \ldots n_k \) значениями \( f(e_{1i}, \ldots, e_{kj}) \in V \), причём эти значения могут быть любыми. Рассмотрим пространство \( V_1 \otimes \ldots \otimes V_k \) размерности \( n_1 \ldots n_k \), базисные элементы которого обозначим \( e_{1i} \otimes \ldots \otimes e_{kj} \). Рассмотрим, далее, отображение

\[
p : V_1 \times \ldots \times V_k \to V_1 \otimes \ldots \otimes V_k,
\]

заданное формулой

\[
p(\bullet x_{1i} e_{1i}, \ldots, \bullet x_{kj} e_{kj}) = \bullet x_{1i} \ldots x_{kj} e_{1i} \otimes \ldots \otimes e_{kj};
\]

элемент \( p(v_1, \ldots, v_k) \) обозначим \( v_1 \otimes \ldots \otimes v_k \). Каждому полилинейному отображению \( f \) соответствует линейное отображение

\[
\tilde{f} : V_1 \otimes \ldots \otimes V_k \to V,
\]

где \( \tilde{f}(e_{1i} \otimes \ldots \otimes e_{kj}) = f(e_{1i}, \ldots, e_{kj}) \); соответствие между полилинейными отображениями \( f \) и линейными отображениями \( \tilde{f} \) взаимно од-