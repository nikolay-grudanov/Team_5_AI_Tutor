---
source_image: page_432.png
page_number: 432
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.36
tokens: 11589
characters: 1400
timestamp: 2025-12-24T01:54:34.340248
finish_reason: stop
---

В стандартном интерфейсе итератора есть два метода:

__next__
Возвращает следующий доступный элемент и возбуждает исключение StopIteration, когда элементов не осталось.

__iter__
Возвращает self; это позволяет использовать итератор там, где ожидается итерируемый объект, например, в цикле for.

Этот интерфейс формализован в абстрактном базовом классе collections.abc.Iterator, где определен абстрактный метод __next__, и в его подклассе Iterable, где определен абстрактный метод __iter__ (см. рис. 14.1).

![Диаграмма иерархии классов Iterable и Iterator](https://i.imgur.com/3Q5z5QG.png)

Рис. 14.1. Абстрактные классы Iterable и Iterator. Курсивом набраны имена абстрактных методов. Конкретный метод Iterable.iter должен возвращать новый экземпляр Iterator. Конкретный Iterator должен реализовывать метод next.
Метод Iterator.iter просто возвращает ссылку на себя

ABC Iterator реализует метод __iter__, возвращая self. Это дает возможность использовать итератор всюду, где требуется итерируемый объект. Исходный код класса abc.Iterator приведен в примере 14.3

Пример 14.3. Класс abc.Iterator; код взят из файла Lib/_collections_abc.py (http://bit.ly/1C14QOj)

class Iterator(Iterable):

__slots__ = ()

@abstractmethod
def __next__(self):
    'Return the next item from the iterator. When exhausted, raise StopIteration'
    raise StopIteration

def __iter__(self):
    return self

@classmethod