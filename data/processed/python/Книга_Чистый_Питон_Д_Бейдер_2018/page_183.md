---
source_image: page_183.png
page_number: 183
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.74
tokens: 7369
characters: 1342
timestamp: 2025-12-24T02:31:33.640489
finish_reason: stop
---

>>> vowels
{'х', 'о', 'э', 'у', 'и', 'ы', 'е', 'е', 'ю', 'а', 'я'}

>>> len(vowels)
6

frozenset — неизменяемые множества

Класс frozenset реализует неизменяемую версию множества set. Такое множество не может быть изменено после того, как оно было сконструировано¹. Множества frozenset статичны и допускают только операции с запросами в отношении своих элементов (ни каких вставок или удалений). Поскольку множества frozenset статичны и хешируемы, они могут использоваться в качестве ключей словаря или в качестве элементов другого множества, а это то, что невозможно с обычными (изменяемыми) объектами-множествами set.

>>> vowels = frozenset({'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'е', 'ю', 'я'})
AttributeError:
"'frozenset' object has no attribute 'add'"

# Множества frozenset хешируемы и могут
# использоваться в качестве ключей словаря:
>>> d = { frozenset({1, 2, 3}): 'привет' }
>>> d[frozenset({1, 2, 3})]
'привет'

collections.Counter — мультимножества

Класс collections.Counter стандартной библиотеки Python реализует тип «мультимножество» (или «мешок»), который допускает неоднократное появление элемента в множестве².

¹ См. документацию Python «frozenset»: https://docs.python.org/3/library/stdtypes.html#frozenset
² См. документацию Python «collections.Counter»: https://docs.python.org/3/library/collections.html#counter-objects