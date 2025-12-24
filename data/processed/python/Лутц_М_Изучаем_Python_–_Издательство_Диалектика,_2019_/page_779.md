---
source_image: page_779.png
page_number: 779
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.88
tokens: 7570
characters: 2159
timestamp: 2025-12-24T01:31:24.289576
finish_reason: stop
---

предложило бы аналогичную функциональность в случае использования для вставки visited.add(module):

#!/python
"""
reloadall.py: транзитивная перезагрузка вложенных модулей (Python 2.x + 3.x).
Вызовайте reload_all с одним и более объектами импортированных модулей.
"""

import types
from imp import reload

def status(module):
    print('reloading ' + module.__name__)

def tryreload(module):
    try:
        reload(module)      # В Python 3.3 (только?) иногда терпело неудачу
    except:
        print('FAILED: %s' % module)

def transitive_reload(module, visited):
    if not module in visited:
        status(module)
        tryreload(module)
        visited[module] = True
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

def tester(reloader, modname):
    import importlib, sys
    if len(sys.argv) > 1: modname = sys.argv[1]  # Командная строка
    module = importlib.import_module(modname)     # Импортировать по строке
    reloader(module)                              # Тестировать переданный аргумент reloader
    if __name__ == '__main__':
        tester(reload_all, 'reloadall')           # Тест: перезагрузка самого себя?

Помимо словарей пространств имен в сценарии применяются другие исследуемые в примере инструменты. Он включает проверку __name__ для выполнения кода самотестирования в случае запуска как сценария верхнего уровня, а его функция tester использует sys.argv для инспектирования аргументов командной строки и importlib для импортирования модуля по имени в строке, переданного в аргументе командной строки. Один любопытный момент: обратите внимание, что базовый вызов reload должен быть помещен внутрь оператора try, чтобы перехватывать исключения — в Python 3.3 перезагрузка иногда терпела неудачу из-за переписанных механизмов импортирования; возможно, ситуация несколько улучшится в последующих версиях (в Python 3.7 ошибку воспроизвести не удалось (исправлено?) — прим.пер.).