---
source_image: page_696.png
page_number: 696
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 46.78
tokens: 11783
characters: 2079
timestamp: 2025-12-24T02:07:02.026714
finish_reason: stop
---

В теории кажется сложным, но на практике все встречавшиеся мне примеры использования __prepare__ оказывались чрезвычайно простыми. Взгляните на пример 21.16.

Пример 21.16. model_v8.py: в метаклассе EntityMeta используется __prepare__, а в классе Entity теперь есть метод класса field_names.

class EntityMeta(type):
    """Метакласс для прикладных классов с контролируемыми полями"""
    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderedDict() ①

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)
        cls._field_names = [] ②
        for key, attr in attr_dict.items(): ③
            if isinstance(attr, Validated):
                type_name = type(attr).__name__
                attr.storage_name = '_{}#{}'.format(type_name, key)
                cls._field_names.append(key) ④

class Entity(metaclass=EntityMeta):
    """Прикладной класс с контролируемыми полями"""

    @classmethod
    def field_names(cls): ⑤
        for name in cls._field_names:
            yield name

① Возвращаем пустой экземпляр OrderedDict, в котором будут храниться атрибуты класса.
② Создаем атрибут _field_names в конструируемом классе.
③ Эта строка такая же, как в предыдущей версии, но здесь attr_dict — экземпляр класса OrderedDict, полученный интерпретатором, когда он вызывал метод __prepare__ перед вызовом __init__. Следовательно, в этом цикле for атрибуты будут перебираться в том порядке, в котором добавлялись.
④ Помещаем имена всех полей типа Validated в _field_names.
⑤ Метод класса field_names просто отдает поля в порядке добавления.

После простых модификаций, показанных в примере 21.16, мы можем обойти поля типа Validated любого подкласса Entity, воспользовавшись методом класса field_names. В примере 21.17 демонстрируется эта новая возможность.

Пример 21.17. bulkfood_v8.py: doctest-скрипт для демонстрации метода field_names — в класс LineItem не пришлось вносить никаких изменений; метод field_names унаследован от model.Entity

>>> for name in LineItem.field_names():
...     print(name)