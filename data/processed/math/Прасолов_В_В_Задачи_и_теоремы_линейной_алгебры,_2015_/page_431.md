---
source_image: page_431.png
page_number: 431
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.68
tokens: 6293
characters: 1857
timestamp: 2025-12-24T08:19:14.089101
finish_reason: stop
---

Глава 8
Матрицы в алгебре и анализе

§ 46. Кватернионы и числа Кэли.
Алгебры Клиффорда

46.1. Удвоение алгебры

Пусть \( \mathcal{A} \) — алгебра с единицей над \( \mathbb{R} \), в которой задана операция сопряжения \( a \mapsto \overline{a} \), обладающая следующими свойствами: \( \overline{\overline{a}} = a \) и \( \overline{ab} = \overline{b} \, \overline{a} \).

Рассмотрим пространство \( \mathcal{A} \oplus \mathcal{A} = \{ (a, b) \mid a, b \in \mathcal{A} \} \) и зададим в нём умножение по формуле

\[
(a, b)(u, v) = (au - \overline{v}b, b\overline{u} + va).
\]

Полученную алгебру называют удвоением алгебры \( \mathcal{A} \). Эта конструкция интересна тем, что алгебра комплексных чисел \( \mathbb{C} \) является удвоением алгебры \( \mathbb{R} \), алгебра кватернионов \( \mathbb{H} \) является удвоением алгебры \( \mathbb{C} \), а алгебра Кэли \( \mathbb{O} \) является удвоением алгебры \( \mathbb{H} \).

Легко проверить, что элемент \( (1, 0) \) является двусторонней единицей. Пусть \( e = (0, 1) \). Тогда \( (b, 0)e = (0, b) \), поэтому, отождествив элемент \( x \) алгебры \( \mathcal{A} \) с элементом \( (x, 0) \) удвоения алгебры \( \mathcal{A} \), получим разложение \( (a, b) = a + be \).

В удвоении алгебры \( \mathcal{A} \) операцию сопряжения можно задать формулой

\[
(\overline{a}, \overline{b}) = (\overline{a}, -b),
\]

т. е. \( \overline{a + be} = \overline{a} - be \). Если \( x = a + be \) и \( y = u + ve \), то

\[
\overline{xy} = \overline{au} + \overline{(be)u} + \overline{a(ve)} + \overline{(be)(ve)} = \overline{u}\overline{a} - \overline{u}(be) - (ve)\overline{a} + (ve)(be) = \overline{y}\overline{x}.
\]

Легко проверить, что \( ea = \overline{a}e \) и \( a(be) = (ba)e \) для \( a, b \in \mathcal{A} \). Поэтому удвоение алгебры \( \mathcal{A} \) некоммутативно, если сопряжение в \( \mathcal{A} \) не тожде-