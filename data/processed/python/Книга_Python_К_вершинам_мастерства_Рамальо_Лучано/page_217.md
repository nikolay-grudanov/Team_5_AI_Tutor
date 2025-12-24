---
source_image: page_217.png
page_number: 217
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 35.00
tokens: 11653
characters: 1535
timestamp: 2025-12-24T01:44:39.744071
finish_reason: stop
---

Замыкания

анонимной или нет; важно лишь, что она может обращаться к неглобальным переменным, определенным вне ее тела.

Эту идею довольно трудно переварить, поэтому лучше продемонстрировать ее на примере.

Рассмотрим функцию avg, которая вычисляет среднее продолжающегося ряда чисел, например, среднюю цену закрытия биржевого товара за всю историю торгов. Каждый день ряд пополняется новой ценой, а при вычислении среднего учитываются все прежние цены.

Если начать с чистого листа, то функцию avg можно было бы использовать следующим образом:

```python
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
```

Откуда берется avg и где она хранит предыдущие значения?
Для начала покажем реализацию, основанную на классах.

Пример 7.8. average_oo.py: класс для вычисления накопительного среднего

```python
class Averager():
    def __init__(self):
        self.series = []
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total/len(self.series)
```

Класс Averager создает вызываемые объекты:

```python
>>> avg = Averager()
>>> avg(10)
10.0
>>> avg(11)
10.5
>>> avg(12)
11.0
```

А теперь покажем функциональную реализацию с использованием функции высшего порядка make_averager.

Пример 7.9. average.py: функция высшего порядка для вычисления накопительного среднего

```python
def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager
```