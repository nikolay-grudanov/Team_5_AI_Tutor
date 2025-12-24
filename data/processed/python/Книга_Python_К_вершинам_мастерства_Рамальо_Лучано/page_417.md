---
source_image: page_417.png
page_number: 417
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.16
tokens: 11714
characters: 1870
timestamp: 2025-12-24T01:53:59.816025
finish_reason: stop
---

Операторы составного присваивания

>>> globe += 1
Traceback (most recent call last):
...
TypeError: right operand in += must be 'AddableBingoCage' or an iterable

1 Создаем синоним, чтобы можно было проверить идентификатор объекта позже.
2 Здесь globe содержит четыре элемента.
3 Объект AddableBingoCage может получать элементы от другого объекта того же класса.
4 Правый операнд += может быть любым итерируемым объектом.
5 В этом примере globe все время ссылается на объект globe_orig.
6 Попытка сложить AddableBingoCage с неитерируемым объектом приводит к исключению TypeError с надлежащим сообщением.

Отметим, что оператор += либеральнее, чем +, относится ко второму операнду. В случае + мы хотели, чтобы оба операнда имели одинаковый тип (в данном случае AddableBingoCage), потому что иначе было бы непонятно, какой тип должен иметь результат. Для += ситуация проще: левый объект обновляется на месте, поэтому тип результата не вызывает сомнений.

Различия в поведении операторов + и += я обосновал, наблюдая за работой встроенного типа list. Запись my_list + x позволяет конкатенировать только один список с другим, но если написать my_list += x, то в правой части может стоять любой итерируемый объект x. Это согласуется с поведением метода list.extend(): он принимает произвольный итерируемый аргумент.

Поняв, чего мы хотим от класса AddableBingoCage, рассмотрим его реализацию.

Пример 13.18. bingoaddable.py: класс AddableBingoCage расширяет BingoCage, добавляя поддержку операторов + и +=

import itertools

from tombola import Tombola
from bingo import BingoCage

class AddableBingoCage(BingoCage):

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):