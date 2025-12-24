---
source_image: page_410.png
page_number: 410
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.60
tokens: 11739
characters: 1780
timestamp: 2025-12-24T01:53:36.272832
finish_reason: stop
---

которому для этой цели стал доступен символ @ (например, a @ b означает скалярное произведение a и b). Для поддержки оператора @ предназначены специальные методы __matmul__, __rmatmul__ и __imatmul__, имена которых — сокращение от «matrix multiplication» (матричное умножение). В настоящее время эти методы не используются нигде в стандартной библиотеке, но распознаются интерпретатором, поэтому разработчики NumPy, а с ними и все мы, могут поддержать оператор @ в пользовательских типах. Синтаксический анализатор также изменен для поддержки инфиксного оператора @ (раньше запись a @ b приводила к синтаксической ошибке).

Собрав версию Python 3.5 из исходного кода, я смог реализовать и протестировать оператор @, вычисляющий скалярное произведение в классе Vector.

Вот простейшие тесты:

```python
>>> va = Vector([1, 2, 3])
>>> vz = Vector([5, 6, 7])
>>> va @ vz == 38.0 # 1*5 + 2*6 + 3*7
True
>>> [10, 20, 30] @ vz
380.0
>>> va @ 3
Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for @: 'Vector' and 'int'
```

А вот код соответствующих специальных методов:

```python
class Vector:
    # в книге многие методы опущены
    def __matmul__(self, other):
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented

    def __rmatmul__(self, other):
        return self @ other
```

Полный код находится в файле vector.py3_5.py в репозитории кода к книге по адресу https://github.com/fluentpython/example-code.

Не забудьте, что выполнять этот код следует в версии Python 3.5, иначе получите исключение SyntaxError!

Операторы сравнения

Обработка операторов сравнения ==, !=, >, <, >=, <= интерпретатором Python похожа на то, что мы видели выше, но имеет два важных отличия.