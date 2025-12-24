---
source_image: page_273.png
page_number: 273
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.64
tokens: 11754
characters: 1803
timestamp: 2025-12-24T01:47:18.653710
finish_reason: stop
---

И снова класс вектора

typecode = 'd' ①

def __init__(self, x, y):
    self.x = float(x) ②
    self.y = float(y)

def __iter__(self):
    return (i for i in (self.x, self.y)) ③

def __repr__(self):
    class_name = type(self).__name__
    return '{!r}, {!r}'.format(class_name, *self) ④

def __str__(self):
    return str(tuple(self)) ⑤

def __bytes__(self):
    return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))) ⑥

def __eq__(self, other):
    return tuple(self) == tuple(other) ⑧

def __abs__(self):
    return math.hypot(self.x, self.y) ⑨

def __bool__(self):
    return bool(abs(self)) 10

① typecode — это атрибут класса, которым мы воспользуемся, когда будем преобразовывать экземпляры Vector2d в последовательности байтов и наоборот.
② Преобразование x и y в тип float в методе __init__ позволяет на ранней стадии обнаруживать ошибки, это полезно в случае, когда конструктор Vector2d вызывается с неподходящими аргументами.
③ Наличие метода __iter__ делает Vector2d итерируемым; именно благодаря ему работает распаковка (например, x, y = my_vector). Мы реализуем его просто с помощью генераторного выражения, которое отдает компоненты поочередно3.
④ Метод __repr__ строит строку, интерполируя компоненты с помощью синтаксиса {!r} для получения их представления, возвращаемого функций repr; поскольку Vector2d — итерируемый объект, *self поставляет компоненты x и y функции format.
⑤ Из итерируемого объекта Vector2d легко построить кортеж для отображения в виде упорядоченной пары.
⑥ Для генерации объекта типа bytes мы преобразуем typecode в bytes и конкатенируем ...

3 Эту строку можно было бы записать и в виде yield self.x; yield self.y. У меня еще найдется что сказать по поводу специального метода __iter__, генераторных выражений и ключевого слова yield в главе 14.