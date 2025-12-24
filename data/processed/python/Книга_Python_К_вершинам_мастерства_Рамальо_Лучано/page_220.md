---
source_image: page_220.png
page_number: 220
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.76
tokens: 11692
characters: 1761
timestamp: 2025-12-24T01:44:50.034366
finish_reason: stop
---

total = 0

def averager(new_value):
    count += 1
    total += new_value
    return total / count

return averager

При попытке выполнить этот код получится вот что:

>>> avg = make_averager()
>>> avg(10)
Traceback (most recent call last):
    ...
UnboundLocalError: local variable 'count' referenced before assignment
>>>

Проблема в том, что предложение count += 1 означает то же самое, что count = count + 1, где count — число или любой неизменяемый тип. То есть мы по сути дела присваиваем count значение в теле averager, делая ее тем самым локальной переменной. То же относится к переменной total.

В примере 7.9 этой проблемы не было, потому что мы ничего не присваивали переменной series; мы лишь вызывали series.append и передавали ее функциям sum и len. То есть воспользовались тем, что список — изменяемый тип.

Однако переменные неизменяемых типов — числа, строки, кортежи и т. д. — разрешается только читать, но не изменять. Если попытаться перепривязать такую переменную, как в случае count = count + 1, то мы неявно создадим локальную переменную count. Она уже не является свободной и потому не запоминается в замыкании.

Чтобы обойти эту проблему, в Python 3 было добавлено объявление nonlocal. Оно позволяет пометить переменную как свободную, даже если ей присваивается новое значение внутри функции. В таком случае изменяется привязка, хранящаяся в замыкании. Корректная реализация функции make_averager показана в примере 7.14.

Пример 7.14. Вычисление накопительного среднего без хранения всей истории (исправленный вариант с nonlocal)

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager