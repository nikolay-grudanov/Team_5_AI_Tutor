---
source_image: page_056.png
page_number: 56
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.35
tokens: 7222
characters: 876
timestamp: 2025-12-24T02:35:30.423494
finish_reason: stop
---

**Неизменяемые целые числа**

Команда | Что делает компьютер
--------|----------------------
a = 1000 | Переменные   Объекты
         | a →
         | Id:2f3b
         | 1000
         | Type:Integer

1: Python создает целое число

a = a + 1 | Переменные   Объекты
          | a →
          | Id:2f3b
          | 1000
          | Type:Integer
          |
          | Id:2f3f
          | 1001
          | Type:Integer

2: Python увеличивает a на 1 и создает целое число

a = a + 1 | Переменные   Объекты
          | a →
          | Id:2f3b
          | 1000
          | Type:Integer
          |
          | Id:2f3f
          | 1001
          | Type:Integer

3: Python связывает a с новым объектом и уничтожает старый объект

Рис. 7.2. Попытка изменить целое число неизбежно приводит к созданию нового целого числа. Целые числа неизменяемы, и их значение должно создаваться заново