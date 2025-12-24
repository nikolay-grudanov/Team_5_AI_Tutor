---
source_image: page_363.png
page_number: 363
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 36.36
tokens: 11728
characters: 1912
timestamp: 2025-12-24T01:51:20.738381
finish_reason: stop
---

Гуси могут вести себя как утки

прещено — его следует вызывать как обычную функцию после определения класса (см. комментарий в примере 11.14).

Однако несмотря на то, что теперь register можно использовать как декоратор, чаще он применяется как функция для регистрации классов, определенных где-то в другом месте. Например, в исходном коде модуля collections.abc (http://bit.ly/1QOA3Lt) встроенные типы tuple, str, range и memoryview зарегистрированы как виртуальные подклассы Sequence:

Sequence.register(tuple)
Sequence.register(str)
Sequence.register(range)
Sequence.register(memoryview)

Еще несколько встроенных типов зарегистрированы как подклассы ABC, содержащихся в файле _collections_abc.py (http://bit.ly/1QOA3Lt). Эти регистрации производятся только при импорте указанного файла, но это нормально, потому что для получения самих ABC модуль так или иначе необходимо импортировать: чтобы написать isinstance(my_dict, MutableMapping), необходимо иметь доступ к MutableMapping.

В заключение сбросим завесу тайны с той магии ABC, о которой Алекс Мартелли упоминал в эссе «Водоплавающие птицы и ABC».

Гуси могут вести себя как утки

В своем эссе «Водоплавающие птицы и ABC» Алекс Мартелли показывает, что класс может быть распознан как виртуальный подкласс ABC даже без регистрации. Приведем еще раз его пример, добавив проверку с использованием функции issubclass:

>>> class Struggle:
... def __len__(self): return 23
...
>>> from collections import abc
>>> isinstance(Struggle(), abc.Sized)
True
>>> issubclass(Struggle, abc.Sized)
True

Функция issubclass (а, значит, и isinstance) считает класс Struggle подклассом abc.Sized, потому что abc.Sized реализует специальный метод класса __subclasshook__ (см. пример 11.17).

Пример 11.17. Определение класса Sized из файла Lib/_collections_abc.py (http://bit.ly/1QOG4aP) (Python 3.4)

class Sized(metaclass=ABCMeta):
    __slots__ = ()
    @abstractmethod