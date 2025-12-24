---
source_image: page_198.png
page_number: 198
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.88
tokens: 11623
characters: 1523
timestamp: 2025-12-24T01:43:41.323308
finish_reason: stop
---

def __init__(self, customer, cart, promotion=None):
    self.customer = customer
    self.cart = list(cart)
    self.promotion = promotion

def total(self):
    if not hasattr(self, '__total'):
        self.__total = sum(item.total() for item in self.cart)
    return self.__total

def due(self):
    if self.promotion is None:
        discount = 0
    else:
        discount = self.promotion(self)
    return self.total() - discount

def __repr__(self):
    fmt = '<Order total: {:.2f} due: {:.2f}>'
    return fmt.format(self.total(), self.due())

def fidelity_promo(order):
    """5%-ая скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0

def bulk_item_promo(order):
    """10%-ая скидка для каждой позиции LineItem, в которой заказано не менее 20 единиц"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount

def large_order_promo(order):
    """7%-ая скидка для заказов, включающих не менее 10 различных позиций"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0

Для вычисления скидки просто вызываем функцию self.promotion().
Абстрактного класса больше нет.
Каждая стратегия является функцией.

Код в примере 6.3 на 12 строчек короче, чем в примере 6.1. Пользоваться новым классом Order также несколько проще, как показано в doctest-скриптах ниже.