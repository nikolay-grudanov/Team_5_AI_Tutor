---
source_image: page_433.png
page_number: 433
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.47
tokens: 11742
characters: 1810
timestamp: 2025-12-24T01:54:55.682579
finish_reason: stop
---

Итерируемые объекты и итераторы

def __subclasshook__(cls, C):
    if cls is Iterator:
        if (any("__next__" in B.__dict__ for B in C.__mro__) and
            any("__iter__" in B.__dict__ for B in C.__mro__)):
            return True
    return NotImplemented

В Python 3 абстрактный метод класса Iterator называется it.__next__(), а в Python 2 — it.next(). Как обычно, не следует вызывать специальные методы напрямую. Просто пользуйтесь встроенной функцией next(it): она сделает все правильно — и в Python 2, и в Python 3.

В исходном файле Lib/types.py (https://hg.python.org/cpython/file/3.4/Lib/types.py) для версии Python 3.4 есть такой комментарий:

# Итераторы в Python следует считать не типом, а протоколом. Многие
# встроенные типы (их число постоянно изменяется) реализуют *какой-то*
# вид итератора. Не проверяйте тип явно! Используйте вместо этого
# функцию hasattr для проверки наличия атрибутов "__iter__" и "__next__".

Нас самом деле, именно это и делает метод __subclasshook__ абстрактного класса abc.Iterator (см. пример 14.3).

Принимая во внимание рекомендацию из файла Lib/types.py и логику, реализованную в файле Lib/_collections_abc.py, согласимся, что лучший способ узнать, является ли объект х итератором, — вызвать функцию isinstance(x, abc.Iterator). Благодаря методу Iterator.__subclasshook__ эта проверка работает даже тогда, когда класс х не является ни настоящим, ни виртуальным подклассом Iterator.

Возвращаясь к классу Sentence из примера 14.1, мы можем в интерактивной оболочке посмотреть, как итератор строится функцией iter(...) и производит обход с помощью next(...):

>>> s3 = Sentence('Pig and Pepper') # 1
>>> it = iter(s3) # 2
>>> it # doctest: +ELLIPSIS
<iterator object at 0x...>
>>> next(it) # 3
'Pig'
>>> next(it)
'and'
>>> next(it)
'Pepper'
>>> next(it) # 4