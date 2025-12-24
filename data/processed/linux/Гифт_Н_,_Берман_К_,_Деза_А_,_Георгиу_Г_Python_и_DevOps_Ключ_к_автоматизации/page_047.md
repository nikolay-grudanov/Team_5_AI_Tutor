---
source_image: page_047.png
page_number: 47
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.53
tokens: 7243
characters: 1170
timestamp: 2025-12-24T03:02:04.067911
finish_reason: stop
---

>>> squares = [i*i for i in range(10) if i%2==0]
>>> squares
[0, 4, 16, 36, 64]
>>>

В числе других методик работы со списковыми включениями — вложение и применение нескольких переменных, но чаще всего встречается более простая их форма, показанная ранее.

Строковые значения

Строковые последовательности представляют собой упорядоченные наборы символов, заключенные в кавычки. В строках Python 3 по умолчанию используется кодировка UTF-8.

Создавать строковые значения можно либо с помощью метода-конструктора для строк str(), либо просто заключая текст в кавычки:

>>> str()
''
>>> "some new string!"
'some new string!'
>>> 'or with single quotes'
'or with single quotes'

С помощью конструктора строк можно создавать строковые значения на основе других объектов:

>>> my_list = list()
>>> str(my_list)
'[]'

Заключая текст в тройные кавычки, можно создавать многострочные строковые значения:

>>> multi_line = """This is a
... multi-line string,
... which includes linebreaks.
... """
>>> print(multi_line)
This is a
multi-line string,
which includes linebreaks.
>>>

Помимо общих для всех последовательностей методов, у строковых значений есть и немало собственных.