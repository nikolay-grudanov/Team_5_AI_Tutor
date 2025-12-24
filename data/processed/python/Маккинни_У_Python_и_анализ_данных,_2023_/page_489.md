---
source_image: page_489.png
page_number: 489
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.77
tokens: 7621
characters: 1884
timestamp: 2025-12-24T02:53:48.366470
finish_reason: stop
---

for i in range(nx):
    result += x[i] - y[i]
    count += 1
return result / count

Эта функция работает медленно:

In [209]: x = rng.standard_normal(10_000_000)

In [210]: y = rng.standard_normal(10_000_000)

In [211]: %timeit mean_distance(x, y)
1 loop, best of 3: 2 s per loop

In [212]: %timeit (x - y).mean()
100 loops, best of 3: 14.7 ms per loop

Версия, встроенная в NumPy, быстрее в сто с лишним раз. Мы можем преобразовать написанную нами функцию в откомпилированную функцию Numba, воспользовавшись функцией numba.jit:

In [213]: import numba as nb
In [214]: numba_mean_distance = nb.jit(mean_distance)

Можно было бы оформить это и в виде декоратора:

@nb.jit
def numba_mean_distance(x, y):
    nx = len(x)
    result = 0.0
    count = 0
    for i in range(nx):
        result += x[i] - y[i]
        count += 1
    return result / count

Получившаяся функция даже быстрее векторной версии из NumPy:

In [215]: %timeit numba_mean_distance(x, y)
100 loops, best of 3: 10.3 ms per loop

Numba не умеет компилировать произвольный код на Python, но поддерживает обширное подмножество Python, наиболее полезное при реализации численных алгоритмов.

Numba — серьезная библиотека, поддерживающая различные виды оборудования, режимы компиляции и пользовательские расширения. Она способна откомпилировать значительное подмножество Python API библиотеки NumPy, не прибегая к явным циклам for. Кроме того, Numba умеет распознавать конструкции, допускающие встраивание на машинном коде, а если не знает, как откомпилировать код функции, то подставляет обращения к CPython API. У функции Numba jit имеется факультативный аргумент nopython=True, который разрешает использовать только такой код на Python, который можно транслировать на LLVM, не прибегая к вызовам Python C API. Вызов jit(nopython=True) имеет короткий псевдоним numba.njit.

Предыдущий пример можно было бы записать и так: