---
source_image: page_233.png
page_number: 233
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 53.04
tokens: 11850
characters: 1889
timestamp: 2025-12-24T01:45:40.028578
finish_reason: stop
---

Параметризованные декораторы

Пример 7.24. Использование модуля registration_param из примера 7.23

>>> from registration_param import *
running register(active=False)->decorate(<function f1 at 0x10073c1e0>)
running register(active=True)->decorate(<function f2 at 0x10073c268>)
>>> registry # ①
{<function f2 at 0x10073c268>}
>>> register()(f3) # ②
running register(active=True)->decorate(<function f3 at 0x10073c158>)
<function f3 at 0x10073c158>
>>> registry # ③
{<function f3 at 0x10073c158>, <function f2 at 0x10073c268>}
>>> register(active=False)(f2) # ④
running register(active=False)->decorate(<function f2 at 0x10073c268>)
<function f2 at 0x10073c268>
>>> registry # ⑤
{<function f3 at 0x10073c158>}

① После импортирования модуля f2 оказывается в registry.
② Выражение register() возвращает декоратор decorate, который затем применяется к f3.
③ В предыдущей строке функция f3 была добавлена в registry.
④ Этот вызов удаляет f2 из registry.
⑤ Убеждаемся, что f3 осталась в registry.

Механизм работы параметризованных декораторов довольно сложен; рассмотренный выше пример проще, чем в большинстве случаев. Параметризованные декораторы обычно заменяют декорируемую функцию, а в их конструкторах необходимо еще один уровень вложенности. В экскурсию по такой пирамиде функций мы отправимся в следующем разделе.

Параметризованный декоратор clock

В этом разделе мы вернемся к декоратору clock и добавим возможность передавать ему строку, управляющую форматом вывода. См. пример 7.25.

Для простоты код в примере 7.25 основан на первоначальной реализации clock в примере 7.15, а не на улучшенной реализации из примера 7.17, в которой использовался декоратор @functools.wraps, добавляющий еще один слой.

Пример 7.25. Модуль clockdeco_param.py: параметризованный декоратор clock

import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'

def clock(fmt=DEFAULT_FMT): ①