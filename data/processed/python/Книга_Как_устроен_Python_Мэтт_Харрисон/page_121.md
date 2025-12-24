---
source_image: page_121.png
page_number: 121
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 24.55
tokens: 7311
characters: 1408
timestamp: 2025-12-24T02:37:03.398490
finish_reason: stop
---

нет. В параметрах функции передается количество лыжников и объект кресла.

Ниже приведен класс, который получает функцию is_stalled в конструкторе. Эта функция будет вызываться при каждом вызове .load:

```python
>>> class StallChair(CorrectChair):
...     def __init__(self, id, is_stalled):
...         super().__init__(id)
...         self.is_stalled = is_stalled
...         self.stalls = 0
...
...     def load(self, number):
...         if self.is_stalled(number, self):
...             self.stalls += 1
...         super().load(number)
```

Чтобы создать экземпляр этого класса, необходимо предоставить функцию is_stalled. Следующая простая функция генерирует остановки в 10 % случаев:

```python
>>> import random
>>> def ten_percent(number, chair):
...     """Return True 10% of time"""
...     return random.random() < .1
```

Теперь можно создать экземпляр, указав функцию ten_percent в качестве параметра is_stalled:

```python
>>> stall42 = StallChair(42, ten_percent)
```

22.2. super

Напомним, что StallChair определяет свой собственный метод __init__, который вызывается при создании экземпляра. Обратите внимание: первая строка конструктора выглядит так:

```python
super().__init__(id)
```

При вызове super внутри метода вы получаете доступ к правильному родительскому классу. Строка в конструкторе позволяет вызвать конструктор CorrectChair. Вместо того чтобы повторять логику назначения