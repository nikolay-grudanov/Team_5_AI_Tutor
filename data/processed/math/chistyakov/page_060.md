---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.39
tokens: 7904
characters: 1458
timestamp: 2025-12-24T07:27:18.721346
finish_reason: stop
---

3) \( p(l_3|l_1l_2) \geq 0, \sum_{l_3=1}^N p(l_3|l_1l_2) = 1 \) при любых \( l_1, l_2; \)

n) \( p(l_n|l_1, \ldots, l_{n-1}) \geq 0, \sum_{l_n=1}^N p(l_n|l_1, \ldots, l_{n-1}) = 1 \)
при любых \( l_1, l_2, \ldots, l_{n-1} \).

Символ \( l_k, k = 1, 2, \ldots, n, \) в обозначении элементарного события \( (l_1l_2 \ldots l_n) \) будем интерпретировать как наступление исхода \( l_k \) в испытании с номером \( k \).
Формула (1.6.6) с числами

\[
p_{u_1(l_1) \ldots u_n(l_n)} = p(l_1l_2 \ldots l_n)
\]

задает распределение вероятностей, если

\[
\sum_{l_1, \ldots, l_n=1}^N p(l_1l_2 \ldots l_n) = 1.
\] (1.6)

Для доказательства (1.6) заметим, что

\[
\sum_{l_1, \ldots, l_n=1}^N p(l_1l_2 \ldots l_n) = \sum_{l_1 \ldots l_{n-1}=1}^N \left( \sum_{l_n=1}^N p(l_1l_2 \ldots l_n) \right) =
\]
\[
= \sum_{l_1 \ldots l_{n-1}=1}^N p(l_1) \ldots p(l_{n-1}|l_1 \ldots l_{n-2}) \times
\]
\[
\times \left( \sum_{l_n=1}^N p(l_n|l_1 \ldots l_{n-1}) \right) =
\]
\[
= \sum_{l_1 \ldots l_{n-1}=1}^N p(l_1) p(l_2|l_1) \ldots p(l_{n-1}|l_1 \ldots l_{n-2}),
\]

так как \( \sum_{l_n=1}^N p(l_n|l_1 \ldots l_{n-1}) = 1 \) согласно (1.5). Далее мы можем выделить сумму по \( l_{n-1} \) и вновь воспользоваться (1.5). Повторив этот процесс \( n \) раз, получим (1.6). Таким образом, мы определили вероятностное пространство, являющееся математической моделью последовательности из \( n \) испытаний. Нетрудно проверить, что число \( p(l_k|l_1l_2 \ldots l_{k-1}) \) является услов-