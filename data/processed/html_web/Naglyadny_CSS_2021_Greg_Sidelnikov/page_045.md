---
source_image: page_045.png
page_number: 45
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.87
tokens: 7278
characters: 1115
timestamp: 2025-12-24T09:21:34.149663
finish_reason: stop
---

Обратите внимание: значение 200px свойства height элемента не меняется, но его физические размеры изменяются в зависимости от box-sizing: [content-box | padding-box | border-box].

Отсутствует область содержимого margin-box, так как поля по определению окружают ее.

CSS Is Awesome

302 × 102

Граница влияет на исходный размер элемента, если по умолчанию задано значение content-box

border: 1px solid gray;
width: 300px;
height: 100px;
background: #eee;
box-sizing: content-box;

Здесь значения свойств width (ширина) и height (высота) увеличились на 2 пикселя с каждой стороны, так как при использовании модели content-box по умолчанию для каждой из четырех сторон была добавлена граница толщиной 1px.

CSS Is Awesome

334 × 134

Граница влияет на исходный размер элемента, если по умолчанию задано значение content-box

border: 1px solid gray;
width: 300px;
height: 100px;
background: #eee;
box-sizing: content-box;
padding: 16px;

При наличии границ и отступов фактическая физическая ширина становится 334px × 134px. Это на 34 пикселя больше, чем исходные размеры (1 пиксел × 2 + 16 пикселов × 2 = 34 пикселя).