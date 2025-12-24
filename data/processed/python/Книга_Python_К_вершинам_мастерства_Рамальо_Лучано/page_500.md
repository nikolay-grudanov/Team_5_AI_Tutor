---
source_image: page_500.png
page_number: 500
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 42.84
tokens: 11644
characters: 1744
timestamp: 2025-12-24T01:58:09.042345
finish_reason: stop
---

Пример 16.12. coro_finally_demo.py: использование try/finally для выполнения некоторых действий по завершении сопрограммы

class DemoException(Exception):
    """An exception type for the demonstration."""

def demo_finally():
    print('-> coroutine started')
    try:
        while True:
            try:
                x = yield
            except DemoException:
                print('*** DemoException handled. Continuing...')
    else:
        print('-> coroutine received: {!r}'.format(x))
    finally:
        print('-> coroutine ending')

Одна из основных причин добавления конструкции yield from в Python 3.3 имеет отношение к возбуждению исключений во вложенных сопрограммах. Другая причина — обеспечить более удобный возврат значений из сопрограмм.

Возврат значения из сопрограммы

В примере 16.13 показан вариант сопрограммы averager, возвращающий результат. Для иллюстрации идеи накопительное среднее возвращается не при каждой активации. Тем самым мы хотим подчеркнуть, что некоторые сопрограммы не отдают ничего интересного, а написаны с целью вернуть значение в конце — зачастую некий аккумулированный результат.

Функция averager из примера 16.13 возвращает именованный кортеж, содержащий количество усредненных элементов (count) и среднее average. Я мог бы вернуть просто average, но возврат кортежа позволяет получить еще один интересный аспект данных: количество членов последовательности.

Пример 16.13. coroaverager2.py: сопрограмма averager, возвращающая результат

from collections import namedtuple

Result = namedtuple('Result', 'count average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break ①
        total += term