---
source_image: page_046.png
page_number: 46
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.62
tokens: 7412
characters: 1944
timestamp: 2025-12-24T02:35:23.013669
finish_reason: stop
---

Встроенные имена (built-ins) — имена функций, классов или переменных, которые Python загружает автоматически, чтобы вам было проще обращаться к ним. В отличие от ключевых слов, Python позволяет использовать встроенное имя в качестве названия переменной без малейших возражений. Тем не менее поступать так не рекомендуется — это считается признаком плохого стиля.

Использование встроенного имени в качестве названия переменной приводит к замещению встроенного имени. Новое имя переменной не позволит получить доступ к исходному встроенному имени. Фактически вы берете встроенную переменную и заимствуете ее для собственного использования. В результате доступ к исходному встроенному имени будет возможен только через модуль __builtins__. Гораздо лучше с самого начала избегать замещения.

Ниже перечислены встроенные имена Python, которые не следует использовать в качестве имен переменных:

>>> dir(__builtins__)

['ArithmeticError', 'AssertionError',
'AttributeError', 'BaseException',
'BlockingIOError', 'BrokenPipeError',
'BufferError', 'BytesWarning', 'ChildProcessError',
'ConnectionAbortedError', 'ConnectionError',
'ConnectionRefusedError', 'ConnectionResetError',
'DeprecationWarning', 'EOFError', 'Ellipsis',
'EnvironmentError', 'Exception', 'False',
'FileExistsError', 'FileNotFoundError',
'FloatingPointError', 'FutureWarning',
'GeneratorExit', 'IOError', 'ImportError',
'ImportWarning', 'IndentationError', 'IndexError',
'InterruptedError', 'IsADirectoryError',
'KeyError', 'KeyboardInterrupt', 'LookupError',
'MemoryError', 'NameError', 'None',
'NotADirectoryError', 'NotImplemented',
'NotImplementedError', 'OSError', 'OverflowError',
'PendingDeprecationWarning', 'PermissionError',
'ProcessLookupError', 'RecursionError',
'ReferenceError', 'ResourceWarning',
'RuntimeError', 'RuntimeWarning',
'StopAsyncIteration', 'StopIteration',
'SyntaxError', 'SyntaxWarning', 'SystemError',
'SystemExit', 'TabError', 'TimeoutError', 'True',