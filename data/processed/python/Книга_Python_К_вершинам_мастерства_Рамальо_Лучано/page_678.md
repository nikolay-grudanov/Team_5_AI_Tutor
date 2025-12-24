---
source_image: page_678.png
page_number: 678
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.42
tokens: 11746
characters: 1958
timestamp: 2025-12-24T02:06:08.111206
finish_reason: stop
---

Для примера 21.2 приведен код фабрики классов record_factory, который создает классы с динамической типизацией итерируемых объектов.

Код record_factory приведен в примере 21.2:

Пример 21.2. record_factory.py: простая фабрика классов

def record_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()  # Динамическая типизация в действии: пытаемся разбить field_names по запятым или пробелам; если не получается, предполагаем, что это уже итерируемый объект, по одному имени в каждом элементе.
    except AttributeError: # нет .replace или .split
        pass # предполагаем, что это уже последовательность идентификаторов
    field_names = tuple(field_names)  # Экземпляр записи изменяемый.

    def __init__(self, *args, **kwargs):  # Удобное представление repr.
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self):  # Экземпляры являются итерируемыми объектами, поэтому их можно распаковывать в момент присваивания...
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self):  # ... или при передаче функциям типа format.
        values = ', '.join('{}={!r}'.format(*i) for i in zip(self.__slots__, self))
        return '{{}}({})'.format(self.__class__.__name__, values)

    cls_attrs = dict(__slots__ = field_names,  # Вновь созданный класс наследует object — никакой связи с нашей фабрикой нет.
        __init__ = __init__,
        __iter__ = __iter__,
        __repr__ = __repr__)

    return type(cls_name, (object,), cls_attrs)  # Код record_factory приведен в примере 21.2.

1 Динамическая типизация в действии: пытаемся разбить field_names по запятым или пробелам; если не получается, предполагаем, что это уже итерируемый объект, по одному имени в каждом элементе.

2 Спасибо моему другу Х. С. Буэно, предложившему это решение.