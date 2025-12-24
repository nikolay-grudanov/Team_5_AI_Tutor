---
source_image: page_076.png
page_number: 76
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.84
tokens: 7548
characters: 1862
timestamp: 2025-12-24T02:41:55.696988
finish_reason: stop
---

else:
    value = default_value

Поэтому методы словаря get и pop могут принимать значение, возвращаемое по умолчанию, так что этот блок if-else можно упростить:

value = some_dict.get(key, default_value)

Метод get по умолчанию возвращает None, если ключ не найден, тогда как pop в этом случае возбуждает исключение. Часто бывает, что значениями в словаре являются другие коллекции, например списки. Так, можно классифицировать слова по первой букве и представить их набор в виде словаря списков:

In [108]: words = ["apple", "bat", "bar", "atom", "book"]

In [109]: by_letter = {}

In [110]: for word in words:
    ....:     letter = word[0]
    ....:     if letter not in by_letter:
    ....:         by_letter[letter] = [word]
    ....:     else:
    ....:         by_letter[letter].append(word)
    ....:

In [111]: by_letter
Out[111]: {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

Метод setdefault предназначен специально для этой цели. Цикл for выше можно переписать так:

In [112]: by_letter = {}

In [113]: for word in words:
    ....:     letter = word[0]
    ....:     by_letter.setdefault(letter, []).append(word)
    ....:

In [114]: by_letter
Out[114]: {'a': ['apple', 'atom'], 'b': ['bat', 'bar', 'book']}

В стандартном модуле collections есть полезный класс defaultdict, который еще больше упрощает решение этой задачи. Его конструктору передается тип или функция, генерирующая значение по умолчанию для каждой записи в словаре:

In [115]: from collections import defaultdict

In [116]: by_letter = defaultdict(list)

In [117]: for word in words:
    ....:     by_letter[word[0]].append(word)

Допустимые типы ключей словаря
Значениями словаря могут быть произвольные объекты Python, но ключами должны быть неизменяемые объекты, например скалярные типы (int, float, строка) или кортежи (причем все объекты кортежа тоже должны быть неиз-