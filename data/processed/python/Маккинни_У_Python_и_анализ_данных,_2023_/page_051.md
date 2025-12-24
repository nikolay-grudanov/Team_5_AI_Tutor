---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.83
tokens: 7597
characters: 2016
timestamp: 2025-12-24T02:41:18.359528
finish_reason: stop
---

Функция isinstance может также принимать кортеж типов и тогда проверяет, что тип переданного объекта присутствует в кортеже:

In [28]: a = 5; b = 4.5

In [29]: isinstance(a, (int, float))
Out[29]: True

In [30]: isinstance(b, (int, float))
Out[30]: True

Атрибуты и методы
Объекты в Python обычно имеют атрибуты — другие объекты, хранящиеся «внутри» данного, — и методы — ассоциированные с объектом функции, имеющие доступ к внутреннему состоянию объекта. Обращение к тем и другим синтаксически выглядит как obj.attribute_name:

In [1]: a = "foo"

In [2]: a.<Press Tab>
capitalize() index() ispace() removesuffix() startswith()
casefold() isprintable() istitle() replace() strip()
center() isalnum() isupper() rfind() swapcase()
count() isalpha() join() rindex() title()
encode() isascii() ljust() rjust() translate()
endswith() isdecimal() lower() rpartition()
expandtabs() isdigit() lstrip() rsplit()
find() isidentifier() maketrans() rstrip()
format() islower() partition() split()
format_map() isnumeric() removeprefix() splitlines()

К атрибутам и методам можно обращаться также с помощью функции getattr:

In [32]: getattr(a, "split")
Out[32]: <function str.split(sep=None, maxsplit=-1)>

Хотя в этой книге мы почти не используем функцию getattr, а также родственные ей hasattr и setattr, они весьма эффективны для написания обобщенного, повторно используемого кода.

Утиная типизация
Часто нас интересует не тип объекта, а лишь наличие у него определенных методов или поведения. Иногда это называют «утиной» типизацией, имея в виду поговорку «если кто-то ходит, как утка, и крякает, как утка, то это утка и есть». Например, объект поддерживает итерирование, если он реализует протокол итератора. Для многих объектов это означает, что имеется «магический метод» __iter__, хотя есть другой — и лучший — способ проверки: попробовать воспользоваться функцией iter:

In [33]: def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # не допускаем итерирования
        return False