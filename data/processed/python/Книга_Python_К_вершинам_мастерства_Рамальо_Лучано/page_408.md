---
source_image: page_408.png
page_number: 408
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.26
tokens: 11725
characters: 1696
timestamp: 2025-12-24T01:53:30.835997
finish_reason: stop
---

Пример 13.11. vector_v7.py: добавлены методы оператора *

from array import array
import reprlib
import math
import functools
import operator
import itertools
import numbers # 1

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    # в книге многие методы опущены, полный код vector_v7.py
    # см. по адресу https://github.com/fluentpython/example-code ...

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real): # 2
            return Vector(n * scalar for n in self)
        else: # 3
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar # 4

1 Импортируем модуль numbers для проверки типа.
2 Если scalar — экземпляр подкласса numbers.Real, создаем новый объект Vector, умножая компоненты исходного на заданное число.
3 В противном случае возбуждаем исключение TypeError с конкретным сообщением.
4 В этом примере __rmul__ просто вычисляет произведение self * scalar, делегируя всю работу методу __mul__.

Код из примера 13.11 позволяет умножать векторы на скалярные значения обычных и не очень обычных числовых типов:

>>> v1 = Vector([1.0, 2.0, 3.0])
>>> 14 * v1
Vector([14.0, 28.0, 42.0])
>>> v1 * True
Vector([1.0, 2.0, 3.0])
>>> from fractions import Fraction
>>> v1 * Fraction(1, 3)
Vector([0.3333333333333333, 0.6666666666666666, 1.0])

При реализации операторов + и * мы познакомились с наиболее распространенными приемами программирования инфиксных операторов. Описанная техника применима ко всем операторам, перечисленным в табл. 13.1 (операторы, вычисляемые на месте, будут рассмотрены в разделе «Составные операторы присваивания» ниже).