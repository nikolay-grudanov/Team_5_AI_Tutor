---
source_image: page_802.png
page_number: 802
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.12
tokens: 7614
characters: 2052
timestamp: 2025-12-24T01:32:13.350025
finish_reason: stop
---

>>> L[2]
Traceback (innermost last):
    File "<stdin>", line 1, in ?
IndexError: list index out of range
Трассировка (самый последний вызов указан последним):
    Файл <stdin>, строка 1, в ?
Ошибка индекса: индекс в списке вышел за допустимые пределы
>>> L[2] = 3
Traceback (innermost last):
    File "<stdin>", line 1, in ?
IndexError: list assignment index out of range
Трассировка (самый последний вызов указан последним):
    Файл <stdin>, строка 1, в ?
Ошибка индекса: присваивание в списке по индексу, выходящему за допустимые пределы

7. Универсальные операции. Ниже приведены ответы на вопросы.

а) Операция + не работает на отличающихся/разнородных типах (например, строка + список, список + кортеж).

б) Операция + не работает для словарей, т.к. они не являются последовательностями.

в) Метод append работает только для списков, но не строк, а метод keys работает только со словарями. Метод append предполагает, что его цель представляет собой изменяемый объект, поскольку он производит расширение на месте; строки являются неизменяемыми.

г) Нарезание и конкатенация всегда возвращают новый объект того же самого типа, что и обрабатываемые объекты:

>>> "x" + 1
Traceback (innermost last):
    File "<stdin>", line 1, in ?
TypeError: can only concatenate str (not "int") to str
Трассировка (самый последний вызов указан последним):
    Файл <stdin>, строка 1, в ?
Ошибка типа: конкатенацию можно выполнять только строки (не целого числа) со строкой
>>>
>>> {} + {}
Traceback (innermost last):
    File "<stdin>", line 1, in ?
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
Трассировка (самый последний вызов указан последним):
    Файл <stdin>, строка 1, в ?
Ошибка типа: неподдерживаемый тип (типы) операнда для +: dict и dict
>>>
>>> [].append(9)
>>> "".append('s')
Traceback (innermost last):
    File "<stdin>", line 1, in ?
AttributeError: 'str' object has no attribute 'append'
Трассировка (самый последний вызов указан последним):
    Файл <stdin>, строка 1, в ?
Ошибка атрибута: объект str не имеет атрибута append