---
source_image: page_471.png
page_number: 471
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 31.86
tokens: 11675
characters: 1633
timestamp: 2025-12-24T01:56:30.801078
finish_reason: stop
---

Пример 14.26. fibo_by_hand.py: генератор чисел Фибоначчи без использования экземпляров типа GeneratorType

class Fibonacci:

    def __iter__(self):
        return FibonacciGenerator()

class FibonacciGenerator:

    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self

Пример 14.26 работает, но это всего лишь примитивная иллюстрация. Вот как выглядит генератор чисел Фибоначчи в духе Python:

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

И, разумеется, всегда можно воспользоваться языковыми средствами генерации для выполнения основных обязанностей итератора: обхода коллекции и отдачи ее элементов.

На практике программисты на Python относятся к этому различию не так строго: генераторы часто называют итераторами даже в официальной документации. Каноническое определение итератора в глоссарии Python (http://docs.python.org/dev/glossary.html#term-iterator) настолько широко, что охватывает и итераторы:

Итератор: объект, представляющий поток данных. [...]

Полное определение итератора (https://docs.python.org/3/glossary.html#term-iterator) в глоссарии Python стоит прочитать. С другой стороны, в определении генератора (https://docs.python.org/3/glossary.html#term-generator) там же итератор и генератор считаются синонимами, а слово «генератор» обозначает как генераторную функцию, так и объект-генератор, который она строит. Поэтому на жargonе питонистов итератор и генератор трактуются почти как синонимы.