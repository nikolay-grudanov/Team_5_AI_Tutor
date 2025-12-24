---
source_image: page_124.png
page_number: 124
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.58
tokens: 6481
characters: 2417
timestamp: 2025-12-24T08:10:51.747365
finish_reason: stop
---

Доказательство. Пусть \( C \) — ограничение отображения \( B \) на \( \operatorname{Im} A \). Тогда \( \dim \operatorname{Ker} C + \dim \operatorname{Im} C = \dim \operatorname{Im} A \), т. е.

\[
\dim (\operatorname{Im} A \cap \operatorname{Ker} B) + \dim \operatorname{Im} BA = \dim \operatorname{Im} A.
\]

Для доказательства второго из требуемых равенств достаточно заметить, что \( \dim \operatorname{Im} BA = \dim V - \dim \operatorname{Ker} BA \) и \( \dim \operatorname{Im} A = \dim V - \dim \operatorname{Ker} A \).

6.2. Альтернатива Фредгольма

Теорема 6.2.1. Ядро и образ оператора \( A \) и сопряжённого к нему оператора \( A^* \) связаны следующими соотношениями: \( \operatorname{Ker} A^* = (\operatorname{Im} A)^{\perp} \) и \( \operatorname{Im} A^* = (\operatorname{Ker} A)^{\perp} \).

Доказательство. Равенство \( A^* f = 0 \) означает, что \( f(Ax) = A^* f(x) = 0 \) для любого \( x \in V \), т. е. \( f \in (\operatorname{Im} A)^{\perp} \). Поэтому \( \operatorname{Ker} A^* = (\operatorname{Im} A)^{\perp} \), а так как \( (A^*)^* = A \), то \( \operatorname{Ker} A = (\operatorname{Im} A^*)^{\perp} \). Следовательно,

\[
(\operatorname{Ker} A)^{\perp} = ((\operatorname{Im} A^*)^{\perp})^{\perp} = \operatorname{Im} A^*.
\]

Следствие. \( \operatorname{rk} A = \operatorname{rk} A^* \).

Доказательство. Ясно, что

\[
\operatorname{rk} A^* = \dim \operatorname{Im} A^* = \dim (\operatorname{Ker} A)^{\perp} = \dim V - \dim \operatorname{Ker} A =
= \dim \operatorname{Im} A = \operatorname{rk} A.
\]

Замечание 1. Из равенства \( \operatorname{rk} A = \operatorname{rk} A^* \) легко получить другое доказательство того, что ранг матрицы по строкам равен рангу по столбцам (см. п. 2.2).

Замечание 2. Если \( V \) — пространство со скалярным произведением, то \( V^* \) можно отождествить с \( V \) и тогда \( V = \operatorname{Im} A \oplus (\operatorname{Im} A)^{\perp} = \operatorname{Im} A \oplus \operatorname{Ker} A^* \). Аналогично \( V = \operatorname{Im} A^* \oplus \operatorname{Ker} A \). (В матричной записи \( A^* = A^T \).)

Теорема 6.2.2 (альтернатива Фредгольма). Пусть \( A : V \to V \) — линейный оператор. Рассмотрим 4 уравнения:

(1) \( Ax = y,\quad x, y \in V; \)
(2) \( A^* f = g,\quad f, g \in V^*; \)
(3) \( Ax = 0; \)
(4) \( A^* f = 0. \)

Тогда либо уравнения (1) и (2) разрешимы при любых правых частях, причём в этом случае решение единствено, либо уравнения (3) и (4)