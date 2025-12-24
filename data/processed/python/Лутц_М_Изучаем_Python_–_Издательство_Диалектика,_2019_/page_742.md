---
source_image: page_742.png
page_number: 742
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.52
tokens: 7670
characters: 2168
timestamp: 2025-12-24T01:30:18.995465
finish_reason: stop
---

C:\code> c:\Python27\python
>>> import pkg.spam
NiNiNiNiNiNiNiNi
<module 'pkg.string' from 'pkg\string.py'>

Операции относительного импортирования выполняют поиск только в пакетах

Также важно отметить, что синтаксис относительного импортирования в действительности является объявлением привязки, а не просто предпочтением. Если теперь мы удалим файл string.py и любой ассоциированный байт-код в данном примере, то операция относительного импортирования в spam.py потерпит отказ в Python 3.x и 2.x вместо того, чтобы использовать версию этого модуля из стандартной библиотеки (или любую другую):

# code\pkg\spam.py
from . import string    # <== Терпит неудачу в Python 2.x и 3.x,
                        # если здесь отсутствует string.py!
C:\code> del pkg\string*
C:\code> C:\python37\python
>>> import pkg.spam
ModuleNotFoundError: No module named 'string'
Ошибка отсутствия модуля: модуль по имени string не найден
C:\code> C:\python27\python
>>> import pkg.spam
ImportError: cannot import name string
Ошибка импортирования: не удалось импортировать имя string

Модули, на которые производится ссылка в операциях относительного импортирования, должны существовать в каталоге пакета.

Операции относительного импортирования по-прежнему относительно к текущему рабочему каталогу (снова)

Несмотря на то что операции абсолютного импортирования позволяют таким способом пропускать модули пакета, они все еще полагаются на другие компоненты sys.path. В качестве последнего теста давайте определим два собственных модуля string. В следующем примере есть один модуль с таким именем в текущем рабочем каталоге, один в пакете и еще один в стандартной библиотеке:

# code\string.py
print('string' * 8)
# code\pkg\spam.py
from . import string    # <== Относительный в Python 2.x и 3.x
print(string)
# code\pkg\string.py
print('Ni' * 8)

Когда мы импортируем модуль string с помощью синтаксиса относительного импортирования вроде показанного, то ожидаемым образом получаем версию в пакете в обеих линейках Python 2.x и 3.x:

C:\code> c:\Python37\python    # В Python 2.x такой же результат
>>> import pkg.spam
NiNiNiNiNiNiNiNiNi
<module 'pkg.string' from '.\\pkg\\string.py'>