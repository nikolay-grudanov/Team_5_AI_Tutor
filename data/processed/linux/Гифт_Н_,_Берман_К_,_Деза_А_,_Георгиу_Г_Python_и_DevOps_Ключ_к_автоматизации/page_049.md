---
source_image: page_049.png
page_number: 49
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 22.84
tokens: 7263
characters: 1171
timestamp: 2025-12-24T03:02:09.672273
finish_reason: stop
---

Часто бывает нужно изменить регистр текста: выровнять для сравнения или поменять для последующего чтения пользователем. В Python есть несколько методов¹, упрощающих эту задачу:

```python
>>> name = "bill monroe"
>>> name.capitalize()
'Bill monroe'
>>> name.upper()
'BILL MONROE'
>>> name.title()
'Bill Monroe'
>>> name.swapcase()
'BILL MONROE'
>>> name = "BILL MONROE"
>>> name.lower()
'bill monroe'
```

Python также предоставляет методы, упрощающие анализ содержимого строковых значений. Таких методов довольно много, начиная от проверки регистра текста до выяснения того, содержит ли он числовое значение. Вот лишь несколько из наиболее часто используемых методов:

```python
>>> "William".startswith('W')
True
>>> "William".startswith('Bill')
False
>>> "Molly".endswith('olly')
True
>>> "abc123".isalnum()
True
>>> "abc123".isalpha()
False
>>> "abc".isalnum()
True
>>> "123".isnumeric()
True
>>> "Sandy".istitle()
True
>>> "Sandy".islower()
False
>>> "SANDY".isupper()
True
```

Можно вставить текст в строку во время выполнения, управляя ее форматом. Программа может при этом использовать в строках значения переменных или

¹ Работают и с кириллицей. — Примеч. пер.