---
source_image: page_443.png
page_number: 443
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.47
tokens: 11673
characters: 1513
timestamp: 2025-12-24T01:55:06.539116
finish_reason: stop
---

Класс Sentence, попытка № 5: генераторное выражение

...
    print('continue')
...
    yield 'B'
...
    print('end.')
...
>>> res1 = [x*3 for x in gen_AB()] # 2
start
continue
end.
>>> for i in res1: # 3
...     print('-->', i)
...
--> AAA
--> BBB
>>> res2 = (x*3 for x in gen_AB()) # 4
>>> res2 # 5
<generator object <genexpr> at 0x10063c240>
>>> for i in res2: # 6
...     print('-->', i)
...
start
--> AAA
continue
--> BBB
end.

1 Та же генераторная функция gen_AB, что в примере 14.6.
2 Списковое включение энергично обходит элементы, порождаемые объектом-генератором, который был создан функцией gen_AB: 'A' и 'B'. Обратите внимание на печать строк start, continue, end.
3 В этом цикле for мы обходим список res1, порожденный списковым включением.
4 Генераторное выражение возвращает res2. Мы вызываем gen_AB(), но в ответ возвращается генератор, который здесь не потребляется.
5 res2 — объект-генератор.
6 Только в цикле for, где производится обход res2, выполняется тело gen_AB. На каждой итерации цикла неявно вызывается next(res2), и выполнение gen_AB продолжается до следующего yield. Обратите внимание на то, как строки, напечатанные внутри gen_AB, чередуются с теми, что печатаются в самом цикле.

Таким образом, генераторное выражение порождает генератор, и мы можем этим воспользоваться, чтобы еще сократить размер класса Sentence.

Пример 14.9. sentence_genexp.py: реализация класса Sentence с помощью генераторного выражения

import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence: