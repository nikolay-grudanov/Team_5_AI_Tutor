---
source_image: page_567.png
page_number: 567
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.51
tokens: 7688
characters: 2141
timestamp: 2025-12-24T01:24:54.664686
finish_reason: stop
---

тов **аргументы для эмуляции большинства того, что делает функция print из Python 3.x. Вообще говоря, в Python 3.x могли бы предложить код подобного рода как вариант, не удаляя print из Python 2.x, но взамен было решено полностью порвать с прошлым.

Как объяснялось в главе 11, в действительности это не требуется, потому что программисты на Python 2.x всегда могут включить функцию print из Python 3.x с помощью импортирования в следующей форме (доступного в версиях Python 2.6 и 2.7):

from __future__ import print_function

Тем не менее, чтобы продемонстрировать сопоставление аргументов в целом, в файле print3.py, содержимое которого приведено ниже, делается та же самая работа в небольшой порции многократно используемого кода путем построения выводимой строки с учетом конфигурационных аргументов:

#!/python
"""
Эмулирует большую часть функции print из Python 3.x для применения в Python 2.x (и Python 3.x).
Сигнатура вызова: print3(*args, sep=' ', end='\n', file=sys.stdout)
"""
import sys
def print3(*args, **kargs):
    sep = kargs.get('sep', ' ') # Keyword arg defaults
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

Чтобы протестировать функцию print3, ее необходимо импортировать в другом файле или в интерактивной подсказке и применять подобно функции print из Python 3.x. Вот содержимое тестового сценария testprint3.py (обратите внимание, что функция должна называться print3, потому что print — зарезервированное слово в Python 2.x):

from print3 import print3
print3(1, 2, 3)
print3(1, 2, 3, sep='')
print3(1, 2, 3, sep='...')
print3(1, [2], (3,), sep='...')
print3(4, 5, 6, sep='', end='')
print3(7, 8, 9)
print3() # Добавление символа новой строки (или пустой строки)
import sys
print3(1, 2, 3, sep='??', end='.\\n', file=sys.stderr) # Перенаправление в файл

Запустив testprint3.py под управлением Python 2.x, мы получаем те же результаты, которые дает функция print из Python 3.x:

C:\code> c:\python27\python testprint3.py
1 2 3
123