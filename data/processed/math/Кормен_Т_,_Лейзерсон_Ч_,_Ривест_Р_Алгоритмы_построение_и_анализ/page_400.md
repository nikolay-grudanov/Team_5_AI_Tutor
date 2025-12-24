---
source_image: page_400.png
page_number: 400
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 71.46
tokens: 11628
characters: 2057
timestamp: 2025-12-24T06:39:28.788566
finish_reason: stop
---

**BINOMIAL-LINK(y, z)**

1. \( p[y] \leftarrow z \)
2. \( sibling[y] \leftarrow child[z] \)
3. \( child[z] \leftarrow y \)
4. \( degree[z] \leftarrow degree[z] + 1 \)

Время работы этой процедуры — \( O(1) \) (удачным образом оказывается, что вершину \( y \) надо добавить в начало списка детей вершины \( z \), что легко сделать в представлении "левый ребёнок, правый сосед").

Теперь напишем процедуру **BINOMIAL-HEAP-UNION**, которая объединяет биномиальные кучи \( H_1 \) и \( H_2 \) (сами кучи при этом исчезают). Помимо процедуры **BINOMIAL-LINK**, нам понадобится процедура **BINOMIAL-HEAP-MERGE**, которая сливает корневые списки куч \( H_1 \) и \( H_2 \) в единый список, вершины в котором идут в порядке возрастания степеней. (Эта процедура аналогична процедуре **MERGE** из раздела 1.3.1, и её мы оставляем читателю в качестве упр. 20.2-2.)

**BINOMIAL-HEAP-UNION(\( H_1, H_2 \))**

1. \( H \leftarrow \text{MAKE-BINOMIAL-HEAP}() \)
2. \( head[H] \leftarrow \text{BINOMIAL-HEAP-MERGE}(H_1, H_2) \)
3. освободить память, занятую под \( H_1 \) и \( H_2 \)
   (сохранив списки, на которые указывают \( H_1 \) и \( H_2 \))
4. **if** \( head[H] = \text{NIL} \)
5. **then return** \( H \)
6. \( prev-x \leftarrow \text{NIL} \)
7. \( x \leftarrow head[H] \)
8. \( next-x \leftarrow sibling[x] \)
9. **while** \( next-x \neq \text{NIL} \)
10. **do if** (\( degree[x] \neq degree[next-x] \)) or
    (\( sibling[next-x] \neq \text{NIL} \)
     and \( degree[sibling[next-x]] = degree[x] \))
11. **then** \( prev-x \leftarrow x \) ▷ Случай 1 и 2
12. \( x \leftarrow next-x \) ▷ Случай 1 и 2
13. **else if** \( key[x] \leq key[next-x] \)
14. **then** \( sibling[x] \leftarrow sibling[next-x] \) ▷ Случай 3
    **BINOMIAL-LINK**(next-x, x) ▷ Случай 3
15. **else if** \( prev-x = \text{NIL} \)
16. **then** \( head[H] \leftarrow next-x \) ▷ Случай 4
17. **else** \( sibling[prev-x] \leftarrow next-x \) ▷ Случай 4
18. **BINOMIAL-LINK**(x, next-x) ▷ Случай 4
19. \( x \leftarrow next-x \) ▷ Случай 4
20. \( next-x \leftarrow sibling[x] \)
21. **return** \( H \)