---
source_image: page_514.png
page_number: 514
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.25
tokens: 7830
characters: 2579
timestamp: 2025-12-24T02:54:37.781436
finish_reason: stop
---

что мы указываем, какую функцию (или функции) хотим профилировать. Порядок вызова такой:

%lprun -f func1 -f func2 профилируемое_предложение

В данном случае мы хотим профилировать функцию add_and_sum, поэтому пишем:

In [573]: %lprun -f add_and_sum add_and_sum(x, y)
Timer unit: 1e-06 s
File: prof_mod.py
Function: add_and_sum at line 3
Total time: 0.045936 s
Line #    Hits    Time Per Hit   % Time   Line Contents
==============================================================================
    3                                                                 def add_and_sum(x, y):
    4        1      36510  36510.0   79.5    added = x + y
    5        1      9425   9425.0   20.5    summed = added.sum(axis=1)
    6        1         1     1.0     0.0    return summed

Так гораздо понятнее. В этом примере мы профилировали ту же функцию, которая составляла предложение. Но можно было бы вызвать функцию call_function из показанного выше модуля и профилировать ее наряду с add_and_sum, это дало бы полную картину производительности кода:

In [574]: %lprun -f add_and_sum -f call_function call_function()
Timer unit: 1e-06 s
File: prof_mod.py
Function: add_and_sum at line 3
Total time: 0.005526 s
Line #    Hits    Time Per Hit   % Time   Line Contents
==============================================================================
    3                                                                 def add_and_sum(x, y):
    4        1      4375   4375.0   79.2    added = x + y
    5        1      1149   1149.0   20.8    summed = added.sum(axis=1)
    6        1         2     2.0     0.0    return summed
File: prof_mod.py
Function: call_function at line 8
Total time: 0.121016 s
Line #    Hits    Time Per Hit   % Time   Line Contents
==============================================================================
    8                                                                 def call_function():
    9        1      57169  57169.0   47.2    x = randn(1000, 1000)
   10        1      58304  58304.0   48.2    y = randn(1000, 1000)
   11        1      554    3  5543.0    4.6    return add_and_sum(x, y)

Обычно я предпочитаю использовать %prun (cProfile) для «макропрофилирования», а %lprun (line_profiler) — для «микропрофилирования». Полезно освоить оба инструмента.

Явно указывать имена подлежащих профилированию функций в команде %lprun необходимо, потому что накладные расходы на «трассировку» времени выполнения каждой строки весьма значительны. Трассировка функций, не представляющих интереса, может существенно изменить результаты профилирования.