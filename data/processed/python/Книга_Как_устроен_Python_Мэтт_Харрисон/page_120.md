---
source_image: page_120.png
page_number: 120
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 29.19
tokens: 7385
characters: 1608
timestamp: 2025-12-24T02:37:08.008417
finish_reason: stop
---

с Chair6. Так как класс Chair6 содержит только атрибут max_occupants, Python не найдет здесь метод __init__. Но поскольку Chair6 является субклассом CorrectChair, он обладает атрибутом __bases__ с перечислением базовых классов, сведенных в кортеж:

```python
>>> Chair6.__bases__
(__main__.CorrectChair,)
```

Затем Python ищет конструктор в базовых классах. Он находит конструктор в CorrectChair и использует его для создания нового класса.

Такой же поиск происходит при вызове .load для экземпляра. У экземпляра нет атрибута, соответствующего имени метода, поэтому Python проверяет класс экземпляра. В Chair6 тоже нет метода .load, поэтому Python ищет атрибут в базовом классе CorrectChair. Здесь метод .load вызывается со слишком большим значением, что приводит к ошибке ValueError:

```python
>>> sixer.load(7)
Traceback (most recent call last):
  File "/tmp/chair.py", line 30, in <module>
    sixer.load(7)
  File "/tmp/chair.py", line 13, in load
    new_val = self._check(self.count + number)
  File "/tmp/chair.py", line 23, in _check
    number))
ValueError: Invalid count:7
```

Python находит метод в базовом классе, но вызов метода ._check приводит к ошибке ValueError.

22.1. Подсчет остановок

Иногда лыжнику не удается нормально сесть на подъемник. В таких случаях оператор замедляет движение или останавливает подъемник, чтобы помочь лыжнику. Мы можем воспользоваться Python для создания нового класса, который будет подсчитывать количество таких остановок.

Предположим, при каждом вызове .load должна вызываться функция, которая возвращает логический признак того, произошла остановка или