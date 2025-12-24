---
source_image: page_513.png
page_number: 513
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.65
tokens: 7738
characters: 2230
timestamp: 2025-12-24T02:54:33.177263
finish_reason: stop
---

Построчное профилирование функции

Иногда информации, полученной от %prun (или добытой иным способом профилирования на основе cProfile), недостаточно, чтобы составить полное представление о времени работы функции. Или она настолько сложна, что результаты, агрегированные по имени функции, с трудом поддаются интерпретации. На такой случай есть небольшая библиотека line_profiler (ее поможет установить PyPI или любой другой инструмент управления пакетами). Она содержит расширение IPython, включающее новую магическую функцию %lprun, которая строит построчный профиль выполнения одной или нескольких функций. Чтобы подключить это расширение, нужно модифицировать конфигурационный файл IPython (см. документацию по IPython или раздел, посвященный конфигурированию, ниже), добавив такую строку:

# Список имен загружаемых модулей с расширениями IPython.
c.InteractiveShellApp.extensions = ['line_profiler']

Библиотеку line_profiler можно использовать из программы (см. полную документацию), но, пожалуй, наиболее эффективна интерактивная работа с ней в IPython. Допустим, имеется модуль prof_mod, содержащий следующий код, в котором выполняются операции с массивом NumPy (если хотите воспроизвести пример, поместите следующий ниже код в файл prof_mod.py):

from numpy.random import randn

def add_and_sum(x, y):
    added = x + y
    summed = added.sum(axis=1)
    return summed

def call_function():
    x = randn(1000, 1000)
    y = randn(1000, 1000)
    return add_and_sum(x, y)

Если бы мы задались целью оценить производительность функции add_and_sum, то команда %prun дала бы такие результаты:

In [569]: %run prof_mod

In [570]: x = randn(3000, 3000)

In [571]: y = randn(3000, 3000)

In [572]: %prun add_and_sum(x, y)
    4 function calls in 0.049 seconds
Ordered by: internal time
ncalls  tottime  percall  cumtime  percall   filename:lineno(function)
    1    0.036     0.036    0.046     0.046   prof_mod.py:3(add_and_sum)
    1    0.009     0.009    0.009     0.009   {method 'sum' of 'numpy.ndarray'}
    1    0.003     0.003    0.049     0.049   <string>:1(<module>)

Не слишком полезно. Но после активации расширения IPython line_profiler становится доступна новая команда %lprun. От %prun она отличается только тем,