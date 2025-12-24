---
source_image: page_658.png
page_number: 658
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.06
tokens: 11734
characters: 1833
timestamp: 2025-12-24T02:05:17.715108
finish_reason: stop
---

между вызовами фабрики, определив ее как атрибут самого объекта фабричной функции (см. пример 20.5).

Пример 20.5. bulkfood_v4prop.py: та же функциональность, что в примере 20.2, но реализованная в виде фабрики свойств, а не дескрипторного класса

def quantity():
    try:
        quantity.counter += 1
    except AttributeError:
        quantity.counter = 0

    storage_name = '_{}:{}'.format('quantity', quantity.counter)

    def qty_getter(instance):
        return getattr(instance, storage_name)

    def qty_setter(instance, value):
        if value > 0:
            setattr(instance, storage_name, value)
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)

1 Аргумента storage_name нет.
2 Мы не можем полагаться на атрибуты класса для сохранения counter между вызовами, поэтому определим эту переменную как атрибут самой функции quantity.
3 Если quantity.counter не определена, присваиваем ей значение 0.
4 Атрибутов экземпляра у нас тоже нет, поэтому создаем storage_name как локальную переменную, а в qty_getter и qty_setter ее значение будет доступно благодаря замыканию.
5 Остальной код отличается от примера 19.24 только тем, что мы можем использовать встроенные функции getattr и setattr, а не манипулировать напрямую атрибутом instance.__dict__.

Ну и что вы предпочтете? Пример 20.2 или 20.5?
Лично я предпочитаю подход на основе дескрипторного класса в основном по двум причинам:
• дескрипторный класс можно расширять посредством наследования; повторно использовать код фабричной функции без копирования и вставки гораздо труднее;
• хранить состояние в атрибутах класса и экземпляров проще, чем в атрибутах функции и замыкании.

С другой стороны, когда я объясняю студентам пример 20.5, у меня не возникает потребности в хреновинах и штуковинах. Код фабрики