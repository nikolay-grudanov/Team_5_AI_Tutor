---
source_image: page_047.png
page_number: 47
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.99
tokens: 7390
characters: 1587
timestamp: 2025-12-24T02:35:22.892940
finish_reason: stop
---

'TypeError', 'UnboundLocalError',
'UnicodeDecodeError', 'UnicodeEncodeError',
'UnicodeError', 'UnicodeTranslateError',
'UnicodeWarning', 'UserWarning', 'ValueError',
'Warning', 'ZeroDivisionError', '_',
'__build_class__', '__debug__', '__doc__',
'__import__', '__loader__', '__name__',
'__package__', '__spec__', 'abs', 'all', 'any',
'ascii', 'bin', 'bool', 'bytearray', 'bytes',
'callable', 'chr', 'classmethod', 'compile',
'complex', 'copyright', 'credits', 'delattr',
'dict', 'dir', 'divmod', 'enumerate', 'eval',
'exec', 'exit', 'filter', 'float', 'format',
'frozenset', 'getattr', 'globals', 'hasattr',
'hash', 'help', 'hex', 'id', 'input', 'int',
'isinstance', 'issubclass', 'iter', 'len',
'license', 'list', 'locals', 'map', 'max',
'memoryview', 'min', 'next', 'object', 'oct',
'open', 'ord', 'pow', 'print', 'property', 'quit',
'range', 'repr', 'reversed', 'round', 'set',
'setattr', 'slice', 'sorted', 'staticmethod',
'str', 'sum', 'super', 'tuple', 'type', 'vars',
'zip']

СОВЕТ

Несколько встроенных имен, которые выглядят особенно соблазнительно в качестве имен переменных: dict, id, list, min, max, open, range, str, sum и type.

6.7. Итоги

В Python все сущности являются объектами. Объекты обладают состоянием, которое также называется значением. Для работы с объектами используются переменные. Переменные Python напоминают бирки: они связываются с объектом и обладают именем. Однако объект содержит важные данные: значение и тип данных.

В этой главе также рассматривается повторное связывание переменных с объектами. Python допускает такую возможность, но вы должны быть