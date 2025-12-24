---
source_image: page_094.png
page_number: 94
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.75
tokens: 8819
characters: 1533
timestamp: 2025-12-24T07:28:12.412480
finish_reason: stop
---

Тогда

\[
P(a_i < \xi < a'_i, b_j < \eta < b'_j) = P(\xi = x_i, \eta = y_j) = p_{ij},
\]
\[
P(a_i < \xi < a'_i) = p_{i.}, \quad P(b_j < \eta < b'_j) = p_{.j}.
\]

Отсюда и из (4.4) следует (4.5).

Достаточность. Пусть выполнено условие (4.5). Для произвольных полуинтервалов \([a_1, b_1), [a_2, b_2)\) нужно доказать (4.4). В \([a_1, b_1)\) попадут некоторые числа из множества \(\{x_1, x_2, \ldots, x_t, \ldots\}\). Обозначим
\[
X = (i_1, i_2, \ldots, i_s) = \{i : x_i \in [a_1, b_1)\}.
\]
В полуинтервал \([a_2, b_2)\) попадут числа из множества \(\{y_1, y_2, \ldots, y_j, \ldots\}\). Положим
\[
Y = (j_1, j_2, \ldots, j_t) = \{j : y_j \in [a_2, b_2)\}.
\]
Используя (4.5), получим
\[
P(a_1 \leq \xi < b_1, a_2 \leq \eta < b_2) =
= \sum_{i \in X} \sum_{j \in Y} p_{ij} = \sum_{i \in X} \sum_{j \in Y} p_{i.} p_{.j}.
\]
Так как
\[
\sum_{i \in X} \sum_{j \in Y} p_{i.} p_{.j} = \left( \sum_{i \in X} p_{i.} \right) \left( \sum_{j \in Y} p_{.j} \right)
\]
и
\[
P(a_1 \leq \xi < b_1) = \sum_{i \in X} p_{i.},
\]
\[
P(a_2 \leq \eta < b_2) = \sum_{j \in Y} p_{.j},
\]
то из (4.6), (4.7), (4.8) следует (4.4). Теорема доказана.

В примере 1 из § 3 случайные величины \(\xi, \eta\) независимы, так как равенства
\[
P(\xi = i, \eta = j) = P(\xi = i) P(\eta = j)
\]
выполняются при любых \(i, j\). Величины \(\xi, \eta\) в примере 2 того же параграфа зависимы, так как
\[
0 = P(\xi = 1, \eta = -1) \neq P(\xi = 1) P(\eta = -1) = \frac{1}{4}.
\]
Если для дискретных величин заданы одномерные распределения и еще известно, что величины незави-