---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 23.96
tokens: 7327
characters: 1289
timestamp: 2025-12-24T02:30:14.827660
finish_reason: stop
---

Далее мы создадим экземпляр Point, а затем его (мелко) скопируем, использовав модуль copy:

```python
>>> a = Point(23, 42)
>>> b = copy.copy(a)
```

Если проинспектировать содержимое оригинального объекта Point и его (мелкого) клона, то мы увидим то, что и ожидали:

```python
>>> a
Point(23, 42)
>>> b
Point(23, 42)
>>> a is b
False
```

Следует иметь в виду кое-что еще. Поскольку наш объект-точка для своих координат использует примитивные типы (целые числа), то в данном случае нет никакой разницы между мелкой и глубокой копией. Но я расширю пример секунду спустя.

Теперь перейдем к более сложному примеру. Я собираюсь определить еще один класс, который будет представлять двумерные прямоугольники. Я сделаю это таким образом, который позволяет создавать более сложную иерархию объектов, — мои прямоугольники будут использовать объекты Point, представляющие их координаты:

```python
class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return (f'Rectangle({self.topleft!r},'
                f'{self.bottomright!r})')
```

Сначала мы попытаемся создать мелкую копию экземпляра Rectangle:

```python
rect = Rectangle(Point(0, 1), Point(5, 6))
srect = copy.copy(rect)
```