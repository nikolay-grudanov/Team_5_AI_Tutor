---
source_image: page_184.png
page_number: 184
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 49.39
tokens: 11966
characters: 2233
timestamp: 2025-12-24T01:43:21.461277
finish_reason: stop
---

Пример 5.24. Применение attrgetter для обработки ранее определенного списка именованных кортежей metro_data ( тот же список, что в примере 5.23)

>>> from collections import namedtuple
>>> LatLong = namedtuple('LatLong', 'lat long') # 1
>>> Metropolis = namedtuple('Metropolis', 'name cc pop coord') # 2
>>> metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long)) # 3
...     for name, cc, pop, (lat, long) in metro_data]
>>> metro_areas[0]
Metropolis(name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722, long=139.691667))
>>> metro_areas[0].coord.lat # 4
35.689722
>>> from operator import attrgetter
>>> name_lat = attrgetter('name', 'coord.lat') # 5
...
>>> for city in sorted(metro_areas, key=attrgetter('coord.lat')): # 6
...     print(name_lat(city)) # 7
...
('Sao Paulo', -23.547778)
('Mexico City', 19.433333)
('Delhi NCR', 28.613889)
('Tokyo', 35.689722)
('New York-Newark', 40.808611)

1 Определяем именованный кортеж LatLong.
2 Определяем также Metropolis.
3 Строим список metro_areas, содержащий экземпляры Metropolis; обратите внимание на распаковку именованного кортежа для извлечения (lat, long) и использование этих данных для построения объекта LatLong, являющегося значением атрибута coord объекта Metropolis.
4 Получаем широту из элемента metro_areas[0].
5 Определяем attrgetter для выборки атрибута name и вложенного атрибута coord.lat.
6 Снова используем attrgetter для сортировки списка городов по широте.
7 Используем определенный выше attrgetter для показа только названия и широты города.

Ниже приведен неполный список функций в модуле operator (имена, начинающиеся знаком подчеркивания, опущены, потому что такие функции содержат детали реализации):

>>> [name for name in dir(operator) if not name.startswith('_')]
['abs', 'add', 'and_', 'attrgetter', 'concat', 'contains',
'countOf', 'delitem', 'eq', 'floordiv', 'ge', 'getitem', 'gt',
'iadd', 'iand', 'iconcat', 'ifloordiv', 'ilshift', 'imod', 'imul',
'index', 'indexOf', 'inv', 'invert', 'ior', 'ipow', 'irshift',
'is_', 'is_not', 'isub', 'itemgetter', 'itruediv', 'ixor', 'le',
'length_hint', 'lshift', 'lt', 'methodcaller', 'mod', 'mul', 'ne',
'neg', 'not_', 'or_', 'pos', 'pow', 'rshift', 'setitem', 'sub',
'truediv', 'truth', 'xor']