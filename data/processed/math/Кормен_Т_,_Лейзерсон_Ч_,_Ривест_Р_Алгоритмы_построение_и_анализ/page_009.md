---
source_image: page_009.png
page_number: 9
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.98
tokens: 11120
characters: 787
timestamp: 2025-12-24T06:20:08.563397
finish_reason: stop
---

Рисунок 1.1  Сортировка карт вставками

INSERTION-SORT(A)
1   for j ← 2 to length[A]
2     do key ← A[j]
3       ▷ добавить A[j] к отсортированной части A[1..j−1].
4         i ← j − 1
5         while i > 0 and A[i] > key
6           do A[i + 1] ← A[i]
7             i ← i − 1
8         A[i + 1] ← key

Рисунок 1.2  Работа процедуры INSERTION-SORT для входа \( A = \langle 5, 2, 4, 6, 1, 3 \rangle \).
Позиция \( j \) показана кружком.

На рис. 1.2 показана работа алгоритма при \( A = \langle 5, 2, 4, 6, 1, 3 \rangle \). Индекс \( j \) указывает "очередную карту" (только что взятую со стола). Участок \( A[1..j-1] \) составляют уже отсортированные карты (левая рука), а \( A[j+1..n] \) — ещё не просмотренные. В цикле for индекс \( j \) пробегает массив слева направо. Мы берём элемент