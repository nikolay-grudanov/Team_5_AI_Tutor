---
source_image: page_024.png
page_number: 24
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.88
tokens: 11683
characters: 1755
timestamp: 2025-12-24T01:35:18.717366
finish_reason: stop
---

ranks = [str(n) for n in range(2, 11)] + list('JQKA')
suits = 'spades diamonds clubs hearts'.split()

def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits
                   for rank in self.ranks]

def __len__(self):
    return len(self._cards)

def __getitem__(self, position):
    return self._cards[position]

Прежде всего, отметим использование collections.namedtuple для конструирования простого класса, представляющего одну карту. Начиная с версии Python 2.6, класс namedtuple можно использовать для построения классов, содержащих только атрибуты и никаких методов, как, например, запись базы данных. В данном примере мы воспользовались им для создания простого представления игральной карты, что продемонстрировано в следующем сценарии оболочки:

>>> beer_card = Card('7', 'diamonds')
>>> beer_card
Card(rank='7', suit='diamonds')

Но изюминка примера — класс FrenchDeck. Совсем короткий, он таит в себе немало интересного. Во-первых, как и для любой стандартной коллекции в Python, для колоды можно вызвать функцию len(), которая вернет количество карт в ней:

>>> deck = FrenchDeck()
>>> len(deck)
52

Получение карты из колоды, например первой или последней, не должно быть сложнее обращения deck[0] или deck[-1], и именно это обеспечивает метод __getitem__:

>>> deck[0]
Card(rank='2', suit='spades')
>>> deck[-1]
Card(rank='A', suit='hearts')

Нужно ли создавать метод для выбора случайной карты? Необязательно. В Python уже есть функция выборки случайного элемента последовательности: random.choice. Достаточно вызвать ее для экземпляра колоды:

>>> from random import choice
>>> choice(deck)
Card(rank='3', suit='hearts')
>>> choice(deck)
Card(rank='K', suit='spades')
>>> choice(deck)
Card(rank='2', suit='clubs')