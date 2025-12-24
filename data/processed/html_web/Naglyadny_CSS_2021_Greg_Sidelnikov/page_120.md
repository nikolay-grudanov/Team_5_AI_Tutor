---
source_image: page_120.png
page_number: 120
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 25.91
tokens: 7136
characters: 623
timestamp: 2025-12-24T09:23:17.954893
finish_reason: stop
---

Порядок перемещения и поворота не имеет значения:

![Пример перемещения и поворота](../images/120.png)

translate(30px, 10px) rotate(5deg) так же как rotate(5deg) translate(30px, 10px)

По умолчанию элемент будет вращаться вокруг средней точки:

transform-origin: 50% 50% (по умолчанию)

![Примеры вращения вокруг средней точки](../images/121.png)

17.3. Свойство transform-origin

Начало вращения подвижного элемента с использованием свойства transform-origin: 0 0:

![Примеры вращения с transform-origin: 0 0](../images/122.png)

transform-origin: 100% 0

![Примеры вращения с transform-origin: 100% 0](../images/123.png)