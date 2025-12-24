---
source_image: page_232.png
page_number: 232
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.69
tokens: 11734
characters: 1896
timestamp: 2025-12-24T01:45:24.539878
finish_reason: stop
---

return decorate

@register(active=False)
def f1():
    print('running f1()')

@register()
def f2():
    print('running f2()')

def f3():
    print('running f3()')

1 Теперь registry имеет тип set, чтобы ускорить добавление и удаление функций.
2 Функция register принимает необязательный именованный аргумент.
3 Собственно декоратором является внутренняя функция decorate, она принимает в качестве аргумента функцию.
4 Регистрируем func, только если аргумент active (определенный в замыкании) равен True.
5 Если not active и функция func присутствует в registry, удаляем ее.
6 Поскольку decorate — декоратор, он должен возвращать функцию.
7 Функция register — наша фабрика декораторов, поэтому она возвращает decorate.
8 Фабрику @register следует вызывать как функцию, передавая ей нужные параметры.
9 Даже если параметров нет, register все равно нужно вызывать как функцию — @register() — чтобы она вернула настоящий декоратор decorate.

Идея в том, что функция register() возвращает декоратор decorate, который затем применяется к декорируемой функции.

Код из примера 7.23 находится в модуле registration_param.py. Если его импортировать, получится вот что:

>>> import registration_param
running register(active=False)->decorate(<function f1 at 0x10063c1e0>)
running register(active=True)->decorate(<function f2 at 0x10063c268>)
>>> registration_param.registry
[<function f2 at 0x10063c268>]

Заметим, что в registry присутствует только функция f2, а функция f1 туда не попала, потому что фабрике декораторов register был передан аргумент active=False.

Если бы мы использовали register как обычную функцию без символа @, то для декорирования функции f, т. е. для добавления ее в registry, нужно было бы написать register()(f), а чтобы не добавлять f в реестр (или удалить оттуда) — register(active=False)(f). В примере 7.24 показано, как добавлять функции в реестр registry и удалять из него.