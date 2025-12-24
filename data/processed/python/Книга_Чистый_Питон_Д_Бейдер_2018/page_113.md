---
source_image: page_113.png
page_number: 113
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.43
tokens: 7286
characters: 1384
timestamp: 2025-12-24T02:30:03.067402
finish_reason: stop
---

реализацию заглушки __str__, которая возвращает представление в виде Юникода в кодировке UTF-8:

def __str__(self):
    return unicode(self).encode('utf-8')

Заглушка __str__ будет одинаковой для большинства классов, ее вы просто можете копипастить повсюду, где это необходимо (либо разместить ее в базовом классе, где это имеет смысл). Тогда весь ваш код преобразования строк, который предназначен для использования не разработчиками, будет лежать в методе __unicode__.

Приведем законченный пример для Python 2.x:

class Car(object):
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    def __repr__(self):
        return '{{}({!r}, {!r})}'.format(
            self.__class__.__name__,
            self.color, self.mileage)
    def __unicode__(self):
        return u'{self.color} автомобиль'.format(
            self=self)
    def __str__(self):
        return unicode(self).encode('utf-8')

Ключевые выводы

□ Управлять преобразованием строк в своих собственных классах можно, используя дандер-методы __str__ и __repr__.

□ Результат метода __str__ должен быть удобочитаемым. Результат метода __repr__ должен быть однозначным.

□ В свои классы всегда следует добавлять метод __repr__. По умолчанию реализация метода __str__ просто вызывает метод __repr__.

□ В Python 2 вместо метода __str__ следует использовать метод __unicode__.