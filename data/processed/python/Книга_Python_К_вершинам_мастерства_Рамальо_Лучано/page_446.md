---
source_image: page_446.png
page_number: 446
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 40.27
tokens: 11923
characters: 2310
timestamp: 2025-12-24T01:55:29.821461
finish_reason: stop
---

Глава 14. Итерируемые объекты, итераторы и генераторы

>>> ap = ArithmeticProgression(0, 1/3, 1)
>>> list(ap)
[0.0, 0.3333333333333333, 0.6666666666666666]
>>> from fractions import Fraction
>>> ap = ArithmeticProgression(0, Fraction(1, 3), 1)
>>> list(ap)
[Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
>>> from decimal import Decimal
>>> ap = ArithmeticProgression(0, Decimal('.1'), .3)
>>> list(ap)
[Decimal('0.0'), Decimal('0.1'), Decimal('0.2')]

Отметим, что числа в получающейся арифметической прогрессии имеют тот же тип, что begin или step, — согласно общим правилам приведения числовых типов в Python. В примере 14.10 мы видим список чисел типа int, float, Fraction и Decimal.

В примере 14.11 показана реализация класса ArithmeticProgression.

Пример 14.11. Класс ArithmeticProgression

class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> "бесконечный" ряд

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)  # 2
        forever = self.end is None  # 3
        index = 0
        while forever or result < self.end:  # 4
            yield result  # 5
            index += 1
            result = self.begin + self.step * index  # 6

1 __init__ требует двух аргументов: begin и step. Аргумент end необязательный, если он равен None, ряд будет неограниченным.
2 Эта строка порождает значение result, равное self.begin, но приведенное к типу последующих слагаемых8.
3 Для большей понятности я завел флаг forever, который равен True, если атрибут self.end равен None, в этом случае получается неограниченный ряд.
4 Этот цикл продолжается вечно или пока значение result не окажется больше или равно self.end. По выходе из цикла завершается и функция.

8 В Python 2 была встроенная функция coerce(), но в Python 3 ее убрали, сочтя лишней, т. к. правила приведения числовых типов неявно встроены в методы арифметических операторов. Поэтому единственный способ, который я смог придумать для приведения начального значения к тому же типу, что остальные члены ряда, — выполнить сложение и воспользоваться его типом для преобразования результата. Я задал этот вопрос в списке рассылки Python-list и получил отличный ответ от Стивена Д'Апрано (http://bit.ly/1JIlbIYO).