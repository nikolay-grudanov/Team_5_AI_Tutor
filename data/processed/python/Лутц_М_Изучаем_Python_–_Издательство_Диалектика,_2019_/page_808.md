---
source_image: page_808.png
page_number: 808
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.64
tokens: 7652
characters: 1900
timestamp: 2025-12-24T01:32:22.823973
finish_reason: stop
---

4. Ключевые аргументы. Далее предлагается мое решение первой и второй частей этого упражнения (содержимое файла mod.py). Для прохода по ключевым аргументам применяйте в заголовке функции форму **args и используйте цикл (скажем, for x in args.keys(): use args[x]) или применяйте args.values(), чтобы делать то же самое, что и суммирование позиционных аргументов *args:

def adder(good=1, bad=2, ugly=3):
    return good + bad + ugly

print(adder())
print(adder(5))
print(adder(5, 6))
print(adder(5, 6, 7))
print(adder(ugly=7, good=6, bad=5))

% python mod.py
6
10
14
18
18

# Решения второй части
def adder1(*args):                # Суммировать любое количество позиционных аргументов
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

def adder2(**args):    # Суммировать любое количество ключевых аргументов
    argskeys = list(args.keys())    # list необходим в Python 3.x!
    tot = args[argskeys[0]]
    for key in argskeys[1:]:
        tot += args[key]
    return tot

def adder3(**args):    # То же самое, но с преобразованием в список значений
    args = list(args.values())    # list необходим для индексации в Python 3.x!
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

def adder4(**args):    # То же самое, но с повторным использованием версии с позиционными аргументами
    return adder1(*args.values())

print(adder1(1, 2, 3), adder1('aa', 'bb', 'cc'))
print(adder2(a=1, b=2, c=3), adder2(a='aa', b='bb', c='cc'))
print(adder3(a=1, b=2, c=3), adder3(a='aa', b='bb', c='cc'))
print(adder4(a=1, b=2, c=3), adder4(a='aa', b='bb', c='cc'))

5. (И 6.) Словарные инструменты. Ниже показаны мои решения упражнений 5 и 6 (файл dicts.py). Однако это всего лишь упражнения по написанию кода, потому что в Python 1.5 появились словарные методы D.copy() и D1.update(D2) для обработки действий вроде копирования и добавления (слияния) словарей.