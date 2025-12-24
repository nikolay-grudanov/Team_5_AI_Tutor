---
source_image: page_405.png
page_number: 405
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.76
tokens: 11876
characters: 2222
timestamp: 2025-12-24T01:53:25.546980
finish_reason: stop
---

Перегрузка оператора сложения векторов +

pairs = itertools.zip_longest(self, other, fillvalue=0.0)
return Vector(a + b for a, b in pairs)

def __radd__(self, other): # ②
    return self + other

① Метод __add__ такой же, как в примере 13.4; приведен только потому, что им пользуется метод __radd__.
② __radd__ просто делегирует свою работу методу __add__.

Часто инверсный оператор можно таким и оставить: просто делегировать работу нужному оператору, в данном случае __add__. Это относится к любому коммутативному оператору; + является коммутативным для чисел и векторов, но перестает быть таковым, когда используется для конкатенации последовательностей в Python.

Методы в примере 13.4 работают как с объектами Vector, так и с любыми другими итерируемыми объектами, содержащими числовые элементы: Vector2d, кортеж целых чисел или массив чисел с плавающей точкой. Но если методу __add__ подсунуть неитерируемый объект, то он выдаст не слишком полезное сообщение об ошибке, как в примере 13.8.

Пример 13.8. Методу Vector.__add__ необходим итерируемый операнд

>>> v1 + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "vector_v6.py", line 328, in __add__
    pairs = itertools.zip_longest(self, other, fillvalue=0.0)
TypeError: zip_longest argument #2 must support iteration

Другое невразумительное сообщение выдается, если operand — итерируемый объект, но его элементы нельзя сложить с компонентами Vector, имеющими тип float. См. пример 13.9.

Пример 13.9. Методу Vector.__add__ необходим итерируемый operand с числами элементами

>>> v1 + 'ABC'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "vector_v6.py", line 329, in __add__
    return Vector(a + b for a, b in pairs)
  File "vector_v6.py", line 243, in __init__
    self._components = array(self.typecode, components)
  File "vector_v6.py", line 329, in <genexpr>
    return Vector(a + b for a, b in pairs)
TypeError: unsupported operand type(s) for +: 'float' and 'str'

Но непонятные сообщения в примерах 13.8 и 13.9 — еще не самое страшное: если специальный метод оператора не может вернуть правильный результат из-за несовместимости типов, он должен возвращать значение NotImplemented, а не