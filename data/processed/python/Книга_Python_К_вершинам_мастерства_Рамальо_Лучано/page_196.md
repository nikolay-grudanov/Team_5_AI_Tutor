---
source_image: page_196.png
page_number: 196
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.97
tokens: 11769
characters: 1824
timestamp: 2025-12-24T01:43:47.136421
finish_reason: stop
---

return order.total() * .05 if order.customer.fidelity >= 1000 else 0

class BulkItemPromo(Promotion): # second Concrete Strategy
    """10%-ая скидка для каждой позиции LineItem, в которой заказано не менее 20 единиц"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount

class LargeOrderPromo(Promotion): # third Concrete Strategy
    """7%-ая скидка для заказов, включающих не менее 10 различных позиций"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0

Отметим, что в примере 6.1 я сделал Promotion абстрактным базовым классом (ABC), чтобы можно было использовать декоратор @abstractmethod и тем самым прояснить структуру паттерна.

В Python 3.4 для создания ABC проще всего унаследовать классу abc.ABC, как в примере 6.1. В версиях от Python 3.0 до 3.3 необходимо использовать ключевое слово metaclass= в предложении class (например, class Promotion(metaclass=ABCMeta):).

Пример 6.2. Пример использования класса Order с различными стратегиями скидок

>>> joe = Customer('John Doe', 0)
>>> ann = Customer('Ann Smith', 1100)
>>> cart = [LineItem('banana', 4, .5),
...         LineItem('apple', 10, 1.5),
...         LineItem('watermelon', 5, 5.0)]
>>> Order(joe, cart, FidelityPromo())   # 3
<Order total: 42.00 due: 42.00>
>>> Order(ann, cart, FidelityPromo())   # 4
<Order total: 42.00 due: 39.90>
>>> banana_cart = [LineItem('banana', 30, .5),
...                 LineItem('apple', 10, 1.5)]   # 5
>>> Order(joe, banana_cart, BulkItemPromo())   # 6
<Order total: 30.00 due: 28.50>
>>> long_order = [LineItem(str(item_code), 1, 1.0)   # 7