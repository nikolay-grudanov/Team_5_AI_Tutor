---
source_image: page_784.png
page_number: 784
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.17
tokens: 7626
characters: 2108
timestamp: 2025-12-24T01:31:40.655903
finish_reason: stop
---

reloading sre_parse
reloading sre_compile
reloading _sre
reloading enum
reloading sys
reloading tkinter.constants
reloading _tkinter
reloading sys
reloading enum

Все три версии инструмента перезагрузки работают в Python 3.x и 2.x — они обеспечивают унифицированный вывод и избегают использования средств, специфичных для версии (хотя в случае Python 2.x потребуется указать имя модуля Tkinter):

c:\code> py -2 reloadall.py
reloading reloadall
reloading types

c:\code> py -2 reloadall2.py Tkinter
reloading Tkinter
reloading _tkinter
reloading FixTk
...и так далее...

Как обычно, мы можем также выполнять тестирование интерактивно, импортируя и вызывая либо главную точку входа с объектом модуля, либо функцию тестирования с передачей ей функций перезагрузки и строки с именем модуля:

C:\code> py -3
>>> import reloadall, reloadall2, reloadall3
>>> import tkinter
>>> reloadall.reload_all(tkinter)        # Нормальное использование
reloading tkinter
reloading enum
reloading sys
...и так далее...
>>> reloadall.tester(reloadall2.reload_all, 'tkinter')   # Функция тестирования
reloading tkinter
reloading enum
reloading sys
...и так далее...
>>> reloadall.tester(reloadall3.reload_all, 'reloadall3')   # Имитация кода
# самотестирования
reloading reloadall3
reloading types

Наконец, если вы заглянете в показанный ранее вывод перезагрузок tkinter, то можете заметить, что все три версии могут выдавать результаты в отличающемся порядке, все они зависят от упорядочения словарей пространств имен, а последние две полагаются на порядок, в котором элементы добавляются в их стек. Фактически в Python 3.3, например, порядок перезагрузки отдельной версии инструмента мог даже варьироваться от запуска к запуску. Чтобы удостовериться в том, что все три версии перезагружают те же самые модули безотносительно к порядку, в котором они это делают, мы можем применить множества (или сортировку) для реализации нейтральной к порядку проверки выводимых сообщений на предмет эквивалентности (сообщения здесь получаются за счет запуска команд оболочки с помощью вызова os.popen, который встречался в главах 13 и 21):