---
source_image: page_336.png
page_number: 336
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.89
tokens: 11691
characters: 1679
timestamp: 2025-12-24T01:49:59.320778
finish_reason: stop
---

Пример 11.3. Частичная реализация протокола последовательности: метода __getitem__
достаточно для доступа к элементам, итерирования и реализации оператора in

```python
>>> class Foo:
...     def __getitem__(self, pos):
...         return range(0, 30, 10)[pos]
...
>>> f[1]
10
>>> f = Foo()
>>> for i in f: print(i)
...
0
10
20
>>> 20 in f
True
>>> 15 in f
False
```

Метода __iter__ в классе Foo нет, однако его экземпляры являются итерируемыми объектами, потому что даже в случае отсутствия __iter__ Python, обнаружив метод __getitem__, пытается обойти объект, вызывая этот метод с целочисленными индексами, начиная с 0. Поскольку Python достаточно «умен», чтобы обойти объекты Foo, он может также реализовать оператор in, даже если в классе Foo нет метода __contains__: для этого достаточно обойти весь объект в поисках элемента.

Итак, принимая во внимание важность протокола последовательности, интерпретатор Python даже в случае отсутствия методов __iter__ и __contains__ умудряется выполнить итерирование и заставить работать оператор in, вызывая метод __getitem__.

Наш класс FrenchDeck из главы 1 тоже не является подклассом abc.Sequence, но реализует оба метода протокола последовательности: __getitem__ и __len__. См. пример 11.4.

Пример 11.4. Колода карт как последовательность (повторение примера 1.1)

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):