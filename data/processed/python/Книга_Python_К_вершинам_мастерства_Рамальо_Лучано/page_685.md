---
source_image: page_685.png
page_number: 685
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.44
tokens: 11599
characters: 1303
timestamp: 2025-12-24T02:06:15.801486
finish_reason: stop
---

Что когда происходит: этап импорта и этап выполнения

print('<[11]> ClassOne tests', 30 * ' .')
one = ClassOne()
one.method_x()
print('<[12]> ClassThree tests', 30 * ' .')
three = ClassThree()
three.method_y()
print('<[13]> ClassFour tests', 30 * ' .')
four = ClassFour()
four.method_y()

print('<[14]> evaltime module end')

Пример 21.7. evalsupport.py: модуль, импортируемый evaltime.py

print('<[100]> evalsupport module start')

def deco_alpha(cls):
    print('<[200]> deco_alpha')
    def inner_1(self):
        print('<[300]> deco_alpha:inner_1')
        cls.method_y = inner_1
        return cls
    # BEGIN META_ALEPH
    class MetaAleph(type):
        print('<[400]> MetaAleph body')
        def __init__(cls, name, bases, dic):
            print('<[500]> MetaAleph.__init__')
            def inner_2(self):
                print('<[600]> MetaAleph.__init__:inner_2')
                cls.method_z = inner_2
        # END META_ALEPH
    print('<[700]> evalsupport module end')

Решение упражнения 1

В примере 21.8 показано, как выглядит экран при импорте модуля evaltime.py в оболочке Python.

Пример 21.8. Упражнение 1: импорт evaltime в оболочке Python

>>> import evaltime
<[100]> evalsupport module start ①
<[400]> MetaAleph body ②
<[700]> evalsupport module end
<[1]> evaltime module start