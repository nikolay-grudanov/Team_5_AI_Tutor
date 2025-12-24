---
source_image: page_328.png
page_number: 328
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.60
tokens: 7310
characters: 1439
timestamp: 2025-12-24T08:54:06.765396
finish_reason: stop
---

менять к нему метод append(). Когда список будет построен, его можно будет преобразовать в строку помощью метода join(). Приведенный ниже код дает тот же результат, что и в предыдущем примере, но гораздо быстрее.

>>> building = []
>>> for c in 'Hello world!':
...     building.append(c)
...
>>> building = ''.join(building)
>>> print(building)

Применение списков вместо строк позволяет значительно ускорить работу программы. Разницу в быстродействии можно замерить с помощью функции time.time(). Откройте в редакторе файлов новое окно и введите в нем следующий код.

stringTest.py

import time

startTime = time.time()
for trial in range(10000):
    building = ''
    for i in range(10000):
        building += 'x'
print('String concatenation: ', (time.time() - startTime))

startTime = time.time()
for trial in range(10000):
    building = []
    for i in range(10000):
        building.append('x')
    building = ''.join(building)
print('List appending:      ', (time.time() - startTime))

Сохраните программу в файле stringTest.py и запустите ее. Результаты будут примерно такими.

String concatenation:   40.317070960998535
List appending:         10.488219022750854

В переменную startTime записывается текущее время, после чего выполняется цикл, в котором к строке присоединяется 10 000 символов путем конкатенации. По завершении цикла программа сообщает общее время, затраченное на эту операцию. Далее в переменную startTime вновь