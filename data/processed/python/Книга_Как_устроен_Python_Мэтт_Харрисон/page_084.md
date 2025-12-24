---
source_image: page_084.png
page_number: 84
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.35
tokens: 7338
characters: 1434
timestamp: 2025-12-24T02:36:13.718921
finish_reason: stop
---

Например, если вы захотите отфильтровать список имен так, чтобы в нем остался только элемент 'John' или 'Paul', делать это так было бы неправильно:

```python
>>> names = ['John', 'Paul', 'George',
...     'Ringo']
>>> for name in names:
...     if name not in ['John', 'Paul']:
...         names.remove(name)

>>> print(names)
['John', 'Paul', 'Ringo']
```

Что произошло? Python предполагает, что списки не изменяются в процессе перебора. Добравшись до 'George', цикл удаляет имя из списка. Во внутренней реализации Python отслеживает текущий индекс цикла for. На этот момент в списке остаются только три элемента: 'John', 'Paul' и 'Ringo'. Однако цикл for думает, что текущей является позиция с индексом 3 (четвертый элемент), а четвертого элемента не существует, поэтому цикл останавливается, и элемент 'Ringo' остается на месте.

Существует два альтернативных решения для удаления элементов из списка в процессе перебора. В первом варианте удаляемые элементы отбираются при первом проходе по списку. Следующий цикл перебирает только те элементы, которые подлежат удалению (names_to_remove), и удаляет их из исходного списка (names):

```python
>>> names = ['John', 'Paul', 'George',
...     'Ringo']
>>> names_to_remove = []
>>> for name in names:
...     if name not in ['John', 'Paul']:
...         names_to_remove.append(name)

>>> for name in names_to_remove:
...     names.remove(name)

>>> print(names)
['John', 'Paul']
```