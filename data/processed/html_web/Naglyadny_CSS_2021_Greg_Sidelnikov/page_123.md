---
source_image: page_123.png
page_number: 123
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 34.83
tokens: 7224
characters: 801
timestamp: 2025-12-24T09:23:29.899415
finish_reason: stop
---

18.2. Свойства rotateY и rotateZ

Вращение элемента по осям Y и Z дает следующие результаты:

rotateY
rotateY(10deg)

rotateX rotateY rotateZ
10 градусов по всем трем осям

rotateY
rotateY(-10deg)

rotateZ
rotateZ(-10deg)

Defaults
perspective: 0px
perspective-origin: 50% 50%
transform: rotateX(0deg);
transform: rotateY(0deg);
transform: rotateZ(0deg);
(по умолчанию)

rotateY(10deg)

18.3. Свойство scale

Масштабирование элемента либо уменьшает, либо увеличивает его относительный размер на любой из трех осей.

rotateX(45deg); scaleX(n)
scalex
1   0.9   0.8   0.7   0.6   0.5   0.4   0.3   0.2   0.1   0

scaleY
scalez

Как видите, аналогичным образом можно «масштабировать» элемент по любой из трех осей. Масштабирование по оси Z не меняет внешний вид элемента, когда перспектива не установлена.