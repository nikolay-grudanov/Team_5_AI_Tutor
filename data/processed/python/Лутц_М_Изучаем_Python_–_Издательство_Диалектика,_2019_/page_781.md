---
source_image: page_781.png
page_number: 781
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.49
tokens: 7572
characters: 1822
timestamp: 2025-12-24T01:31:37.782278
finish_reason: stop
---

>>> reload_all(tkinter)
reloading tkinter
reloading enum
reloading sys
reloading _tkinter
reloading tkinter.constants
reloading re
reloading sre_compile
reloading _sre
reloading sre_parse
reloading functools
reloading _locale
reloading copyreg

Наконец, далее представлен сеанс, в котором сравнивается нормальная и транзитивная перезагрузка — изменения, внесенные в два вложенных файла, подхватываются только при транзитивной перезагрузке:

import b    # Файл a.py
X = 1
import c    # Файл b.py
Y = 2
Z = 3        # Файл c.py
C:\code> py -3
>>> import a
>>> a.X, a.b.Y, a.b.c.Z
(1, 2, 3)

# Не останавливая Python, измените присваиваемые значения
# во всех трех файлах и сохраните их
>>> from imp import reload
>>> reload(a)                # Встроенная функция reload выполняет
                             # перезагрузку только на верхнем уровне
<module 'a' from '.\\a.py'>
>>> a.X, a.b.Y, a.b.c.Z
(111, 2, 3)
>>> from reloadall import reload_all
>>> reload_all(a)             # Нормальный режим использования
reloading a
reloading b
reloading c
>>> a.X, a.b.Y, a.b.c.Z      # Перезагружает также и все вложенные модули
(111, 222, 333)

Изучите код инструмента перезагрузки и результаты его запуска, чтобы больше узнать о его работе. В следующем разделе мы продолжим его развивать.

Альтернативные реализации

Для поклонников рекурсии ниже показана альтернативная рекурсивная версия функции из предыдущего раздела — для обнаружения циклов в ней применяется множество, она чуть более прямая из-за устранения цикла верхнего уровня и служит общей иллюстрацией методик с рекурсивными функциями (сравните ее с первоначальной версией, чтобы выяснить отличия). Данная версия получает часть работы даром от первоначальной, хотя порядок перезагрузки модулей может меняться, если также меняется порядок в словарях пространств имен: