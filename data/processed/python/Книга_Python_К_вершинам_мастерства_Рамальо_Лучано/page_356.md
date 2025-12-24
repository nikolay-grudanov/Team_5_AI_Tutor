---
source_image: page_356.png
page_number: 356
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.50
tokens: 11777
characters: 2033
timestamp: 2025-12-24T01:51:02.064138
finish_reason: stop
---

Глава 11. Интерфейсы: от протоколов до абстрактных базовых...

В примере 11.13 показана совершенно другая, но тоже корректная реализация интерфейса Tombola. Вместо перетасовывания «шаров» и выталкивания последнего класс LotteryBlower выбирает элемент в случайной позиции.

Пример 11.13. lotto.py: LotteryBlower — конкретный подкласс, в котором переопределены методы inspect и loaded ABC Tombola

import random

from tombola import Tombola

class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable) ①

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls)) ②
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position) ③

    def loaded(self): ④
        return bool(self._balls)

    def inspect(self): ⑤
        return tuple(sorted(self._balls))

① Инициализатор принимает произвольный итерируемый объект, аргумент используется для построения списка.
② Функция random.randrange(...) возбуждает исключение ValueError, если диапазон пуст, мы перехватываем его и возбуждаем взамен исключение LookupError, сохраняя совместимость с ABC Tombola.
③ В противном случае из self._balls выбирается случайный элемент.
④ Перегружаем метод loaded, чтобы не вызывать inspect (как в методе Tombola.loaded из примера 11.9). Мы можем ускорить его, работая непосредственно с self._balls, — нет необходимости строить весь отсортированный кортеж.
⑤ Перегружаем метод inspect, новый код состоит всего из одной строки.

В примере 11.13 иллюстрируется достойная отдельного упоминания идиома: в методе __init__ в атрибуте self._balls сохраняется list(iterable), а не просто ссылка на iterable (т.е. мы не просто присваиваем iterable атрибуту self._balls). Как уже отмечалось выше13, это повышает гибкость класса LotteryBlower,

13 Я приводил этот код как пример динамической типизации после вставного эссе Мартелли «Водоплавающие птицы и ABC».