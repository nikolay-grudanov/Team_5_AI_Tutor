---
source_image: page_110.png
page_number: 110
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.14
tokens: 7373
characters: 1512
timestamp: 2025-12-24T03:03:48.394784
finish_reason: stop
---

ОПИСАНИЕ КЛАССОВ

Описание класса начинается с ключевого слова class, за которым следуют имя класса и скобки:

In [1]: class MyClass():
Далее в блоке кода, сдвинутом вправо с помощью отступов, размещаются описания атрибутов и методов. Все методы класса получают в качестве первого параметра копию объекта класса. По соглашению она называется self:

In [1]: class MyClass():
    ...:     def some_method(self):
    ...:         print(f"Say hi to {self}")
    ...:
In [2]: myObject = MyClass()
In [3]: myObject.some_method()
Say hi to <__main__.MyClass object at 0x1056f4160>

У каждого класса есть метод init, вызываемый при создании экземпляра этого класса. Если не опи- сать этот метод, класс унаследует от базового класса object языка Python метод по умолчанию:

In [4]: MyClass.__init__
Out[4]: <slot wrapper '__init__' of 'object' objects>

Атрибуты объекта обычно описываются в методе init:

In [5]: class MyOtherClass():
    ...:     def __init__(self, name):
    ...:         self.name = name
    ...:
In [6]: myOtherObject = MyOtherClass('Sammy')
In [7]: myOtherObject.name
Out[7]: 'Sammy'

fire

Попробуем еще дальше продвинуться по пути создания утилиты командной строки с помощью минимального объема кода. Пакет fire создает интерфейсы автоматически с помощью интроспекции кода. Если нужно сделать доступной в командной строке простую функцию, можно просто вызвать метод fire.Fire, указав ее в качестве аргумента:

#!/usr/bin/env python
"""
Простой пример использования библиотеки fire
"""
import fire