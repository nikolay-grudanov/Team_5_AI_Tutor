---
source_image: page_085.png
page_number: 85
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.88
tokens: 7258
characters: 1211
timestamp: 2025-12-24T02:36:12.029071
finish_reason: stop
---

Другое решение — перебор по копии списка. Оно довольно легко реализуется конструкцией копирования среза [ : ], которая будет рассмотрена в главе, посвященной срезам:

```python
>>> names = ['John', 'Paul', 'George',
...    'Ringo']
>>> for name in names[:]: # copy of names
...     if name not in ['John', 'Paul']:
...         names.remove(name)

>>> print(names)
['John', 'Paul']
```

15.6. Блок else

Цикл for также может содержать блок else. Любой код в блоке else будет выполнен в том случае, если цикл for не достиг команды break. Следующий пример проверяет, являются ли числа из цикла положительными:

```python
>>> positive = False
>>> for num in items:
...     if num < 0:
...         break
... else:
...     positive = True
```

Команды continue не влияют на выполнение блока else.

Имя команды else выглядит несколько странно. Для цикла for она показывает, что была обработана вся последовательность. Блок else в цикле for часто применяется для обработки отсутствия элементов.

15.7. Циклы while

Python позволяет многократно выполнять блок кода, пока некоторое условие остается истинным. Такая конструкция называется циклом while, а для ее создания используется команда while. За циклом while следует