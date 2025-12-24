---
source_image: page_657.png
page_number: 657
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.95
tokens: 7810
characters: 2598
timestamp: 2025-12-24T01:27:36.620023
finish_reason: stop
---

repslist = list(range(_reps))  # Вынести range наружу для списков Python 2.x
start = timer()
for i in repslist:
    ret = func(*pargs, **kargs)
    elapsed = timer() - start
    return (elapsed, ret)

def bestof(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 5)
    best = 2 ** 32
    for i in range(_reps):
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start
        if elapsed < best: best = elapsed
    return (best, ret)

def bestoftotal(func, *pargs, **kargs):
    _reps1 = kargs.pop('_reps1', 5)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))

Строки документации в начале файла модуля timer2.py описывают планируемое использование. С применением словарных операций рор аргумент _reps удаляется из аргументов, предназначенных для тестируемой функции, и снабжается стандартным значением (аргумент имеет необычное имя, чтобы избежать конфликта с реальными ключевыми аргументами, относящимися к хронометрируемой функции).

Обратите внимание, что функция bestoftotal здесь вместо вложенных вызовов использует показанную ранее схему с min и генератором, отчасти из-за того, что это упрощает результаты и устраняет небольшой расход времени, который был в предыдущей версии (где код извлекал лучшее время после измерения суммарного времени), но также и потому, что она обязана поддерживать два разных ключевых аргумента для повторений со стандартными значениями — total и bestof не могут применять одно и то же имя аргумента. Добавьте в код вывод аргументов, если он поможет отследить его работу.

Чтобы задействовать новый модуль для измерения времени, можно следующим образом изменить сценарий или обратиться к готовому файлу timeseqs_timer2.py в коде примеров; результаты будут по существу теми же, что и ранее (изменения касаются только API-интерфейса), поэтому здесь они не показаны:

import sys, timer2

...
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    (total, result) = timer2.bestoftotal(test, _reps1=5, _reps=1000)
# Или:
#   (total, result) = timer2.bestoftotal(test)
#   (total, result) = timer2.bestof(test, _reps=5)
#   (total, result) = timer2.total(test, _reps=1000)
#   (bestof, (total, result)) = timer2.bestof(timer2.total, test, _reps=5)
print ('%-9s: %.5f => [%s...%s]' % (test.__name__, total, result[0], result[-1])))

Можно также запустить несколько интерактивных тестов, как делалось для первоначальной версии — результаты в Python 3.7 снова оказываются похожими, но мы передаем счетчики повторений в виде ключевых аргументов и получаем стандартные значения, если аргументы не указаны: