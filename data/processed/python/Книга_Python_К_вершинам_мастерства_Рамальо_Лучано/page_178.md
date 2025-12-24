---
source_image: page_178.png
page_number: 178
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.68
tokens: 11790
characters: 2101
timestamp: 2025-12-24T01:42:53.563534
finish_reason: stop
---

>>> clip.__code__.co_varnames
('text', 'max_len', 'end', 'space_before', 'space_after')
>>> clip.__code__.co_argcount

Как видим, организация информации не блещет удобством. Имена аргументов находятся в атрибуте __code__.co_varnames, но там же хранятся имена локальных переменных, созданных в теле функции. Таким образом, имена аргументов — это первые N строк, где N равно значению __code__.co_argcount, и, кстати говоря, в их число не входят переменные аргументы с префиксами * и **. Значения по умолчанию определяются исключительно по позиции в кортеже __defaults__, поэтому чтобы связать значение с соответствующим аргументом, необходимо просматривать от начала к концу. В данном примере есть два аргумента, text и max_len, и одно значение по умолчанию, 80, поэтому оно должно ассоциироваться с последним аргументом max_len. Очень неудобно.

По счастью, есть способ лучше: модуль inspect.
Взгляните на пример 5.17.

Пример 5.17. Получение сигнатуры функции

>>> from clip import clip
>>> from inspect import signature
>>> sig = signature(clip)
>>> sig # doctest: +ELLIPSIS
<inspect.Signature object at 0x...>
>>> str(sig)
'(text, max_len=80)'
>>> for name, param in sig.parameters.items():
...     print(param.kind, ':', name, '=', param.default)
...
POSITIONAL_OR_KEYWORD : text = <class 'inspect._empty'>
POSITIONAL_OR_KEYWORD : max_len = 80

Так гораздо лучше. Метод inspect.signature возвращает объект inspect.
Signature, у которого есть атрибут parameters, позволяющий прочитать упорядоченное отображение имен на объекты типа inspect.Parameter. У каждого объекта Parameter есть набор атрибутов, например: name, default и kind. Специальное значение inspect._empty обозначает параметры, не имеющие значений по умолчанию, и это разумно, если принять во внимание, что None — допустимое и даже весьма популярное значение по умолчанию.

Атрибут kind может принимать одно из пяти значений типа _ParameterKind:

POSITIONAL_OR_KEYWORD
Параметр может быть передан как позиционный или как именованный (большинство параметров функций в Python именно таковы).

VAR_POSITIONAL
Кортеж позиционных параметров.