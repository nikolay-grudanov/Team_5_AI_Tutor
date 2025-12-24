---
source_image: page_222.png
page_number: 222
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 33.18
tokens: 11658
characters: 1358
timestamp: 2025-12-24T01:44:50.395977
finish_reason: stop
---

Пример 7.16. Использование декоратора clock

# clockdeco_demo.py

import time
from clockdeco import clock

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

if __name__ == '__main__':
    print('*' * 40, 'Calling snooze(.123)')
    snooze(.123)
    print('*' * 40, 'Calling factorial(6)')
    print('6! =', factorial(6))

Вот что выводит этот код:

$ python3 clockdeco_demo.py
************************************************************************** Calling snooze(123)
[0.12405610s] snooze(.123) -> None
************************************************************************** Calling factorial(6)
[0.00000191s] factorial(1) -> 1
[0.00004911s] factorial(2) -> 2
[0.00008488s] factorial(3) -> 6
[0.00013208s] factorial(4) -> 24
[0.00019193s] factorial(5) -> 120
[0.00026107s] factorial(6) -> 720
6! = 720

Как это работает

Напомним, что код

@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)

на самом деле эквивалентен следующему:

def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)
factorial = clock(factorial)

То есть в обоих случаях декоратор clock получает функцию factorial в качестве аргумента func (см. пример 7.15). Затем он создает и возвращает функцию clocked, которую интерпретатор Python за кулисами связывает с именем factorial. На са-