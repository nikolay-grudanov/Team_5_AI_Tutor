---
source_image: page_740.png
page_number: 740
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.65
tokens: 7672
characters: 2065
timestamp: 2025-12-24T01:30:16.452278
finish_reason: stop
---

В первом файле пакета предпринимается попытка импортировать второй файл с помощью нормального оператора import. Из-за того, что это считается относительным в Python 2.X, но абсолютным в Python 3.X, во втором случае возникает ошибка. То есть Python 2.X ищет сначала в содержащем пакете, а Python 3.X не ищет. О таком несовместимом поведении следует помнить, имея дело с Python 3.X:

C:\code> c:\Python27\python
>>> import pkg.spam
<module 'string' from 'C:\Python27\lib\string.pyc'>
99999

C:\code> c:\Python37\python
>>> import pkg.spam
ModuleNotFoundError: No module named 'pkg'
Ошибка отсутствия модуля: модуль по имени pkg не найден

Чтобы заставить пример работать в обеих линейках Python 2.X и Python 3.X, модифицируем первый файл для применения специального синтаксиса относительного импортирования, так что в Python 3.X тоже будет выполняться поиск в каталоге пакета:

# code\pkg\spam.py
from . import eggs    # <== Использовать относительное импортирование
#   в Python 2.X или Python 3.X
print(eggs.X)

# code\pkg\eggs.py
x = 99999
import string
print(string)

C:\code> c:\Python27\python
>>> import pkg.spam
<module 'string' from 'C:\Python27\lib\string.pyc'>
99999

C:\code> c:\Python37\python
>>> import pkg.spam
<module 'string' from 'C:\\Python37\\lib\\string.py'>
99999

Операции импортирования по-прежнему относительно к текущему рабочему каталогу

В предыдущем примере обратите внимание на то, что модули пакета все еще имеют доступ к стандартным библиотечным модулям вроде string — их нормальные операции импортирования по-прежнему относительно к элементам в пути поиска модулей. В действительноности, если вы снова добавите модуль string в текущий рабочий каталог, тогда операции импортирования в пакете найдут его там, а не в стандартной библиотеке. Хотя вы можете пропустить поиск в каталоге пакета посредством операции абсолютного импортирования в Python 3.X, вы не в состоянии пропустить поиск в домашнем каталоге программы, которая импортирует пакет:

# code\string.py
print('string' * 8)

# code\pkg\spam.py
from . import eggs
print(eggs.X)