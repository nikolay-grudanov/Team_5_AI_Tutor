---
source_image: page_026.png
page_number: 26
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.62
tokens: 11843
characters: 2183
timestamp: 2025-12-24T01:35:43.332944
finish_reason: stop
---

Глава 1. Модель данных в языке Python

Итерирование часто подразумевается неявно. Если в коллекции отсутствует метод __contains__, то оператор in производит последовательный просмотр. Конкретный пример — в классе FrenchDeck оператор in работает, потому что этот класс итерируемый. Проверим:

>>> Card('Q', 'hearts') in deck
True
>>> Card('7', 'beasts') in deck
False

А как насчет сортировки? Обычно карты ранжируются по достоинству (тузы — самые старшие), а затем по масти в порядке пики (старшая масть), черви, бубны и трефы (младшая масть). Приведенная ниже функция ранжирует карты, следуя этому правилу: 0 означает двойку треф, а 21 — туза пик.

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

С помощью функции spades_high мы теперь можем расположить колоду в порядке возрастания:

>>> for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
... print(card)
Card(rank='2', suit='clubs')
Card(rank='2', suit='diamonds')
Card(rank='2', suit='hearts')
... (46 карт опущено)
Card(rank='A', suit='diamonds')
Card(rank='A', suit='hearts')
Card(rank='A', suit='spades')

Хотя класс FrenchDeck неявно наследует object⁴, его функциональность не наследуется, а является следствием использования модели данных и композиции. Вследствие реализации специальных методов __len__ и __getitem__ класс FrenchDeck ведет себя, как стандартная последовательность, и позволяет использовать базовые средства языка (например, итерирование и получение среза), а также функции reversed и sorted. Благодаря композиции реализации методов __len__ и __getitem__ могут перепоручать работу объекту self._cards класса list.

⁴ В Python 2 необходимо было бы явно написать FrenchDeck(object), а в Python 3 это подразумевается по умолчанию.

А как насчет тасования?

В текущей реализации объект класса FrenchDeck нельзя перетасовать, потому что он неизменяемый: ни карты, ни их позиции невозможно изменить, не нарушая инкапсуляцию (т. е. манипулируя атрибутом _cards непосредственно). В главе 11 мы исправим это, добавив односторочный метод __setitem__.