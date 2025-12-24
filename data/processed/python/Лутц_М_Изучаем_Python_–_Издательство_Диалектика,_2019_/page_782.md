---
source_image: page_782.png
page_number: 782
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.04
tokens: 7675
characters: 2437
timestamp: 2025-12-24T01:31:40.565854
finish_reason: stop
---

```python
"""
reloadall2.py: транзитивная перезагрузка вложенных модулей
(альтернативная версия)
"""

import types
from imp import reload                # from требуется в Python 3.x
from reloadall import status, tryreload, tester

def transitive_reload(objects, visited):
    for obj in objects:
        if type(obj) == types.ModuleType and obj not in visited:
            status(obj)
            tryreload(obj)           # Перезагрузить это, рекурсия по атрибутам
            visited.add(obj)
            transitive_reload(obj.__dict__.values(), visited)

def reload_all(*args):
    transitive_reload(args, set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall2')   # Тест: перезагрузка самого себя?

Как объяснялось в главе 19, для большинства рекурсивных функций обычно имеется эквивалент в виде явного стека или очереди, который в ряде контекстов может оказаться предпочтительнее. Далее представлен инструмент транзитивной перезагрузки такого рода; в нем используется генераторное выражение для фильтрации объектов, отличающихся от модулей, и модулей, уже посещенных в пространстве имен текущего модуля. По причине извлечения и добавления элементов в конец списка он основан на стеке, хотя порядок заталкивания элементов и значения словаря влияют на порядок, в котором достигаются и перезагружаются модули. Инструмент посещает подмодули в словарях пространств имен справа налево в отличие от порядка слева направо, поддерживаемого в рекурсивных версиях. Мы могли бы это изменить, но порядок в словарях все равно произвольный.

"""
reloadall3.py: транзитивная перезагрузка вложенных модулей (явный стек)
"""

import types
from imp import reload                # from требуется в Python 3.x
from reloadall import status, tryreload, tester

def transitive_reload(modules, visited):
    while modules:
        next = modules.pop()      # Удалить элемент next в конце
        status(next)               # Перезагрузить это, затолкнуть атрибуты в стек
        tryreload(next)
        visited.add(next)
        modules.extend(x for x in next.__dict__.values())
        if type(x) == types.ModuleType and x not in visited)

def reload_all(*modules):
    transitive_reload(list(modules), set())

if __name__ == '__main__':
    tester(reload_all, 'reloadall3')   # Тест: перезагрузка самого себя?

Если рекурсивная и нерекурсивная версии сбивают с толку, тогда еще раз просмотрите обсуждение рекурсивных функций в главе 19.
```