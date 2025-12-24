---
source_image: page_345.png
page_number: 345
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.37
tokens: 11745
characters: 2117
timestamp: 2025-12-24T01:50:17.147243
finish_reason: stop
---

Создание подкласса ABC

Пример 11.8. frenchdeck2.py: FrenchDeck2, подкласс collections.MutableSequence

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value): # ①
        self._cards[position] = value

    def __delitem__(self, position): # ②
        del self._cards[position]

    def insert(self, position, value): # ③
        self._cards.insert(position, value)

① Метод __setitem__ — все, что нам нужно для поддержки тасования...
② Но чтобы создать подкласс MutableSequence, нам придется реализовать также __delitem__ — абстрактный метод, определенный в этом ABC.
③ Также необходимо реализовать insert, третий абстрактный метод MutableSequence.

На этапе импорта (когда модуль frenchdeck2.py загружается и компилируется) Python не проверяет, реализованы ли абстрактные методы. Это происходит только на этапе выполнения, когда мы пытаемся создать объект FrenchDeck2. И тогда, если абстрактный метод не реализован, мы получим исключение TypeError с сообщением вида "Can't instantiate abstract class FrenchDeck2 with abstract methods __delitem__, insert". Вот поэтому мы и обязаны реализовать методы __delitem__ и insert, хотя в наших примерах класс FrenchDeck2 в них и не нуждается; ничего не поделаешь — абстрактный базовый класс MutableSequence требует.

Как показано на рис. 11.2, не все методы ABC Sequence и MutableSequence абстрактны.

От Sequence класс FrenchDeck2 наследует готовые к применению конкретные методы __contains__, __iter__, __reversed__, index и count. От MutableSequence он получает append, reverse, extend, pop, remove и __iadd__.

Конкретные методы в каждом ABC из модуля collections.abc реализованы в