---
source_image: page_211.png
page_number: 211
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.55
tokens: 11811
characters: 1953
timestamp: 2025-12-24T01:44:30.754663
finish_reason: stop
---

Когда Python выполняет декораторы

1 В registry хранятся ссылки на функции, декорированные @register.
2 register принимает функцию в качестве аргумента.
3 Показываем, какая функция декорируется, — для демонстрации.
4 Включаем func в registry.
5 Возвращаем func: мы должны вернуть функцию, в данном случае возвращается та же функция, что была передана на входе.
6 f1 и f2 декорированы @register.
7 f3 не декорирована.
8 main распечатывает registry, затем вызывает f1(), f2() и f3().
9 main() вызывается только тогда, когда registration.py запускается как скрипт.

Будучи запущена как скрипт, программа registration.py выводит следующие строки:

$ python3 registration.py
running register(<function f1 at 0x100631bf8>)
running register(<function f2 at 0x100631c80>)
running main()
registry -> [<function f1 at 0x100631bf8>, <function f2 at 0x100631c80>]
running f1()
running f2()
running f3()

Отметим, что register выполняется (дважды) до любой другой функции в модуле. При вызове register получает в качестве аргумент декорируемый объект-функцию, например, <function f1 at 0x100631bf8>.

После загрузки модуля в registry оказываются ссылки на две декорированные функции: f1 и f2. Они, как и функция f3, выполняются только при явном вызове из main.

Если registration.py импортируется (а не запускается как скрипт), то вывод выглядит так:

>>> import registration
running register(<function f1 at 0x10063ble0>)
running register(<function f2 at 0x10063b268>)

Если сейчас заглянуть в registry, то мы увидим:

>>> registration.registry
[<function f1 at 0x10063ble0>, <function f2 at 0x10063b268>]

Основная цель примера 7.2 — подчеркнуть, что декораторы функций выполняются сразу после импорта модуля, но сами декорируемые функции — только в результате явного вызова. В этом проявляется различие между этапом импорта и этапом выполнения в Python.

По сравнению с типичным применением декораторов в реальных программах пример 7.2 необычен в двух отношениях.