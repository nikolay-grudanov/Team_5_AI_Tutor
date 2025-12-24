---
source_image: page_158.png
page_number: 158
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.19
tokens: 7349
characters: 1452
timestamp: 2025-12-24T02:30:53.995842
finish_reason: stop
---

имеет значение, лучше всего четко донести эту идею, задействовав класс OrderDict явным образом.

Между прочим, OrderedDict не является встроенной составной частью базового языка и должен быть импортирован из модуля collections, находящегося в стандартной библиотеке.

>>> import collections
>>> d = collections.OrderedDict(one=1, two=2, three=3)
>>> d
OrderedDict([('один', 1), ('два', 2), ('три', 3)])

>>> d['четыре'] = 4
>>> d
OrderedDict([('один', 1), ('два', 2),
              ('три', 3), ('четыре', 4)])

>>> d.keys()
odict_keys(['один', 'два', 'три', 'четыре'])

collections.defaultdict — возвращает значения, заданные по умолчанию для отсутствующих ключей

Класс defaultdict — это еще один подкласс словаря, который в своем конструкторе принимает вызываемый объект, возвращаемое значение которого будет использовано, если требуемый ключ нельзя найти¹.

Это свойство может сэкономить на наборе кода и сделать замысел программиста яснее в сравнении с использованием методов get() или отлавливанием исключения KeyError в обычных словарях.

>>> from collections import defaultdict
>>> dd = defaultdict(list)
# Попытка доступа к отсутствующему ключу его создает и
# инициализирует, используя принятую по умолчанию фабрику,
# то есть в данном примере list():
>>> dd['собаки'].append('Руфус')
>>> dd['собаки'].append('Кэтрин')

¹ См. документацию Python «collections.defaultdict»: https://docs.python.org/3/library/collections.html#defaultdict-objects