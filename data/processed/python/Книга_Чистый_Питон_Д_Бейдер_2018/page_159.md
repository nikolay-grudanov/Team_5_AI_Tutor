---
source_image: page_159.png
page_number: 159
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.30
tokens: 7345
characters: 1390
timestamp: 2025-12-24T02:30:54.045648
finish_reason: stop
---

5.1. Словари, ассоциативные массивы и хеш-таблицы

>>> dd['собаки'].append('Сниф')
>>> dd['собаки']
['Руфус', 'Кэтрин', 'Сниф']

collections.ChainMap — производит поиск в многочисленных словарях как в одной таблице соответствия

Структура данных collections.ChainMap группирует многочисленные словари в одну таблицу соответствия¹. Поиск проводится по очереди во всех базовых ассоциативных объектах до тех пор, пока ключ не будет найден. Операции вставки, обновления и удаления затрагивают только первую таблицу соответствия, добавленную в цепочку.

>>> from collections import ChainMap
>>> dict1 = {'один': 1, 'два': 2}
>>> dict2 = {'три': 3, 'четыре': 4}
>>> chain = ChainMap(dict1, dict2)
>>> chain
ChainMap({'один': 1, 'два': 2}, {'три': 3, 'четыре': 4})

# ChainMap выполняет поиск в каждой коллекции в цепочке
# слева направо, пока не найдет ключ (или не потерпит неудачу):
>>> chain['три']
3
>>> chain['один']
1
>>> chain['отсутствует']
    : 'отсутствует'

types.MappingProxyType — обертка для создания словарей только для чтения

MappingProxyType — это обертка стандартного словаря, которая предоставляет доступ только для чтения данных обернутого словаря². Этот

¹ См. документацию Python «collections.ChainMap»: https://docs.python.org/3/library/collections.html#collections.ChainMap
² См. документацию Python «types.MappingProxyType»: https://docs.python.org/3/library/types.html