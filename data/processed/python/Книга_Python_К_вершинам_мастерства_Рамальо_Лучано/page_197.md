---
source_image: page_197.png
page_number: 197
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.36
tokens: 11736
characters: 1707
timestamp: 2025-12-24T01:43:47.781657
finish_reason: stop
---

Функционально-ориентированная стратегия

...
    for item_code in range(10)]
>>> Order(joe, long_order, LargeOrderPromo())  # 8
<Order total: 10.00 due: 9.30>
>>> Order(joe, cart, LargeOrderPromo())
<Order total: 42.00 due: 42.00>

1 Два заказчика: у joe 0 баллов лояльности, у ann — 1100.
2 Одна корзина покупок с тремя позициями.
3 Класс FidelityPromo не дает joe никаких скидок.
4 ann получает скидку 5 %, поскольку имеет не менее 1000 баллов лояльности.
5 В корзине banana_cart находится 30 бананов и 10 яблок.
6 Класс BulkItemPromo дает joe скидку $1.50 на бананы.
7 В заказе long_order имеется 10 различных позиций стоимостью $1.00 каждая.
8 joe получает скидку 7 % на весь заказ благодаря классу LargerOrderPromo.

Пример 6.1 работает без нареканий, но ту же функциональность можно реализовать в Python гораздо короче, воспользовавшись функциями как объектами.

Функционально-ориентированная стратегия

Каждая конкретная стратегия в примере 6.1 — это класс с одним методом discount. К тому же, объекты стратегии не имеют состояния (атрибутов экземпляра). Мы могли бы сказать, что они сильно напоминают функции, и были бы правы. В примере 6.3 код из примера 6.1 переработан — конкретные стратегии заменены простыми функциями, а абстрактный класс Promo исключен вовсе.

Пример 6.3. Класс Order, в котором стратегии предоставления скидок реализованы в виде функций

from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order: # the Context