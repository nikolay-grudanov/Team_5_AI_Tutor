---
source_image: page_559.png
page_number: 559
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.39
tokens: 7679
characters: 2089
timestamp: 2025-12-24T01:24:40.870320
finish_reason: stop
---

TypeError: kwonly() takes 1 positional argument but 3 were given
Ошибка типа: kwonly() принимает 1 позиционный аргумент, но было передано 3
>>> kwonly(1)
TypeError: kwonly() missing 2 required keyword-only arguments: 'b' and 'c'
Ошибка типа: kwonly() отсутствуют 2 обязательных аргумента с передачей только по ключевым словам: b и c

Вы по-прежнему можете использовать стандартные значения для аргументов с передачей только по ключевым словам, хотя они находятся после символа * в заголовке функции. В следующем коде a может передаваться по имени или по позиции, а b и c являются необязательными, но должны передаваться по ключевым словам, если присутствуют:

>>> def kwonly(a, *, b='spam', c='ham'):
    print(a, b, c)

>>> kwonly(1)
1 spam ham
>>> kwonly(1, c=3)
1 spam 3
>>> kwonly(a=1)
1 spam ham
>>> kwonly(c=3, b=2, a=1)
1 2 3
>>> kwonly(1, 2)
TypeError: kwonly() takes 1 positional argument but 2 were given
Ошибка типа: kwonly() принимает 1 позиционный аргумент, но было передано 2

На самом деле аргументы с передачей только по ключевым словам со стандартными значениями необязательны, но такие аргументы без стандартных значений становятся обязательными ключевыми словами для функции:

>>> def kwonly(a, *, b, c='spam'):
    print(a, b, c)

>>> kwonly(1, b='eggs')
1 eggs spam
>>> kwonly(1, c='eggs')
TypeError: kwonly() missing 1 required keyword-only argument: 'b'
Ошибка типа: kwonly() отсутствует 1 обязательный аргумент с передачей только по ключевым словам: b
>>> kwonly(1, 2)
TypeError: kwonly() takes 1 positional argument but 2 were given
Ошибка типа: kwonly() принимает 1 позиционный аргумент, но было передано 2

>>> def kwonly(a, *, b=1, c, d=2):
    print(a, b, c, d)

>>> kwonly(3, c=4)
3 1 4 2
>>> kwonly(3, c=4, b=5)
3 5 4 2
>>> kwonly(3)
TypeError: kwonly() missing 1 required keyword-only argument: 'c'
Ошибка типа: kwonly() отсутствует 1 обязательный аргумент с передачей только по ключевым словам: c
>>> kwonly(1, 2, 3)
TypeError: kwonly() takes 1 positional argument but 3 were given
Ошибка типа: kwonly() принимает 1 позиционный аргумент, но было передано 3