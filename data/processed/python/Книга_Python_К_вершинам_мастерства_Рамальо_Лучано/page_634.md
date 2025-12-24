---
source_image: page_634.png
page_number: 634
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.65
tokens: 11603
characters: 1368
timestamp: 2025-12-24T02:03:53.076819
finish_reason: stop
---

return self.__dict__['bar']

@bar.setter
def bar(self, value):
    self.__dict__['bar'] = value

Разобравшись с основами, вернемся к вопросу о том, как защитить атрибуты weight и price экземпляра LineItem, чтобы им можно было присвоить только положительные значения, — но при этом не писать вручную две почти одинаковые пары методов чтения и установки.

![Рис. 19.2. Как выглядит оболочка Python после выполнения команд help(Foo.bar) и help(Foo). Исходный код см. в примере 19.22](../images/ch19_02.png)

Рис. 19.2. Как выглядит оболочка Python после выполнения команд help(Foo.bar) и help(Foo). Исходный код см. в примере 19.22

Программирование фабрики свойств

Мы создадим фабрику свойств quantity — такое название выбрано, потому что управляемые атрибуты представляют собой количественные величины, которые в приложении должны быть положительны. В примере 19.23 показано, как выглядит класс LineItem с двумя свойствами, порожденными фабрикой quantity: для управления атрибутами weight и price.

Пример 19.23. bulkfood_v2prop.py: фабрика свойств quantity в действии

class LineItem:
    weight = quantity('weight') ①
    price = quantity('price') ②

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight ③
        self.price = price

    def subtotal(self):
        return self.weight * self.price ④