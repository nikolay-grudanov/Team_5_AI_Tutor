---
source_image: page_511.png
page_number: 511
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.12
tokens: 7718
characters: 2117
timestamp: 2025-12-24T02:54:30.598867
finish_reason: stop
---

In [565]: x = 'foobar'

In [566]: y = 'foo'

In [567]: %timeit x.startswith(y)
1000000 loops, best of 3: 267 ns per loop

In [568]: %timeit x[:3] == y
10000000 loops, best of 3: 147 ns per loop

Простейшее профилирование: %prun и %run -p
Профилирование кода тесно связано с хронометражем, только отвечает на вопрос, где именно тратится время. В Python основное средство профилирования — модуль cProfile, который предназначен отнюдь не только для IPython. cProfile исполняет программу или произвольный блок кода и следит за тем, сколько времени проведено в каждой функции.

Обычно cProfile запускают из командной строки, профилируют программу целиком и выводят агрегированные временные характеристики каждой функции. Пусть имеется простой скрипт, который выполняет в цикле какой-нибудь алгоритм линейной алгебры (скажем, вычисляет максимальное по абсолютной величине собственное значение для последовательности матриц размерности 100×100):

import numpy as np
from numpy.linalg import eigvals

def run_experiment(niter=100):
    K = 100
    results = []
    for _ in range(niter):
        mat = np.random.standard_normal((K, K))
        max_eigenvalue = np.abs(eigvals(mat)).max()
        results.append(max_eigenvalue)
    return results
some_results = run_experiment()
print('Largest one we saw: {0}'.format(np.max(some_results)))

Это скрипт можно запустить под управлением cProfile из командной строки следующим образом:

python -m cProfile cprof_example.py

Попробуйте и убедитесь, что результаты отсортированы по имени функции. Такой отчет не позволяет сразу увидеть, где тратится время, поэтому обычно порядок сортировки задают с помощью флага -s:

$ python -m cProfile -s cumulative cprof_example.py
Largest one we saw: 11.923204422
15116 function calls (14927 primitive calls) in 0.720 seconds
Ordered by: cumulative time
ncalls  tottime  percall  cumtime  percall  filename:lineno(function)
      1   0.001    0.001    0.721    0.721  cprof_example.py:1(<module>)
     100   0.003    0.000    0.586    0.006  linalg.py:702(eigvals)
    200   0.572    0.003    0.572    0.003  {numpy.linalg.lapack_lite.dgeev}