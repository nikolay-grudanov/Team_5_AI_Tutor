---
source_image: page_113.png
page_number: 113
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.37
tokens: 7293
characters: 1331
timestamp: 2025-12-24T02:36:54.620677
finish_reason: stop
---

...
    def __init__(self, id):
        self.id = id
        self.count = 0

    def load(self, number):
        new_val = self._check(self.count + number)
        self.count = new_val

    def unload(self, number):
        new_val = self._check(self.count - number)
        self.count = new_val

    def _check(self, number):
        if number < 0 or number > self.max_occupants:
            raise ValueError('Invalid count:{}'.format(number))
        return number

Метод ._check считается приватным — к нему должны обращаться только экземпляры. Приватные методы вызываются методами .load и .unload класса. При желании вы сможете вызвать их за пределами класса. Тем не менее делать этого не следует — все компоненты с символом подчеркивания считаются подробностями реализации, которые могут отсутствовать в будущих версиях класса.

21.7. Простая программа, моделирующая поток посетителей

Воспользуемся классом для моделирования потока лыжников на горнолыжном курорте. Мы сделаем ряд базовых допущений — например, что на каждом кресле могут с равной вероятностью ехать от 0 до max_occupants лыжников. Класс включает подъемник, загружает его и работает в бесконечном цикле. Четыре раза в секунду выводится текущая статистика:

import random
import time

class CorrectChair:
    ''' A Chair on a chairlift '''
    max_occupants = 4