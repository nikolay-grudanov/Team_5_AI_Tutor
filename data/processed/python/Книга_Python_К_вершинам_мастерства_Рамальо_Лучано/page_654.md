---
source_image: page_654.png
page_number: 654
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.93
tokens: 11657
characters: 1741
timestamp: 2025-12-24T02:05:06.910830
finish_reason: stop
---

prefix = cls.__name__
index = cls.__counter
self.storage_name = '_{}#{}'.format(prefix, index)
cls.__counter += 1

def __get__(self, instance, owner):
    return getattr(instance, self.storage_name)

def __set__(self, instance, value):
    if value > 0:
        setattr(instance, self.storage_name, value)
    else:
        raise ValueError('value must be > 0')

class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

1 __counter — атрибут класса Quantity, служащий для подсчета экземпляров Quantity.
2 cls — ссылка на класс Quantity.
3 Значение storage_name для каждого экземпляра дескриптора уникально, потому что образуется из имени дескрипторного класса и текущего значения __counter (например, _Quantity#0).
4 Увеличиваем __counter.
5 Мы должны реализовать метод __get__, потому что имя управляемого атрибута не совпадает со значением storage_name. Смысл аргумента owner будет объяснен ниже.
6 Используем встроенную функцию getattr, чтобы прочитать значение из instance.
7 Используем встроенную функцию setattr, чтобы сохранить значение в instance.
8 Теперь передавать имя управляемого атрибута конструктору Quantity не нужно. А этого мы и добивались.

Здесь мы можем пользоваться высокоуровневыми функциями getattr и setattr для чтения и сохранения значения, а не манипулировать напрямую instance.__dict__, потому что имена управляемого атрибута и атрибута хранения различны, а, значит, вызов getattr для атрибута хранения не приведет к вызову дескриптора и бесконечной рекурсии, как в примере 20.1, не возникнет.