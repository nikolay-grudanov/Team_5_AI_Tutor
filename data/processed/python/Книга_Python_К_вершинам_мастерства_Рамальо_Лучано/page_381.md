---
source_image: page_381.png
page_number: 381
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.58
tokens: 11880
characters: 2128
timestamp: 2025-12-24T01:52:25.672299
finish_reason: stop
---

Множественное наследование и порядок разрешения методов

При изучении класса я часто просматриваю его __mro__ в интерактивной оболочке. Ниже приведено несколько примеров для хорошо знакомых классов.

Пример 12.8. Инспектирование класса __mro__ в нескольких классах

```python
>>> bool.__mro__  # 1
(<class 'bool'>, <class 'int'>, <class 'object'>)
>>> def print_mro(cls):  # 2
...     print(', '.join(c.__name__ for c in cls.__mro__))
...
>>> print_mro(bool)
bool, int, object
>>> from frenchdeck2 import FrenchDeck2
>>> print_mro(FrenchDeck2)  # 3
FrenchDeck2, MutableSequence, Sequence, Sized, Iterable, Container, object
>>> import numbers
>>> print_mro(numbers.Integral)  # 4
Integral, Rational, Real, Complex, Number, object
>>> import io  # 5
>>> print_mro(io.BytesIO)
BytesIO, _BufferedIOBase, _IOWrapper, object
>>> print_mro(io.TextIOWrapper)
TextIOWrapper, _TextIOBase, _IOWrapper, object
```

1 bool наследует методы и атрибуты int и object.
2 print_mro выводит более компактное представление MRO.
3 В состав предков FrenchDeck2 входят несколько ABC из модуля collections.abc.
4 Это числовые ABC из модуля numbers.
5 Модуль io включает ABC (с суффиксом ...Base) и конкретные классы, например BytesIO и TextIOWrapper, определяющие тип объекта двоичного или текстового файла, который метод open() возвращает в зависимости от аргумента mode.

При вычислении MRO применяется алгоритм CЗ. Он описан в канонической статье Мишеля Симионато «The Python 2.3 Method Resolution Order» (http://bit.ly/1OwVqBd). Для тех, кого интересуют тонкости MRO, в разделе «Дополнительная литература» имеются еще ссылки. Но не нужно особенно «заморачиваться» по этому поводу, алгоритм ведет себя вполне разумно; как пишет Симионато:

[...] если вы не злоупотребляете множественным наследованием и не работаете с особо сложными иерархиями, то понимать алгоритм CЗ необязательно, и вы можете спокойно не читать статью.

Чтобы подвести итоги обсуждению MRO, я на рис. 12.2 изобразил часть сложного графа множественного наследования пакета Tkinter для построения пользовательских интерфейсов из стандартной библиотеки Python. Изучая этот рисунок,