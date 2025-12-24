---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 59.68
tokens: 11595
characters: 2352
timestamp: 2025-12-24T06:33:06.211727
finish_reason: stop
---

RB-DELETE-FIXUP(T, x)
1   while \( x \neq root[T] \) и \( color[x] = BLACK \)
2     do if \( x = left[p[x]] \)
3       then \( w \leftarrow right[p[x]] \)
4         if \( color[w] = RED \)
5           then \( color[w] \leftarrow BLACK \) ▷ Случай 1
6             \( color[p[x]] \leftarrow RED \) ▷ Случай 1
7             LEFT-ROTATE(T, p[x]) ▷ Случай 1
8             \( w \leftarrow right[p[x]] \) ▷ Случай 1
9           if \( color[left[w]] = BLACK \) и \( color[right[w]] = BLACK \)
10             then \( color[w] \leftarrow RED \) ▷ Случай 2
11               \( x \leftarrow p[x] \) ▷ Случай 2
12           else if \( color[right[w]] = BLACK \)
13             then \( color[left[w]] \leftarrow BLACK \) ▷ Случай 3
14               \( color[w] \leftarrow RED \) ▷ Случай 3
15               RIGHT-ROTATE(T, w) ▷ Случай 3
16               \( w \leftarrow right[p[x]] \) ▷ Случай 3
17               \( color[w] \leftarrow color[p[x]] \) ▷ Случай 4
18               \( color[p[x]] \leftarrow BLACK \) ▷ Случай 4
19               \( color[right[w]] \leftarrow BLACK \) ▷ Случай 4
20               LEFT-ROTATE(T, p[x]) ▷ Случай 4
21               \( x \leftarrow root[T] \) ▷ Случай 4
22           else (симметричный фрагмент с заменой \( left \leftrightarrow right \))
23   \( color[x] \leftarrow BLACK \)

Если удалённая процедурой RB-DELETE вершина y была чёрной, то любой путь, через неё проходивший, теперь содержит на одну чёрную вершину меньше. Таким образом, свойство 4 нарушилось. Мы можем компенсировать это за счёт вершины x (занявшей место вершины y). Если x — красная, сделаем её чёрной (заодно мы избежаем опасности получить красную вершину с красным родителем). Если x — чёрная, объявим её "дважды чёрной" и будем считать за две при подсчёте числа чёрных вершин на пути от корня к листьям. Конечно, такой выход может быть лишь временным, поскольку определение красно-чёрных деревьев не предусматривает дважды чёрных вершин, и мы должны постепенно от такой вершины избавиться.

Процедура RB-DELETE-FIXUP(T, x) применяется к дереву, которое обладает свойствами красно-чёрного дерева, если учесть дополнительную единицу черноты в вершине x, и превращает его в настоящее красно-чёрное дерево. В цикле (строки 1–22) дерево меняется, и значение переменной x тоже меняется (выделенная вершина может сдвигаться вверх по дереву), но сформулированное