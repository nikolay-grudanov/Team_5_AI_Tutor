---
source_image: page_681.png
page_number: 681
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.39
tokens: 11797
characters: 2114
timestamp: 2025-12-24T02:06:21.075021
finish_reason: stop
---

Декоратор класса для настройки дескрипторов

могем проинспектировать класс и сопоставить дескрипторам подходящие имена атрибутов хранения. Это можно было бы сделать в методе __new__ класса LineItem, чтобы к моменту, когда дескрипторы используются в методе __init__, уже были установлены правильные имена атрибутов хранения. Проблема в том, что использование __new__ для этой цели означает растранжирование ресурсов: __new__ будет работать при создании каждого экземпляра LineItem, хотя привязка дескриптора к управляемому атрибуту уже не изменится после создания самого класса LineItem. Поэтому устанавливать имена атрибутов хранения нужно в момент создания класса. Это можно сделать с помощью декоратора класса или метакласса. Сначала пойдем по простому пути.

Декоратор класса очень похож на декоратор функции: это функция, которая получает объект класса и возвращает тот же самый или модифицированный класс.

В примере 21.3 класс LineItem компилируется интерпретатором и получающийся в результате объект класса передается функции model.entity. Python свяжет глобальное имя с объектом, который вернет эта функция. В данном примере model.entity возвращает тот же самый класс LineItem, но с измененным атрибутом storage_name в каждом экземпляре дескриптора.

Пример 21.3. bulkfood_v6.py: класс LineItem с дескрипторами Quantity и NonBlank

import model_v6 as model

@model.entity
class LineItem:
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

1 Единственное изменение — добавление декоратора.

В примере 21.4 приведена реализация декоратора. Показан только новый код в конце файла model_v6.py; все остальное не отличается от файла model_v5.py (при мер 20.6).

Пример 21.4. model_v6.py: декоратор класса

def entity(cls): ①
    for key, attr in cls.__dict__.items(): ②
        if isinstance(attr, Validated): ③
            type_name = type(attr).__name__