---
source_image: page_423.png
page_number: 423
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 27.21
tokens: 7433
characters: 1069
timestamp: 2025-12-24T08:42:03.612757
finish_reason: stop
---

10.6. Какие из следующих адресов являются segwit-адресами? К каким видам segwit-адресов они относятся?

а) bc1qeqzjk7vume5wmrdgz5xyehh54cchdjag6jdmkj
б) c8052b799cde68ed8da8150c4cdef4ae3176cba8
в) bc1qnqaewluxhx7wzfrf9e5fqjf47hjk9jyzy6l0hpt4kjjj3u2wmjp3qr31ft8
г) 3KsJCgA6ubxgmmzvZaQYR485tsk2G6C1Be
д) 00 bb4d49777d981096a75215ccdba8dc8675ff02d1

10.7. Для чего используется версия свидетеля? Версия свидетеля — это первое число в segwit-выходе, например 00 в
00 bb4d49777d981096a75215ccdba8dc8675ff02d1

Придется пораскинуть мозгами

10.8. Объясните, как старый узел определит действительность segwit-транзакции, которая ничего не знает о segwit. Вот что видит старый узел:

![Схема сегментации транзакции](https://i.imgur.com/3Q5z5QG.png)

10.9. Объясните, как новый узел проверит segwit-транзакцию, которая ничего знает о segwit. Вот что видит новый узел:

![Схема сегментации транзакции с подписью](https://i.imgur.com/3Q5z5QG.png)

10.10. Предположим, вы решили обновить систему Биткоин так, чтобы свидетельство тоже удостоверяло комиссионные за транзакции в блоке