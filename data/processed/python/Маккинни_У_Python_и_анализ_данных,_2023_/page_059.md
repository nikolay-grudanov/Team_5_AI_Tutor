---
source_image: page_059.png
page_number: 59
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.54
tokens: 7491
characters: 1428
timestamp: 2025-12-24T02:41:24.266592
finish_reason: stop
---

В предположении, что известна Unicode-кодировка объекта bytes, мы можем обратить эту операцию методом decode:

In [91]: val_utf8.decode("utf-8")
Out[91]: 'español'

Хотя в наши дни обычно используют кодировку UTF-8 для любых текстов, в силу исторических причин иногда можно встретить данные и в других кодировках:

In [92]: val.encode("latin1")
Out[92]: b'espá\xf1ol'

In [93]: val.encode("utf-16")
Out[93]: b'\xff\xffee\x00s\x00p\x00a\x00\xf1\x00o\x00l\x00'

In [94]: val.encode("utf-16le")
Out[94]: b'e\x00s\x00p\x00a\x00\xf1\x00o\x00l\x00'

Чаще всего объекты типа bytes встречаются при работе с файлами, когда неявно перекодировать все данные в Unicode-строки не всегда желательно.

Булевые значения
Два булевых значения записываются в Python как True и False. Результатом сравнения и вычисления условных выражений является True или False. Булевые значения объединяются с помощью ключевых слов and и or:

In [95]: True and True
Out[95]: True

In [96]: False or True
Out[96]: True

В процессе преобразования в число False становится равным 0, а True — 1:

In [97]: int(False)
Out[97]: 0

In [98]: int(True)
Out[98]: 1

Ключевое слово not переводит True в False и наоборот:

In [99]: a = True

In [100]: b = False

In [101]: not a
Out[101]: False

In [102]: not b
Out[102]: True

Приведение типов
Типы str, bool, int и float являются также функциями, которые можно использовать для приведения значения к соответствующему типу: