---
source_image: page_171.png
page_number: 171
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.51
tokens: 11684
characters: 1730
timestamp: 2025-12-24T01:42:32.012973
finish_reason: stop
---

Пользовательские вызываемые типы

>>> abs, str, 13
(<built-in function abs>, <class 'str'>, 13)
>>> [callable(obj) for obj in (abs, str, 13)]
[True, True, False]

Теперь займемся созданием экземпляров классов, ведущих себя как вызываемые объекты.

Пользовательские вызываемые типы

Мало того что в Python функции являются настоящими объектами, так еще и любой объект можно заставить вести себя как функция. Для этого нужно лишь реализовать метод экземпляра __call__.
В примере 5.8 реализован класс BingoCage. Экземпляр этого класса строится из любого итерируемого объекта и хранит внутри себя список элементов в случайном порядке. При вызове экземпляра из списка удаляется один элемент.

Пример 5.8. bingocall.py: экземпляр BingoCage делает всего одну вещь: выбирает элементы из перетасованного списка

import random

class BingoCage:

    def __init__(self, items):
        self._items = list(items) ①
        random.shuffle(self._items) ②

    def pick(self): ③
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage') ④

    def __call__(self): ⑤
        return self.pick()

① Метод __init__ принимает произвольный итерируемый объект; создание локальной копии предотвращает изменение списка, переданного в качестве аргумента.
② Метод shuffle гарантированно работает, потому что self._items — объект типа list.
③ Основной метод.
④ Возбудить исключение со специальным сообщением, если список self._items пуст.
⑤ Позволяет писать просто bingo() вместо bingo.pick().

Ниже приведена простая демонстрация этого кода. Обратите внимание, что объект bingo можно вызывать как функцию, и встроенная функция callable(...) распознает его как вызываемый объект: