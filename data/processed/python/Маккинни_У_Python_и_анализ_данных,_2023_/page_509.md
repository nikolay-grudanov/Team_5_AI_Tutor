---
source_image: page_509.png
page_number: 509
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.39
tokens: 7623
characters: 2018
timestamp: 2025-12-24T02:54:22.578798
finish_reason: stop
---

Обычно f используется примерно так: f(1, 2, z=3). А чтобы войти в эту функцию, передайте f в качестве первого аргумента функции debug, а затем ее позиционные и именованные аргументы:

In [6]: debug(f, 1, 2, z=3)
> <ipython-input>(2)f()
    1 def f(x, y, z):
----> 2     tmp = x + y
    3     return tmp / z
ipdb>

Мне эти две простенькие функции ежедневно экономят уйму времени.
Наконец, отладчик можно использовать в сочетании с функцией %run. Запустив скрипт командой %run -d, вы попадете прямо в отладчик и сможете расставить точки останова и начать выполнение:

In [1]: %run -d examples/ipython_bug.py
Breakpoint 1 at /home/wesm/code/pydata-book/examples/ipython_bug.py:1
NOTE: Enter 'c' at the ipdb> prompt to start your script.
> <string>(1)<module>()

ipdb>

Если добавить еще флаг -b, указав номер строки, то после входа в отладчик на этой строке уже будет стоять точка останова:

In [2]: %run -d -b2 examples/ipython_bug.py
Breakpoint 1 at /home/wesm/code/pydata-book/examples/ipython_bug.py:2
NOTE: Enter 'c' at the ipdb> prompt to start your script.
> <string>(1)<module>()

ipdb> c
> /home/wesm/code/pydata-book/examples/ipython_bug.py(2)works_fine()
    1 def works_fine():
1----> 2     a = 5
    3     b = 6
ipdb>

Хронометраж программы: %time и %timeit
Для больших или долго работающих аналитических приложений бывает желательно измерить время выполнения различных участков кода или даже отдельных предложений или вызовов функций. Интересно получить отчет о том, какие функции занимают больше всего времени в сложном процессе. По счастью, IPython позволяет без труда получить эту информацию по ходу разработки и тестирования программы.

Ручной хронометраж с помощью встроенного модуля time и его функций time.clock и time.time зачастую оказывается скучной и утомительной процедурой, поскольку приходится писать один и тот же трафаретный код:

import time
start = time.time()
for i in range(iterations):
    # здесь код, который требуется хронометрировать
elapsed_per = (time.time() - start) / iterations