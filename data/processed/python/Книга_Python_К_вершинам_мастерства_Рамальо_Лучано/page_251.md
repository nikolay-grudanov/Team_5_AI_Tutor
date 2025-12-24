---
source_image: page_251.png
page_number: 251
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.58
tokens: 11830
characters: 1778
timestamp: 2025-12-24T01:46:21.910700
finish_reason: stop
---

По умолчанию копирование поверхностное

self.passengers = []
else:
    self.passengers = list(passengers)

def pick(self, name):
    self.passengers.append(name)

def drop(self, name):
    self.passengers.remove(name)

Далее в интерактивном примере 8.9 мы создадим объект класса Bus (bus1) и два его клона: поверхностную копию (bus2) и глубокую копию (bus3) — и понаблюдаем за тем, что происходит, когда bus1 высаживает школьника.

Пример 8.9. Сравнение copy и deepcopy

>>> import copy
>>> bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
>>> bus2 = copy.copy(bus1)
>>> bus3 = copy.deepcopy(bus1)
>>> id(bus1), id(bus2), id(bus3)
(4301498296, 4301499416, 4301499752) ①
>>> bus1.drop('Bill')
>>> bus2.passengers
['Alice', 'Claire', 'David'] ②
>>> id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)
(4302658568, 4302658568, 4302657800) ③
>>> bus3.passengers
['Alice', 'Bill', 'Claire', 'David'] ④

① Используя copy и deepcopy, мы создаем три объекта Bus.
② После высадки 'Bill' из автобуса bus1 он исчезает и из bus2.
③ Инспекция атрибута passengers показывает, что bus1 и bus2 разделяют один и тот же объект списка, т. к. bus2 — поверхностная копия bus1.
④ bus3 — глубокая копия bus1, поэтому ее атрибут passengers ссылается на другой список.

Отметим, что в общем случае создание глубокой копии — дело не простое. Между объектами могут существовать циклические ссылки, из-за которых навальный алгоритм попадет в бесконечный цикл. Для корректной обработки циклических ссылок функция deepcopy запоминает, какие объекты она уже копировала. Это продемонстрировано в примере 8.10.

Пример 8.10. Циклические ссылки: b ссылается на a, а затем добавляется в конец a; тем не менее, deepcopy справляется с копированием a

>>> a = [10, 20]
>>> b = [a, 30]
>>> a.append(b)
>>> a