---
source_image: page_095.png
page_number: 95
model: model-run-olm-ocr
prompt_type: olmocr_technical
processing_time: 21.62
tokens: 7234
characters: 829
timestamp: 2025-12-24T09:22:39.793839
finish_reason: stop
---

13.6. Фильтр hue-rotate()

Меняет цвета изображения в зависимости от заданного угла поворота в цветовом круге. Значение задается в градусах (от 0deg до 360deg).

001 .hue-rotate { filter: hue-rotate(180deg); }

13.7. Фильтр invert()

Инвертирует цвета. Значение указывается в процентах. Значение 50% создает серое изображение.

001 .invert { filter: invert(100%); }

13.8. Фильтр saturate()

Управляет насыщенностью цветов: значение указывается в виде числа от 0 до 100. Значение больше 100 обычно приводит к чрезмерно насыщенному изображению.

001 .saturate { filter: saturate(7); }

13.9. Фильтр sepia()

Эффект, имитирующий старину (похоже на старую фотографию).

001 .sepia { filter: sepia(100%); }

13.10. Фильтр drop-shadow()

Действует подобно свойству box-shadow.

001 .shadow { filter: drop-shadow(8px 8px 10px green); }