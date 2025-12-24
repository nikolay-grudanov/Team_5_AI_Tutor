---
source_image: page_155.png
page_number: 155
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.77
tokens: 11783
characters: 1989
timestamp: 2025-12-24T01:41:43.674588
finish_reason: stop
---

Двухрежимный API

менты типа bytes, и при этом они возвращают значения типа bytes. Это позволяет работать с любыми именами файлов и путями, сколько бы в них ни было крокозябров. См. пример 4.23.

Пример 4.23. Функция listdir с аргументами типа str и bytes и ее результаты

```python
>>> os.listdir('.')
['abc.txt', 'digits-of-π.txt']
>>> os.listdir(b'.')
[b'abc.txt', b'digits-of-\xcf\x80.txt']
```

1 Второе имя файла равно «digits-of-π.txt» (с греческой буквой «пи»).
2 Если аргумент имеет типа bytes, то listdir возвращает имена файлов как байты: b'\xcf\x80' — представление греческой буквы «пи» в кодировке UTF-8.

Чтобы помочь обрабатывать последовательности типа str или bytes, составляющие имена файлов или пути, модуль os предоставляет специальные функции кодирования и декодирования.

fsencode(filename)
Преобразует filename (может иметь тип str или bytes) в bytes с помощью кодека, возвращаемого функцией sys.getfilesystemencoding(), если filename имеет тип str, в противном случае возвращает аргумент filename (типа bytes) без изменения.

fsdecode(filename)
Преобразует filename (может иметь тип str или bytes) в str с помощью кодека, возвращаемого функцией sys.getfilesystemencoding(), если filename имеет тип bytes, в противном случае возвращает аргумент filename (типа str) без изменения.

На платформах, ведущих происхождение от Unix, эти функции пользуются обработчиком ошибок surrogateescape (см. врезку ниже), чтобы неожиданные байты не приводили к аварийному завершению. В Windows используется обработчик ошибок strict.

Использование surrogateescape для борьбы с крокозябрами
На случай встречи неожиданных байтов или неизвестной кодировки в версии Python 3.1 появился обработчик ошибок кодека surrogateescape, описанный в документе «PEP 383 — Non-decodable Bytes in System Character Interfaces» (https://www.python.org/dev/peps/pep-0383/).
Идея заключается в том, чтобы заменить байты, которые невозможно декодировать, кодовой позицией из диапазона от U+DC00 до U+DCFF,