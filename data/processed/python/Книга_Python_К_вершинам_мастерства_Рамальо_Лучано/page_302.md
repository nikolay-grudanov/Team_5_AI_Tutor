---
source_image: page_302.png
page_number: 302
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.97
tokens: 11785
characters: 1917
timestamp: 2025-12-24T01:48:32.230733
finish_reason: stop
---

components = reprlib.repr(self._components) ③
components = components[components.find('['):-1] ④
return 'Vector({})'.format(components)

def __str__(self):
    return str(tuple(self))

def __bytes__(self):
    return (bytes([ord(self.typecode)]) +
            bytes(self._components)) ⑤

def __eq__(self, other):
    return tuple(self) == tuple(other)

def __abs__(self):
    return math.sqrt(sum(x * x for x in self)) ⑥

def __bool__(self):
    return bool(abs(self))

@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[1:]).cast(typecode)
    return cls(memv) ⑦

① В «защищенном» атрибуте экземпляра self._components хранится массив array компонент Vector.
② Чтобы было возможно итерирование, возвращаем итератор, построенный по self._components.¹
③ Используем reprlib.repr() для получения представления self._components ограниченной длины (например, array('d', [0.0, 1.0, 2.0, 3.0, 4.0, ...]).
④ Удаляем префикс array('d' и закрывающую скобку ), перед тем как подставить строку в вызов конструктора Vector.
⑤ Строим объект bytes из self._components.
⑥ Метод hypot больше не применим, поэтому вычисляем сумму квадратов компонент и извлекаем из нее квадратный корень.
⑦ Единственное отличие от написанного ранее метода frombytes — последняя строка: мы передаем объект memoryview напрямую конструктору, не распаковывая его с помощью *, как раньше.

То, как я использовал функцию reprlib.repr, заслуживает пояснения. Эта функция порождает безопасное представление длинной или рекурсивной структуры путем ограничения длины выходной строки с заменой отброшенного окончания многоточием '...'. Я хотел, чтобы repr-представление Vector имело вид Vector([3.0, 4.0, 5.0]), а не Vector(array('d', [3.0, 4.0, 5.0])), потому что присутствие array внутри Vector — деталь реализации. Поскольку оба вызова кон-

¹ Функция iter() рассматривается в главе 14 наряду с методом __iter__.