---
source_image: page_651.png
page_number: 651
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.71
tokens: 11867
characters: 2192
timestamp: 2025-12-24T02:04:52.487090
finish_reason: stop
---

Пример дескриптора: проверка значений атрибутов

Пример 20.1. bulkfood_v3.py: дескрипторы Quantity управляют атрибутами LineItem

class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name
    def __set__(self, instance, value):
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')

class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price
    def subtotal(self):
        return self.weight * self.price

1 Дескриптор основан на протоколе, для его реализации не требуется наследование.
2 В каждом экземпляре Quantity имеется атрибут storage_name: имя атрибута, в котором хранится значение управляемого экземпляра.
3 Метод __set__ вызывается при любой попытке присвоить значение управляемому атрибуту. В данном случае self — экземпляр дескриптора (т. е. LineItem.weight или LineItem.price), instance — управляемый экземпляр (экземпляр LineItem), а value — присваиваемое значение.
4 Здесь мы должны работать с атрибутом __dict__ управляемого экземпляра напрямую; попытка воспользоваться встроенной функцией setattr привела бы к повторному вызову метода __set__ и, стало быть, к бесконечной рекурсии.
5 Первый экземпляр дескриптора связывается с атрибутом weight.
6 Второй экземпляр дескриптора связывается с атрибутом price.
7 Оставшаяся часть тела класса так же проста и понятна, как первоначальный код в файле bulkfood_v1.py (пример 19.15).

В примере 20.1 управляемые атрибуты называются также, как соответствующий атрибут хранения, и никакой особой логики чтения нет, поэтому метод __get__ в классе Quantity не нужен.

Код из примера 20.1 работает, как и ожидается, — не позволяет продать трюфели за 0 долларов:

3 Белые трюфели стоят тысячи долларов за фунт. Запрет продажи трюфелей за $0.01 оставляю в качестве упражнения для увлеченных читателей. Я знаю человека, который купил энциклопедию статистики, стоящую 1800 долларов, за 18 долларов из-за ошибки в ПО Интернет-магазина (не Amazon.com).