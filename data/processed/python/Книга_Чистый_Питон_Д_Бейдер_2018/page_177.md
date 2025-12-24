---
source_image: page_177.png
page_number: 177
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.46
tokens: 7332
characters: 1276
timestamp: 2025-12-24T02:31:22.707956
finish_reason: stop
---

>>> car1 = Car('красный', 3812.4, True)

# Экземпляры имеют хороший метод repr:
>>> car1 Авто(цвет='красный', пробег=3812.4, автомат=True)

# Доступ к полям:
>>> car1.пробег
3812.4

# Поля неизменяемы:
>>> car1.пробег = 12
    : "can't set attribute"
>>> car1.лобовое_стекло = 'треснутое'
AttributeError:
"'Car' object has no attribute 'лобовое_стекло'"

typing.NamedTuple — усовершенствованные именованные кортежи

Этот класс был добавлен в Python 3.6 и является младшим братом класса namedtuple в модуле collections¹. Он очень похож на namedtuple, и его главное отличие состоит в том, что у него есть обновленный синтаксис для определения новых типов записей и добавленная поддержка подсказок при вводе исходного кода.

Кроме того, обратите внимание, что сигнатуры типов не поддерживаются без отдельного инструмента проверки типов, такого как mypy². Но даже без инструментальной поддержки они могут предоставлять полезные подсказки для других программистов (или могут быть ужасно запутанными, если подсказки в отношении типов становятся устаревшими).

>>> from typing import NamedTuple
class Car(NamedTuple):
    цвет: str
    пробег: float
    автомат: bool

¹ См. документацию Python «typing.NamedTuple»: https://docs.python.org/3.6/library/typing.html
² См. mypy-lang.org