---
source_image: page_612.png
page_number: 612
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.47
tokens: 11822
characters: 1974
timestamp: 2025-12-24T02:03:11.231325
finish_reason: stop
---

Глава 19. Динамические атрибуты и свойства

357
>>> sorted(feed.Schedule.keys()) ③
['conferences', 'events', 'speakers', 'venues']
>>> for key, value in sorted(feed.Schedule.items()):
...     print('({:3}) {}'.format(len(value), key))
...
1 conferences
484 events
357 speakers
53 venues
>>> feed.Schedule.speakers[-1].name ⑤
'Carina C. Zona'
>>> talk = feed.Schedule.events[40]
>>> type(talk) ⑥
<class 'explore0.FrozenJSON'>
>>> talk.name
'There *Will* Be Bugs'
>>> talk.speakers ⑦
[3471, 5199]
>>> talk.flavor ⑧
Traceback (most recent call last):
    ...
KeyError: 'flavor'

① Строим экземпляр FrozenJSON по словарю raw_feed, содержащему вложенные словари и списки.
② FrozenJSON допускает обход вложенных словарей с помощью нотации атрибутов; здесь мы получаем длину списка докладчиков.
③ Методы скрытых за объектом FrozenJSON словарей также доступны, например, метод .keys() возвращает имена коллекций.
④ С помощью метода items() мы можем извлечь имена коллекций записей и их содержимое, чтобы показать длину каждого значения.
⑤ Список, например feed.Schedule.speakers, остается списком, но те объекты внутри него, которые являются отображениями, преобразуются в тип FrozenJSON.
⑥ Элемент 40 списка events был объектом типа JSON; теперь это экземпляр класса FrozenJSON.
⑦ С каждым мероприятием связан список speakers, содержащий порядковые номера докладчиков.
⑧ При попытке прочитать несуществующий атрибут возбуждается исключение KeyError, а не AttributeError, как обычно.

Краеугольным камнем класса FrozenJSON является метод __getattr__, которым мы уже пользовались в примере класса Vector из раздела «Vector, попытка № 3: доступ к динамическим атрибутам» главы 10, чтобы обращаться к компонентам вектора по буквам — v.x, v.y, v.z и т. д. Напомним, что интерпретатор вызывает специальный метод __getattr__, только если обычный процесс поиска атрибута завершается неудачно (т. е. именованный атрибут не удается найти ни в экземпляре, ни в классе, ни в его суперклассах).