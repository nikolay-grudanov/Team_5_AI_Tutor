---
source_image: page_114.png
page_number: 114
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 26.09
tokens: 7326
characters: 1443
timestamp: 2025-12-24T02:36:57.869440
finish_reason: stop
---

Вот текст программы на русском языке:

```python
def __init__(self, id):
    self.id = id
    self.count = 0

def load(self, number):
    new_val = self._check(self.count + number)
    self.count = new_val

def unload(self, number):
    new_val = self._check(self.count - number)
    self.count = new_val

def _check(self, number):
    if number < 0 or number > self.max_occupants:
        raise ValueError('Invalid count:{}'.format(number))
    return number

NUM_CHAIRS = 100

chairs = []
for num in range(1, NUM_CHAIRS + 1):
    chairs.append(CorrectChair(num))

def avg(chairs):
    total = 0
    for c in chairs:
        total += c.count
    return total/len(chairs)

in_use = []
transported = 0
while True:
    # загрузка
    loading = chairs.pop(0)
    in_use.append(loading)
    in_use[-1].load(random.randint(0, CorrectChair.max_occupants))

    # выгрузка
    if len(in_use) > NUM_CHAIRS / 2:
        unloading = in_use.pop(0)
        transported += unloading.count
        unloading.unload(unloading.count)
        chairs.append(unloading)
```

Эта программа создает класс `CorrectChair` с методами `__init__`, `load`, `unload` и `_check`. Затем создается список из 100 объектов этого класса. Далее определяется функция `avg` для вычисления среднего значения `count` всех объектов в списке. В бесконечном цикле происходит загрузка и выгрузка объектов из списка `in_use`, и подсчитывается количество объектов, которое было выгружено.