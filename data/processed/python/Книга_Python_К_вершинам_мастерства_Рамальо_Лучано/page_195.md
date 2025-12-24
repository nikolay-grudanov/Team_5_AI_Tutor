---
source_image: page_195.png
page_number: 195
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.74
tokens: 11572
characters: 1546
timestamp: 2025-12-24T01:43:29.814462
finish_reason: stop
---

Практический пример: переработка паттерна Стратегия

Пример 6.1. Реализация класса Order с помощью взаимозаменяемых стратегий предоставления скидки

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')

class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

class Order: # Контекст

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
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

class Promotion(ABC): # Стратегия: абстрактный базовый класс

    @abstractmethod
    def discount(self, order):
        """Вернуть скидку в виде положительной суммы в долларах"""

class FidelityPromo(Promotion): # first Concrete Strategy
    """5%-ая скидка для заказчиков, имеющих не менее 1000 баллов лояльности"""

    def discount(self, order):
        return order.customer.fidelity * 5 / 100