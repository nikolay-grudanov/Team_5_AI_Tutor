---
source_image: page_045.png
page_number: 45
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 30.10
tokens: 7378
characters: 1341
timestamp: 2025-12-24T03:02:12.449260
finish_reason: stop
---

>>> list("Henry Miller")
['H', 'e', 'n', 'r', 'y', ' ', 'M', 'i', 'l', 'l', 'e', 'r']
>>>

Чаще всего встречаются списки, созданные непосредственно с помощью квадратных скобок. Элементы в них перечисляются явно. Напомним, что элементы списка могут относиться к различным типам данных:

>>> empty = []
>>> empty
[]
>>> nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> nine
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> mixed = [0, 'a', empty, 'WheelHoss']
>>> mixed
[0, 'a', [], 'WheelHoss']
>>>

Самый быстрый способ добавления отдельных элементов в список — присоединение (append) их в его конец. Менее быстрый способ, insert, позволяет вставлять элементы в любое место списка на ваше усмотрение:

>>> pies = ['cherry', 'apple']
>>> pies
['cherry', 'apple']
>>> pies.append('rhubarb')
>>> pies
['cherry', 'apple', 'rhubarb']
>>> pies.insert(1, 'cream')
>>> pies
['cherry', 'cream', 'apple', 'rhubarb']
>>>

С помощью метода extend можно добавить содержимое одного списка в конец другого:

>>> pies
['cherry', 'cream', 'apple', 'rhubarb']
>>> desserts = ['cookies', 'paste']
>>> desserts
['cookies', 'paste']
>>> desserts.extend(pies)
>>> desserts
['cookies', 'paste', 'cherry', 'cream', 'apple', 'rhubarb']
>>>

Наиболее эффективный и часто встречающийся способ удаления последнего элемента списка, с возвратом его значения — pop. В этот метод можно передать