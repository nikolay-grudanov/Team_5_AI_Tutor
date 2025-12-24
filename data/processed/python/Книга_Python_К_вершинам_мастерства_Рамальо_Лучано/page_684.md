---
source_image: page_684.png
page_number: 684
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.17
tokens: 11542
characters: 1163
timestamp: 2025-12-24T02:06:08.797379
finish_reason: stop
---

Глава 21. Метапрограммирование классов

Листинги приведены в примерах 21.6 и 21.7. Возьмите бумагу и ручку и — не выполняя код — выпишите маркеры в том порядке, в каком они, по вашему мнению, будут напечатаны.

Упражнение 1
Модуль evaltime.py интерактивно импортируется в оболочке Python:
>>> import evaltime

Упражнение 2
Модуль evaltime.py выполняется из командной строки:
$ python3 evaltime.py

Пример 21.6. evaltime.py: выпишите пронумерованные маркеры <[N]> в порядке появления на экране

from evalsupport import deco_alpha

print('<[1]> evaltime module start')

class ClassOne():
    print('<[2]> ClassOne body')
    def __init__(self):
        print('<[3]> ClassOne.__init__')
    def __del__(self):
        print('<[4]> ClassOne.__del__')
    def method_x(self):
        print('<[5]> ClassOne.method_x')

class ClassTwo(object):
    print('<[6]> ClassTwo body')

@deco_alpha
class ClassThree():
    print('<[7]> ClassThree body')
    def method_y(self):
        print('<[8]> ClassThree.method_y')

class ClassFour(ClassThree):
    print('<[9]> ClassFour body')
    def method_y(self):
        print('<[10]> ClassFour.method_y')

if __name__ == '__main__':