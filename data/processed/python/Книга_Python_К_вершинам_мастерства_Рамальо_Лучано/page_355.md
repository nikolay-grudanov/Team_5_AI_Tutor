---
source_image: page_355.png
page_number: 355
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 38.83
tokens: 11736
characters: 1930
timestamp: 2025-12-24T01:51:01.360252
finish_reason: stop
---

Определение и использование ABC

ледован от Tombola метод loaded, переопределен метод inspect и добавлен метод __call__.

Пример 11.12. bingo.py: BingoCage — конкретный подкласс Tombola

import random

from tombola import Tombola

class BingoCage(Tombola): ①

    def __init__(self, items):
        self._randomizer = random.SystemRandom() ②
        self._items = []
        self.load(items) ③

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items) ④

    def pick(self): ⑤
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self): ⑥
        self.pick()

① Этот класс BingoCage явно расширяет Tombola.
② Качества класса random.SystemRandom достаточно для программирования азартных игр в сети, он реализует API random, пользуясь функцией os.urandom(...), которая возвращает случайные байты, «пригодные для использования в криптографических приложениях» (документация по модулю os, http://docs.python.org/3/library/os.html#os.urandom).
③ Делегируем начальную загрузку методу .load(...).
④ Вместо функции random.shuffle() используем метод .shuffle() нашего экземпляра SystemRandom.
⑤ Метод pick реализован, как в примере 5.8.
⑥ Метод __call__ также заимствован из примера 5.8. Для согласованности с интерфейсом Tombola он не нужен, но дополнительные методы никакого вреда не принесут.

BingoCage наследует накладный метод loaded и простодушный метод inspect от Tombola. Тот и другой можно переопределить гораздо более быстрыми однорядными методами, как в примере 11.13. Но хочу подчеркнуть — мы можем не утруждать себя и просто унаследовать неоптимальные конкретные методы от ABC. Методы, унаследованные от Tombola, работают не так быстро, как могли бы в BingoCage, но дают правильные результаты для любого подкласса Tombola, в котором корректно реализованы методы pick и load.