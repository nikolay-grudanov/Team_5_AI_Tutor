---
source_image: page_456.png
page_number: 456
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 32.53
tokens: 7854
characters: 2371
timestamp: 2025-12-24T01:21:40.275614
finish_reason: stop
---

>>> a, b, c, d = open('script2.py')    # Присваивание последовательностей
>>> a, d
('import sys\n', 'print(x ** 32)\n')
>>> a, *b = open('script2.py')    # Расширенная форма
>>> a, b
('import sys\n', ['print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n'])
>>> 'y = 2\n' in open('script2.py')    # Проверка членства
False
>>> 'x = 2\n' in open('script2.py')
True
>>> L = [11, 22, 33, 44]    # Присваивание срезов
>>> L[1:3] = open('script2.py')
>>> L
[11, 'import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n', 44]
>>> L = [11]
>>> L.extend(open('script2.py'))    # Метод list.extend
>>> L
[11, 'import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n']

Согласно главе 8 метод extend выполняет итерацию автоматически, но метод append — нет; применяйте последний (или похожий метод) для добавления итерируемого объекта в список без итерации с потенциальной итерацией в более позднее время:

>>> L = [11]
>>> L.append(open('script2.py'))    # Метод list.append не выполняет итерацию
>>> L
[11, <_io.TextIOWrapper name='script2.py' mode='r' encoding='cp1252'>]
>>> list(L[1])
['import sys\n', 'print(sys.path)\n', 'x = 2\n', 'print(x ** 32)\n']

Итерация является широко поддерживаемой и мощной моделью. Ранее мы видели, что встроенный вызов dict тоже принимает итерируемый результат zip (см. главы 8 и 13). То же самое касается вызова set, а также более новых выражений включения множеств и словарей в Python 3.x и 2.7, которые встречались в главах 4, 5 и 8:

>>> set(open('script2.py'))
{'print(x ** 32)\n', 'import sys\n', 'print(sys.path)\n', 'x = 2\n'}
>>> {line for line in open('script2.py')}
{'print(x ** 32)\n', 'import sys\n', 'print(sys.path)\n', 'x = 2\n'}
>>> {ix: line for ix, line in enumerate(open('script2.py'))}
{0: 'import sys\n', 1: 'print(sys.path)\n', 2: 'x = 2\n', 3: 'print(x ** 32)\n'}

На самом деле включения множеств и словарей поддерживают расширенный синтаксис списковых включений, который мы обсуждали выше в главе, в том числе проверки if:

>>> {line for line in open('script2.py') if line[0] == 'p'}
{'print(x ** 32)\n', 'print(sys.path)\n'}
>>> {ix: line for (ix, line) in enumerate(open('script2.py')) if line[0] == 'p'}
{1: 'print(sys.path)\n', 3: 'print(x ** 32)\n'}

Подобно списковому включению оба выражения просматривают файл строка за строкой и отбирают строки, начинающиеся с буквы p. В конечном итоге они также