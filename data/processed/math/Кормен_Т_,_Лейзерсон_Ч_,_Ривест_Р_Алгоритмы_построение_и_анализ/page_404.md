---
source_image: page_404.png
page_number: 404
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.74
tokens: 11071
characters: 757
timestamp: 2025-12-24T06:38:48.205406
finish_reason: stop
---

Рисунок 20.6 Четыре случая в процедуре Binomial-Heap-Union. На всех рисунках вершина x — корень дерева B_k и l > k. (а) Случай 1: degree[x] ≠ degree[next-x]. Указатели продвигаются на одну позицию. (б) Случай 2: degree[x] = degree[next-x] = degree[sibling[next-x]]. И в этом случае указатели продвигаются, и при следующей итерации цикла возникнет случай 3 или 4. (в) Случай 3: degree[x] = degree[next-x] ≠ degree[sibling[next-x]], и key[x] ≤ key[next-x]. Мы удаляем вершину next-x из корневого списка и подвешиваем её к вершине x, получая дерево B_{k+1}. (г) Случай 4: degree[x] = degree[next-x] ≠ degree[sibling[next-x]], и key[next-x] < key[x]. Мы удаляем вершину x из корневого списка и подвешиваем её к вершине next-x, опять-таки получая дерево B_{k+1}.