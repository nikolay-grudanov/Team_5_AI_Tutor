---
source_image: page_358.png
page_number: 358
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.58
tokens: 11775
characters: 2045
timestamp: 2025-12-24T01:51:15.362382
finish_reason: stop
---

```python
raise LookupError('pop from empty TomboList')

load = list.extend # 5

def loaded(self):
    return bool(self) # 6

def inspect(self):
    return tuple(sorted(self))

# Tombola.register(TomboList) # 7

1 Tombolist зарегистрирован как виртуальный подкласс Tombola.
2 Tombolist расширяет list.
3 Tombolist наследует от list метод __bool__, который возвращает True, если список не пуст.
4 Наш метод pick вызывает метод self.pop, унаследованный от list, передавая ему индекс случайного элемента.
5 Tombolist.load — то же самое, что list.extend.
6 Метод loaded делегирует работу методу bool.15
7 В версии Python 3.3 и более ранних использовать .register в качестве декоратора нельзя. Необходимо пользоваться стандартным синтаксисом вызова.

Отметим, что благодаря регистрации функции issubclass и isinstance считают, что TomboList — подкласс Tombola:

>>> from tombola import Tombola
>>> from tombolist import TomboList
>>> issubclass(TomboList, Tombola)
True
>>> t = TomboList(range(100))
>>> isinstance(t, Tombola)
True

Однако наследование управляет специальным атрибутом класса __mro__ — Method Resolution Order (порядок разрешения методов). По существу, в нем перечисляются класс и его суперклассы в том порядке, в котором Python просматривает их в поисках методов.16 Если вывести атрибут __mro__ класса TomboList, то мы увидим в нем только «настоящие» суперклассы — list и object:

>>> TomboList.__mro__
<class 'tombolist.TomboList'>, <class 'list'>, <class 'object'>

15 Прием, использованный в методе load, для loaded работать не будет, потому что в типе list не реализован метод __bool__, который я хотел бы связать с loaded. С другой стороны, встроенная функция bool не нуждается в методе __bool__, потому что может использовать также метод __len__. См. раздел 4.1 «Проверка значения истинности» главы «Встроенные типы» (https://docs.python.org/3/library/stdtypes.html#truth).
16 Ниже целый раздел «Множественное наследование и порядок разрешения методов» посвящен атрибуту класса __mro__. А пока нам хватит и краткого объяснения.