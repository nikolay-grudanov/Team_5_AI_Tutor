---
source_image: page_366.png
page_number: 366
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 12.56
tokens: 11296
characters: 400
timestamp: 2025-12-24T10:33:18.271199
finish_reason: stop
---

Листинг 13-16. Использование метода filter с замыканием, фиксирующим shoe_size

Функция shoes_in_size принимает в качестве параметров вектор с экземплярами обуви и размер обуви, а возвращает вектор, содержащий только обувь указанного размера.

В теле shoes_in_my_size мы вызываем into_iter чтобы создать итератор, который становится владельцем вектора. Затем мы вызываем filter, чтобы превратить этот