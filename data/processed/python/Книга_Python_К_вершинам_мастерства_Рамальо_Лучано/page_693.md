---
source_image: page_693.png
page_number: 693
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 47.96
tokens: 11738
characters: 1834
timestamp: 2025-12-24T02:06:56.179280
finish_reason: stop
---

Метакласс для настройки дескрипторов

< [600] > MetaAleph.__init__:inner_2 ③
< [14] > ClassSix tests ..........................................
< [7] > ClassFive.__init__
< [600] > MetaAleph.__init__:inner_2 ④
< [15] > evaltime_meta module end

① Когда декоратор применяется к классу ClassThree, метод method_y последнего заменяется методом inner_1 ...
② ... но это никак не отражается на недекорированном классе ClassFour, хотя ClassFour является подклассом ClassThree.
③ Метод __init__ метакласса MetaAleph заменяет метод ClassFive.method_z своей функцией inner_2.
④ То же самое происходит с подклассом ClassSix класса ClassFive: его метод method_z заменяется функцией inner_2.

Отметим, что в ClassSix нет прямых ссылок на MetaAleph, и, тем не менее, он изменился, потому что является подклассом ClassFive, а, значит, также и экземпляром MetaAleph, и потому инициализируется методом MetaAleph.__init__.

Дальнейшую настройку класса можно выполнить, реализовав в метаклассе метод __new__. Но обычно реализации метода __init__ достаточно.

Теперь всю эту теорию мы применим на практике и создадим метакласс, который окончательно решит проблему дескрипторов с автоматическими именами атрибутов хранения.

Метакласс для настройки дескрипторов

Вернемся к классу LineItem. Было бы хорошо, если бы пользователю вообще не нужно было знать о каких-то декораторах или метаклассах, а надо было лишь унаследовать классу из нашей библиотеки, как в примере 21.14.

Пример 21.14. bulkfood_v7.py: наследование классу model.Entity сработает, если за кулисами маячит метакласс

import model_v7 as model

class LineItem(model.Entity):
    description = model.NonBlank()
    weight = model.Quantity()
    price = model.Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight