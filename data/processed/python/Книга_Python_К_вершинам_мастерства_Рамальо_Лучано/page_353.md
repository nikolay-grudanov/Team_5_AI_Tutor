---
source_image: page_353.png
page_number: 353
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 39.30
tokens: 11749
characters: 1953
timestamp: 2025-12-24T01:50:56.558578
finish_reason: stop
---

Определение и использование ABC

1 LookupError — исключение, обрабатываемое в методе Tombola.inspect.
2 IndexError — подкласс LookupError, это исключение возбуждается при попытке получить из последовательности элемент с индексом, большим индекса последнего элемента.
3 Исключение KeyError возбуждается при обращении к несуществующему ключу отображения.

Вот мы и создали собственный ABC Tombola. Чтобы посмотреть, как производится проверка интерфейса ABC, попробуем обмануть Tombola, предоставив дефектную реализацию.

Пример 11.11. Непригодная реализация Tombola не останется незамеченной

```python
>>> from tombola import Tombola
>>> class Fake(Tombola): # 1
...     def pick(self):
...         return 13
...
>>> Fake # 2
<class '__main__.Fake'>
<class 'abc.ABC'>, <class 'object'>
>>> f = Fake() # 3
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Fake with abstract methods load
```

1 Объявляем Fake подклассом Tombola.
2 Класс создан, пока никаких ошибок.
3 При попытке создать экземпляр класса Fake возникает исключение TypeError. Сообщение не оставляет сомнений: класс Fake считается абстрактным, потому что в нем не реализован метод load — один из абстрактных методов, объявленных в ABC Tombola.

Итак, мы написали свой первый ABC и проверили, как контролируется его корректность. Скоро мы создадим подкласс Tombola, но сначала поговорим о некоторых правилах программирования ABC.

Синтаксические детали ABC

Лучший способ объявить ABC — сделать его подклассом abc.ABC или какого-нибудь другого ABC.

Однако класс abc.ABC появился только в версии Python 3.4, а если вы пользуетесь более ранней версией (и наследовать другому существующему ABC не имеет смысла), то придется включить в предложение class именованный аргумент metaclass=, указывающий на abc.ABCMeta (не abc.ABC). В примере 11.9 следовало бы написать:

```python
class Tombola(metaclass=abc.ABCMeta):
# ...
```