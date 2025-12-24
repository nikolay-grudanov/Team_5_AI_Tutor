---
source_image: page_753.png
page_number: 753
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.62
tokens: 7754
characters: 2271
timestamp: 2025-12-24T01:30:35.053571
finish_reason: stop
---

>>> mod1
<module 'sub.mod1' from 'C:\\code\\ns\\dir1\\sub\\mod1.py'>
>>> sub.mod2
<module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>

Сказанное также справедливо, если мы импортируем через имя пакета пространства имен непосредственно — поскольку пакет пространства имен создается, когда впервые достигается, синхронизация расширений пути к делу не относится:

c:\code> C:\Python37\python
>>> import sub.mod1
dir1\sub\mod1
>>> import sub.mod2    # Один пакет охватывает два каталога
dir2\sub\mod2
>>> sub.mod1
<module 'sub.mod1' from 'C:\\code\\ns\\dir1\\sub\\mod1.py'>
>>> sub.mod2
<module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>
>>> sub
<module 'sub' (namespace)>
>>> sub.__path__
_namespacePath(['C:\\code\\ns\\dir1\\sub', 'C:\\code\\ns\\dir2\\sub'])

Интересно отметить, что операции относительного импортирования тоже работают с пакетами пространств имен — следующий оператор относительного импортирования ссылается на файл в пакете, хотя указанный файл находится в другом каталоге.

c:\code> type ns\dir1\sub\mod1.py
from . import mod2    # И from . import string по-прежнему терпит неудачу
print(r'dir1\sub\mod1')

c:\code> C:\Python37\python
>>> import sub.mod1    # Относительное импортирование mod2 из другого каталога
dir2\sub\mod2
dir1\sub\mod1
>>> import sub.mod2    # Уже импортированный модуль не выполняется повторно
>>> sub.mod2
<module 'sub.mod2' from 'C:\\code\\ns\\dir2\\sub\\mod2.py'>

Как видите, пакеты пространств имен похожи на обыкновенные пакеты с единственным каталогом во всех отношениях кроме наличия расщепленного физического хранилища — вот почему пакеты пространств имен с единственным каталогом без файлов __init__.py в точности подобны обычным пакетам, но без инициализационной логики, подлежащей выполнению.

Вложение пакетов пространств имен

Пакеты пространств имен даже поддерживают произвольное вложение — после того как пакет пространства имен создан, он на своем уровне исполняет по существу ту же самую роль, что и sys.path на верхнем уровне, становясь "родительским путем" для более низких уровней. Продолжим пример из предыдущего раздела:

c:\code> mkdir ns\dir2\sub\lower   # Дальнейшие вложенные компоненты
c:\code> type ns\dir2\sub\lower\mod3.py
print(r'dir2\sub\lower\mod3')
c:\code> C:\Python37\python