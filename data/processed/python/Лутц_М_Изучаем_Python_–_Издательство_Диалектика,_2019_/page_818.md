---
source_image: page_818.png
page_number: 818
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.93
tokens: 7659
characters: 2284
timestamp: 2025-12-24T01:32:40.169212
finish_reason: stop
---

Вероятно, именно здесь я бы начал подумывать об использовании аргументов командной строки или пользовательского ввода для предоставления имени файла, подлежащего подсчету, вместо его жесткого кодирования в сценарии (sys.argv более подробно рассматривается в главе 25, а ввод обсуждается в главе 10 — и применяйте raw_input в Python 2.x):

if __name__ == '__main__':
    print(test(input('Enter file name:')))  # Консоль (raw_input в Python 2.x)
if __name__ == '__main__':
    import sys  # Командная строка
    print(test(sys.argv[1]))

4. Вложенные операции импортирования. Вот мое решение (файл myclient.py):

from mymod import countLines, countChars
print(countLines('mymod.py'), countChars('mymod.py'))

% python myclient.py
13 346

Что касается остатка, то функции mymod доступны (т.е. импортируемы) из верхнего уровня myclient, поскольку from просто присваивает их именам в импортере (он работает, как если бы операторы def модуля mymod находились в myclient). Например, в другом файле может быть следующее:

import myclient
myclient.countLines(...)

from myclient import countChars
countChars(...)

Если в myclient вместо from используется import, тогда для того, чтобы добраться до функций модуля mymod из myclient, потребуется указывать путь:

import myclient
myclient.mymod.countLines(...)

from myclient import mymod
mymod.countChars(...)

В общем случае вы можете определять модули накопителей, которые импортируют все имена из других модулей, чтобы они были доступными в единственном удобном модуле. Скажем, в показанном ниже коде создаются три разных копии имени somename — mod1.somename, collector.somename и __main__.somename; изначально все три разделяют тот же самый объект целого числа и только имя somename существует в интерактивной подсказке в том виде как есть:

# Файл mod1.py
somename = 42

# Файл collector.py
from mod1 import *  # Накопить здесь множество имен
from mod2 import *  # from присваивает имена
from mod3 import *
>>> from collector import somename

5. Операции импортирования пакетов. Для этого я поместил файл решения mymod.py упражнения 3 в каталог пакета. Далее описаны мои действия в консоли Windows по настройке каталога и файла __init__.py, который был обязательным до версии Python 3.3; вам понадобится интерполировать их для других плат-