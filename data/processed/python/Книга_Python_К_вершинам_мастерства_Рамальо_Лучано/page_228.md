---
source_image: page_228.png
page_number: 228
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.77
tokens: 11742
characters: 1979
timestamp: 2025-12-24T01:45:08.331923
finish_reason: stop
---

4 Каждый элемент списка форматируется в соответствии со своим типом, а вся последовательность оформляется как HTML-список.

Поскольку в Python нет механизма перегрузки методов или функций, то мы не можем создать варианты htmlize с разными сигнатурами для каждого типа данных, который желательно обрабатывать специальным образом. Общее решение состоит в том, чтобы преобразовать htmlize в функцию диспетчеризации, содержащую предложение if с несколькими ветвями elif, в каждой из которых вызывается некая специализированная функция: htmlize_str, htmlize_int и т. д. Но такое решение не поддается расширению пользователями модуля и слишком неуклюже: со временем диспетчер htmlize чрезмерно разрастется, а связь между ним и специализированными функциями станет недопустимо тесной.

Новый декоратор functools.singledispatch, появившийся в Python 3.4, позволяет каждому модулю вносить свой вклад в общее решение, так что пользователь легко может добавить специализированную функцию, даже не имея возможности изменять класс. Обычная функция, декорированная @singledispatch, становится обобщенной функцией: группой функций, выполняющих одну и ту же логическую операцию по-разному в зависимости от типа первого аргумента2. В примере 7.21 показано, как это делается.

Декоратор functools.singledispatch добавлен в версии Python 3.4, но в архиве PyPI имеется пакет singledispatch (https://pypi.python.org/pypi/singledispatch), для обратной совместимости с версиями от Python 2.6 до 3.3.

Пример 7.21. Декоратор singledispatch создает функцию htmlize.register для объединения нескольких функций в одну обобщенную

from functools import singledispatch
from collections import abc
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)