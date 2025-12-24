---
source_image: page_225.png
page_number: 225
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 58.44
tokens: 11927
characters: 1499
timestamp: 2025-12-24T01:45:24.664524
finish_reason: stop
---

Декораторы в стандартной библиотеке

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == '__main__':
    print(fibonacci(6))

Вот результат работы fibo_demo.py. Все строки, кроме последней, выведены декоратором clock:

$ python3 fibo_demo.py
[0.00000095s] fibonacci(0) -> 0
[0.00000095s] fibonacci(1) -> 1
[0.00007892s] fibonacci(2) -> 1
[0.00000095s] fibonacci(1) -> 1
[0.00000095s] fibonacci(0) -> 0
[0.00000095s] fibonacci(1) -> 1
[0.00003815s] fibonacci(2) -> 1
[0.00007391s] fibonacci(3) -> 2
[0.00018883s] fibonacci(4) -> 3
[0.00000000s] fibonacci(1) -> 1
[0.00000095s] fibonacci(0) -> 0
[0.00000119s] fibonacci(1) -> 1
[0.00004911s] fibonacci(2) -> 1
[0.00009704s] fibonacci(3) -> 2
[0.00000000s] fibonacci(0) -> 0
[0.00000000s] fibonacci(1) -> 1
[0.00002694s] fibonacci(2) -> 1
[0.00000095s] fibonacci(1) -> 1
[0.00000095s] fibonacci(0) -> 0
[0.00000095s] fibonacci(1) -> 1
[0.00005102s] fibonacci(2) -> 1
[0.00008917s] fibonacci(3) -> 2
[0.00015593s] fibonacci(4) -> 3
[0.00029993s] fibonacci(5) -> 5
[0.00052810s] fibonacci(6) -> 8

Непроизводительные затраты бросаются в глаза: fibonacci(1) вызывается во семь раз, fibonacci(2) — пять раз и т. д. Но если добавить две строчки, чтобы задействовать lru_cache, то производительность резко возрастет.

Пример 7.19. Более быстрая реализация с использованием кэширования

import functools

from clockdeco import clock

@functools.lru_cache() # ①
@clock # ②
def fibonacci(n):
    if n < 2: