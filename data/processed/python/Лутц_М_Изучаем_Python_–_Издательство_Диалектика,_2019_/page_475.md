---
source_image: page_475.png
page_number: 475
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.42
tokens: 7328
characters: 1445
timestamp: 2025-12-24T01:21:57.766794
finish_reason: stop
---

>>> help(str.replace)
Help on method_descriptor:
replace(self, old, new, count=-1, /)
    Return a copy with all occurrences of substring old replaced by new.
    ...остальной текст не показан...
>>> help('.replace')
...похоже на предыдущий результат...
>>> help(ord)
Help on built-in function ord in module builtins:
ord(c, /)
    Return the Unicode code point for a one-character string.

Наконец функция help работает с вашими модулями настолько же хорошо, как и с встроенными. Ниже показан отчет по созданному ранее файлу docstrings.py. И снова часть вывода — это строки документации, а часть — информация, автоматически извлеченная при инспектировании структур объектов:

>>> import docstrings
>>> help(docstrings.square)
Help on function square in module docstrings:
square(x)
    function documentation
    can we have your liver then?
>>> help(docstrings.Employee)
Help on class Employee in module docstrings:
class Employee(builtins.object)
    | class documentation
    |
    ...остальной текст не показан...
>>> help(docstrings)
Help on module docstrings:
NAME
    docstrings
DESCRIPTION
    Module documentation
    Words Go Here
CLASSES
    builtins.object
        Employee
    class Employee(builtins.object)
        | class documentation
        |
        ...остальной текст не показан...
FUNCTIONS
    square(x)
        function documentation
        can we have your liver then?
DATA
    spam = 40
FILE
    c:\code\docstrings.py