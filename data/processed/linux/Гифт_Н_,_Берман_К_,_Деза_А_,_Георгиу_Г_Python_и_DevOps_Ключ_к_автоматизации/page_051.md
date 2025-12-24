---
source_image: page_051.png
page_number: 51
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.75
tokens: 7510
characters: 1925
timestamp: 2025-12-24T03:02:19.891253
finish_reason: stop
---

>>> '{1} comes after {0}, but {1} comes before {2}'.format('first',
    'second',
    'third')
'second comes after first, but second comes before third'
>>>

Еще более интересная возможность — указание вставляемых значений по имени:

>>> "''{country} is an island.
... {country} is off of the coast of
... {continent} in the {ocean}'''.format(ocean='Indian Ocean',
... continent='Africa',
... country='Madagascar')
'Madagascar is an island.
Madagascar is off of the coast of
Africa in the Indian Ocean'

Здесь значения ключей для поименованных подстановочных полей задаются в ассоциативном массиве:

>>> values = {'first': 'Bill', 'last': 'Bailey'}
>>> "Won't you come home {first} {last}?".format(**values)
"Won't you come home Bill Bailey?"

Можно также указывать аргументы со спецификациями форматирования. В следующем примере с помощью > и < производится дополнение пробелами справа и слева. Во втором из примеров указывается символ для дополнения:

>>> text = "|{0:>22}||{0:<22}|"
>>> text.format('0','0')
'|        0||0        |'
>>> text = "|{0:<>22}||{0:<>22}|"
>>> text.format('0','0')
'|<<<<<<<<<<<<<<<<<<<<<<0||0>>>>>>>>>>>>>>>>>>>>>|'

Спецификации формата задаются с помощью мини-языка спецификаций формата (https://oreil.ly/ZOFJg). Можно применять и еще одну разновидность языка — f-строки.

Язык форматирования f-строк Python аналогичен методу format, но механизм использования проще и интуитивно понятнее. Перед первым знаком кавычек в f-строках ставится f или F. Как и описанные ранее строки format, подстановочные поля в f-строках обозначаются фигурными кавычками. Впрочем, в f-строках содержимое подстановочного поля представляет собой выражение. Благодаря такому подходу оно может ссылаться на переменные, определенные в текущей области видимости, или включать какие-либо вычисления:

>>> a = 1
>>> b = 2
>>> f"a is {a}, b is {b}. Adding them results in {a + b}"
'a is 1, b is 2. Adding them results in 3'