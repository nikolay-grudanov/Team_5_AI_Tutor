---
source_image: page_668.png
page_number: 668
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.76
tokens: 7884
characters: 1936
timestamp: 2025-12-24T01:28:04.459091
finish_reason: stop
---

на стандартные библиотечные инструменты os.popen и sys.argv для запуска команды оболочки и инспектирования аргументов командной строки. Дополнительные сведения о них ищите в руководствах по Python и других источниках; инструмент os.popen использовался при рассмотрении файлов в главе 9 и циклов в главе 13. Флаг -t позволяет следить за выполнением командных строк:

c:\code> py -3 pybench_cases.py -a
3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
['[x ** 2 for x in range(1000)]']
C:\python37\python
    1000 loops, best of 5: 487 usec per loop
C:\python27\python
    1000 loops, best of 5: 71.4 usec per loop
C:\pypy\pypy-1.9\pypy
    1000 loops, best of 5: 5.71 usec per loop

['res=[]\nfor x in range(1000): res.append(x ** 2)']
C:\python37\python
    1000 loops, best of 5: 558 usec per loop
C:\python27\python
    1000 loops, best of 5: 130 usec per loop
C:\pypy\pypy-1.9\pypy
    1000 loops, best of 5: 9.81 usec per loop

['$listif3(map(lambda x: x ** 2, range(1000)))']
C:\python37\python
    1000 loops, best of 5: 589 usec per loop
C:\python27\python
    1000 loops, best of 5: 161 usec per loop
C:\pypy\pypy-1.9\pypy
    1000 loops, best of 5: 9.45 usec per loop

['list(x ** 2 for x in range(1000))']
C:\python37\python
    1000 loops, best of 5: 553 usec per loop
C:\python27\python
    1000 loops, best of 5: 92.3 usec per loop
C:\pypy\pypy-1.9\pypy
    1000 loops, best of 5: 15.1 usec per loop

["s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"]
C:\python37\python
    1000 loops, best of 5: 848 usec per loop
C:\python27\python
    1000 loops, best of 5: 614 usec per loop
C:\pypy\pypy-1.9\pypy
    1000 loops, best of 5: 118 usec per loop

["s = '?'\nfor i in range(10000): s += '?'"]
C:\python37\python
    1000 loops, best of 5: 2.83 msec per loop
C:\python27\python
    1000 loops, best of 5: 1.94 msec per loop
C:\pypy\pypy-1.9\pypy
    1000 loops, best of 5: 5.68 msec per loop