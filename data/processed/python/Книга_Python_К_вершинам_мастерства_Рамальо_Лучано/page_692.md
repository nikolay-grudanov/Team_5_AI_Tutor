---
source_image: page_692.png
page_number: 692
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 41.03
tokens: 11690
characters: 1534
timestamp: 2025-12-24T02:06:42.896886
finish_reason: stop
---

Пример 21.12. evalsupport.py: определение метакласса MetaAleph из примера 21.7

class MetaAleph(type):
    print('<[400]> MetaAleph body')

    def __init__(cls, name, bases, dic):
        print('<[500]> MetaAleph.__init__')

    def inner_2(self):
        print('<[600]> MetaAleph.__init__:inner_2')

    cls.method_z = inner_2

При кодировании метакласса удобно заменить self на cls. Например, в методе метакласса __init__ благодаря использованию cls для именования первого аргумента сразу становится понятно, что конструируемый экземпляр является классом.

В теле метода __init__ определяется функция inner_2, которая затем связывается с методом cls.method_z. Имя cls в сигнатуре MetaAleph.__init__ относится к создаваемому классу (например, ClassFive). С другой стороны, имя self в сигнатуре inner_2 в конечном итоге будет ссылаться на экземпляр создаваемого класса (например, экземпляр ClassFive).

Решение упражнения 4

В примере 21.13 показан результат запуска команды python evaltime.py из командной строки.

Пример 21.13. Упражнение 4: запуск evaltime_meta.py из оболочки ОС

$ python3 evaltime.py
<[100]> evalsupport module start
<[400]> MetaAleph body
<[700]> evalsupport module end
<[1]> evaltime_meta module start
<[2]> ClassThree body
<[200]> deco_alpha
<[4]> ClassFour body
<[6]> ClassFive body
<[500]> MetaAleph.__init__
<[9]> ClassSix body
<[500]> MetaAleph.__init__
<[11]> ClassThree tests
<[300]> deco_alpha:inner_1 ①
<[12]> ClassFour tests
<[5]> ClassFour.method_y ②
<[13]> ClassFive tests
<[7]> ClassFive.__init__