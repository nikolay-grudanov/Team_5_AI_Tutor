---
source_image: page_127.png
page_number: 127
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 18.01
tokens: 7267
characters: 1225
timestamp: 2025-12-24T02:30:16.095643
finish_reason: stop
---

Более того, и создание экземпляра, и использование Concrete работают так, как ожидалось. И если вызвать не реализованный в нем метод, такой как bar(), то в результате тоже будет вызвано исключение:

```python
>>> c = Concrete()
>>> c.foo()
'вызвана foo()'
>>> c.bar()
NotImplementedError
```

Эта первая реализация выглядит неплохо, но пока не идеально. Ее оборотными сторонами является то, что мы по-прежнему можем

- легко создавать экземпляры Base, не получая ошибку, а также
- обеспечивать неполные подклассы — создание экземпляра Concrete не будет вызывать ошибку до тех пор, пока мы не вызовем отсутствующий метод bar().

При помощи модуля Python abc, который был добавлен в Python 2.6¹, мы можем добиться большего успеха и решить эти оставшиеся проблемы. Вот обновленная реализация с использованием абстрактного класса, определенного в модуле abc:

```python
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass
    # Мы снова забыли объявить bar()...
```

¹ См. документацию Python «Модуль abc»: https://docs.python.org/3/library/abc.html