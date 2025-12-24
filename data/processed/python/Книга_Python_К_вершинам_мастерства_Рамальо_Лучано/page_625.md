---
source_image: page_625.png
page_number: 625
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 45.72
tokens: 11773
characters: 2208
timestamp: 2025-12-24T02:03:53.353611
finish_reason: stop
---

Вот мы и добрались до самого главного в этом примере: класса Event.

Пример 19.13. schedule2.py: класс Event

class Event(DbRecord):
    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speakers']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key))
                for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}>'.format(cls_name, self.name)
        else:
            return super().__repr__()

1 Класс Event расширяет DbRecord.
2 Свойство venue строит ключ key по атрибуту venue_serial и передает его методу класса fetch, унаследованному от DbRecord (см. пояснение ниже).
3 Свойство speakers проверяет, есть ли в записи атрибут _speaker_objs.
4 Если нет, то атрибут 'speakers' берется непосредственно из атрибута экземпляра __dict__ во избежание бесконечной рекурсии, поскольку открытое имя этого свойства — тоже speakers.
5 Получаем ссылку на метод класса fetch (зачем, будет объяснено ниже).
6 В self._speaker_objs методом fetch загружаем список записей speaker.
7 Возвращаем этот список.
8 Если в записи есть атрибут name, включаем его в строковое представление.
9 В противном случае по умолчанию используем унаследованный метод __repr__.

В свойстве venue из примера 19.13 последняя строка возвращает self.__class__.fetch(key). Почему бы не написать просто self.fetch(key)? Это более простое выражение работает для набора данных OSCON, потому что в нем нет записи о мероприятии с ключом 'fetch'. Но если бы такая запись существовала, то в соответствующем экземпляре Event выражение self.fetch было бы значением этого поля, а не ссылкой на метод класса fetch, унаследованный классом Event от DbRecord. Это тонкая ошибка, которая легко могла бы остаться незамеченной при тестировании и проявиться только в производственной системе при выборе записей venue или speaker, связанных с такой записью Event.