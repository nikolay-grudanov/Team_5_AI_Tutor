---
source_image: page_060.png
page_number: 60
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 16.46
tokens: 7395
characters: 1094
timestamp: 2025-12-24T02:41:18.017151
finish_reason: stop
---

In [103]: s = "3.14159"

In [104]: fval = float(s)

In [105]: type(fval)
Out[105]: float

In [106]: int(fval)
Out[106]: 3

In [107]: bool(fval)
Out[107]: True

In [108]: bool(0)
Out[108]: False

Отметим, что ненулевые значения после приведения к типу bool чаще всего становятся равны True.

Тип None

None — это тип, позволяющий записать значение null в Python.

In [109]: a = None

In [110]: a is None
Out[110]: True

In [111]: b = 5

In [112]: b is not None
Out[112]: True

None также часто применяется в качестве значения по умолчанию для необязательных аргументов функции:

def add_and_maybe_multiply(a, b, c=None):
    result = a + b

    if c is not None:
        result = result * c

    return result

Дата и время

Стандартный модуль Python datetime предоставляет типы datetime, date и time. Тип datetime, как нетрудно сообразить, объединяет информацию, хранящуюся в date и time. Именно он чаще всего и используется:

In [113]: from datetime import datetime, date, time

In [114]: dt = datetime(2011, 10, 29, 20, 30, 21)

In [115]: dt.day
Out[115]: 29

In [116]: dt.minute
Out[116]: 30