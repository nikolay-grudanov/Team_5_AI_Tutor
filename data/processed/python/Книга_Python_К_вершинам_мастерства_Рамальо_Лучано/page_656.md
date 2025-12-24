---
source_image: page_656.png
page_number: 656
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 44.27
tokens: 11733
characters: 1859
timestamp: 2025-12-24T02:05:15.952940
finish_reason: stop
---

С другой стороны, для поддержки интроспекции и других приемов метапрограммирования рекомендуется возвращать из __get__ экземпляр дескриптора, когда доступ к управляемому атрибуту производится через класс. В примере 20.3 показана слегка измененная по сравнению с примером 20.2 реализация метода Quantity.__get__.

Пример 20.3. bulkfood_v4b.py (неполный листинг): при вызове через управляемый класс метод __get__ возвращает ссылку на сам дескриптор

class Quantity:
    __counter = 0

    def __init__(self):
        cls = self.__class__
        prefix = cls.__name__
        index = cls.__counter
        self.storage_name = '_{}#{}'.format(prefix, index)
        cls.__counter += 1

    def __get__(self, instance, owner):
        if instance is None:
            return self ①
        else:
            return getattr(instance, self.storage_name) ②

    def __set__(self, instance, value):
        if value > 0:
            setattr(instance, self.storage_name, value)
        else:
            raise ValueError('value must be > 0')

① Если вызов производился не от имени экземпляра, то возвращаем сам дескриптор.
② В противном случае, как обычно, возвращаем значение управляемого атрибута.

Ниже показан результат выполнения примера 20.3:

>>> from bulkfood_v4b import LineItem
>>> LineItem.price
<bulkfood_v4b.Quantity object at 0x100721be0>
>>> br_nuts = LineItem('Brazil nuts', 10, 34.95)
>>> br_nuts.price
34.95

При взгляде на пример 20.2 возникает чувство, что уж слишком много кода для управления всего двумя атрибутами, однако важно понимать, что логика дескриптора теперь вынесена в отдельную единицу кода: класс Quantity. Обычно дескриптор определяется не в том же модуле, где используется, а в отдельном служебном модуле, который предназначен для использования в разных местах приложения — и даже в разных приложениях, если разрабатывается каркас.