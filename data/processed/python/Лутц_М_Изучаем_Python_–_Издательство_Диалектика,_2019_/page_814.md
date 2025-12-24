---
source_image: page_814.png
page_number: 814
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.60
tokens: 7709
characters: 1956
timestamp: 2025-12-24T01:32:37.568487
finish_reason: stop
---

>>> countdown(20)
20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 stop
# Нерекурсивные варианты:
>>> list(range(5, 0, -1))
[5, 4, 3, 2, 1]
# Только в Python 3.x:
>>> t = [print(i, end=' ') for i in range(5, 0, -1)]
5 4 3 2 1
>>> t = list(map(lambda x: print(x, end=' '), range(5, 0, -1)))
5 4 3 2 1

Из соображений гуманности я не хотел включать в решение этого упражнения вариант на основе генератора, но все-таки он приведен ниже; в данном случае все остальные методики выглядят гораздо более простыми — хороший пример ситуации, когда лучше избегать использования генераторов. Не забывайте, что генераторы не производят результатов до прохода по ним, поэтому здесь нужен оператор for или yield from (yield from работает, только начиная с версии Python 3.3):

def countdown2(N):
    if N == 0:
        yield 'stop'
    else:
        yield N
        for x in countdown2(N-1): yield x  # Python 3.3+:
        # yield from countdown2(N-1)

>>> list(countdown2(5))
[5, 4, 3, 2, 1, 'stop']
# Nonrecursive options:
>>> def countdown3():
    yield from range(5, 0, -1)  # Генераторная функция, более простая
    # До версии Python 3.3:
    # for x in range(): yield x
>>> list(countdown3())
[5, 4, 3, 2, 1]
>>> list(x for x in range(5, 0, -1))  # Эквивалентное генераторное выражение
[5, 4, 3, 2, 1]
>>> list(range(5, 0, -1))  # Эквивалентная негенераторная форма
[5, 4, 3, 2, 1]

12. Вычисление факториалов. Ниже показано мое решение этого упражнения; оно выполняется под управлением Python 3.x и 2.x, а в строковом литерале в конце приведен вывод, полученный в Python 3.7. Естественно, существует множество возможных вариаций такого кода; например, range можно было бы вызывать для 2..N+1, чтобы пропустить итерацию, а в fact2 можно было бы применять reduce(operator.mul, range(N, 1, -1)), избежав использования lambda.

#!/python
from __future__ import print_function  # Файл factorials.py
from functools import reduce
from timeit import repeat
import math