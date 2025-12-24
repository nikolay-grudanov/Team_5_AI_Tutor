---
source_image: page_667.png
page_number: 667
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 43.41
tokens: 8206
characters: 2892
timestamp: 2025-12-24T01:28:14.684859
finish_reason: stop
---

(0, 0, "list(x ** 2 for x in range(1000))"), # $ = list или ''
(0, 0, "s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"),
    # Строчные операции
(0, 0, "s = '?'\nfor i in range(10000): s += '?'"),
]
tracecmd = '-t' in sys.argv        # -t: трассировать командные строки?
pythons = pythons if '-a' in sys.argv else None   # -a: все версии Python
                                                    # в списке, иначе одну?
pybench.runner(stmts, pythons, tracecmd)

Результаты запуска сценария оценочных испытаний

Ниже приведен вывод сценария при его запуске для тестирования специфической версии Python (которая выполняет сценарий) — в таком режиме применяются прямые вызовы API-интерфейса, а не командные строки, с выводом суммарного времени слева и тестируемым оператором справа. В первых двух тестах снова используется запускающий модуль Windows для измерения времени CPython 3.7 и 2.7, а в третьем — выпуск 1.9 реализации PyPy:

c:\code> py -3 pybench_cases.py
3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)]
0.4270 ['[x ** 2 for x in range(1000)]']
0.5445 ['res=[]\nfor x in range(1000): res.append(x ** 2)']
0.5073 ['list(map(lambda x: x ** 2, range(1000)))']
0.4792 ['list(x ** 2 for x in range(1000))']
1.3119 ["s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"]
2.4669 ["s = '?'\nfor i in range(10000): s += '?']"

c:\code> py -2 pybench_cases.py
2.7.3 (default, Apr 10 2012, 23:24:47) [MSC v.1500 64 bit (AMD64)]
0.0696 ['[x ** 2 for x in range(1000)]']
0.1285 ['res=[]\nfor x in range(1000): res.append(x ** 2)']
0.1636 ['(map(lambda x: x ** 2, range(1000)))']
0.0952 ['list(x ** 2 for x in range(1000))']
0.6143 ["s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"]
2.0657 ["s = '?'\nfor i in range(10000): s += '?']"

c:\code> c:\pypy\pypy-1.9\pypy pybench_cases.py
2.7.2 (341ele3821ff, Jun 07 2012, 15:43:00)
[PyPy 1.9.0 with MSC v.1500 32 bit]
0.0059 ['[x ** 2 for x in range(1000)]']
0.0102 ['res=[]\nfor x in range(1000): res.append(x ** 2)']
0.0099 ['(map(lambda x: x ** 2, range(1000)))']
0.0156 ['list(x ** 2 for x in range(1000))']
0.1298 ["s = 'spam' * 2500\nx = [s[i] for i in range(10000)]"]
5.5242 ["s = '?'\nfor i in range(10000): s += '?']"

Далее показан вывод сценария при его запуске для тестирования множества версий Python на каждой строке оператора. В таком режиме сам сценарий выполняется под управлением версии Python 3.7, но выдает командные строки оболочки, которые запускают другие версии Python, чтобы выполнить модуль timeit на тестовых строках операторов. В этом режиме требуется разделение, форматирование и помещение в кавычки многострочных операторов для применения в командных строках согласно ожиданиям модуля timeit и требованиям командной оболочки.

Данный режим полагается на флаг -m командной строки интерпретатора Python для нахождения timeit в пути поиска модулей и его выполнения как сценария, а также