---
source_image: page_105.png
page_number: 105
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.59
tokens: 7291
characters: 1131
timestamp: 2025-12-24T02:36:43.868328
finish_reason: stop
---

>>> num = 42
>>> answer = str(num)
>>> answer
'42'

Говорят, что Python «поставляется с батарейками» — вместе с библиотеками и классами, заранее определенными для разработчика. Эти классы обычно получаются достаточно универсальными. Вы можете определять собственные классы, специализированные для вашей предметной области, специализированные объекты с состоянием и логику для изменения этого состояния.

Классы

Код	Что делает компьютер
status = "off"	Переменные	Объекты
status		Id:2e6a
			"off"
			__class__:str
			...
			__class__:type
			...
			__class__:method_descriptor
			Id:1be2
			__call__
			...
			__class__:method_descriptor
			Id:1aea
			capitalize
			...
			__class__:type
			...
			__class__:method_descriptor
			Id:2e6a
			"off"
			__class__:str
			...
			__class__:type
			...
			__class__:method_descriptor

Рис. 21.2. Обновленная версия объекта строки. Тип изменился на __class__, потому что при анализе объекта атрибут __class__ указывает на класс объекта. Этот класс содержит разные методы (на схеме показан только метод capitalize, но есть много других). Методы тоже являются объектами, как видно из диаграммы