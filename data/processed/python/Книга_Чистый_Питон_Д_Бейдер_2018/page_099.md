---
source_image: page_099.png
page_number: 99
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.61
tokens: 7244
characters: 1193
timestamp: 2025-12-24T02:29:38.581423
finish_reason: stop
---

Это означает, что инструкции return None можно заменять на пустые инструкции return или даже пропускать их полностью и по-прежнему получать тот же самый результат:

def foo1(value):
    if value:
        return value
    else:
        return None

def foo2(value):
    """Пустая инструкция return подразумевает `return None`"""
    if value:
        return value
    else:
        return
def foo3(value):
    """Пропущенная инструкция return подразумевает `return None`"""
    if value:
        return value

Все три функции правильно возвращают None, если передать им в качестве единственного аргумента фиктивное значение:

>>> type(foo1(0))
<class 'NoneType'>

>>> type(foo2(0))
<class 'NoneType'>

>>> type(foo3(0))
<class 'NoneType'>

Итак, когда же лучше всего использовать это функциональное средство языка Python в своем собственном программном коде?

Мое эмпирическое правило заключается в следующем: если функция не имеет возвращаемого значения (в других языках такая функция называется процедурой), то я исключаю инструкцию return. Добавлять эту инструкцию было бы лишним и вносило бы путаницу. Примером процедуры является встроенная в Python функция печати print, которая вызывается