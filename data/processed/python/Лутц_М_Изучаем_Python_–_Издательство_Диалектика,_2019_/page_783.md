---
source_image: page_783.png
page_number: 783
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 20.97
tokens: 7438
characters: 1501
timestamp: 2025-12-24T01:31:34.350191
finish_reason: stop
---

Тестирование версий инструмента перезагрузки

Чтобы удостовериться в том, все три версии инструмента перезагрузки работают одинаково, давайте протестируем их. Благодаря общей функции тестирования мы можем запускать все три версии в командной строке без аргументов для проверки перезагрузки самого модуля и с именем модуля, подлежащего перезагрузке (в sys.argv):

c:\code> reloadall.py
reloading reloadall
reloading types

c:\code> reloadall2.py
reloading reloadall2
reloading types

c:\code> reloadall3.py
reloading reloadall3
reloading types

Несмотря на то что это трудно заметить, мы на самом деле протестировали альтернативные версии инструмента перезагрузки — в каждом тесте применяется общая функция tester, но ей передается reload_all из собственного файла. Далее демонстрируется перезагрузка всеми версиями модуля tkinter из Python 3.x и всех импортируемых в нем модулей:

c:\code> reloadall.py tkinter
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

c:\code> reloadall2.py tkinter
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

c:\code> reloadall3.py tkinter
reloading tkinter
reloading re
reloading copyreg
reloading _locale
reloading functools