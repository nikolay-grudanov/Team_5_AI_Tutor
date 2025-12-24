---
source_image: page_611.png
page_number: 611
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 50.33
tokens: 11853
characters: 2156
timestamp: 2025-12-24T02:03:19.413837
finish_reason: stop
---

Применение динамических атрибутов для обработки данных

```python
>>> for key, value in sorted(feed['Schedule'].items()):
...     print('{:3} {}'.format(len(value), key))  # 3
...
1 conferences
484 events
357 speakers
53 venues
>>> feed['Schedule']['speakers'][-1]['name']  # 4
'Carina C. Zona'
>>> feed['Schedule']['speakers'][-1]['serial']  # 5
141590
>>> feed['Schedule']['events'][40]['name']
'There *Will* Be Bugs'
>>> feed['Schedule']['events'][40]['speakers']  # 6
[3471, 5199]
```

1. feed — словарь dict, содержащий вложенные словари и списки, в которых хранятся строковые и целые значения.
2. Перечисляем все четыре коллекции внутри "Schedule".
3. Выводим количество записей в каждой коллекции
4. Перебираем вложенные словари и списки, чтобы получить имя последнего докладчика.
5. Получаем порядковый номер этого докладчика.
6. Для каждого мероприятия имеется список 'speakers', содержащий 0 или более порядковых номеров докладчиков.

Исследование JSON-подобных данных с динамическими атрибутами

Пример 19.2 достаточно прост, но синтаксис feed['Schedule']['events'][40]['name'] слишком громоздкий. В JavaScript то же самое можно было бы записать в виде feed.Schedule.events[40].name. На Python нетрудно реализовать похожий на словарь класс, который ведет себя подобным образом, — в сети нет недостатка в примерах4. Я реализовал свой собственный класс FrozenJSON, который проще большинства готовых, т. к. поддерживает только чтение; он предназначен исключительно для исследования данных. Однако он рекурсивный и автоматически обрабатывает вложенные отображения и списки.

В примере 19.4 демонстрируется использование класса FrozenJSON, а в примере 19.5 приведен его исходный код.

Пример 19.4. Класс FrozenJSON из примера 19.5 позволяет читать атрибуты, например name, и вызывать методы, например .keys() и .items()

```python
>>> from osconfeed import load
>>> raw_feed = load()
>>> feed = FrozenJSON(raw_feed)  # 1
>>> len(feed.Schedule.speakers)  # 2
```

4 Часто упоминают класс AttrDict (https://pypi.python.org/pypi/attrdict); другой класс, позволяющий быстро создавать вложенные отображения, — addict (https://pypi.python.org/pypi/addict).