---
source_image: page_666.png
page_number: 666
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.27
tokens: 7844
characters: 2649
timestamp: 2025-12-24T01:27:56.971005
finish_reason: stop
---

if not pythons:
    # Запустить оператор stmt в этой версии Python: вызов API-интерфейса
    # Нет необходимости разделять строки или помещать в кавычки
    ispy3 = sys.version[0] == '3'
    stmt = stmt.replace('$listif3', 'list' if ispy3 else '')
    best = min(timeit.repeat(stmt=stmt, number=number, repeat=repeat))
    print('%.4f [%r]' % (best, stmt[:70]))
else:
    # Запустить оператор stmt во всех версиях Python: командная строка
    # Разделить строки на аргументы в кавычках
    print('-' * 80)
    print('[%r]' % stmt)
    for (ispy3, python) in pythons:
        stmt1 = stmt.replace('$listif3', 'list' if ispy3 else '')
        stmt1 = stmt1.replace('\t', ' ' * 4)
        lines = stmt1.split('\n')
        args = ' '.join('"%s"' % line for line in lines)
        cmd = '%s -m timeit -n %s -r %s %s' % (python, number, repeat, args)
        print(python)
        if tracecmd: print(cmd)
        print('\t' + os.popen(cmd).read().rstrip())

Однако данный файл отражает лишь половину картины. Тестовые сценарии применяют функцию модуля, передавая конкретные (хотя и изменяемые) списки операторов и подлежащих тестированию версий Python в зависимости от желаемого режима использования. Скажем, сценарий pybench_cases.py, содержимое которого приведено далее, тестирует несколько операторов и версий Python, позволяя с помощью аргументов командной строки определять часть своей работы. Указание -a означает тестирование всех перечисленных версий Python, а не только одной, наличие -t заставляет выполнять трассировку создаваемых командных строк, чтобы можно было видеть, каким образом многострочные операторы и отступы обрабатываются согласно показанным ранее форматам (детали описаны в строках документации обоих файлов):

"""
pybench_cases.py: запускает pybench на наборе версий Python и операторов.
Выбирайте режимы путем редактирования этого сценария либо использования аргументов командной строки (в sys.argv): например, запускайте
C:\python27\python pybench_cases.py, чтобы протестировать только одну версию Python из перечисленных в stmts, pybench_cases.py -a
для тестирования всех версий Python и py -3 pybench_cases.py -a -t
для трассировки командных строк.
"""

import pybench, sys

pythons = [
    (1, 'C:\\python33\\python'),
    (0, 'C:\\python27\\python'),
    (0, 'C:\\pyru\\pyru-1.9\\pyru')
]

stmts = [
    (0, 0, "[x ** 2 for x in range(1000)]"),           # (Python 3?, путь)
    (0, 0, "res=[]\nfor x in range(1000): res.append(x ** 2)"),   # Итерации
    (0, 0, "$listif3(map(lambda x: x ** 2, range(1000)))"),   # количество, повторения, оператор
    (0, 0, "\n\t = отступ")                              # \n\t = отступ