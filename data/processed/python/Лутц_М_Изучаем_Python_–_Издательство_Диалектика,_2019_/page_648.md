---
source_image: page_648.png
page_number: 648
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.88
tokens: 7649
characters: 2264
timestamp: 2025-12-24T01:27:22.144634
finish_reason: stop
---

# Файл timer.py

"""
Homegrown timing tools for function calls.
Does total time, best-of time, and best-of-totals time
Любительские инструменты для измерения времени выполнения вызовов функций.
Определяют суммарное время, лучшее время и лучшее суммарное время
"""

import time, sys
timer = time.clock if sys.platform[:3] == 'win' else time.time

def total(reps, func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    Суммарное время выполнения функции func() reps раз
    Возвращает (суммарное время, последний результат)
    """
    repslist = list(range(reps))  # Вынести за пределы, уравнять Python 2.x, 3.x
    start = timer()                # Или perf_counter/другая в Python 3.3+
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(reps, func, *pargs, **kargs):
    """
    Quickest func() among reps runs.
    Returns (best time, last result)
    Самая быстрая функция func() среди reps запусков.
    Возвращает (лучшее время, последний результат)
    """
    best = 2 ** 32                  # 136 лет представляется достаточным
    for i in range(reps):            # Использование range при измерении времени не учитывается
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start    # Или вызвать total() с reps=1
        if elapsed < best: best = elapsed  # Или добавить в список и найти min()
    return (best, ret)

def bestoftotal(reps1, reps2, func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    Лучшее суммарное время:
    (лучшее время из reps1 запусков (суммарное время reps2 запусков func))
    """
    return bestof(reps1, total, reps2, func, *pargs, **kargs)

В модуле timer реализованы функции измерения суммарного (total) и лучшего (bestof) времени выполнения вызовов, а также функция измерения лучшего суммарного (bestoftotal) времени, которая комбинирует первые две функции. В каждой измеряется время выполнения вызова любой функции с любыми позиционными и ключевыми аргументами, переданными по отдельности, за счет извлечения времени начала, вызова функции и вычитания времени начала из времени окончания.