---
source_image: page_193.png
page_number: 193
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.92
tokens: 7328
characters: 1427
timestamp: 2025-12-24T02:31:54.542449
finish_reason: stop
---

>>> q = []
>>> q.append('есть')
>>> q.append('спать')
>>> q.append('программировать')

>>> q
['есть', 'спать', 'программировать']

# Осторожно: это очень медленная операция!
>>> q.pop(0)
'есть'

collections.deque — быстрые и надежные очереди

Класс deque реализует очередь с двусторонним доступом, которая поддерживает добавление и удаление элементов с любого конца за \( O(1) \) (неамортизируемое) время. Поскольку двусторонние очереди одинаково хорошо поддерживают добавление и удаление элементов с любого конца, они могут служить в качестве очередей и в качестве стеков\(^1\).

Объекты Python deque реализованы как двунаправленные связные списки (doubly-linked lists)\(^2\). Это придает им превосходную и стабильную производительность для операций вставки и удаления элементов, но при этом плохую \( O(n) \) производительность для произвольного доступа к элементам в середине очереди.

Как результат, двусторонняя очередь collections.deque будет хорошим выбором, если вы ищете структуру данных очередь в стандартной библиотеке Python.

>>> from collections import deque
>>> q = deque()
>>> q.append('есть')
>>> q.append('спать')
>>> q.append('программировать')

\footnotetext{1}{См. документацию Python «collections.deque»: https://docs.python.org/3.6/library/collections.html#collections.deque}
\footnotetext{2}{См. CPython «_collectionsmodule.c»: https://github.com/python/cpython/blob/master/Modules/_collectionsmodule.c}