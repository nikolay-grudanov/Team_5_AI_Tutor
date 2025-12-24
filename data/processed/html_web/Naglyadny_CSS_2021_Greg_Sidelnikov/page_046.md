---
source_image: page_046.png
page_number: 46
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 28.34
tokens: 7299
characters: 1176
timestamp: 2025-12-24T09:21:41.922423
finish_reason: stop
---

Значение padding-box определяет отступ как часть содержимого. Теперь исходные размеры сохраняются, но содержимое еще включает отступ:

Внутренний отступ не влияет на размер элемента при использовании вместе с padding-box

border: 1px solid gray;
width: 300px;
height: 100px;
background: #eee;
box-sizing: padding-box;
padding: 16px;

Далее мы перезаписываем исходное значение border: 1px solid gray на border: 16px, и вместе с padding: 16px исходная ширина и высота элемента теперь дополняются 32 пикселями с каждой стороны, прибавляя всего 64 пикселя для каждого размера элемента:

Использование отступа и границы вместе

border: 1px solid gray;
width: 300px;
height: 100px;
background: #eee;
box-sizing: content-box;
padding: 16px;
border: 16px;

Использование border-box инвертирует border (границы) и padding (отступы), сохраняя исходную width (ширину) и height (высоту) элемента. Данная опция полезна, когда необходимо убедиться, что элемент сохранит идеальные размеры в пикселях, независимо от величины его границы или внутреннего отступа:

box-sizing: border-box
Заполняет и границы, и отступы в области 300 × 100
border-box не изменяет изначально установленные размеры