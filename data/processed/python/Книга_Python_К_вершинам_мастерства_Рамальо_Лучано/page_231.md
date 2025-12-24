---
source_image: page_231.png
page_number: 231
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.30
tokens: 11629
characters: 1519
timestamp: 2025-12-24T01:45:08.803338
finish_reason: stop
---

Параметризованные декораторы

сделать, чтобы декоратор принимал и другие аргументы? Ответ таков: написать фабрику декораторов, которая принимает эти аргументы и возвращает декоратор, который затем применяется к декорируемой функции. Непонятно? Естественно. Начнем с примера, основанного на простейшем из рассмотренных до сих пор декораторов: register (см. пример 7.22).

Пример 7.22. Модуль registration.py из примера 7.2 повторен для удобства

registry = []

def register(func):
    print('running register(%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')
print('running main()')
print('registry ->', registry)
f1()

Параметризованный регистрационный декоратор

Чтобы функцию регистрации, вызываемую декоратором register, можно было активировать и деактивировать, мы снабдим ее необязательным параметром active: если он равен False, то декорируемая функция не регистрируется. В примере 7.23 показано, как это делается. Концептуально новая функция register — не декоратор, а фабрика декораторов. Будучи вызвана, она возвращает настоящий декоратор, который применяется к декорируемой функции.

Пример 7.23. Чтобы декоратор мог принимать параметры, его следует вызывать как функцию

registry = set() ①

def register(active=True): ②
    def decorate(func): ③
        print('running register(active=%s)->decorate(%s)' %
              (active, func))
        if active: ④
            registry.add(func)
        else:
            registry.discard(func) ⑤
    return func ⑥