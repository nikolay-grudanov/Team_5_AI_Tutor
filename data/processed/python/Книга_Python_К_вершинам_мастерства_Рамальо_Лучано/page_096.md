---
source_image: page_096.png
page_number: 96
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.80
tokens: 11556
characters: 1305
timestamp: 2025-12-24T01:38:43.398157
finish_reason: stop
---

'two'
>>> d.get(4)
'four'
>>> d.get(1, 'N/A')
'N/A'

Tests for the `in` operator::

    >>> 2 in d
True
    >>> 1 in d
False

В примере 3.7 реализован класс StrKeyDict0, для которого все приведенные выше тесты проходят.

Более правильный способ реализовать тип отображения — унаследовать классу collections.UserDict, а не dict (мы так и поступим в примере 3.8). Здесь мы создали подкласс dict просто для демонстрации того, что метод __missing__ поддерживается встроенным методом dict.__getitem__.

Пример 3.7. Класс StrKeyDict0 преобразует нестроковые ключи в тип str во время поиска (см. тесты в примере 3.6)

class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()

1 StrKeyDict0 наследует dict.
2 Проверяем, принадлежит ли ключ key типу str. Если да и при этом отсутствует в словаре, возбуждаем исключение KeyError.
3 Преобразуем key в str и ищем.
4 Метод get делегирует свою работу методу __getitem__ благодаря нотации self[key]; это приводит в действие наш метод __missing__.