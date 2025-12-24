---
source_image: page_775.png
page_number: 775
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.40
tokens: 7677
characters: 2044
timestamp: 2025-12-24T01:31:10.470677
finish_reason: stop
---

Обратите внимание на строку документации в начале. Как и в предыдущем примере formats.py, из-за того, что мы хотим применять его как универсальный инструмент, строка документации предоставляет функциональную информацию, доступную через help и режимы графического пользовательского интерфейса или браузера PyDoc — инструмента, который в своей работе использует похожие средства самоанализа. В конце модуля также предоставляется код самотестирования, который импортирует и строит листинг для самого модуля mydir. Ниже приведен вывод, полученный в Python 3.7; сценарий работает и в Python 2.X (где листинг может содержать меньшее количество имен) по причине импортирования функции вывода из __future__:

c:\code> py -3 mydir.py

name: mydir file: C:\Code\mydir.py

00) __builtins__ <built-in name>
01) __cached__ <built-in name>
02) __doc__ <built-in name>
03) __file__ <built-in name>
04) __loader__ <built-in name>
05) __name__ <built-in name>
06) __package__ <built-in name>
07) __spec__ <built-in name>
08) listing <function listing at 0x02DBAAE0>
09) print_function _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 65536)
10) sepchr -
11) seplen 60

mydir has 12 names

Чтобы применять модуль mydir в качестве инструмента получения листингов для других модулей, функции listing этого модуля необходимо передавать объекты других модулей. Далее показан листинг атрибутов в модуле для построения графических пользовательских интерфейсов tkinter (Tkinter в Python 2.X) из стандартной библиотеки; формально mydir будет работать с любым объектом, имеющим атрибуты __name__, __file__ и __dict__:

>>> import mydir
>>> import tkinter
>>> mydir.listing(tkinter)

name: tkinter file: F:\Python37\lib\tkinter\_init__.py

00) ACTIVE active
01) ALL all
02) ANCHOR anchor
03) ARC arc
04) BASELINE baseline
... остальные имена не показаны...
155) image_types <function image_types at 0x00E784B0>
156) mainloop <function mainloop at 0x00E64108>
157) re <module 're' from 'F:\\Python37\\lib\\re.py'>
158) sys <module 'sys' (built-in)>
159) wantobjects 1