---
source_image: page_780.png
page_number: 780
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.74
tokens: 7593
characters: 2056
timestamp: 2025-12-24T01:31:34.442833
finish_reason: stop
---

Предварительный обзор оператора try был дан в главе 10, а полностью он рассматривается в части VII.

Тестирование рекурсивной перезагрузки

Теперь, чтобы применить созданный модуль в нормальных условиях, импортируем его функцию reload_all и передадим ей объект уже загруженного модуля — в точности как делалось бы для встроенной функции reload. Когда файл запускается автономно, его код самотестирования автоматически вызывает reload_all, по умолчанию перезагружая собственный модуль, если аргументы командной строки не указаны. В таком режиме модуль обязан импортировать сам себя, потому что без операции импортирования его собственное имя в файле не определено. Код работает в Python 3.X и Python 2.X, поскольку при выводе мы используем + и % вместо запятой, хотя список применяемых и, следовательно, перезагружаемых модулей может варьироваться между линейками:

C:\code> c:\Python37\python reloadall.py
reloading reloadall
reloading types

c:\code> C:\Python27\python reloadall.py
reloading reloadall
reloading types

При наличии аргумента командной строки функция tester взамен перезагружает указанный модуль по строке с его именем — здесь модуль pybench, созданный в главе 21. Обратите внимание, что в этом режиме мы передаем имя модуля, а не имя файла (как и в операторах импортирования расширение .py не включается); в конечном итоге сценарий импортирует модуль, обычным образом используя путь поиска модулей:

c:\code> reloadall.py pybench
reloading pybench
reloading sys
reloading os
reloading abc
reloading stat
reloading ntpath
reloading genericpath
reloading timeit
reloading gc
reloading time
reloading itertools

Чаще всего мы можем вводить в действие модуль reloadall в интерактивной подсказке — ниже демонстрируется пример для нескольких стандартных библиотечных модулей в Python 3.7 (в Python 2.X вместо tkinter укажите Tkinter):

>>> from reloadall import reload_all
>>> import os, tkinter
>> reload_all(os)    # Нормальный режим использования
reloading os
reloading abc
reloading sys
reloading stat
reloading ntpath
reloading genericpath