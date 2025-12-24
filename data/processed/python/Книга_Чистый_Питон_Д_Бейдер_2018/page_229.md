---
source_image: page_229.png
page_number: 229
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.35
tokens: 7222
characters: 1145
timestamp: 2025-12-24T02:32:39.253424
finish_reason: stop
---

'Всем привет'
>>> next(iterator)
'Всем привет'
>>> next(iterator)
StopIteration
>>> next(iterator)
StopIteration

Этот итератор вел себя именно так, как мы и ожидали. Как только мы достигаем конца функции-генератора, он начинает вызывать StopIteration, сигнализируя о том, что у него больше нет значений, которые он мог бы предоставить.

Давайте вернемся к еще одному примеру из раздела об итераторах. Класс BoundedIterator реализовал итератор, который будет повторять значение, заданное определенное количество раз:

class BoundedRepeater:
    def __init__(self, value, max_repeats):
        self.value = value
        self.max_repeats = max_repeats
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            raise StopIteration
        self.count += 1
        return self.value

Почему бы не попробовать реализовать класс BoundedRepeater заново как функцию-генератор? Сделаю первую попытку:

def bounded_repeater(value, max_repeats):
    count = 0
    while True:
        if count >= max_repeats:
            return
        count += 1
        yield value