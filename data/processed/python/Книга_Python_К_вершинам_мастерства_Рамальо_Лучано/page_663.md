---
source_image: page_663.png
page_number: 663
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.39
tokens: 11715
characters: 1808
timestamp: 2025-12-24T02:05:32.557281
finish_reason: stop
---

Переопределяющие и непереопределяющие дескрипторы

pseudo_args = ', '.join(display(x) for x in args)
print('-> {}.__{}__({})'.format(cls_name(args[0]), name, pseudo_args))

### существенные для этого примера классы ##

class Overriding:
    """он же дескриптор данных или принудительный дескриптор"""
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class OverridingNoGet:
    """переопределяющий дескриптор без '__get__'"""
    def __set__(self, instance, value):
        print_args('set', self, instance, value)

class NonOverriding:
    """он же дескриптор без данных или маскируемый дескриптор"""
    def __get__(self, instance, owner):
        print_args('get', self, instance, owner)

class Managed:
    over = Overriding()
    over_no_get = OverridingNoGet()
    non_over = NonOverriding()

    def spam(self):
        print('-> Managed.spam({})'.format(display(self)))

1 Типичный переопределяющий дескрипторный класс с методами __get__ и __set__.
2 В этом примере функция print_args вызывается из каждого метода дескриптора.
3 Переопределяющий дескриптор без метода __get__.
4 Здесь нет метода __set__, т. е. этот дескриптор непереопределяющий.
5 Управляемый класс, в котором используется по одному экземпляру каждого дескрипторного класса.
6 Метод spam включен для сравнения, потому что методы — также дескрипторы.

В следующих разделах мы исследуем поведение операций чтения и записи атрибутов класса Managed и одного его экземпляра с помощью каждого из определенных выше дескрипторов.

Переопределяющий дескриптор

Дескриптор, в котором реализован метод __set__, называется переопределяющим, потому что несмотря на то, что этот дескриптор является атрибутом класса,