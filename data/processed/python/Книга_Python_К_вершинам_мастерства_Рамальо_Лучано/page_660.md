---
source_image: page_660.png
page_number: 660
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.24
tokens: 11612
characters: 1578
timestamp: 2025-12-24T02:05:15.201428
finish_reason: stop
---

Глава 20. Дескрипторы атрибутов

Соотношение между классами Validated, Quantity и NonBlank — пример паттерна проектирования Шаблонный метод. Конкретно, метод Validated.__set__ — типичный пример того, что «банда четырех» называет шаблонным методом:

Шаблонный метод определяет алгоритм в терминах абстрактных операций, которые переопределяются в подклассах для обеспечения конкретного поведения.

В данном случае абстрактной операцией является проверка. В примере 20.6 приведена реализация всех классов, показанных на рис. 20.5.

Пример 20.6. model_v5.py: дескрипторные классы после рефакторинга

import abc

class AutoStorage:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return getattr(instance, self.storage_name)

    def __set__(self, instance, value):
        setattr(instance, self.storage_name, value)

class Validated(abc.ABC, AutoStorage):

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        super().__set__(instance, value)

    @abc.abstractmethod
    def validate(self, instance, value):
        """возвращает проверенное значение или возбуждает ValueError"""

class Quantity(Validated):
    """число больше нуля"""
    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')