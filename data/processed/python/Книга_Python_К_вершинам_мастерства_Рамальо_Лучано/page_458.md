---
source_image: page_458.png
page_number: 458
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.46
tokens: 11805
characters: 1865
timestamp: 2025-12-24T01:55:50.981829
finish_reason: stop
---

В примере 14.21 демонстрируется использование функций itertools.groupby и the reversed. Отметим, что itertools.groupby ожидает, что входной итерируемый объект отсортирован в соответствии с критерием группировки или, по крайней мере, что элементы, удовлетворяющие этому критерию, идут подряд, пусть даже и не по порядку.

Пример 14.21. itertools.groupby

```python
>>> list(itertools.groupby('LLLLAAGGG')) # 1
[('L', <itertools._grouper object at 0x102227cc0>),
 ('A', <itertools._grouper object at 0x102227b38>),
 ('G', <itertools._grouper object at 0x102227b70>)]
>>> for char, group in itertools.groupby('LLLLAAAGG'): # 2
...     print(char, '->', list(group))
...
L -> ['L', 'L', 'L', 'L']
A -> ['A', 'A',]
G -> ['G', 'G', 'G']
>>> animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
...             'bat', 'dolphin', 'shark', 'lion']
>>> animals.sort(key=len) # 3
>>> animals
['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark',
'giraffe', 'dolphin']
>>> for length, group in itertools.groupby(animals, len): # 4
...     print(length, '->', list(group))
...
3 -> ['rat', 'bat']
4 -> ['duck', 'bear', 'lion']
5 -> ['eagle', 'shark']
7 -> ['giraffe', 'dolphin']
>>> for length, group in itertools.groupby(reversed(animals), len): # 5
...     print(length, '->', list(group))
...
7 -> ['dolphin', 'giraffe']
5 -> ['shark', 'eagle']
4 -> ['lion', 'bear', 'duck']
3 -> ['bat', 'rat']
```

1 groupby отдает кортежи (key, group_generator).
2 Для работы с генераторами, порожденными groupby, необходимы вложенные итерации: в данном случае внешний цикл for и внутренний конструктор list.
3 Для использования groupby входной объект должен быть отсортирован; в данном случае слова отсортированы по длине.
4 Еще один цикл по парам (key, group), чтобы вывести ключ и развернуть группу в список.
5 Здесь генератор reversed используется для обхода animals справа налево.