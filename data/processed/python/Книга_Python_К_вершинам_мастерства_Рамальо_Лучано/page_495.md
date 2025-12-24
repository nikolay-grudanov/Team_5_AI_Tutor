---
source_image: page_495.png
page_number: 495
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.14
tokens: 11773
characters: 1797
timestamp: 2025-12-24T01:57:48.279275
finish_reason: stop
---

Декораторы для инициализации сопрограмм

Чтобы защититься от такой напасти, можно применить к сопрограмме специальный декоратор. Один такой декоратор представлен ниже.

Декораторы для инициализации сопрограмм

Пока сопрограмма не инициализирована, она практически бесполезна, нужно не забыть вызвать next(my_coro) до my_coro.send(x). Чтобы облегчить работу с сопрограммами, иногда используется инициализирующий декоратор. Один такой декоратор coroutine показан ниже3.

Пример 16.5. coroutil.py: декоратор для инициализации сопрограмм

from functools import wraps

def coroutine(func):
    """Decorator: primes `func` by advancing to first 'yield'"""
    @wraps(func)
    def primer(*args, **kwargs): ①
        gen = func(*args, **kwargs) ②
        next(gen) ③
        return gen ④
    return primer

① Декорированная генераторная функция подменяется этой функцией primer, которая при вызове возвращает инициализированный генератор.
② Вызываем декорированную функцию, чтобы получить инициализированный генератор.
③ Инициализируем генератор.
④ Возвращаем его

В примере 16.6 показано, как используется декоратор @coroutine. Сравните с примером 16.3.

Пример 16.6. coroaverager1.py: doctest-скрипт и код сопрограммы вычисления накопительного среднего с использованием декоратора @coroutine из примера 16.5

"""
A coroutine to compute a running average

>>> coro_avg = averager() ①
>>> from inspect import getgeneratorstate
>>> getgeneratorstate(coro_avg) ②
'GEN_SUSPENDED'
>>> coro_avg.send(10) ③
10.0
>>> coro_avg.send(30)

3 В вебе опубликовано несколько подобных декораторов. Конкретно этот — слегка видоизмененный вариант рецепта «Pipeline made of coroutines» на сайте компании ActiveState, предложенного Чоо Бин Танем, который, в свою очередь, ссылается на Дэвида Бизли. (http://bit.ly/1MMciCx).