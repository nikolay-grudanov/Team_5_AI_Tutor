---
source_image: page_613.png
page_number: 613
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.96
tokens: 11823
characters: 2288
timestamp: 2025-12-24T02:03:14.491886
finish_reason: stop
---

Применение динамических атрибутов для обработки данных

Последняя строка в примере 19.4 выявляет небольшой дефект реализации: в идеале хотелось бы, чтобы попытка чтения несуществующего атрибута приводила к исключению AttributeError. Я даже реализовал такую обработку ошибок, но при этом метод __getattr__ стал вдвое длиннее, и это отвлекало внимание от той важной логики, которую я стремился продемонстрировать, поэтому из педагогических соображений я отказался от этой идеи.

Как видно из примера 19.5, в классе FrozenJSON всего два метода (__init__ и __getattr__) и атрибут экземпляра __data, поэтому попытка получить атрибут с любым другим именем приводит к вызову __getattr__. Этот метод сначала смотрит, есть ли в словаре self.__data атрибут (не ключ!) с таким именем; это позволяет экземплярам FrozenJSON обрабатывать методы самого класса dict, например items, делегируя работу методу self.__data.items(). Если в self.__data нет атрибута с именем name, то __getattr__ использует name как ключ, читает из self.__dict__ элемент с таким ключом и передает его методу FrozenJSON.build. Это позволяет обходить вложенные структуры в JSON-данных, поскольку каждое вложенное отображение преобразуется в новый экземпляр FrozenJSON методом класса build.

Пример 19.5. explore0.py: преобразование набора данных из формата JSON в объект FrozenJSON, содержащий вложенные объекты FrozenJSON, списки и значения примитивных типов

from collections import abc

class FrozenJSON:
    """Допускающий только чтение фасад для навигации по JSON-подобному объекту с применением нотации атрибутов
    """
    def __init__(self, mapping):
        self.__data = dict(mapping)

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

1 Строим объект dict по аргументу mapping. Тем самым мы решаем две задачи: проверяем, что получили словарь (или нечто, что можно преобразовать в словарь), и для безопасности делаем его копию.