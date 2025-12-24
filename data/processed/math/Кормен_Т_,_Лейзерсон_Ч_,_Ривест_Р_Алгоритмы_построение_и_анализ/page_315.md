---
source_image: page_315.png
page_number: 315
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 37.17
tokens: 11341
characters: 1210
timestamp: 2025-12-24T06:34:39.883513
finish_reason: stop
---

Наибольшая общая подпоследовательность

Рисунок 16.3 Таблицы c и b, созданные алгоритмом LCS-LENGTH при X = ⟨A, B, C, B, D, A, B⟩ и Y = ⟨B, D, C, A, B, A⟩. В клетке с координатами (i, j) записаны число c[i, j] и стрелка b[i, j]. Число 4 в правой нижней клетке есть длина НОП. При i, j > 0 значение c[i, j] определяется тем, равны ли x_i и y_j, и вычисленными ранее значениями c[i - 1, j], c[i, j - 1] и c[i - 1, j - 1]. Путь по стрелкам, ведущий из c[7, 6], заштрихован. Каждая косая стрелка на этом пути соответствует элементу НОП (эти элементы выделены).

LCS-LENGTH(X, Y)
1   m ← length[X]
2   n ← length[Y]
3   for i ← 1 to m
4     do c[i, 0] ← 0
5   for j ← 0 to n
6     do c[0, j] ← 0
7   for i ← 1 to m
8     do for j ← 1 to n
9       do if x_i = y_j
10         then c[i, j] ← c[i - 1, j - 1] + 1
11           b[i, j] ← "↖"
12         else if c[i - 1, j] ≥ c[i, j - 1]
13           then c[i, j] ← c[i - 1, j]
14             b[i, j] ← "↑"
15           else c[i, j] ← c[i, j - 1]
16             b[i, j] ← "←"
17   return c, b

На рис. 16.3 показана работа LCS-LENGTH для X = ⟨A, B, C, B, D, A, B⟩ и Y = ⟨B, D, C, A, B, A⟩.

Алгоритм LCS-LENGTH требует времени O(mn): на каждую клетку требуется O(1) шагов.