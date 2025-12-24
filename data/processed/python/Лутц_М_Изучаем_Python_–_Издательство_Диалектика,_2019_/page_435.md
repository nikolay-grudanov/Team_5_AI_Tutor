---
source_image: page_435.png
page_number: 435
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.54
tokens: 7633
characters: 1994
timestamp: 2025-12-24T01:20:55.508492
finish_reason: stop
---

<enumerate object at 0x000000002A8B900>
>>> next(E)
(0, 's')
>>> next(E)
(1, 'p')
>>> next(E)
(2, 'a')

Обычно мы не видим данный механизм, т.к. все контексты итерации, в том числе списковые включения, рассматриваемые в главе 14, автоматически следуют протоколу итерации:

>>> [c * i for (i, c) in enumerate(S)]
['', 'p', 'aa', 'mmm']

>>> for (i, l) in enumerate(open('test.txt')):
...    print('%s %s' % (i, l.rstrip()))
...
0) aaaaaa
1) bbbbbb
2) ccccccc

Однако для полного понимания концепций итерации вроде enumerate, zip и списковых включений необходим более формальный анализ, который проводится в следующей главе.

Что потребует внимания: команды оболочки и другое

В предыдущей врезке были показаны циклы, примененные к файлам. Как кратко отмечалось в главе 9, связанный вызов os.popen в Python также предоставляет интерфейс, подобный файлам, для чтения вывода, порождаемого командами оболочки. Поскольку вы уже освоили операторы цикла, ниже приведен пример упомянутого инструмента в действии — чтобы запустить команду оболочки и прочитать текст из ее стандартного вывода, передайте команду в виде строки вызову os.popen и выполните чтение из возвращенного им объекта, подобного файлу (в случае возникновения проблемы с кодировкой Unicode решить ее может помочь обсуждение в главе 25):

>>> import os
>>> F = os.popen('dir')                # Чтение строки за строкой
>>> F.readline()
' Volume in drive C has no label.\n'
>>> F = os.popen('dir')                # Чтение блоками заданного размера
>>> F.read(50)
' Volume in drive C has no label.\n Volume Serial Nu'

>>> os.popen('dir').readlines()[0]     # Чтение всех строк: индексация
' Volume in drive C has no label.\n'
>>> os.popen('dir').read()[:50]         # Чтение всего сразу: срез
' Volume in drive C has no label.\n Volume Serial Nu'

>>> for line in os.popen('dir'):       # Цикл с файловым итератором строк
...    print(line.rstrip())
...
Volume in drive C has no label.
Volume Serial Number is D093-D1F7
...и так далее...