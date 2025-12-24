---
source_image: page_256.png
page_number: 256
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.20
tokens: 11752
characters: 1906
timestamp: 2025-12-24T01:46:33.975039
finish_reason: stop
---

1 В списке basketball_team пять школьников.
2 TwilightBus везет всю баскетбольную команду.
3 Из автобуса bus вышел сначала один школьник, за ним второй.
4 Вышедшие пассажиры исчезли из баскетбольной команды!

Класс TwilightBus нарушает «принцип наименьшего удивления» — одну из рекомендаций по проектированию интерфейсов. Поистине удивительно, что стоит школьнику выйти из автобуса, как он исчезает из состава баскетбольной команды.

В примере 8.15 приведена реализация класса TwilightBus и объяснена причина проблема.

Пример 8.15. Простой класс, иллюстрирующий опасности, которыми чревато изменение полученных аргументов

class TwilightBus:
    """Автобус, из которого бесследно исчезают пассажиры"""
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = [] ①
        else:
            self.passengers = passengers ②

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name) ③

① Здесь мы честно создаем пустой список, когда passengers совпадает с None.
② Но в результате этого присваивания self.passengers становится синонимом параметра passengers, который сам является синонимом фактического аргумента, переданного методу __init__ т. е. basketball_team в примере 8.14).
③ Применяя методы .remove() и .append() к self.passengers, мы в действительности изменяем исходный список, переданный конструктору в качестве аргумента.

Проблема здесь в том, что в объекте bus создается синоним списка, переданного конструктору. А надо бы хранить собственный список пассажиров. Исправить ошибку просто: в методе __init__ атрибут self.passengers следует инициализировать копией параметра passengers, если тот задан, как и было сделано в примере 8.8.

def __init__(self, passengers=None):
    if passengers is None:
        self.passengers = []
    else:
        self.passengers = list(passengers) ①