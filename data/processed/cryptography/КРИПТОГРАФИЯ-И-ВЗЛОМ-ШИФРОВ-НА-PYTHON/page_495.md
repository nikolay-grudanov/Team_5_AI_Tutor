---
source_image: page_495.png
page_number: 495
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.09
tokens: 7377
characters: 1277
timestamp: 2025-12-24T08:58:49.602169
finish_reason: stop
---

<table>
  <tr>
    <th>Оператор not</th>
    <th></th>
    <th></th>
    <th>Результат</th>
  </tr>
  <tr>
    <td>not</td>
    <td>A</td>
    <td>= =</td>
    <td></td>
  </tr>
  <tr>
    <td>not</td>
    <td>True</td>
    <td>= =</td>
    <td>False</td>
  </tr>
  <tr>
    <td>not</td>
    <td>False</td>
    <td>= =</td>
    <td>True</td>
  </tr>
</table>

4. Какая из приведенных ниже инструкций корректна?

if __name__ == '__main__':
if __main__ == '__name__':
if _name_ == '_main_':
if _main_ == '_name_':

ОТВЕТ: if __name__ == '__main__':

Глава 9

1. Если вы запустили приведенную ниже программу и она вывела на экран число 8, то что будет выведено на экран, когда вы запустите программу в следующий раз?

import random
random.seed(9)
print(random.randint(1, 10))

ОТВЕТ: 8. (В результате задания одного и того же затравочного числа будут генерироваться одни и те же псевдослучайные числа.)

2. Что выведет на экран следующая программа?

spam = [1, 2, 3]
eggs = spam
ham = eggs
ham[0] = 99
print(ham == spam)

ОТВЕТ: True

3. В каком модуле содержится функция deepcopy()?

ОТВЕТ: в модуле copy.

4. Что выведет на экран следующая программа?

import copy
spam = [1, 2, 3]
eggs = copy.deepcopy(spam)
ham = copy.deepcopy(eggs)
ham[0] = 99
print(ham == spam)

ОТВЕТ: False