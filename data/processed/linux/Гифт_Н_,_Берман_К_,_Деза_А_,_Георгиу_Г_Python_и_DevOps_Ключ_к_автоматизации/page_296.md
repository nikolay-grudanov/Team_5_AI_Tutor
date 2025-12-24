---
source_image: page_296.png
page_number: 296
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.04
tokens: 7469
characters: 1816
timestamp: 2025-12-24T03:08:37.235821
finish_reason: stop
---

проходит через динамический компилятор и оптимизируется с помощью LLVM-компилятора. Если не указать эту опцию, то все не транслированное в LLVM останется обычным кодом на языке Python:

import numpy as np
from numba import jit

@jit(nopython=True)
def go_fast(a):
    """На вход должен быть подан массив Numpy"""

    count = 0
    for i in range(a.shape[0]):
        count += np.tanh(a[i, i])
    return count + trace

Далее мы создаем массив numpy и измеряем время выполнения с помощью «магической» функции IPython:

x = np.arange(100).reshape(10, 10)
%timeit go_fast(x)

Как видно из результатов, код выполняется 855 наносекунд:

The slowest run took 33.43 times longer than the fastest. This example could mean that an intermediate result is cached. 1000000 loops, best of 3: 855 ns per loop

С помощью этой уловки можно запустить и обычную версию, чтобы не нужно было использовать декоратор:

%timeit go_fast.py_func(x)

Как видно из результатов, без динамического компилятора обычный код Python выполняется в 20 раз медленнее:

The slowest run took 4.15 times longer than the fastest. This result could mean that an intermediate run is cached. 10000 loops, best of 3: 20.5 μs per loop

Динамический компилятор Numba умеет оптимизировать циклы for, ускоряя их выполнение, а также функции и структуры данных numpy. Главный вывод из этого примера: возможно, имеет смысл проанализировать уже существующий код, работающий многие годы, и выяснить, не принесет ли пользу критическим компонентам инфраструктуры Python компиляция с помощью динамического компилятора Numba.

Высокопроизводительные серверы

Самореализация — важнейшая составляющая человеческого развития. Простейшее определение самореализации: достижение индивидуумом своего истинного потенциала. Для этого необходимо принять свою человеческую природу со