---
source_image: page_813.png
page_number: 813
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.31
tokens: 7802
characters: 1742
timestamp: 2025-12-24T01:32:40.579076
finish_reason: stop
---

того, чтобы воспринимать эти результаты как абсолютную истину, вы должны провести самостоятельные исследования на своем компьютере и со своей версией Python:

C:\code> c:\python37\python
>>>
>>> def dictcomp(I):
    return {i: i for i in range(I)}
>>> def dictloop(I):
    new = {}
    for i in range(I): new[i] = i
    return new

>>> dictcomp(10)
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
>>> dictloop(10)
{0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
>>>
>>> from timer2 import total, bestof
>>> bestof(dictcomp, 10000)[0]        # Словарь из 10 000 элементов
0.001206016999987014
>>> bestof(dictloop, 10000)[0]
0.001582992999999533
>>>
>>> bestof(dictcomp, 100000)[0]       # Словарь из 100 000 элементов:
# на порядок медленнее
0.01313573400000223
>>> bestof(dictloop, 100000)[0]
0.017253260000003934
>>>
>>> bestof(dictcomp, 1000000)[0]      # Словарь из 1 000 000 элементов:
# еще на порядок медленнее
0.1279122199999847
>>> bestof(dictloop, 1000000)[0]
0.16962867899999878
>>>
>>> total(dictcomp, 1000000, _reps=50)[0]   # Итоги по созданию 50 словарей
# из 1 000 000 элементов
7.04316026699999
>>> total(dictloop, 1000000, _reps=50)[0]
9.104445693000002

11. Рекурсивные функции. Я написал эту функцию следующим образом; подошла бы также встроенная функция range, включение или map, но рекурсия достаточно полезна, чтобы поэкспериментировать с ней здесь (print является функцией в Python 3.x, если только вы не импортировали ее из модуля __future__ или не реализовали собственный эквивалент):

def countdown(N):
    if N == 0:
        print('stop')        # Python 2.x: print 'stop'
    else:
        print(N, end=' ')    # Python 2.x: print N,
        countdown(N-1)
>>> countdown(5)
5 4 3 2 1 stop