---
source_image: page_139.png
page_number: 139
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.84
tokens: 11217
characters: 1182
timestamp: 2025-12-24T06:26:30.043439
finish_reason: stop
---

Рисунок 7.2 Работа процедуры HEAPIFY(A, 2) при heap-size[A] = 10. (а) Начальное состояние кучи. В вершине i = 2 основное свойство нарушено. Чтобы восстановить его, необходимо поменять A[2] и A[4]. После этого (б) основное свойство нарушается в вершине с индексом 4. Рекурсивный вызов процедуры HEAPIFY(A, 4) восстанавливает основное свойство в вершине с индексом 4 путём перестановки A[4] ↔ A[9] (в). После этого основное свойство выполнено для всех вершин, так что процедура HEAPIFY(A, 9) уже ничего не делает.

HEAPIFY(A, i)
1   l ← LEFT(i)
2   r ← RIGHT(i)
3   if l ≤ heap-size[A] и A[l] > A[i]
4     then largest ← l
5     else largest ← i
6   if r ≤ heap-size[A] и A[r] > A[largest]
7     then largest ← r
8   if largest ≠ i
9     then обменять A[i] ↔ A[largest]
10    HEAPIFY(A, largest)

Работа процедуры HEAPIFY показана на рис. 7.2. В строках 3–7 в переменную largest помещается индекс наибольшего из элементов A[i], A[LEFT(i)] и A[RIGHT(i)]. Если largest = i, то элемент A[i] уже "погрузился" до нужного места, и работа процедуры закончена. Иначе процедура меняет местами A[i] и A[largest] (что обеспечивает выполнение свойства (7.1) в вершине i, но возможно, нарушает это