---
source_image: page_037.png
page_number: 37
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 17.23
tokens: 7240
characters: 1076
timestamp: 2025-12-24T03:01:46.790883
finish_reason: stop
---

...    print('i is greater than 10')
... elif i%3 == 0:
...     print('i is a multiple of 3')
... else:
...     print('I don't know much about i...')
...
...
i is a multiple of 3
>>>

Операторы if могут быть вложенными, с содержащими операторы if блоками, которые выполняются только в том случае, если условие во внешнем операторе if равно True:

>>> cat = 'spot'
>>> if 's' in cat:
...     print("Found an 's' in a cat")
...     if cat == 'Sheba':
...         print("I found Sheba")
...     else:
...         print("Some other cat")
... else:
...     print(" a cat without 's'")
...
Found an 's' in a cat
Some other cat
>>>

Циклы for

Циклы for позволяют повторять выполнение блока операторов (блока кода) столько раз, сколько содержится элементов в последовательности (упорядоченной группе элементов). При проходе в цикле по последовательности блок кода обращается к текущему элементу. Чаще всего циклы используются для прохода по объекту range для выполнения какой-либо операции заданное число раз:

>>> for i in range(10):
...     x = i*2
...     print(x)
...
...
0
2
4
6