---
source_image: page_254.png
page_number: 254
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.77
tokens: 11826
characters: 1911
timestamp: 2025-12-24T01:46:27.934414
finish_reason: stop
---

Глава 8. Ссылки на объекты, изменяемость и повторное...

3 Применяя методы .remove() и .append() к self.passengers, мы на самом деле изменяем список по умолчанию, который является атрибутом объекта-функции.

В примере 8.13 показано потустороннее поведение объекта HauntedBus.

Пример 8.13. Автобусы, облюбованные пассажирами-призраками

>>> bus1 = HauntedBus(['Alice', 'Bill'])
>>> bus1.passengers
['Alice', 'Bill']
>>> bus1.pick('Charlie')
>>> bus1.drop('Alice')
>>> bus1.passengers ①
['Bill', 'Charlie']
>>> bus2 = HauntedBus() ②
>>> bus2.pick('Carrie')
>>> bus2.passengers
['Carrie']
>>> bus3 = HauntedBus() ③
>>> bus3.passengers ④
['Carrie']
>>> bus3.pick('Dave') ⑤
>>> bus2.passengers
['Carrie', 'Dave']
>>> bus2.passengers is bus3.passengers ⑥
True
>>> bus1.passengers ⑦
['Bill', 'Charlie']

① Пока все хорошо: bus1 не таит никаких сюрпризов.
② bus2 вначале пуст, поэтому атрибуту self.passengers присвоен пустой список по умолчанию.
③ bus3 также вначале пуст, self.passengers — снова список по умолчанию.
④ Список по умолчанию уже не пуст!
⑤ Теперь Dave, севший в автобус bus3, оказался и в bus2.
⑥ Проблема: bus2.passengers и bus3.passengers ссылаются на один и тот же список.
⑦ Но bus1.passengers — другой список.

Проблема в том, что все экземпляры HauntedBus, конструктору которых не был явно передан список пассажиров, разделяют один и тот же список по умолчанию.

Это тонкая ошибка. Из примера 8.13 видно, что когда объект HauntedBus инициализируется списком пассажиров, он работает правильно. Страннысти начинаются, когда HauntedBus вначале пуст, потому что в этом случае self.passengers оказывается синонимом значения по умолчанию для параметра passengers. Беда в том, что любое значение по умолчанию вычисляется в момент определения функции, т. е. обычно на этапе загрузки модуля, после чего значения по умолчанию становятся атрибутами объекта-функции. Так что если значение по умолчанию — изме-