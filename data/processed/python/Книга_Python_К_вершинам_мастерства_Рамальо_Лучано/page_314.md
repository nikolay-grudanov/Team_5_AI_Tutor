---
source_image: page_314.png
page_number: 314
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.50
tokens: 11652
characters: 1490
timestamp: 2025-12-24T01:48:48.877559
finish_reason: stop
---

Глава 10. Рубим, перемешиваем и нарезаем последовательности

Пример 10.11. Три способа вычислить результат применения оператора ИСКЛЮЧАЮЩЕЕ ИЛИ к целым числам от 0 до 5

```python
>>> n = 0
>>> for i in range(1, 6): # 1
...     n ^= i
...
>>> n
1
>>> import functools
>>> functools.reduce(lambda a, b: a^b, range(6)) # 2
1
>>> import operator
>>> functools.reduce(operator.xor, range(6)) # 3
1
```

1 Агрегирование в цикле for в накопительную переменную.
2 functools.reduce с анонимной функцией.
3 functools.reduce с заменой специально написанного лямбда-выражения функцией operator.xor.

Из представленных вариантов мне больше всего нравится последний, а на втором месте стоит цикл for. А вам как кажется?

На стр. 188 мы видели, что модуль operator предоставляет функциональность всех инфиксных операторов Python в форме функций, снижая потребность в лямбда-выражениях.

Чтобы написать метод Vector.__hash__ в том стиле, который я предпочитаю, необходимо импортировать модули functools и operator. Изменения показаны в примере 10.12.

Пример 10.12. Часть файла vector_v4.py: в класс Vector из файла vector_v3.py добавлены два предложения импорта и метод hash

```python
from array import array
import reprlib
import math
import functools # 1
import operator # 2

class Vector:
    typecode = 'd'

    # много строк опущено...

    def __eq__(self, other): # 3
        return tuple(self) == tuple(other)

    def __hash__(self):
        hashes = (hash(x) for x in self._components) # 4
```