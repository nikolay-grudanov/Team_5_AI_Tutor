---
source_image: page_661.png
page_number: 661
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.07
tokens: 11711
characters: 1945
timestamp: 2025-12-24T02:05:29.599406
finish_reason: stop
---

Пример дескриптора: проверка значений атрибутов

return value

class NonBlank(Validated):
    """строка содержит хотя бы один непробельный символ"""
    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value cannot be empty or blank')
        return value

1 Класс AutoStorage предоставляет большую часть функциональности бывшего дескриптора Quantity...
2 ...за исключением проверки.
3 Класс Validated абстрактный, но наследует AutoStorage.
4 Метод __set__ делегирует проверку методу validate ...
5 ...а затем передает возвращенное значение value методу __set__ суперкласса, который и производит сохранение.
6 В этом класс метод validate абстрактный.
7 Классы Quantity и NonBlank наследуют Validated.
8 Требуя, чтобы конкретные методы validate возвращали проверенное значение, мы оставляем им возможность очистить, преобразовать или нормализовать полученные данные. В данном случае значение value перед возвратом очищается от начальных и конечных пробелов.

Пользователям модуля model_v5.py все эти детали знать необязательно. Важно лишь, что они получают возможность использовать классы Quantity и NonBlank для автоматизации проверки атрибутов экземпляра. Последняя версия класса LineItem приведена в примере 20.7.

Пример 20.7. bulkfood_v5.py: использование дескрипторов Quantity и NonBlank в классе LineItem

import model_v5 as model

class LineItem:
    description = model.NonBlank()  # Используем model.NonBlank. Больше ничего в коде не изменилось.
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

1 Импортируем модуль model_v5 и попутно сопоставляем ему более короткое имя.
2 Используем model.NonBlank. Больше ничего в коде не изменилось.