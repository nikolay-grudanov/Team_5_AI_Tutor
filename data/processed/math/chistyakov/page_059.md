---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.38
tokens: 5613
characters: 1603
timestamp: 2025-12-24T07:27:18.662618
finish_reason: stop
---

Тогда

\[
B_1 = \{A_1 A_2 \overline{A}_3, \quad A_1 \overline{A}_2 \overline{A}_3\},
\]
\[
B_2 = \{A_1 A_2 A_3, \quad A_1 \overline{A}_2 A_3, \quad \overline{A}_1 A_2 \overline{A}_3, \quad \overline{A}_1 \overline{A}_2 A_3\},
\]
\[
B_3 = \{\overline{A}_1 A_2 A_3, \quad \overline{A}_1 \overline{A}_2 A_3\}
\]

и

\[
P(B_1) = \frac{14}{125}, \quad P(B_2) = \frac{60}{125}, \quad P(B_3) = \frac{51}{125}.
\]

Вероятность сохранения состава шаров — 60/125. Таким образом, более вероятно изменение состава шаров в первой урне, но наиболее вероятным составом является первоначальный состав. В решенной задаче легко проверить, что (1.2) определяют распределения вероятностей. Дадим теперь общее определение последовательности из n испытаний, в каждом из которых может произойти один из N исходов. Исходы в каждом испытании занумеруем числами: 1, 2, ..., N. Под последовательностью из n испытаний мы будем понимать (см. гл. 1 § 6.2) дискретное вероятностное пространство (\( \Omega, \mathcal{F}, P \)), в котором

\[
\Omega = \{(l_1 l_2 \ldots l_n)\}, \quad l_k = 1, 2, \ldots, N; \quad k = 1, \ldots, n,
\]

и вероятности \( p(l_1 l_2 \ldots l_k) \), приписываемые элементарным событиям \( \omega = (l_1 l_2 \ldots l_n) \), задаются формулой

\[
p(l_1 l_2 \ldots l_n) = p(l_1) p(l_2 | l_1) p(l_3 | l_1 l_2) \ldots p(l_n | l_1 \ldots l_{n-1}),
\]

где числа \( p(l_1), \ p(l_2 | l_1), \ldots, \ p(l_n | l_1 l_2 \ldots l_{n-1}) \) удовлетворяют условиям:

1) \( p(l_1) \geqslant 0, \quad \sum_{l_1=1}^N p(l_1) = 1; \)
2) \( p(l_2 | l_1) \geqslant 0, \quad \sum_{l_2=1}^N p(l_2 | l_1) = 1 \) при любом \( l_1; \)