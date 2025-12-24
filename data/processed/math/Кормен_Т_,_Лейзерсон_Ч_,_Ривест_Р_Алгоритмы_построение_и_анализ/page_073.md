---
source_image: page_073.png
page_number: 73
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 55.52
tokens: 11546
characters: 1931
timestamp: 2025-12-24T06:23:31.232207
finish_reason: stop
---

??? На картинке следует заменить минус на \setminus

Рисунок 5.1 Диаграмма Венна, иллюстрирующая первый из законов де Моргана (5.2). Множества \(A, B, C\) изображены кругами на плоскости.

Ассоциативность (associative laws):
\[
A \cap (B \cap C) = (A \cap B) \cap C, \qquad A \cup (B \cup C) = (A \cup B) \cup C.
\]

Дистрибутивность (distributive laws):
\[
A \cap (B \cup C) = (A \cap B) \cup (A \cap C), \\
A \cup (B \cap C) = (A \cup B) \cap (A \cup C)
\]
(5.1)

Законы поглощения (absorption laws):
\[
A \cap (A \cup B) = A, \qquad A \cup (A \cap B) = A
\]

Законы де Моргана (DeMorgan’s laws):
\[
A \setminus (B \cap C) = (A \setminus B) \cup (A \setminus C), \\
A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)
\]
(5.2)

Рис. 5.1 иллюстрирует первый из законов де Моргана (5.1); множества \(A, B\) и \(C\) изображены в виде кругов на плоскости.

Часто все рассматриваемые множества являются подмножества некоторого фиксированного множества, называемого универсумом (universe). Например, если нас интересуют множества, элементами которых являются целые числа, то в качестве универсума можно взять множество \(\mathbb{Z}\) целых чисел. Если универсум \(U\) фиксирован, можно определить дополнение (complement) множества \(A\) как \(\overline{A} = U \setminus A\). Для любого \(A \subseteq U\) верны такие утверждения:
\[
\overline{\overline{A}} = A, \qquad A \cap \overline{A} = \varnothing, \qquad A \cup \overline{A} = U.
\]

Из законов де Моргана (5.2) следует, что для любых множеств \(A, B \subseteq U\) имеют место равенства
\[
\overline{A \cap B} = \overline{A} \cup \overline{B}, \qquad \overline{A \cup B} = \overline{A} \cap \overline{B}.
\]

Два множества \(A\) и \(B\) называются непересекающимися (disjoint), если они не имеют общих элементов, т.е. если \(A \cap B = \varnothing\). Говорят, что семейство \(\mathcal{S} = \{S_i\}\) непустых множеств образует разбиение (partition) множества \(S\), если