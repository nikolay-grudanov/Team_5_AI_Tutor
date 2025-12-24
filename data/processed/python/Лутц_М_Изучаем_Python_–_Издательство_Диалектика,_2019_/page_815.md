---
source_image: page_815.png
page_number: 815
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.83
tokens: 7659
characters: 1744
timestamp: 2025-12-24T01:32:37.963030
finish_reason: stop
---

def fact0(N):
    if N == 1:
        return N
    else:
        return N * fact0(N-1)

def fact1(N):
    return N if N == 1 else N * fact1(N-1)

def fact2(N):
    return reduce(lambda x, y: x * y, range(1, N+1))

def fact3(N):
    res = 1
    for i in range(1, N+1): res *= i
    return res

def fact4(N):
    return math.factorial(N)

# Тесты
print(fact0(6), fact1(6), fact2(6), fact3(6), fact4(6))  # 6*5*4*3*2*1:
                                                        # все дают 720
print(fact0(500) == fact1(500) == fact2(500) == fact3(500) == fact4(500))
# True

for test in (fact0, fact1, fact2, fact3, fact4):
    print(test.__name__, min(repeat(stmt=lambda: test(500), number=20, repeat=3)))

r"""
C:\code> py -3 factorials.py
720 720 720 720 720
True
fact0 0.006387722999999956
fact1 0.006470778000000066
fact2 0.004472884999999982
fact3 0.0037610310000000258
fact4 0.0011195480000000257
"""

Вывод: рекурсивная реализация на компьютере с имеющейся версией Python выполняется медленнее всех и терпит неудачу, как только N достигает значения 999, из-за стандартного размера стека, установленного в sys. В главе 19 упоминалось, что данный предел может быть увеличен, но в любом случае простые циклы или стандартный библиотечный инструмент выглядит более удачным вариантом.

Такой общий вывод часто остается справедливым. Скажем, ''.join(reversed(S)) может оказываться предпочтительным способом обращения строки, несмотря на то, что возможны рекурсивные решения. Измерьте время выполнения следующего кода, чтобы выяснить почему: что касается вычисления факториалов в Python 3.x, то рекурсия на сегодняшний день на порядок медленнее в CPython, хотя в PyPy результаты могут варьироваться:

def rev1(S):
    if len(S) == 1:
        return S